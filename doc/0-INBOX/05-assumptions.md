# Assumptions

Giả định tạm thời của Codex khi user chưa chốt nhưng cần tiếp tục.

| ID | Assumption | Vì sao tạm dùng | Cần xác nhận trước | Trạng thái |
| --- | --- | --- | --- | --- |
| AS-001 | Dùng tên làm việc `fresh-market` cho folder dự án | User chưa cung cấp tên tại thời điểm khởi tạo | Chốt thương hiệu hoặc yêu cầu đổi tên folder | Superseded — user chốt Thực phẩm xanh (TPX) ngày 2026-10-20; folder hiện tại giữ nguyên |

Không giả định giờ chốt đơn, ngày giao, khu vực phục vụ, nguồn gốc hàng, quy tắc giá, trọng lượng, thanh toán hoặc xử lý thiếu hàng.

## Phương án PRD v0.1

Các chi tiết P-001–012 trong [review register](../2-PRD/11-review-decisions.md) là proposal có nguồn OQ, không phải giả định đã được chấp nhận để implement. Không tự biến amount/SLA/loyalty caps/referral rewards ví dụ thành config production. Scope chuẩn bị PRD được user giao D-090; các gate vẫn chưa freeze.
