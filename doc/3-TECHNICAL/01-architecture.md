# Architecture

> Cập nhật 2026-10-21; gói kiến trúc/stack duyệt TD-019, chưa freeze schema/contracts. Admin TD-020, social login TD-021, Firebase Auth Proposed TD-024. Flutter/không Docker giữ nguyên.

## Goals

- Bao phủ web, admin, iOS/Android và hai nhóm mua hàng trong cùng một đơn.
- Tổ chức backend theo module nghiệp vụ; giữ logic giá, tiền và quyền ở API.
- Hỗ trợ xử lý lại job an toàn, truy vết thao tác admin và kiểm thử giao dịch.

## System Context

Storefront Next.js, Admin React/Vite và mobile Flutter -> REST API NestJS -> PostgreSQL. Worker chạy job nền từ Redis/BullMQ, gửi thông báo qua adapter OTP/Zalo/push và xử lý sự kiện có thể retry. Push Flutter dùng Firebase Cloud Messaging theo TD-019. Ảnh catalog lưu object storage tương thích S3. Stack/tooling đã duyệt TD-019; Firebase Auth là đề xuất riêng TD-024.

## Module Boundaries

| Module | Responsibility | Notes |
| --- | --- | --- |
| Identity/Access | Social login khách, account admin cố định, phiên và RBAC | Google/Facebook/Apple; admin không OTP; phone sau; Firebase Auth Proposed |
| Catalog | Sản phẩm thô, món sơ chế, quy cách/khẩu phần, giá công bố | Hai loại có variant để đưa vào giỏ chung |
| Recipes | Thành phần/định lượng theo khẩu phần món sơ chế | Phục vụ thu mua/sơ chế; không tự tính lại giá bán |
| Cart/Pricing | Giỏ chung, báo giá và phân bổ điểm/số dư | Thứ tự và công thức theo D-070/075/081/082; thời điểm giữ/trừ còn OQ-023 |
| Orders | Đơn/dòng đơn, snapshot, trạng thái, cutoff/ngày giao | Cần freeze state machine ở PRD |
| Payments | Xác nhận chuyển khoản và lịch sử thu tiền | COD hoãn, không tự coi duyệt mua là đã thanh toán |
| CustomerBalance | Tiền hoàn, điều chỉnh theo đơn, yêu cầu rút ngân hàng | Transaction/audit, quy trình rút còn mở |
| Loyalty/Referral | Tích/dùng điểm và giới thiệu bạn bè | Dùng 1 điểm giảm 1.000đ, không rút tiền; mức thưởng settings, xử lý chống trùng |
| Procurement | Gom nhu cầu trước cutoff, nhân viên duyệt mua/loại | Tổng hợp nguyên liệu thô + cấu thành món |
| Fulfillment/Delivery | Tập kết, sơ chế, đóng gói, phân công và ghi nhận giao | Không quota khung giờ; quyền thao tác cần chốt |
| Content/Reviews | Thông tin minh bạch, ảnh và đánh giá khách đã mua | Luồng duyệt/hiển thị cần đặc tả |
| RepeatPurchase | Mua lại đơn, món thường mua, yêu cầu nhắc đặt | Kiểm tra lại giá/quy cách/khả dụng lúc mua lại |
| Notifications | Adapter OTP/Zalo/push, trạng thái gửi, retry | Tách sự kiện giao dịch khỏi việc gửi mạng |
| Settings/Audit | Cấu hình nghiệp vụ và lịch sử thay đổi | Không để thay đổi settings âm thầm sửa đơn đã đặt |

## Folder Structure

Cấu trúc repo đã duyệt TD-019 trong `code/` với `apps/api`, `apps/worker`, `apps/storefront`, `apps/admin`, `apps/mobile`; pnpm quản lý các app TypeScript, Flutter/Dart dùng toolchain riêng. Flutter có models/API client theo contract REST/OpenAPI; không import trực tiếp package TypeScript. Tokens thương hiệu có thể xuất theo từng nền tảng. Chưa tạo app/package trước khi freeze Technical.
