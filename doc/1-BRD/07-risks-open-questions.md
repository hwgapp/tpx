# Risks And Open Questions

> Draft. Chi tiết và trạng thái theo `../0-INBOX/04-open-questions.md`. Các mục dưới phục vụ hoàn thiện tài liệu; chưa phải quyết định nghiệp vụ mới.

| ID | Type | Risk / Question | Impact | Mitigation / Next Step |
| --- | --- | --- | --- | --- |
| R-001 | Resolved | Đã chốt 1 điểm giảm 1.000đ trong hạn mức, không rút điểm thành tiền (D-075–077) | Giá trị đổi điểm đã rõ | Mang ví dụ đơn 1.000.000đ, trần 5%, dùng 50 điểm sang acceptance criteria |
| R-002 | PRD detail | Đã chốt cơ sở trần/tích, làm tròn xuống và chính sách hoàn/thu hồi điểm D-081–085; còn phân bổ hoàn một phần, trường hợp điểm đã dùng | Cần tránh hoàn vượt và thu hồi sai điểm | Đặc tả theo từng nguồn; không tự quyết số điểm âm hoặc công thức hoàn một phần |
| R-003 | Open question | Duyệt mua đơn chưa thanh toán và thời điểm phải thu đủ chuyển khoản (OQ-017) | Cần nhất quán với việc chưa có COD ở bản đầu | Làm rõ ngoại lệ; duyệt mua không tự ghi nhận đã thanh toán |
| R-004 | Open question | Rút hoàn ngân hàng và quyền điều chỉnh số dư (OQ-019/022/023) | Cần thao tác, trạng thái và quyền đầy đủ | Đặc tả PRD/RBAC; chưa coi là chuyển tiền ngân hàng tự động |
| R-005 | Open question | Vùng giao cụ thể, ngày ra mắt và danh mục cấu hình ban đầu (OQ-002/012/014) | Cần dữ liệu vận hành trước khi mở bán | Tiếp tục xác định ở PRD/release; vùng thử nghiệm và quy mô kỳ vọng đã có |
| R-006 | Operational policy | Hoàn tiền theo thỏa thuận; giao không thành công do vận hành quyết với khách | Phần mềm cần ghi nhận kết quả xử lý, không tự áp chính sách cứng | Thiết kế thao tác nhân viên và lịch sử ở PRD theo D-049/D-050 |
