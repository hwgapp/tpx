# API Contract Map

> PRD v0.1 — Draft. Các endpoint/DTO là thiết kế đề xuất để review, không phải OpenAPI/code đã generate. Dùng prefix `/api/v1`; [P] trong permission là policy còn review.

| Contract ID | Feature | Method / endpoint | Quyền | Input | Output | Errors |
| --- | --- | --- | --- | --- | --- | --- |
| API-001 | F-001 | POST /auth/firebase | Public | firebase_id_token, client_type, installation_id tùy platform | user, customer session; is_new_user | 401/409/422/429/503 |
| API-002 | F-001 | POST /auth/refresh | Customer refresh session | refresh token/cookie, device binding | session mới/rotation | 401/409/429 |
| API-003 | F-001 | POST /auth/logout | Customer | current hoặc all sessions [P] | revocation result | 401/403/404/409/422 |
| API-004 | F-001 | GET /me | Customer own | — | profile, identities, contact verification, permissions | 401/403/404/409/422 |
| API-005 | F-001 | PATCH /me | Customer own | name, contact_phone; profile version | profile cập nhật | 401/403/404/409/422 |
| API-006 | F-001 | POST /me/identities/sync | Customer own + reauth | fresh Firebase token cùng firebase_uid, provider state từ server | danh sách identities verified; không merge users | 401/403/404/409/422 |
| API-007 | F-001 | DELETE /me/account | Customer own + reauth [P] | request reason/confirmation | deletion request; outstanding settlement summary | 401/403/404/409/422 |
| API-008 | F-004 | GET /me/addresses | Customer own | pagination | addresses | 401/403/404/409/422 |
| API-009 | F-004 | POST /me/addresses | Customer own | recipient, phone, area_id, address, default | address | 401/403/404/409/422 |
| API-010 | F-004 | PATCH /me/addresses/:id | Customer own | fields + version | address | 401/403/404/409/422 |
| API-011 | F-004 | DELETE /me/addresses/:id | Customer own | version | removed saved address; order snapshots unchanged | 401/403/404/409/422 |
| API-012 | F-002 | GET /catalog/categories | Public | active filter | categories | 422/503 |
| API-013 | F-002 | GET /catalog/products | Public | query/category/kind/cursor/limit | products+variants summary | 422/503 |
| API-014 | F-002 | GET /catalog/products/:id | Public | id hoặc resolved slug | product/variants/availability/media | 404/503 |
| API-015 | F-003 | GET /catalog/meals | Public | query/portion/cursor/limit | meal summaries | 422/503 |
| API-016 | F-003 | GET /catalog/meals/:id | Public | meal id | meal, portions, supplied ingredients, instructions, availability | 404/503 |
| API-017 | F-015 | GET /content/:slug | Public | slug | published content/metadata | 404/503 |
| API-018 | F-016 | GET /catalog/products/:id/reviews | Public | cursor/limit | published verified reviews, average | 404/422/503 |
| API-019 | F-004 | GET /me/cart | Customer own | — | cart/version, repricing warnings | 401/403/404/409/422 |
| API-020 | F-004 | PUT /me/cart/items/:variantId | Customer own | qty, cart_version | cart updated | 401/403/404/409/422 |
| API-021 | F-004 | DELETE /me/cart/items/:variantId | Customer own | cart_version | cart updated | 401/403/404/409/422 |
| API-022 | F-004 | POST /checkout/quotes | Customer own | cart_version, recipient/phone/address, date/slot, use_points | quote_id, expiry, version, money allocation, cutoff, issues | 401/403/404/409/422 |
| API-023 | F-004 | POST /orders | Customer own | quote_id, current cart/config version, key | order, snapshot, funding state, bank instructions, cash_order_hold/points_hold summary D-099 | 401/403/404/409/422 |
| API-024 | F-004 | GET /me/orders | Customer own | status/date/cursor/limit | own orders | 401/403/404/409/422 |
| API-025 | F-004 | GET /me/orders/:id | Customer own | order id | detail, timeline, available actions, source allocations | 401/403/404/409/422 |
| API-026 | F-005 | POST /me/orders/:id/transfer-notices | Customer own [P] | amount/reference/message optional | notice submitted, NOT PAID | 401/403/404/409/422 |
| API-027 | F-008 | GET /delivery/options | Public or Customer | area_id, server uses current clock | server_time, earliest/latest, slots, cutoff | 404/422/503 |
| API-028 | F-008 | GET /service-areas | Public | active | configured areas | 503 |
| API-029 | F-010 | GET /me/balance | Customer own | — | available/held_order/pending_withdrawal/total, version | 401/403/404/409/422 |
| API-030 | F-010 | GET /me/balance/entries | Customer own | cursor/limit | redacted ledger | 401/403/404/409/422 |
| API-031 | F-011 | POST /me/withdrawals | Customer own | amount, bank code/account/name, key | withdrawal + updated available/pending | 401/403/404/409/422 |
| API-032 | F-011 | GET /me/withdrawals | Customer own | cursor/status | own withdrawals | 401/403/404/409/422 |
| API-033 | F-011 | GET /me/withdrawals/:id | Customer own | id | own withdrawal detail | 401/403/404/409/422 |
| API-034 | F-011 | POST /me/withdrawals/:id/cancel | Customer own [P] | version/key | CANCELLED, released balance | 401/403/404/409/422 |
| API-035 | F-012 | GET /me/loyalty | Customer own | — | available/held/total_points, rate, caps summary; post-complete refund giữ ORDER_EARN D-100 | 401/403/404/409/422 |
| API-036 | F-012 | GET /me/loyalty/entries | Customer own | cursor/limit | point ledger | 401/403/404/409/422 |
| API-037 | F-013 | PUT /me/devices/:installationId | Customer own | platform/env/push_token, consent permission state | device token binding | 401/403/404/409/422 |
| API-038 | F-013 | DELETE /me/devices/:installationId | Customer own | — | token detached | 401/403/404/409/422 |
| API-039 | F-013 | GET /me/notifications | Customer own [P] | cursor/limit | notification center | 401/403/404/409/422 |
| API-040 | F-013 | PATCH /me/notifications/:id | Customer own [P] | read_at intent | notification read state | 401/403/404/409/422 |
| API-041 | F-020 | GET /me/notification-preferences | Customer own | — | per-channel consent/reminder settings | 401/403/404/409/422 |
| API-042 | F-020 | PUT /me/notification-preferences | Customer own | transactional preferences, marketing opt_in/channel, reminder schedule/version | preferences with recorded consent time | 401/403/404/409/422 |
| API-043 | F-017 | GET /me/referral | Customer own | — | code/link/reward terms/qualifying status | 401/403/404/409/422 |
| API-044 | F-017 | POST /me/referral/claim | Customer own [P] | referral code/key | attribution result | 401/403/404/409/422 |
| API-045 | F-018 | POST /me/orders/:id/reorder-preview | Customer own | mode append/replace [P] | eligible items, price/availability diffs; no mutation | 401/403/404/409/422 |
| API-046 | F-018 | POST /me/orders/:id/reorder | Customer own [P] | confirmed item choices, cart_version, mode | new cart only | 401/403/404/409/422 |
| API-047 | F-019 | GET /me/frequent-items | Customer own [P] | cursor/limit | own frequent/pinned items | 401/403/404/409/422 |
| API-048 | F-019 | PUT /me/frequent-items/:variantId | Customer own [P] | pinned/hidden | preference | 401/403/404/409/422 |
| API-049 | F-016 | POST /me/orders/:id/items/:itemId/review | Customer own [P] | rating/text/key | review PENDING | 401/403/404/409/422 |
| API-050 | F-021 | POST /me/orders/:id/cancel | Customer own | reason, version, key | cancel result, held-points release, cash resolution/refund case summary | 401/403/404/409/422 |
| API-051 | F-021 | GET /me/orders/:id/refunds | Customer own | order id | own adjustments/refund status | 401/403/404/409/422 |
| API-052 | F-009 | POST /admin/auth/login | Admin public entry | login/password | admin session cookie; NO OTP | 401/422/429/503 |
| API-053 | F-009 | POST /admin/auth/logout | Admin | — | session revoked | 401/403/404/409/422 |
| API-054 | F-009 | GET /admin/me | Admin | — | actor, roles/permissions | 401/403/404/409/422 |
| API-055 | F-009 | GET /admin/dashboard | dashboard.read | business date/range | operational counters with generated_at | 401/403/404/409/422 |
| API-056 | F-009 | GET /admin/accounts | access.manage | cursor/status | fixed admin accounts, no hashes | 401/403/404/409/422 |
| API-057 | F-009 | PATCH /admin/accounts/:id | access.manage [P] | status/role_ids/version/reason | updated account, revocation summary | 401/403/404/409/422 |
| API-058 | F-009 | GET /admin/roles | access.manage | — | roles/permissions catalog | 401/403/404/409/422 |
| API-059 | F-009 | PUT /admin/roles/:id/permissions | access.manage [P] | permission_ids/version/reason | role version | 401/403/404/409/422 |
| API-060 | F-009 | GET /admin/audit | audit.read | actor/entity/date/cursor | redacted append-only audit | 401/403/404/409/422 |
| API-061 | F-009 | GET /admin/customers | customers.read | query/cursor/limit | customer summaries | 401/403/404/409/422 |
| API-062 | F-009 | GET /admin/customers/:id | customers.read | id | profile/orders/ledger summaries by granted permissions | 401/403/404/409/422 |
| API-063 | F-002 | GET /admin/products | catalog.manage | query/status/kind/cursor | catalog management list | 401/403/404/409/422 |
| API-064 | F-002 | POST /admin/products | catalog.manage | product metadata/media/variants | draft product/version | 401/403/404/409/422 |
| API-065 | F-002 | PATCH /admin/products/:id | catalog.manage | metadata/status/version | product updated, impacted variants | 401/403/404/409/422 |
| API-066 | F-002 | PUT /admin/products/:id/variants | catalog.manage | variants/ingredient mappings/version | validated variants, warnings | 401/403/404/409/422 |
| API-067 | F-003 | GET /admin/ingredients | catalog.manage | query/status | ingredients | 401/403/404/409/422 |
| API-068 | F-003 | POST /admin/ingredients | catalog.manage | name/base_unit | ingredient | 401/403/404/409/422 |
| API-069 | F-003 | PATCH /admin/ingredients/:id | catalog.manage | available/unit metadata/version/reason | ingredient, affected products/meals | 401/403/404/409/422 |
| API-070 | F-003 | POST /admin/meals | catalog.manage | product metadata/portion variants | draft meal | 401/403/404/409/422 |
| API-071 | F-003 | GET /admin/meals/:id | catalog.manage | id | recipe versions/variants/instructions | 401/403/404/409/422 |
| API-072 | F-003 | POST /admin/meals/:id/recipe-versions | catalog.manage | BOM per variant/instructions/source/version | new immutable recipe version, publish issues | 401/403/404/409/422 |
| API-073 | F-003 | PATCH /admin/meals/:id | catalog.manage | metadata/manual_enabled/active_recipe/version | meal, effective availability | 401/403/404/409/422 |
| API-074 | F-004 | GET /admin/orders | orders.read | date/status/payment/procurement/cursor | order list | 401/403/404/409/422 |
| API-075 | F-004 | GET /admin/orders/:id | orders.read | id | detail/actions by permission, source snapshots | 401/403/404/409/422 |
| API-076 | F-005 | GET /admin/payments | payments.confirm | status/date/cursor | receipts and orders needing confirmation | 401/403/404/409/422 |
| API-077 | F-005 | POST /admin/orders/:id/payment-receipts | payments.confirm | actual amount/date/bank ref/reason/version/key | receipt/funding status; excess case if applicable | 401/403/404/409/422 |
| API-078 | F-006 | GET /admin/procurement/batches | procurement.manage | delivery_date/status/cursor | batch list | 401/403/404/409/422 |
| API-079 | F-006 | POST /admin/procurement/batches/build | procurement.manage | delivery_date/key | batch build version; retry no duplicate | 401/403/404/409/422 |
| API-080 | F-006 | GET /admin/procurement/batches/:id | procurement.manage | id | orders/decisions/ingredient totals/sources | 401/403/404/409/422 |
| API-081 | F-006 | POST /admin/procurement/batches/:id/decisions | procurement.manage; thêm procurement.unpaid_override nếu unpaid | order_ids/decision/unpaid reason/version/key | decisions, updated totals; override checked separately | 401/403/404/409/422 |
| API-082 | F-006 | POST /admin/procurement/batches/:id/purchases | procurement.manage | ingredient quantities/cost/quality/reason/version/key | purchase receipt, shortages/cases | 401/403/404/409/422 |
| API-083 | F-006 | GET /admin/procurement/batches/:id/export | procurement.manage [P] | format csv | ingredient list/source summary; export audit | 401/403/404/409/422 |
| API-084 | F-007 | GET /admin/fulfillment | fulfillment.manage | date/stage/cursor | preparation tasks | 401/403/404/409/422 |
| API-085 | F-007 | POST /admin/fulfillment/:id/transitions | fulfillment.manage | target_stage/checklist/version/key | task/order events | 401/403/404/409/422 |
| API-086 | F-007 | GET /admin/deliveries | delivery.manage | date/slot/status | delivery board | 401/403/404/409/422 |
| API-087 | F-007 | POST /admin/deliveries/:id/transitions | delivery.manage | target/outcome/reason/version/key, explicit admin funding override decision if dispatch unpaid | delivery state/case; no implicit refund | 401/403/404/409/422 |
| API-088 | F-007 | POST /admin/orders/:id/complete | orders.complete | delivery result/version/key | COMPLETED, once-only points capture + accrual/referral event; complete-unpaid guard OQ-050 | 401/403/404/409/422 |
| API-089 | F-010 | GET /admin/customers/:id/balance-entries | balance.read | cursor | own customer financial ledger if authorized | 401/403/404/409/422 |
| API-090 | F-010 | POST /admin/orders/:id/balance-credits | balance.adjust | approved adjustment_id/amount/reason/key | linked balance credit; not arbitrary top-up | 401/403/404/409/422 |
| API-091 | F-011 | GET /admin/withdrawals | withdrawals.manage | status/date/cursor | redacted withdrawal queue | 401/403/404/409/422 |
| API-092 | F-011 | GET /admin/withdrawals/:id | withdrawals.manage | id | withdrawal + allowed actions | 401/403/404/409/422 |
| API-093 | F-011 | POST /admin/withdrawals/:id/transitions | withdrawals.manage [P] | approve/reject/claim-processing/mark-paid, reference/reason/version/key | new state/balance effect | 401/403/404/409/422 |
| API-094 | F-012 | GET /admin/customers/:id/loyalty-entries | loyalty.read | cursor | point ledger HOLD/CAPTURE/RELEASE/earn/return; D-100 giữ ORDER_EARN, không debt | 401/403/404/409/422 |
| API-095 | F-013 | GET /admin/notifications | notifications.manage | channel/status/date/cursor | delivery attempts/errors, no credentials | 401/403/404/409/422 |
| API-096 | F-013 | POST /admin/notifications/:id/retry | notifications.manage | reason/key | requeued if event/current consent valid | 401/403/404/409/422 |
| API-097 | F-014 | GET /admin/settings | settings.manage | section | active version+validation schema, secrets redacted | 401/403/404/409/422 |
| API-098 | F-014 | POST /admin/settings/versions | settings.manage | section/value/effective_at/reason/version/key | validated new version | 401/403/404/409/422 |
| API-099 | F-014 | GET /admin/reports | reports.read [P] | business date range/basis created-or-delivery | metric definitions/data/cost completeness | 401/403/404/409/422 |
| API-100 | F-015 | POST /admin/media/upload-intents | content.manage | MIME/size/checksum/purpose | restricted signed upload + media id | 401/403/404/409/422 |
| API-101 | F-015 | POST /admin/media/:id/finalize | content.manage | storage key/checksum/source | validated asset ready | 401/403/404/409/422 |
| API-102 | F-015 | GET /admin/content | content.manage | status/slug | content drafts/published | 401/403/404/409/422 |
| API-103 | F-015 | PUT /admin/content/:slug | content.manage | body/media/status/version/source | content version | 401/403/404/409/422 |
| API-104 | F-016 | GET /admin/reviews | reviews.moderate | status/cursor | review moderation queue | 401/403/404/409/422 |
| API-105 | F-016 | POST /admin/reviews/:id/moderate | reviews.moderate [P] | publish/hide/reason/version/key | review moderation state, aggregate invalidated | 401/403/404/409/422 |
| API-106 | F-017 | GET /admin/referrals | loyalty.read | user/status/cursor | attribution/reward status | 401/403/404/409/422 |
| API-107 | F-021 | GET /admin/cases | adjustments.manage | type/status/date/cursor | exception cases | 401/403/404/409/422 |
| API-108 | F-021 | POST /admin/orders/:id/cases | adjustments.manage | affected items/type/reason | case OPEN | 401/403/404/409/422 |
| API-109 | F-021 | POST /admin/cases/:id/agreements | adjustments.manage | plan/evidence/actor/reference/version/key | agreed adjustment plan; no implicit credit | 401/403/404/409/422 |
| API-110 | F-021 | POST /admin/orders/:id/refund-previews | refunds.manage | agreement/items/cash_goods/cash_shipping/cash_excess/points/original_sources/method | remaining caps/reversal preview/version; no effect | 401/403/404/409/422 |
| API-111 | F-021 | POST /admin/orders/:id/refunds | refunds.manage [P] | agreement_id/preview_id/allocations/reason/key | refund + per-leg state; debit/credit only once per leg | 401/403/404/409/422 |
| API-112 | F-021 | GET /admin/refunds | refunds.manage | status/date/cursor | refund queue | 401/403/404/409/422 |
| API-113 | F-021 | GET /admin/refunds/:id | refunds.manage | id | plan/legs/cumulative totals/allowed actions | 401/403/404/409/422 |
| API-114 | F-021 | POST /admin/refunds/:id/transitions | refunds.manage [P] | approve/claim-bank/mark-bank-settled/reject, leg_ids, group/reference/version/key | refund state, per-leg ledger effects | 401/403/404/409/422 |
| API-115 | F-021 | POST /admin/cases/:id/close | adjustments.manage | resolution/version/key | case CLOSED if all required legs resolved | 401/403/404/409/422 |
| API-116 | F-002 | GET /admin/categories | catalog.manage | kind/status/cursor | category management list | 401/403/422 |
| API-117 | F-002 | POST /admin/categories | catalog.manage | name/slug/kind/sort_order/active | validated category/version | 401/403/409/422 |
| API-118 | F-002 | PATCH /admin/categories/:id | catalog.manage | metadata/active/version; archive check references | category/version; active product conflicts if archive | 401/403/404/409/422 |
| API-119 | F-021 | POST /admin/orders/:id/cancel | orders.cancel [C D-094], contract draft | operation reason, agreement/refund resolution, version/key | CANCELLED, released cash/points holds, refund obligations separate; only actual received cash refundable | 401/403/404/409/422 |

## Contract chung

- API server tính giá, ngày giao, tiền/điểm và kiểm tra state; client không quyết quyền hoặc totals. ID path không thay ownership.
- Money là chuỗi số nguyên VND (`"200000"`); points là số nguyên không phần lẻ; quantity decimal dùng chuỗi kèm unit. Timestamp ISO8601 UTC, ngày giao `YYYY-MM-DD` theo Asia/Ho_Chi_Minh.
- Mutation tiền/state có `Idempotency-Key`, `expected_version` (hoặc If-Match được thống nhất khi freeze API). Trùng key/cùng payload trả kết quả cũ; khác payload trả409; version cũ409.
- GET list có cursor/limit (đề xuất20, tối đa100), filters allowlist; không có GET thay đổi tiền/trạng thái.
- `reorder-preview` và `refund-previews` dùng POST để nhận payload nhưng chỉ đọc/tính, không phát ledger/event tài chính.
- Lỗi trả code ổn định, message Việt, field_errors, request_id, retryable; không trả stack trace/secrets. Quy ước chi tiết tại [API design](../3-TECHNICAL/03-api-design.md).
- Token exchange không đòi SMS OTP. Admin password flow riêng; không cung cấp public endpoint tạo admin. Phone auth endpoints chưa thuộc R1.

## Flow audit addendum — contracts còn thiếu

Baseline vẫn118 operations, chưa thêm endpoint hoặc sửa DTO chỉ từ mockup. [16 action/capability gaps](../4-DESIGN/15-action-contract-gaps.md) chỉ rõ cart merge/recovery, unmatched/correction, terminal resolution, supplemental payment, shortage allocation, my-review, impact queues, admin/deletion và payout recovery. Gap có thể giải bằng read DTO/subview/SDK/runbook hoặc contract mới sau review; chưa coi controls tương ứng là implementation-ready.
