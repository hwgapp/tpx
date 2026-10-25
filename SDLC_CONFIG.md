# SDLC Config

> Bật/tắt module checklist theo từng dự án. Không dùng file này để chốt technical chi tiết; technical sẽ nằm trong `doc/3-TECHNICAL`.

## Project Preset

| Mục | Chọn |
| --- | --- |
| App archetype | Thương mại điện tử thực phẩm tươi; gom đơn rồi mua tại chợ đầu mối |
| Seller model | TPX trực tiếp bán toàn bộ |
| Shopping groups | Nguyên liệu thô theo yêu cầu; nguyên liệu đã sơ chế theo món |
| Launch area | Thử nghiệm các quận nội thành TP.HCM; kỳ vọng vài chục đơn/ngày; vùng giao cụ thể TBD |
| Order cycle | Đặt trước tối đa 7 ngày; giao ngày D chốt mua/khóa hủy 22:00 ngày D−1; sớm nhất D+1 trước cutoff, D+2 từ cutoff; thiếu nguyên liệu thì hoàn; khung giao không quota |
| Meal preparation | Làm sạch, cắt/chia nguyên liệu chính; không gia vị/nước sốt; có hướng dẫn nấu, menu cố định và tắt khi thị trường hết |
| Platform | iOS, Android, Web app, Admin/CMS, Backend/API |
| Release target | Bản production dùng được; kênh phân phối mobile và tiêu chí release chi tiết TBD |
| Technical stack fixed? | Gói TD-019 đã duyệt: NestJS modular monolith REST/OpenAPI, Next.js, React/Vite, PostgreSQL/Prisma, Flutter, Redis/BullMQ, S3-compatible, FCM, monorepo; native không Docker trên server user có sẵn; GitHub; Firebase Auth đã duyệt TD-025 |
| Default language | Tiếng Việt |

## Optional Modules

| Module | Enabled | Notes |
| --- | --- | --- |
| Backend/API | Yes | NestJS trên Node.js, modular; ranh giới module cần freeze Technical |
| Admin/CMS | Yes | Gồm settings phí giao/đơn tối thiểu/giới hạn đổi điểm, xác nhận chuyển khoản, RBAC và quản lý số dư; COD hoãn khỏi bản đầu |
| AI/OCR | TBD | |
| Auth/account | Yes | Google/Facebook/Apple bản đầu; phone + OTP sau; admin cố định tài khoản/mật khẩu không OTP, giữ RBAC; Firebase Auth đã duyệt TD-025; chưa có tài khoản dịch vụ |
| Payment/IAP/subscription | Yes — thanh toán đơn hàng | Thứ tự số dư -> điểm trong hạn mức nếu chọn -> chuyển khoản phần còn lại khi đặt; không COD; admin cấp quyền nhân viên quyết ngoại lệ chưa thanh toán |
| Ads | TBD | |
| Push notification | Yes | Push trên app và thông báo Zalo; sự kiện/tích hợp TBD |
| Customer balance | Yes | Available dùng trước điểm; pending giữ tiền yêu cầu rút và không dùng thanh toán; không tự nạp/không hết hạn; admin điều chỉnh theo đơn và duyệt/chuyển hoàn |
| Loyalty | Yes — từ bản đầu | D-093: points HOLD khi order tạo thành công, complete mới CAPTURE, cancel RELEASE. Tích sau hoàn thành trên tiền hàng sau giảm giá, trừ điểm dùng, loại phí giao; số dư vẫn tích, làm tròn xuống mỗi 1.000đ; 1 điểm giảm 1.000đ, không rút/hết hạn; trần % trên tiền hàng trước số dư và trần tiền admin set; hoàn điểm bằng điểm, giữ nguyên ORDER_EARN khi hoàn sau complete D-100 |
| Upload/media | TBD | |
| Referral | Yes | Thưởng điểm loyalty, mức điểm settings; sau đơn đầu hoàn thành; điều kiện/phân bổ cụ thể cần đặc tả |
| Repeat purchase | Yes | Mua lại đơn, món thường mua và nhắc đặt trên kênh khách đồng ý nhận |
| Transparency/reviews | Yes | Thông tin thực tế và đánh giá từ khách đã mua |
| Offline/local-first | TBD | |
| Analytics | TBD | |
| Kids/privacy sensitive | TBD | |
| User-generated content | TBD | |
| Multi-language | TBD | |

## Delivery Defaults

| Mục | Giá trị mặc định |
| --- | --- |
| ORCA concurrency target | High: 4-8 tasks song song |
| Progress tracking | Markdown simple |
| Token policy | Compact task packets, reference docs by path |
| Code skeleton | Chỉ tạo sau Technical gate |


## Review2026-10-25

Admin quyết giao khi chưa thu đủ D-095 và có update đơn D-096; không đổi PAID giả/COD. Refund pending không chặn phần hàng đã thống nhất D-097. Cash cùng hold D-099; hoàn sau complete RETURN captured points, giữ ORDER_EARN D-100 và complete-unpaid OQ-050 chưa chốt.
