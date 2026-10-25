# API Design và DTO contracts

> Technical appendix PRD v0.1 — Draft review. REST/OpenAPI đã chốt TD-019. Đây là contract thiết kế; chưa có OpenAPI generated hoặc code chạy. Danh mục118 operations: [product API map](../2-PRD/06-api-contract-map.md).

## 1. Protocol và dữ liệu

- Base `/api/v1`; HTTPS; UTF-8 JSON. Public catalog/content, customer `/me`, admin `/admin`. Không dùng frontend route guards thay API authorization.
- UUID opaque cho IDs; mã order public riêng để chuyển khoản/hỗ trợ. Path chứa orderId không đủ quyền xem đơn.
- Money chuỗi số nguyên VND (`"200000"`), không dấu ngăn cách/float; bigint arithmetic server. Point fields là integer không fraction và trong range an toàn schema API. Pack count integer; physical quantities chuỗi decimal và unit cơ sở.
- Business dates `YYYY-MM-DD`; timestamp UTC ISO8601 cóZ; server trả `server_time`, `cutoff_at`, `earliest_date`, `latest_date`. Không lấy giờ máy khách làm guard.
- Lists: `{data:[], page:{next_cursor,has_more}, meta:{request_id,generated_at}}`; default20/max100 [P-011]. Chỉ filters/sorts allowlist, cursor không chứa secret.
- Single: `{data:{...}, meta:{request_id}}`; errors dưới đây. Mutation success trả resource/version và số dư sau transaction khi liên quan.

## 2. Xác thực và phiên [P-011 kỹ thuật]

1. Web/Flutter dùng Firebase SDK đăng nhập Google/Facebook/Apple. Lấy Firebase ID token gửi `/auth/firebase` qua HTTPS.
2. Backend Admin SDK verify chữ ký/issuer/audience/project/expiry; tra user theo verified Firebase UID/project. Không nhận user_id/email/role client làm bằng chứng. Khóa/unique chặn hai first-login tạo hai user.
3. Đề xuất exchange sang session TPX: web cookie HttpOnly/Secure, SameSite theo topology cùng site và kiểm soát CSRF/Origin; Flutter nhận bearer access và refresh lưu secure storage. Không trả token qua query string hoặc ghi log.
4. Customer access đề xuất15 phút/refresh30 ngày có rotation và revoke. Admin account/password session riêng audience ADMIN, idle30 phút/max8giờ, không OTP/TOTP. Các TTL là P-011, chưa chốt.
5. Local user/admin disabled hoặc quyền thay đổi phải được kiểm tra tại API, không đợi client tự logout. CORS chỉ origins cấu hình; không wildcard credentialed CORS.
6. Identity sync nhận fresh token cùng UID, server đọc canonical provider state. Link mới yêu cầu authenticated user/reauth; không tự merge users trùng email/phone. Phone sau link cùng user; SĐT contact chưa OTP không có quyền login.
7. Token/credential lifecycle trên Firebase và TPX cần test revoke, unlink-last, identity-already-in-use, Apple email ẩn/thiếu, OAuth user-cancel, redirect/deeplink resume. Không buộc profile có email từ mọi provider.

Nguồn: [Firebase ID token verification](https://firebase.google.com/docs/auth/admin/verify-id-tokens), [account linking](https://firebase.google.com/docs/auth/flutter/account-linking).

## 3. DTO trọng tâm

| DTO | Fields bắt buộc | Validation | Output/hành vi |
| --- | --- | --- | --- |
| FirebaseSessionInput | id_token, client_type WEB/MOBILE | đúng project/token; client_type không tự cấp quyền | user TPX, phiên phù hợp platform |
| AddressInput | recipient_name, contact_phone, area_id, address_lines | trường không rỗng, vùng phục vụ; phone normalize và chưa verified | address snapshot-ready; không tự login phone |
| CartItemInput | variant_id, pack_count, expected_cart_version | count>0/nguyên/đúngstep; variant hợp lệ | cart/version, warnings |
| QuoteInput | cart_version, recipient/address, delivery_date/slot_id, use_points BOOL | active/config/availability/cutoff/date+7, available money | QuoteDTO, không debit |
| QuoteDTO | quote_id, expires_at, server_time, G/F/B/P/D/T, cap_snapshot, cutoff_at, cart/config/variant_versions | tiền string, points integer; totals đối soát | client hiển thị breakdown, đồng ý trước đặt |
| PlaceOrderInput | quote_id, expected_cart_version, key | quote chưa hết hạn, revalidate mọi resource và account state | OrderDTO; transaction nếu bất kỳ guardfail rollback hết |
| OrderDTO | id/public_code, state, funding/refund/procurement, items snapshots, money breakdown, date/slot/cutoff, actions | owner data only; actions do server tính | không cần client suy diễn action từ label |
| ReceiptConfirmInput | amount_vnd, received_at, bank_ref, bank_account_id, reason, version, key | actual>0, dedupe bank receipt, source amount matched≤actual | actual/matched/excess và funding; khách notice khác command này |
| WithdrawalInput | amount_vnd, bank_code, account_number, holder_name, key | amount>0≤available, không điểm | request PENDING + available/pending mới |
| WithdrawalTransition | action, expected_version, key; reference nếu paid; reason khi reject | allowed state + permission, processing claim, unknown outcome guard | state/ledger delta đã commit |
| AgreementInput | case_id, affected_items, plan, customer_agreed_at, communication_reference | reference hợp lệ, authority, snapshot version | plan AGREED, chưa tự hoàn |
| RefundPreviewInput | agreement_id, lines/qty, cash_goods_vnd/cash_shipping_vnd/cash_excess_vnd/points_return, original sources, money_method | nguồn còn hoàn, số đã cam kết, points nguyên | preview_id/version, remaining caps, earn revoke/debt proposal |
| RefundCommitInput | preview_id, agreement_id, allocations, version, key | preview current, cumulative cap lock, source rights | refund/per-leg states; BANK không tự settled |
| SettingsInput | section, payload, expected_version, effective_at, reason | schema & semantic bounds; không secret | new version, impacted quotes, không sửa order cũ |

Input length/size cụ thể được đưa vào OpenAPI khi pin dependencies; đề xuất giới hạn hợp lý (text/profile không vô hạn, upload allowlist). Không coi giá trị UI là đủ validation server.

### Contract hoàn theo leg [P-003/006]

Refund parent transitions có `leg_ids` khi claim/settle ngân hàng, `transfer_group_id`, `bank_reference`, amount và expected version/key. Chỉ các legs cùng plan/destination được gom vào một lần chuyển; tổng amount phải khớp legs được chọn. Approve chỉ post internal legs; BANK vẫn pending. Reject chỉ trước posted/processing.

`RefundLegDTO` phân biệt `original_funding_id` hoặc `excess_receipt_id` với `payout_method`. Cash leg có goods/shipping/excess breakdown để ghi earn reversal đúng phần hàng đã hoàn, không theo phí hoặc tiền thừa. Receipt excess đã reserved/refunded không được match lại sang funding. API không dùng cùng một field source để vừa nói nguồn gốc vừa nói kênh hoàn.

## 4. Concurrency và idempotency

- `Idempotency-Key` bắt buộc với place/withdraw/cancel/payment/refund/credits/complete/batch decisions. Scoped actor+operation+key, request fingerprint; stored resource/result cùng transaction với effect.
- Key đang chạy: trả409 `OPERATION_IN_PROGRESS` kèm resource nếu có, client đọc lại; đã xong trả cùng resource, khác payload: 409 `IDEMPOTENCY_CONFLICT`.
- `expected_version`/If-Match cho resource mutable. Version stale409 `VERSION_CONFLICT`, không âm thầm last-write-wins trên tiền/state/settings.
- Mọi DB lock ordering thống nhất, transaction ngắn, không provider/network call trong lock. Retry deadlock/serialization bounded và giữ business key. Unique domain operation keys vẫn cần dù idempotency record đã hết TTL.
- Quote chỉ là báo giá: khi available bị rút/giá đổi/vùng tắt/22h qua thì không debit/đặt một nửa; trả409 và quote lại. Không tự giảm nguồn thanh toán rồi đặt mà khách chưa xác nhận breakdown mới.
- External bank transfer thủ công không có exactly-once API: PROCESSING claim và reconciliation trước retry. DB transaction không chứng minh đã chuyển ngân hàng.

## 5. Error catalog

| HTTP | code | Trường hợp | Client xử lý |
| --- | --- | --- | --- |
| 400/422 | VALIDATION_ERROR | fields sai/amountfraction/qty | field_errors, giữ form |
| 401 | AUTH_REQUIRED / TOKEN_INVALID / SESSION_REVOKED | chưa login/token sai/đã thu hồi | login/refresh một lần, không loop |
| 403 | PERMISSION_DENIED | không action permission | hiển thị quyền, không retry ngầm |
| 404 | RESOURCE_NOT_FOUND | không tồn tại hoặc không owner | không leak existence người khác |
| 409 | VERSION_CONFLICT / QUOTE_CHANGED | state/config/giá đổi | refetch+preview lại |
| 409 | INSUFFICIENT_AVAILABLE / INSUFFICIENT_POINTS | concurrent funds changed | cập nhật available/quote, không âm |
| 409 | CUTOFF_PASSED / DELIVERY_DATE_INVALID | qua22h/ngày không hợp lệ | đổi ngày/ẩn hủy theo server |
| 409 | ITEM_UNAVAILABLE / STATE_TRANSITION_INVALID | tắtbán/command sai state | hiển thị lý do và hành động hợp lệ |
| 409 | REFUND_LIMIT_EXCEEDED / BANK_RECONCILIATION_REQUIRED | đã hoàn/không rõ chuyển bank | giữplan, admin đối soát |
| 409 | IDENTITY_ALREADY_LINKED / LAST_IDENTITY | link/unlink sai | hướng dẫn reauth/support, không merge |
| 409 | IDEMPOTENCY_CONFLICT / OPERATION_IN_PROGRESS | key khác payload/đangxửlý | đọc resource trước retry |
| 429 | RATE_LIMITED | login/provider/command burst | Retry-After, không gửi liên tục |
| 502/503 | PROVIDER_UNAVAILABLE / DEPENDENCY_UNAVAILABLE | Firebase/S3/DB/queue không sẵn | trạng thái lỗi đúng, không fake success |

Error envelope: `{error:{code,message,field_errors?,retryable,resource_id?},meta:{request_id}}`. Không trả stack trace, SQL, hash/token hoặc thông tin tài khoản ngân hàng người khác.

## 6. Outbox và jobs

- Transaction domain ghi outbox; dispatcher enqueue BullMQ với event_id stable. Consumer dùng unique business operation key và durable outcome ở PostgreSQL.
- Batch chốt mua chỉ được final build từ cutoff_at; trước đó chỉ xem nhu cầu dự kiến. API/worker không được chuyển trạng thái để khóa hủy trước giờ khách được hủy.
- Jobs: batch.build(date), notification.deliver(event/channel/destination), reminder.schedule(date/user), loyalty/referral reconcile, catalog cache invalidate. Earn có thể được ghi ngay complete transaction để không hiển thị trễ; nếu dùng worker phải atomic unique và đọc remaining eligible mới nhất [P implementation].
- Job payload tối thiểu IDs, không token/secret/bank data; cần gửi thì worker đọc lại qua quyền nội bộ và current consent. Failed job queue có retry controlled, không mất source event khi Redis restart.
- API money fail closed khi DB unavailable. Gửi notification lỗi không rollback đơn; readiness phản ánh dependency để ops biết.

## Cấu hình danh mục, vùng và ngân hàng

Admin quản lý categories qua API-116–118; archive không xóa lịch sử, yêu cầu xử lý sản phẩm còn active trước khi ẩn danh mục đang dùng. Settings versions theo section SERVICE_AREAS/DELIVERY_SLOTS/BANKING/COMMERCE/LOYALTY/REFERRAL/REMINDERS đồng bộ dữ liệu normalized và version snapshot trong cùng transaction; không chỉ lưu JSON rồi bỏ mặc bảng vùng/khung/ngân hàng. Các section có schema/validation, active records cập nhật theo quyền settings.manage; đơn cũ giữ snapshot. Đây là thiết kế để review theo P-007/009.
