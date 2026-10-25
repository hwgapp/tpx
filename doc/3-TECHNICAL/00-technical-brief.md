# Technical Brief

## Stack Summary

> Cập nhật ngày 2026-10-21; **chưa freeze Technical**. User duyệt gói stack TD-019, admin cố định không OTP TD-020, Google/Facebook/Apple TD-021, server có sẵn TD-022 và GitHub TD-023. TD-008/012/018 đã bị thay; Firebase Auth đã duyệt TD-025. Chưa tạo code skeleton.

| Thành phần | Công nghệ / phương án | Trạng thái |
| --- | --- | --- |
| Backend | NestJS trên Node.js, modular | User chọn |
| Web UI | React, Next.js | User chọn; phân bổ duyệt TD-019 |
| Database | PostgreSQL | User chọn |
| Storefront | Next.js App Router | Approved TD-019 |
| Admin | React + Vite | Approved TD-019 |
| Mobile | Flutter / Dart cho iOS và Android | User chọn |
| ORM | Prisma | Approved TD-019 |
| Job nền | Redis + BullMQ | Approved TD-019 |
| UI web/admin | Tailwind CSS + shadcn/ui, tokens #309953/#F9A01B | Approved TD-019; màu đã chốt |
| Workspace | TypeScript/pnpm/Turborepo cho web/admin/API/worker; Flutter toolchain riêng trong cùng repo | Approved TD-019 |
| Ảnh | Object storage tương thích S3 | Approved TD-019; provider cấu hình sau |
| Deploy | Không Docker; Node.js trực tiếp, admin build static; staging/production riêng | Approved TD-019/022; server có sẵn |
| Push mobile | Firebase Cloud Messaging cho Flutter | Approved TD-019 |

## Architecture Summary

Một backend NestJS chia module nghiệp vụ, phục vụ storefront, admin và app mobile qua REST API. Worker dùng cùng code nghiệp vụ cho job nền. PostgreSQL là nguồn sự thật cho đơn và giao dịch; Redis phục vụ queue/trạng thái tạm. Kiến trúc duyệt TD-019; data model vẫn khái niệm, chưa freeze schema/contracts.

Món sơ chế có cấu thành nguyên liệu theo từng khẩu phần để hỗ trợ tổng hợp mua/sơ chế; giá bán vẫn là giá TPX đặt trước. Dòng nguyên liệu thô và món sơ chế cùng một giỏ/đơn/lần giao, giữ snapshot giá/quy cách lúc đặt.

## Key Decisions

- Backend sở hữu công thức giá, ngày giao theo cutoff, quyền, tiền và điểm; client hiển thị kết quả được tính/xác nhận từ API.
- Deadline 22:00 và ngày giao kiểm tra bằng giờ server theo `Asia/Ho_Chi_Minh`; job gom mua hỗ trợ vận hành, không quyết định tính hợp lệ bằng thời điểm job thực chạy.
- Tiền hoàn và điểm có sổ giao dịch riêng. Xử lý đơn hoàn thành/cộng điểm và retry cần transaction/khóa duy nhất để không ghi nhận trùng.
- RBAC kiểm tra quyền và phạm vi dữ liệu ở API; ẩn nút trên giao diện chỉ là trải nghiệm người dùng.
- Các phiên bản package cụ thể và lệnh kiểm tra chỉ chốt khi freeze stack/test plan.

## Risks

- OQ-029–031 đã đóng: catalog nguyên liệu thô, món sơ chế theo khẩu phần có giá sẵn, giỏ/đơn/giao chung.
- OQ-019/022/023/032 và chi tiết phân bổ hoàn một phần/điểm đã tiêu cần rõ trước khi freeze giao dịch. Cơ sở trần/tích, làm tròn xuống và chính sách hoàn đã chốt D-081–085.
- OQ-033: stack/tooling đã duyệt; server user có sẵn, GitHub đã chọn. Chưa có account OTP/Zalo/Firebase; phone sau; Firebase Auth TD-025 đã duyệt, provider credentials cấu hình ở bước tích hợp.

## Tài Liệu Chính Thức Đã Đối Chiếu

- [Next.js App Router](https://nextjs.org/docs/app/getting-started/installation).
- [NestJS BullMQ queues](https://docs.nestjs.com/techniques/queues).
- [Prisma transactions](https://www.prisma.io/docs/orm/fundamentals/transactions).
- [Firebase Cloud Messaging cho Flutter](https://firebase.google.com/docs/cloud-messaging/flutter/get-started).
- [Next.js chạy Node.js server](https://nextjs.org/docs/app/getting-started/deploying).
- [shadcn/ui với Vite](https://ui.shadcn.com/docs/installation/vite).
- [Turborepo workspace structure](https://turborepo.dev/docs/crafting-your-repository/structuring-a-repository).
- [S3 compatibility của R2](https://developers.cloudflare.com/r2/api/s3/api/).
- [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).

## Review Technical vòng 1 — 2026-10-21 (lịch sử đề xuất)

User yêu cầu chuyển sang trao đổi Technical. Chưa xác nhận thêm stack hoặc freeze gate.

### Gói đề xuất để review

- TD-005/006: cùng repo; pnpm/Turborepo quản lý TypeScript; Flutter dùng toolchain riêng. NestJS modular monolith, REST/OpenAPI dùng chung cho ba client; API và worker là các process riêng cùng code nghiệp vụ.
- TD-007/009/010: Next.js storefront; React/Vite admin; Tailwind/shadcn UI web; Prisma/PostgreSQL; Redis/BullMQ cho job nền.
- TD-011/016/017: object storage tương thích S3, FCM Flutter; deploy native, không Docker. Đề xuất Linux VPS, Nginx reverse proxy, systemd quản lý Node processes; tài nguyên/provider phụ thuộc máy sẵn có và ngân sách.
- TD-013: PostgreSQL sở hữu số dư/loyalty, ledger riêng, transaction và kiểm soát đồng thời/idempotency. Redis không phải sổ tiền. Outbox đề xuất để commit giao dịch rồi gửi việc nền, có retry không trùng.
- Đề xuất auth admin email + mật khẩu + TOTP; khách vẫn SĐT + OTP. Đây là phương án để user review, chưa phải quyết định được duyệt.
- Kiểm thử trọng tâm: checkout đồng thời với rút tiền, retry xác nhận/hoàn đơn, cutoff 22h và giới hạn 7 ngày, hoàn/thu hồi loyalty. Staging/production tách dữ liệu và secrets; backup ngoài máy và kiểm tra khôi phục trước release.
- Chưa pin phiên bản package hoặc suy diễn API Prisma theo phiên bản cũ; xác minh tương thích Node/Nest/ORM khi freeze stack.

### Cần user cung cấp/chốt trong vòng này

1. Có đồng ý gói stack/kiến trúc đề xuất trên hay muốn thay thành phần nào?
2. Admin đăng nhập email + mật khẩu + TOTP hay muốn phương thức khác?
3. Đã có server/domain chưa; ngân sách hạ tầng mỗi tháng dự kiến bao nhiêu?
4. Đã có SMS OTP provider, Zalo OA, Firebase project chưa; nếu chưa, tiếp tục thiết kế adapter và chọn dịch vụ sau?
5. Mã nguồn/CI dùng GitHub hay GitLab, có repository sẵn chưa?

### Tài liệu đã đối chiếu cho vòng review

- [Prisma transactions](https://www.prisma.io/docs/orm/fundamentals/transactions).
- [NestJS queues](https://docs.nestjs.com/techniques/queues).
- [Next.js self-hosting và reverse proxy](https://nextjs.org/docs/app/guides/self-hosting).
- [FCM Flutter](https://firebase.google.com/docs/cloud-messaging/flutter/get-started).
- [shadcn/ui Vite](https://ui.shadcn.com/docs/installation/vite).

## Kết quả vòng 1 — 2026-10-21

- Duyệt gói TD-019 gồm TD-005/006/007/009/010/011/013/016/017; chưa freeze toàn bộ Technical/schema/contracts.
- Một số account admin cố định user tạo, tài khoản/mật khẩu không OTP/TOTP; giữ RBAC/audit TD-020, thay phương án một account/TOTP.
- Server user có sẵn TD-022, không tiếp tục hỏi mua máy/ngân sách. GitHub TD-023; GitHub Actions Proposed.
- Google/Facebook/Apple khách bản đầu, phone + OTP sau TD-021. Chưa có account OTP/Zalo/Firebase; không tự bỏ Zalo/push vì chưa có account.
- Firebase Authentication đề xuất riêng TD-024 cho social login web/Flutter. NestJS verify ID token/map user TPX; nghiệp vụ vẫn PostgreSQL. FCM đã duyệt không đồng nghĩa Firebase Auth đã duyệt.
- Đề xuất SĐT nhận hàng nhập checkout, trạng thái xác minh riêng; link thêm login method vào user hiện có để giữ đơn/tiền/điểm, không tự gộp theo email/phone.

Nguồn: [Firebase social login](https://firebase.google.com/docs/auth/flutter/federated-auth), [verify ID token](https://firebase.google.com/docs/auth/admin/verify-id-tokens), [link provider](https://firebase.google.com/docs/auth/flutter/account-linking).

## PRD toàn hệ thống v0.1 — 2026-10-21

- Firebase Authentication đã duyệt TD-025; SĐT nhận hàng nhập checkout chưa cần OTP D-089. Các phần trước có nhãn lịch sử đề xuất không còn là câu hỏi chưa chốt về hai điểm này.
- [PRD overview](../2-PRD/00-prd-overview.md): 21 feature specs, 63 screens/routes, 118 API operations, 68 bảng logic, 104 feature AC, 42 QA scenarios và18 NFR.
- Data/API/state/security là phụ lục thiết kế để review, chưa schema/migration/code. [P-001–012](../2-PRD/11-review-decisions.md) là proposal cho những chi tiết chưa được duyệt, không được âm thầm coi thành business rule.
- Hồ sơ đủ để review PRD và chuẩn bị design/task decomposition; Technical freeze/implementation chưa được mở chỉ vì tài liệu đã soạn xong.
