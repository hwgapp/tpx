# Release Scope — bản đầy đủ R1

> PRD v0.1 — Draft review. R1 bao phủ toàn bộ21 features và cả web/iOS/Android/admin/backend. PriorityP1 là thứ tự thực hiện, không tự loại khỏi release. Chưa có ngày phát hành hoặc commit triển khai.

| Release | Included | Excluded/later | Exit criteria |
| --- | --- | --- | --- |
| R1 | F-001–021; web storefront, Flutter iOS/Android, admin RBAC, API/worker/DB, social3 providers, thủ công bank transfer, balance/rút, loyalty/referral, catalog/BOM, gom mua/sơ chế/giao, content/review/repeat/reminders, Zalo/push | Phone+OTP sau; COD, auto bank reconcile, marketplace, tự nạp, farm traceability/story, crawler chưa giao; không ReactNative/Expo/Docker | User review policy money/state, Technical/design ready, critical QA/AC + NFR được chấp nhận, provider thật/config data/backup restore, release checklist |

## Delivery slices để triển khai sau review

1. Foundation: fixed admin/password/RBAC + Firebase customer identities/sessions, settings/version và audit; catalog RAW/MEAL/BOM/media.
2. Commerce: cart/quote/date/contact, money/points core và order transaction, manual bank confirmation, customer order states.
3. Operations: procurement batches/decisions/BOM aggregation, purchase/quality/preparation/delivery, complete accrual.
4. Finance exceptions: balance history, withdrawals, agreements/refunds/returns/revocations/debt proposal, reconciliation.
5. Engagement và production readiness: transparency/reviews/referral/reorder/frequent, notifications/reminders, dashboards/reports, performance/security/recovery, store distribution.

Slices là thứ tự nghiệm thu nội bộ; chưa phải chia MVP làm mất featureR1. Không mở public money flows chỉ vì đã có giao diện mà chưa hoàn thiện ledger/guards.

## Dữ liệu và tích hợp cần trước release

| Nhóm | Cần có | Hành vi khi chưa sẵn |
| --- | --- | --- |
| Firebase/customer OAuth | Project theo môi trường, Google/Meta/Apple app/client IDs, callbacks/domains, app capabilities/credentials | Mock chỉ ở tests; không báo social login đã chạy production |
| FCM và Zalo | Device/push configs, Apple push credentials, OA/service/template hợp lệ và quyền gửi | Queue/adapter còn giữ scope; hiển thị thiếu config, không fake gửi thành công hoặc bỏ kênh âm thầm |
| Sales configuration | Địa bàn/slot, bank nhận tiền, fees/minimum/caps/rewards, catalog/prices/spec/BOM/ảnh/hướng dẫn/chính sách | Checkout/publish validation fail rõ; không lấy giá trị ví dụ làm default |
| Admin | Account cố định user tạo, password provision an toàn và quyền, không OTP | Không public signup, không seedpassword mặc định |
| Hosting | Server user có sẵn, DB/Redis/S3 connectivity/secrets/env/reverseproxy/process setup | Chỉ cấu hình khi triển khai, không khảo sát mua server/ngân sách lại |
| GitHub/CI/mobile distribution | Repository URL/access, native CI runners, signing và AppStore/Play setup | Chưa tự tạo repo/push/deploy; chưa chốt public store release chỉ từ PRD |

## Exit checklist

- [ ] P-001–019 có kết luận review, đặc biệt money/withdraw/refund/points debt/complete guard.
- [ ] Toàn bộ screens/flows/permissions có design và thực thi đúng AC web/app/admin.
- [ ] DB migrations/constraints/concurrency/idempotency/reconcile được kiểm thử trên PostgreSQL native, không Docker.
- [ ] Cả3 social providers và push/Zalo test thực; không lấy mock kết quả làm nghiệm thu production.
- [ ] Native CI build/test, secrets tách môi trường, audit không PII/credentials, backup restore và fault recovery pass.
- [ ] Dữ liệu production/khung giao/vùng/fees/caps/rewards được TPX cấu hình và kiểm tra.
- [ ] QAcritical/knownissues và store/release checklist được review; thời điểm release do user chốt sau.

Tất cả ô trên đang chưa hoàn thành vì đây là giai đoạn chuẩn bị PRD. Không đánh dấu product tested/released hoặc freeze gate khi chỉ kiểm tra docs.
