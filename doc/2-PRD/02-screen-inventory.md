# Screen Inventory

> PRD v0.1 — 2026-10-21 — Draft sẵn review, chưa freeze. **[C]**: đã chốt trong decision log. **[P]**: phương án chi tiết cần review tại [sổ review](11-review-decisions.md). Không coi [P] là yêu cầu user đã duyệt.

Mỗi màn web/app dùng cùng dữ liệu/AC; thiết kế responsive và native navigation riêng. Modal/sheet được liệt kê khi có thao tác tiền/quyết định. Admin responsive là P-010, không có app nhân viên riêng.

| Screen ID | Màn hình | Platform | Feature | Quyền | Nội dung/thao tác |
| --- | --- | --- | --- | --- | --- |
| S-001 | Trang chủ | Web + Flutter iOS/Android | F-002/F-003/F-015 | Public | Nhóm nguyên liệu thô/món sơ chế; thời hạn đặt, vùng giao, ảnh thật |
| S-002 | Danh sách nguyên liệu | Web + Flutter iOS/Android | F-002 | Public | Danh mục, lọc, phân trang, chỉ rõ đang tắt bán |
| S-003 | Tìm kiếm | Web + Flutter iOS/Android | F-002/F-003 | Public | Từ khóa, loại sản phẩm, xóa lọc; không lưu nội dung nhạy cảm analytics |
| S-004 | Chi tiết nguyên liệu | Web + Flutter iOS/Android | F-002/F-015/F-016 | Public | Giá/quy cách/đơn vị, ảnh, chọn lượng, thêm giỏ, đánh giá |
| S-005 | Danh sách món | Web + Flutter iOS/Android | F-003 | Public | Món cố định, tình trạng nguyên liệu, chọn xem |
| S-006 | Chi tiết món và khẩu phần | Web + Flutter iOS/Android | F-003/F-015/F-016 | Public | Thành phần TPX giao, định lượng, không gia vị/sốt, giá gói, khẩu phần |
| S-007 | Hướng dẫn nấu | Web + Flutter iOS/Android | F-003/F-015 | Public | Các bước, ảnh, nguồn; phân biệt thành phần không có trong gói |
| S-008 | Giỏ hàng chung | Web + Flutter iOS/Android | F-004 | Public → Customer | Đổi số lượng, dòng hết hàng, tổng tạm; đăng nhập trước đặt |
| S-009 | Đăng nhập social | Web + Flutter iOS/Android | F-001 | Public | Google/Facebook/Apple; đóng/cancel provider, tiếp tục giỏ và return path hợp lệ |
| S-010 | Tài khoản | Web + Flutter iOS/Android | F-001 | Customer | Tên, liên hệ, trạng thái SĐT chưa OTP, đăng xuất, yêu cầu xóa tài khoản [P] |
| S-011 | Liên kết đăng nhập | Web + Flutter iOS/Android | F-001 | Customer | Các provider đã liên kết; link mới với xác thực; phone để sau |
| S-012 | Sổ địa chỉ | Web + Flutter iOS/Android | F-004/F-008 | Customer | Danh sách, mặc định, thêm/sửa; không ảnh hưởng snapshot đơn cũ |
| S-013 | Thêm/sửa địa chỉ | Web + Flutter iOS/Android | F-004/F-008 | Customer | Tên người nhận, SĐT, địa chỉ, vùng giao, ghi chú |
| S-014 | Checkout | Web + Flutter iOS/Android | F-004/F-005/F-008/F-012 | Customer | Địa chỉ/SĐT, ngày/khung, breakdown tiền, số dư, dùng điểm opt-in |
| S-015 | Chọn ngày/khung giao | Web + Flutter iOS/Android | F-008 | Customer | Ngày sớm nhất, tối đa +7 ngày, cutoff tương ứng; không quota |
| S-016 | Hướng dẫn chuyển khoản | Web + Flutter iOS/Android | F-005 | Customer | Ngân hàng, số tiền còn phải thu, nội dung theo đơn; gửi thông báo đã chuyển [P] |
| S-017 | Kết quả đặt đơn | Web + Flutter iOS/Android | F-004/F-005 | Customer | Mã đơn, đã ghi nhận đơn, trạng thái xác nhận tiền; không báo đã thanh toán sai |
| S-018 | Lịch sử đơn | Web + Flutter iOS/Android | F-004/F-018 | Customer | Lọc trạng thái/ngày, xem, mua lại |
| S-019 | Chi tiết và tiến trình đơn | Web + Flutter iOS/Android | F-004/F-007/F-021 | Customer | Snapshot hàng/giá, cutoff, nguồn thanh toán, tiến trình, điều chỉnh/hoàn |
| S-020 | Xác nhận hủy | Web + Flutter iOS/Android | F-021 | Customer | Điều kiện trước cutoff, preview số tiền/điểm, kết quả; không tạo thao tác sau cutoff |
| S-021 | Chi tiết điều chỉnh/hoàn | Web + Flutter iOS/Android | F-021/F-012 | Customer | Phương án đã thỏa thuận, tiền/điểm, tiến trình chuyển hoàn, hỗ trợ |
| S-022 | Số dư tiền hoàn | Web + Flutter iOS/Android | F-010 | Customer | Available/pending rút/tổng, lịch sử và yêu cầu rút; không nạp |
| S-023 | Tạo yêu cầu rút | Web + Flutter iOS/Android | F-011 | Customer | Số tiền ≤ available, ngân hàng/tài khoản/chủ tài khoản, xác nhận giữ tiền |
| S-024 | Theo dõi yêu cầu rút | Web + Flutter iOS/Android | F-011 | Customer | Trạng thái, pending, lý do từ chối, tham chiếu chuyển; hủy nếu còn PENDING [P] |
| S-025 | Điểm loyalty | Web + Flutter iOS/Android | F-012 | Customer | Số điểm dùng được, giá trị sử dụng/trần, lịch sử; không rút thành tiền |
| S-026 | Giới thiệu bạn bè | Web + Flutter iOS/Android | F-017 | Customer | Mã/link chia sẻ, điều kiện, trạng thái và lịch sử thưởng; không tự gửi tin |
| S-027 | Món thường mua | Web + Flutter iOS/Android | F-019 | Customer | Danh sách thường mua, tình trạng hiện tại, thêm giỏ |
| S-028 | Viết đánh giá | Web + Flutter iOS/Android | F-016 | Customer | Chỉ dòng đã hoàn thành; sao, nội dung, điều kiện moderation [P] |
| S-029 | Thông báo trong tài khoản [P] | Web + Flutter iOS/Android | F-013 | Customer | Thông báo của mình, đọc/xem đơn; hỗ trợ push bị từ chối |
| S-030 | Tùy chọn thông báo/nhắc đặt | Web + Flutter iOS/Android | F-013/F-020 | Customer | Đồng ý/thu hồi marketing, bật/tắt nhắc, xin quyền push đúng ngữ cảnh |
| S-031 | Thông tin TPX/chính sách/hỗ trợ | Web + Flutter iOS/Android | F-015 | Public | Liên hệ, nguồn thông tin, giao/hủy/hoàn, quyền riêng tư; nội dung TPX duyệt |
| S-032 | Kết quả xác thực/deep link | Web + Flutter iOS/Android | F-001 | Public | Kiểm tra phiên/return path; lỗi provider, không lộ token trong URL/log |
| S-033 | Đăng nhập admin | Admin web responsive [P] | F-009 | Admin public entry | Account cố định + mật khẩu, không OTP/TOTP |
| S-034 | Dashboard vận hành | Admin web responsive [P] | F-009 | dashboard.read | Đơn theo ngày giao, chưa xác nhận tiền, ngoại lệ/rút cần xử lý; số liệu định nghĩa rõ |
| S-035 | Catalog nguyên liệu | Admin web responsive [P] | F-002/F-009 | catalog.manage | Quản lý danh mục; tìm/lọc, tạo/sửa sản phẩm, giá, quy cách, ảnh, bật/tắt |
| S-036 | Sản phẩm và variants | Admin web responsive [P] | F-002/F-009 | catalog.manage | Thông tin, variant, mapping nguyên liệu và lượng chuẩn cho gom mua |
| S-037 | Nguyên liệu thị trường | Admin web responsive [P] | F-003/F-006 | catalog.manage | Đơn vị chuẩn, khả dụng, xem món bị ảnh hưởng khi tắt |
| S-038 | Danh mục món | Admin web responsive [P] | F-003/F-009 | catalog.manage | Danh sách, giá theo khẩu phần, trạng thái tắt tay/tắt do nguyên liệu |
| S-039 | Món, khẩu phần và công thức giao | Admin web responsive [P] | F-003/F-006 | catalog.manage | BOM từng variant/khẩu phần, hướng dẫn, nguồn, version, ảnh |
| S-040 | Thư viện ảnh | Admin web responsive [P] | F-015 | content.manage | Upload, alt text/nguồn, validate file, không nhận ảnh làm bằng chứng chuyển tiền mặc định |
| S-041 | Quản lý đơn | Admin web responsive [P] | F-004/F-021 | orders.read | Lọc ngày giao/payment/procurement, tìm mã/khách, xem chi tiết |
| S-042 | Chi tiết đơn vận hành | Admin web responsive [P] | F-004/F-005/F-007/F-021 | orders.read | Nguồn tiền, cutoff, timeline, contact, actions theo quyền và trạng thái |
| S-043 | Hàng đợi chuyển khoản | Admin web responsive [P] | F-005 | payments.confirm | Chờ xác nhận, số phải thu, tiền thiếu/thừa, reference, confirm có audit |
| S-044 | Danh sách đợt thu mua | Admin web responsive [P] | F-006 | procurement.manage | Theo ngày giao/cutoff, trạng thái tổng hợp, đơn cần quyết ngoại lệ |
| S-045 | Chi tiết đợt và quyết định mua | Admin web responsive [P] | F-006 | procurement.manage | Duyệt/loại unpaid từng đơn, lý do, tổng hợp nhu cầu, snapshot/export [P] |
| S-046 | Ghi nhận mua/nhận thực tế | Admin web responsive [P] | F-006/F-007 | procurement.manage | Lượng cần/mua/đạt/thiếu, giá vốn thực tế, không sửa giá bán đơn |
| S-047 | Bảng tập kết/sơ chế/đóng gói | Admin web responsive [P] | F-007 | fulfillment.manage | Checklist nguyên liệu/dòng đơn, thiếu/không đạt, pack ready |
| S-048 | Bảng giao hàng | Admin web responsive [P] | F-007/F-008 | delivery.manage | Ngày/khung/địa chỉ, TPX tự sắp, trạng thái, danh sách in [P] |
| S-049 | Chi tiết giao/kết quả | Admin web responsive [P] | F-007/F-021 | delivery.manage | Liên hệ, bắt đầu giao, thành công/thất bại, lý do, complete có guard |
| S-050 | Ngoại lệ/thỏa thuận khách | Admin web responsive [P] | F-021 | adjustments.manage | Thiếu hàng, đổi món, giao lỗi; phương án/đồng ý, không tự quyết hoàn cứng |
| S-051 | Danh sách điều chỉnh/hoàn | Admin web responsive [P] | F-021 | refunds.manage | Theo pending/approved/settled, tiền và điểm, trường hợp cần xem xét |
| S-052 | Lập/duyệt/thực hiện hoàn | Admin web responsive [P] | F-021/F-010/F-012 | refunds.manage | Preview theo nguồn, số còn hoàn, thu hồi điểm, chuyển hoàn thủ công |
| S-053 | Danh sách yêu cầu rút | Admin web responsive [P] | F-011 | withdrawals.manage | Chờ duyệt/đang chuyển, số pending, ưu tiên thủ công |
| S-054 | Duyệt/chuyển hoàn rút | Admin web responsive [P] | F-011 | withdrawals.manage | Ngân hàng được che theo màn hình, duyệt/reject/processing/paid theo P-002 |
| S-055 | Danh sách khách | Admin web responsive [P] | F-009/F-010/F-012 | customers.read | Tìm, trạng thái, lịch sử đơn, không tự gộp identity |
| S-056 | Chi tiết khách và sổ giao dịch | Admin web responsive [P] | F-009/F-010/F-012/F-017 | customers.read | Đơn, liên hệ, tiền/điểm, referral, credits gắn adjustment có quyền |
| S-057 | Tài khoản admin/quyền | Admin web responsive [P] | F-009 | access.manage | Account user tạo trước; enable/disable, quyền, phiên; không public signup |
| S-058 | Nhật ký thao tác | Admin web responsive [P] | F-009 | audit.read | Actor, entity, reason, request ID, không token/mật khẩu, dữ liệu che |
| S-059 | Settings nghiệp vụ | Admin web responsive [P] | F-014 | settings.manage | Phí/đơn tối thiểu, vùng/khung giao, trần điểm, referral, lịch nhắc, version |
| S-060 | Theo dõi gửi thông báo | Admin web responsive [P] | F-013/F-020 | notifications.manage | Trạng thái kênh, lỗi/template/token, retry; không sửa trạng thái đơn |
| S-061 | Nội dung/chính sách | Admin web responsive [P] | F-015 | content.manage | Ảnh thực tế, nội dung TPX, hướng dẫn/nguồn; preview/publish [P] |
| S-062 | Duyệt đánh giá | Admin web responsive [P] | F-016 | reviews.moderate | Kiểm tra verified purchase, ẩn/hiện có lý do, không sửa sao/nội dung khách |
| S-063 | Báo cáo vận hành/tài chính [P] | Admin web responsive [P] | F-009/F-014 | reports.read | Giá trị đơn, tiền nhận, hoàn, liability tiền/điểm và chênh lệch gộp có nhãn |

## Trạng thái UI bắt buộc

- Màn đọc: loading/skeleton, dữ liệu rỗng kèm hành động phù hợp, lỗi mạng/thử lại, nội dung không tồn tại/đã tắt, phân trang khi có danh sách.
- Form/mutation: kiểm tra từng trường, đang gửi/chặn bấm lặp, thành công, lỗi validation, conflict phiên bản, lỗi quyền/phiên hết hạn, unknown outcome cần đọc lại trạng thái trước retry.
- Web/app: offline được xem cache có nhãn cũ; đặt/hủy/rút/đổi điểm luôn cần online và xác nhận từ API; không queue ngầm giao dịch tài chính.
- Catalog/checkout: đơn vị và quy cách rõ, thay giá/hết hàng cần xác nhận lại; pending rút không khả dụng; cutoff lấy server, không dựa đồng hồ thiết bị.
- Admin: 401 về login giữ return path nội bộ; 403 màn quyền; action không hợp lệ có lý do; cảnh báo thay đổi chưa lưu, confirm trước thao tác tiền.
- Accessibility đề xuất: nhãn form, focus/keyboard, thông báo lỗi đọc được, không dùng màu xanh/cam đơn độc biểu diễn trạng thái. Không cố định màu brand thành màu chữ không đủ tương phản.
