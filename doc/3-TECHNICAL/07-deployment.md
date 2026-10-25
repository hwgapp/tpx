# Deployment

> Không Docker TD-015; native Linux/Nginx/systemd đã duyệt TD-019. Server user có sẵn TD-022, không khảo sát mua máy/ngân sách. Chưa truy cập server/deploy.

## Environments

| Environment | Purpose | URL/App Target | Notes |
| --- | --- | --- | --- |
| Local | Dev | TBD | TBD |
| Staging | Kiểm tra trước release | TBD | Database, queue, bucket và cấu hình thông báo tách production |
| Production | Vận hành thử nghiệm/thật | TBD | Server user có sẵn; cấu hình kết nối lúc triển khai |

## Build / Release

Đã duyệt NestJS API/worker và Next.js native bằng Node.js; admin React/Vite static; Linux/Nginx/systemd TD-019 trên server user có sẵn. Cấu hình cụ thể lúc triển khai. PostgreSQL/Redis cài native hoặc dùng managed, có lưu trữ bền vững, backup và thử khôi phục. Local và CI không yêu cầu Docker.

CI cho TypeScript chạy kiểm tra types, tests nghiệp vụ, build và migration validation; Flutter chạy kiểm tra/phân tích/build bằng toolchain Flutter/Dart riêng. Lệnh và phiên bản cụ thể chốt trong test plan. Mobile build/release bằng Flutter và công cụ ký/phát hành iOS/Android; không dùng Expo. Không đặt cutoff 22:00 chỉ trong lịch chạy worker.

GitHub TD-023 cho mã nguồn. Đề xuất GitHub Actions CI kiểm tra/build PR; workflow và quyền deploy tách riêng. Chưa tạo repo, push hoặc deploy.
