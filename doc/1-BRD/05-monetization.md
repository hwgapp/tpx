# Monetization

> Draft theo các yêu cầu đã nhận; chưa freeze BRD. Nguồn: `01-decision-log.md`.

## Strategy

Doanh thu từ chênh lệch mua-bán thực phẩm (D-005). Bên thu mua nghiên cứu và đặt giá bán trước; giá đơn đã đặt không đổi theo giá chợ (D-017). Phí giao và đơn tối thiểu cấu hình trong admin (D-021). Chưa chốt mức giá hoặc biên lợi nhuận mục tiêu.

## Plans / Products

| Plan/Product | Price | Includes | Limits | Notes |
| --- | ---: | --- | --- | --- |
| Rau, củ, quả, thịt, cá, trứng | Do TPX đặt trước | Quy cách do TPX tạo theo sản phẩm | Đơn tối thiểu cấu hình admin | Không có luồng giá sỉ/flow B2B riêng được yêu cầu |

## Paywall / Ads / IAP Rules

- Chưa có yêu cầu paywall, ads hoặc IAP trong phạm vi trao đổi hiện tại.

## Số Dư Tiền Hoàn

- Khách không tự nạp tiền; admin được cộng khi điều chỉnh đơn.
- Ưu tiên tự dùng số dư khi mua hàng; không hết hạn.
- Thứ tự thanh toán: tiền hoàn -> điểm trong hạn mức nếu khách chọn -> chuyển khoản phần còn lại (D-070).
- Khách được yêu cầu hoàn ngân hàng, admin duyệt/chuyển hoàn; tiền yêu cầu rút chuyển pending, chỉ available được thanh toán. Lifecycle và thời gian xử lý cần đặc tả.
- Ví dụ D-078: tổng 200.000đ, yêu cầu rút 150.000đ -> pending 150.000đ, available 50.000đ. Tổng chưa giảm chỉ vì tạo yêu cầu; tiền pending chưa phải tiền đã chuyển ngân hàng.
- Khách thanh toán ngay khi đặt, kể cả đơn tương lai (D-068); bản đầu chuyển khoản, không COD (D-048); hoàn theo thỏa thuận (D-049).

## Loyalty — Có Từ Bản Đầu

| Nội dung | Quy tắc |
| --- | --- |
| Tích điểm | Chi tiêu 1.000đ tích 1 điểm |
| Giá trị dùng điểm | 1 điểm giảm 1.000đ; 100 điểm tương đương 100.000đ trước hạn mức (D-075) |
| Rút điểm thành tiền | Không được phép (D-076); chỉ số dư tiền hoàn thuộc luồng rút ngân hàng |
| Lựa chọn dùng điểm | Khách chọn dùng hoặc không khi mua hàng |
| Giới hạn đổi | Admin cấu hình trần phần trăm và trần tiền, áp dụng mức thấp hơn; ví dụ 10%, tối đa 100.000đ; cơ sở % là tiền hàng sau giảm giá, không phí giao, trước trừ số dư (D-081) |
| Thời điểm tích | Sau khi đơn hàng hoàn thành (D-044); tiêu chí trạng thái Hoàn thành đặc tả ở PRD |
| Cơ sở tích | Tiền hàng sau giảm giá trừ giá trị điểm đã dùng; phần trả số dư vẫn tích, phí giao không tích (D-082) |
| Hết hạn | Tạm thời không làm hết hạn ở bản đầu (D-047) |
| Làm tròn tích điểm | Làm tròn xuống mỗi 1.000đ được 1 điểm (D-082) |
| Hoàn/hủy điểm | Hoàn phần trả điểm bằng điểm; phần tiền theo thỏa thuận; thu hồi điểm đã tích tương ứng phần hoàn sau hoàn thành (D-083–085) |
| Kết hợp với số dư tiền hoàn | Số dư dùng trước, sau đó điểm nếu khách chọn và còn hạn mức, chuyển khoản phần còn lại |

Ví dụ D-077: đơn 1.000.000đ, trần dùng điểm 5% thì giá trị dùng tối đa 50.000đ = 50 điểm, dù khách có 100 điểm. Trần vẫn do admin cấu hình; 5% chỉ là ví dụ đã xác nhận cách tính. Điểm không được rút ngân hàng; số dư tiền hoàn có quy trình rút riêng. Bản đầu admin toàn quyền thực hiện bước duyệt/chuyển hoàn.

## Referral

- Thưởng bằng điểm loyalty; số điểm cấu hình trong settings (D-073).
- Mốc thưởng người giới thiệu là sau đơn đầu của khách mới hoàn thành (D-054).
- Phân bổ cho từng bên và điều kiện cụ thể còn OQ-032; chưa đặt mức điểm mặc định.

## Compliance Notes

- TBD

## Ví dụ tính loyalty đã được đồng ý

Tiền hàng sau giảm giá 1.000.000đ, số dư available dùng 200.000đ, trần 5% và trần tiền không thấp hơn 50.000đ, khách đủ điểm và chọn dùng: giảm 50.000đ bằng 50 điểm, chuyển khoản 750.000đ khi không có phí giao. Hoàn thành tích floor((1.000.000 − 50.000) / 1.000) = 950 điểm. Nếu phí giao 20.000đ thì chuyển khoản 770.000đ, vẫn tích 950 điểm. Tỷ lệ 5% là dữ liệu ví dụ, không phải mặc định settings.
