# Thuật ngữ TPX

| Thuật ngữ | Nghĩa | UI Việt | Code | Ghi chú |
| --- | --- | --- | --- | --- |
| TPX | Thực phẩm xanh | Thực phẩm xanh | TPX | Không dùng tên làm việc cũ trong sản phẩm |
| Nguyên liệu thô | Sản phẩm catalog theo quy cách | Nguyên liệu | RAW | Không shopping list tự do |
| Món sơ chế | Gói nguyên liệu chính theo khẩu phần | Món ăn / Nguyên liệu theo món | MEAL_KIT | Làm sạch/cắt/chia; không gia vị/sốt |
| BOM | Thành phần và lượng theo variant | Thành phần gói | recipe_components | Snapshot lúc đặt để gom mua |
| Cutoff | Giờ chốt mua/khóa hủy | Hạn hủy / Giờ chốt | cutoff_at | 22h ngày trước ngày giao |
| Available | Số dư có thể mua/rút | Số dư khả dụng | available_vnd | Không gồm pending |
| Pending rút | Tiền giữ cho yêu cầu rút | Đang chờ rút | pending_withdrawal_vnd | Duyệt chưa đồng nghĩa chuyển tiền |
| Tổng số dư | Available + pending rút | Tổng số dư | wallet_total | Không cộng pending lần hai |
| Điểm loyalty | Đơn vị ưu đãi, không rút tiền | Điểm tích lũy | points | 1điểm dùng=1.000đ; earn chỉ sau complete |
| Thu hồi điểm | Giảm earn tương ứng phần hoàn | Điều chỉnh điểm | earn_revocation | Khác hoàn điểm đã dùng |
| Điểm cần bù [P] | Earn đã dùng cần thu hồi | Điểm đang chờ bù | debt_points | P-004 chưa duyệt, không lấy tiền bù |
| Báo giá | Tính hiện tại trước tạo đơn | Chi tiết thanh toán | checkout_quote | Không giữ/trừ tiền |
| Funding | Nguồn tiền/điểm áp cho order | Thanh toán | order_funding | Tách receipt và procurement |
| Thông báo đã chuyển | Khách khai đã chuyển | Đã chuyển khoản | payment_notice | Không PAID |
| Receipt | Tiền ngân hàng thực nhận | Xác nhận chuyển khoản | payment_receipt | Admin đối soát thủ công |
| Refund leg | Từng phần trả tiền/điểm | Chi tiết hoàn | refund_leg | Bank leg có pending/processing/settled |
| User TPX | Định danh nội bộ ổn định | Tài khoản | user_id | Không khóa theo email/phone |
| Identity | Phương thức login đã xác minh | Liên kết đăng nhập | auth_identity | Social trước, phone sau |
| [C] | Đã chốt trong decision log | — | Confirmed | Không bị proposal ghi đè |
| [P] | Phương án chi tiết để review | — | Proposed | Không tự coi đã duyệt để implement |
