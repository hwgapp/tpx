# Review PRD vòng1 — 2026-10-25

> Nguồn mới nhất **D-093–100**, bao gồm hai câu làm rõ. Các nội dung dưới là phần user đã xác định; không đồng nghĩa duyệt mọi P-001–019. Chưa có implementation.

| Chủ đề | Đã chốt | Còn mở |
| --- | --- | --- |
| Nguồn nội bộ | Cả số dư tiền hoàn và điểm HOLD khi order tạo thành công, không dùng/rút tiếp. Complete mới CAPTURE, cancel RELEASE | Hold delta khi admin sửa đơn: OQ-042 |
| Không thực hiện được | Admin hủy/CANCELLED, mở hold, hoàn tiền thật theo thỏa thuận; không NOT_FULFILLED | Chi tiết partial/refund P-003 |
| Đơn thiếu tiền | Admin quyết định có giao; giữ remaining due và không ghi PAID giả/COD | Complete-unpaid và earn khi đó: OQ-050 |
| Sửa/thay món | Admin có chức năng update thay đổi | Xác nhận/thu thêm, thay hold/fee/caps: OQ-042 |
| Hàng còn lại / tiền hoàn | Phần hàng đã thống nhất có thể giao khi bank refund pending | Không tự bỏ guard hàng/quyền, không settled giả |
| Hoàn sau complete | Được phép; **không thu hồi ORDER_EARN đã thưởng**, dù đã dùng hay chưa. D-100 thay D-085; không debt/offset | Referral reward là nhóm khác, vẫn theo review P-006 |

## Hai loại hold tiền phải tách

```text
wallet_total = available_vnd + held_order_vnd + pending_withdrawal_vnd
points_total = available_points + held_points
```

Ví200k: rút150k → available50k / pending-rút150k / held-đơn0 / total200k. Dùng50k cho đơn mới → available0 / pending-rút150k / held-đơn50k / total200k. Cancel đơn → available50k / pending-rút150k / held-đơn0 / total200k. Complete đơn → available0 / pending-rút150k / held-đơn0 / total150k trước các sự kiện khác. Chỉavailable mới có thể đặt/rút.

Điểm100/chọn50: place→available50/held50/total100; cancel→100/0/100; complete→50/0/50 trước earn. CAPTURE chỉ giảm held, không trừ available lần hai. Quote chưa tạo đơn không giữ nguồn. Hai nguồn reserve atomically, không hold một nguồn mồ côi nếu place thất bại.

## Hoàn trước và sau complete

- Trước complete: hủy/giảm đơn release đúng phần cash/points còn hold. Release không phải refund một khoản đã capture, không cộng available thêm lần nữa qua refund leg.
- Complete: capture đúng phần cash/points còn allocated, cộng ORDER_EARN riêng theo nội dung cuối đã thống nhất, một lần.
- Sau complete: hoàn tiền/điểm đã capture theo nguồn/thỏa thuận; giữ nguyên ORDER_EARN đã cấp. Không debt_points, không lấy tiền khách bù điểm, không chạy complete lại để thưởng thêm.
- Partial trước complete cần chốt split/hold delta qua admin update; không tự áp tỷ lệ giảm/thu thêm ngoài thỏa thuận.

## Trạng thái

OQ-048/049 đã đóng bằng hai câu trả lời rõ. OQ-050 và OQ-042 còn chi tiết; không tự coi quyền giao thiếu tiền là quyết định complete/earn chưa thu đủ hoặc coi admin update là mọi cách settlement đã chốt. Đã unblock đặc tả joint hold/capture/release và refund giữ earned points; chưa freeze gates.
