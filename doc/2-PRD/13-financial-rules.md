# Tiền, điểm và holds — review2026-10-25

> Nguồn D-093–100. Cash và points HOLD khi order tạo thành công, CAPTURE khi complete, RELEASE khi cancel. Hoàn sau complete được phép và giữ nguyên ORDER_EARN; D-100 thay D-085. Split partial/fee allocation P-003/005 và complete-unpaid OQ-050 còn review; chưa có implementation.

## 1. Quote và phân bổ

G là tiền hàng sau giảm giá trước số dư/points; F là phí giao; A là cash available (không held_order hoặc pending rút); L là available points (không held). r_bp và M là trần %/VND admin cấu hình, không tự lấy số ví dụ làm mặc định.

```text
B = min(A, G + F)
B_fee = min(B, F)                         # fee-first là P-005 còn review
B_goods = B - B_fee
cap_percent_vnd = floor(G * r_bp / 10000)
max_point_value = min(cap_percent_vnd, M, max(0, G - B_goods))
P = use_points ? min(L, floor(max_point_value / 1000)) : 0
D = 1000 * P
T = G + F - B - D
Earn_target = floor(max(0, G_final - D_final) / 1000)
```

Trần % vẫn dựa G trước số dư, không phí giao. Điểm không trả phí theo P-005, không vượt phần hàng còn lại/caps/available. Cash vẫn được tính tích điểm; D và F không tích. Quote không hold; submit lấy available/config/date/price mới và reserve atomically. G_final/D_final là nội dung cuối đã thống nhất trước complete; không tự sửa giá snapshot. Không thêm voucher engine từ trường discount.

Ví dụ G1m/F0/cash200k/points50: hold200k+50points, bank750k; complete capture holds rồi earn950. F20k→bank770k, vẫn earn950. Opt-outpoints khi F20k→bank820k, earn1000. T0 không yêu cầu receipt0đ. Những cấu hình trần5%/10%/100k là demo.

## 2. Cash wallet và points

```text
wallet_total = available_vnd + held_order_vnd + pending_withdrawal_vnd
points_total = available_points + held_points
place:    cash(available -= B; held_order += B), points(available -= P; held += P)
cancel:   cash(held_order -= B_rem; available += B_rem), points(held -= P_rem; available += P_rem)
complete: cash(held_order -= B_rem), points(held -= P_rem)  # không trừ available lần hai
```

HOLD chưa giảm tổng, CAPTURE mới tiêu chính thức. Số held gắn đúng order, unavailable cho order khác hoặc withdraw. Complete/cancel/retry không capture/release trùng; cancel không tạo earn. Không có order commit thì không để hold một nguồn mồ côi. Pending rút là trục khác, không gộp vào held_order.

Ví200k, rút150k→available50k/pending150k/held0/total200k. Place dùng50k→available0/pending150k/held50k/total200k. Cancel→available50k/pending150k/held0/total200k. Complete→available0/pending150k/held0/total150k trước sự kiện khác.

Points100/chọn50→place available50/held50/total100; cancel100/0/100; complete50/0/50 trước earn riêng. Không nạp cash, không rút points, không hết hạn bản đầu.

## 3. Funding và quyền vận hành

Holds bảo đảm phần B/D trên quote; phần T vẫn cần chuyển khoản. FUNDED phải đọc nguồn đã bảo đảm/đã xác nhận, không đồng nghĩa cash wallet đã capture hoặc mọi nguồn đều là tiền bank nhận mới. Report cash-in chỉ đếm receipt bank thực; order hold chưa giảm liability ví. Customer notice hoặc admin approve mua/giao không thay receipt/funding giả.

D-095: admin quyết định giao khi còn thiếu tiền, phải giữ remaining due và audit decision. Không tự thêm COD. Quyền complete khi còn thiếu và lúc earn của trường hợp đó còn OQ-050; không tự hard-code đủ tiền trước dispatch hoặc tự complete mọi order thiếu tiền.

D-094: admin cancel vận hành dùng CANCELLED với reason/actor, release cả cash/points hold còn lại; khách vẫn chỉ tự cancel trước22h. Tiền bank đến sau hủy/EXCLUDED vào đối soát, không tự khôi phục mua.

## 4. Rút tiền

Create(x): available−=x, pending_withdrawal+=x atomically, không dùng held_order. Duyệt chưa chuyển thật. Theo P-002: cancel/reject khi trạng thái cho phép trả pending về available; PAID khi đã chuyển có reference mới giảm pending/tổng. PROCESSING/unknown giữ pending tới đối soát, không auto-release hoặc chuyển lại vì HTTP timeout. Lifecycle/known-failed correction P-002/016 còn phần review.

## 5. Hoàn và điều chỉnh

Trước complete, hủy/giảm đơn RELEASE phần cash/points còn hold theo nội dung đã thống nhất. Không vừa release hold vừa credit refund cùng khoản. Order update phải preview hold delta/caps/nguồn/fee và agreement/version; không tự tăng hold hoặc thu thêm. Split và settlement update còn P-003/OQ-042.

Sau complete, return cash/points đã capture hoặc bank đã thực nhận theo nguồn/thỏa thuận. **Giữ nguyên ORDER_EARN đã cấp**, kể cả khách đã dùng ở đơn khác; không debt/offset/clawback, không lấy tiền bù điểm. RETURN points thanh toán không phải thưởng mới, không earn lần hai. Order đã complete không mở lại hoặc chạy completion lần nữa vì refund. Referral rewards vẫn là topic P-006 riêng, không tự quyết từ câu hỏi ORDER_EARN.

Mỗi refund ghi affected items/qty, cash_goods/shipping/excess, captured_points_return, original source và payout_method. Cash có thể hoàn BALANCE/BANK theo thỏa thuận, points chỉ POINTS. Tổng các lần đã hoàn+còn reserved không vượt nguồn đã capture/thực nhận; không hoàn tiền chưa thu hoặc points chưa capture bằng RETURN. Before-complete bank refund vẫn được theo thực nhận, trong khi held sources release riêng.

BANK leg pending/processing chưa settled; giữ remaining cap, unknown không chuyển lại mù. Internal legs posted once; các khoản tiền chưa rõ order/thừa/đến muộn không tự nạp ví. Receipt matched+excess_reserved+excess_refunded không vượt actual_received, không vừa hoàn excess vừa match vào order. Tiền thừa không tạo earn.

D-097: phần hàng đã thống nhất có thể giao khi hoàn bank pending; fulfillment resolution và financial settlement riêng, không báo settled giả hoặc bỏ guard hàng/quyền. Full/partial refund sau complete không tính lại hoặc thu hồi ORDER_EARN. Hoàn trước complete điều chỉnh eligible base trước lần earn đầu tiên.

## 6. Bất biến triển khai cần kiểm thử

Các bucket available/held_order/pending và available_points/held_points không âm; projections khớp ledger. Reserve/capture/release có unique operation references, transaction/lock/version, không gọi bank/provider trong DB transaction. Snapshot và bút toán bù giữ lịch sử; không sửa/xóa posted entry. Đây là đặc tả kiểm thử, chưa phải kết quả sản phẩm.
