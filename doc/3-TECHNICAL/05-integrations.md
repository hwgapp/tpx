# Integrations

> Cập nhật 2026-10-21; FCM/S3-compatible duyệt TD-019, social providers chọn TD-021; chưa có tài khoản dịch vụ. Firebase Auth đã duyệt TD-025; không tạo tài nguyên lúc này.

| Integration | Purpose | Auth/Security | Environment | Notes |
| --- | --- | --- | --- | --- |
| OTP provider | Phone login bổ sung sau | Secret backend, giới hạn gửi/xác thực | Later | Chưa có dịch vụ; không chặn social login bản đầu |
| Zalo | Thông báo cho khách | Adapter backend, tài khoản/template/quyền theo dịch vụ hiện hành | TBD | Chọn phương thức theo tài khoản TPX; chưa giả định thông báo giao dịch cho phép gửi mọi nội dung nhắc mua |
| Firebase Cloud Messaging cho Flutter | Push iOS/Android | Device token, Firebase/Apple credentials theo môi trường | Dev/staging/prod | Đã duyệt TD-019; project chưa có, cần cấu hình và kiểm tra thiết bị thật |
| S3-compatible storage | Ảnh catalog/nội dung | Upload theo quyền, public/private theo dữ liệu | Bucket theo môi trường | Đã duyệt TD-019; provider/config sau |
| Bank transfer | Nhân viên xác nhận chuyển khoản | Quyền xác nhận, audit và tham chiếu đơn | Manual ở bản đầu | Chưa có tích hợp ngân hàng tự động; không có COD |

## Đăng nhập khách

- Google/Facebook/Apple được chọn cho bản đầu TD-021; cần client/app IDs và callback/domain cấu hình riêng theo môi trường; chưa có provider apps.
- Firebase Authentication đã duyệt TD-025: web/Flutter thực hiện social flow qua SDK; NestJS xác minh ID token, map về user TPX/PostgreSQL. User đã duyệt dịch vụ trung gian; chưa tạo provider project/apps hoặc credentials.
- Phone login sau khi dịch vụ OTP sẵn sàng; đề xuất link số đã xác minh vào user hiện có, không tạo lại sổ tiền/điểm.
- Zalo vẫn là yêu cầu thông báo, chưa có OA/tích hợp; không tự coi là đã vận hành hoặc tự bỏ kênh này.
