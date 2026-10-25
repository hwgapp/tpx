# Test Plan — TPX

> PRD v0.1 — Draft strategy để review. Chưa có implementation hoặc product test results. Tập trung verification theo rủi ro; docs task chỉ kiểm tra nhất quán và số học, không tạo unit tests giả lập implementation.

| Layer | Phạm vi | Dữ liệu/môi trường | Điều kiện |
| --- | --- | --- | --- |
| Domain/unit | Cutoff/date+7, allocations, points caps/earn, cumulative refunds, state guards | Clock injection; fixtures có cả missing/zero/boundary | Business policy phải được duyệt trước code |
| DB integration | Transactions, FK/unique, idempotency, concurrent checkout/rút/refund/complete | Native PostgreSQL disposable, Redis native khi cần; không Docker/Testcontainers | Thực chạy cạnh tranh, không chỉ mock repository |
| API/contract/security | DTO/error, ownership/admin permissions, auth exchange/rotation, provider fakes | Seed accounts/users/variants không có secret thật | Token sai/provider fail, unknown outcome, stale version |
| Worker/fault recovery | Outbox crash windows, Redis restart, retry/referral dedupe, reminder consent | DB+queue thật, fake external providers có deterministic failures | Retry không tạo money/point duplicate |
| Web/admin E2E | Catalog→checkout→bankconfirm→batch→delivery→complete; cancel/withdraw/refund | Staging seeded dataset, browser routes/cookies | Admin/customer contexts riêng, one failure path mỗi critical flow |
| Flutter integration/manual | Google/FB/Apple, deep link/push, secure session, offline/resume/cutoff | iOS/Android thiết bị thật + staging configs | Provider credentials sẵn sàng trước nghiệm thu |
| Ops/performance | Migrations dry-run, backup restore/reconcile, load profile target | Staging trên server được cung cấp, dữ liệu khôngproductionPII | TargetsP-012 chưa là SLA hoặc số đo hiện tại |

## QA scenarios

Đủ42 scenario QA-001–042 được mô tả tại [acceptance criteria](../2-PRD/09-acceptance-criteria.md); [traceability](12-traceability-matrix.md) bảo đảm mọi feature có scenario. Không viết test chỉ mirror implementation, ưu tiên invariant/boundary/concurrency/permission và failure có ý nghĩa.

## Critical suites bắt buộc trước release

1. Social3 providers/owner isolation/admin noOTP; không tạo role từ client, không merge user theo email/contact.
2. Mixed checkout và allocation: retry/idempotency, funds cạnh tranh rút, quote đổi, zero bank due.
3.22h boundary, ngày giao+7, future batch mapping; UI clock/job chậm không đổi guard.
4. Manual receipts thiếu/thừa/muộn/unpaid override; không giảPAID.
5. Procurement snapshot/BOM/unit conversion, quality case/prep/delivery fail, complete earn/referral once.
6. Withdraw200k/150k, cancel/reject/approve/processing/paid, hai admin, unknown bank outcome.
7. Partial/full refund và pending cap, points return khác earn revoke, debt proposal và refund trướccomplete.
8. Notification consent/token reassignment/providerfail, retrykhôngrollbackdomain, reminder sau cutoff skip.
9. Ledger projection reconcile sau crash/restart, migration/restore và production config validation.

## Commands sau khi tạo skeleton

Các lệnh dưới là **contract script đề xuất**, chưa tồn tại ở repo hiện tại và chưa được chạy. Pin toolchain và tạo package scripts đúng tên khi Technical freeze; không ghi nhận chúng pass từ tài liệu.

| Area | Script dự kiến | Lưu ý |
| --- | --- | --- |
| TypeScript checks | pnpm lint; pnpm typecheck | Scope web/admin/api/worker |
| Domain/backend | pnpm --filter api test; pnpm --filter api test:integration | PostgreSQL native test DB riêng |
| Web/admin E2E | pnpm test:e2e | Browser contexts owner/admin riêng |
| Flutter | flutter analyze; flutter test; flutter test integration_test | Chạy từ code/apps/mobile sau khi được tạo; thiết bị phù hợp |
| Builds | pnpm build; flutter build appbundle; flutter build ios --no-codesign | Build không đồng nghĩa store-ready/signed release |
| Database | script migrate-test/restore-test được chốt sau ORM version | Không chạy migration production trong review PRD |

## Verification hiện tại cho task hồ sơ

- Kiểm tra local Markdown links, uniqueness/continuity IDs, all21 feature specs, screen/route/API/DB/AC/QA coverage và dependency references.
- Kiểm tra các ví dụ amount/caps/points/date/cutoff trong PRD bằng tính toán độc lập; đây là kiểm tra công thức tài liệu, không phải test backend chưa tồn tại.
- Kiểm tra decisions approved/superseded, phone login deferred, adminnoOTP, noDocker, giữscope R1P1, không hard-code ví dụ settings thành production default.

## Acceptance report sau implementation

Mỗi suite ghi commit/env/toolchain/data fixture, lệnh thật/thiết bị, expected/actual, pass/fail, log redacted và known gaps. Provider/device/restore chưa test thì giữ pending, không đổi trạng thái chỉ vì mocks pass.
