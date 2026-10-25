# Security và phân loại dữ liệu

> Technical appendix PRD v0.1 — Draft. Admin không OTP/TOTP TD-020; Firebase Auth đã duyệt TD-025; SĐT nhận hàng D-089. Session/retention chi tiết là P-011, chưa freeze. Không tạo account/credentials thật.

## Dữ liệu

| Loại | Lưu | Quyền xem | Bảo vệ |
| --- | --- | --- | --- |
| User/social identity/contact/address | PostgreSQL, Firebase chỉauth | Owner/admin có permission | ownership guard, mask list/log, không email/phone làm khóa merge |
| Bank nhận tiền TPX | PostgreSQL/config | Public thông tin đã công bố | validate version khi checkout |
| Bank rút/hoàn khách | Snapshot PostgreSQL | Owner/admin xử lý, danh sách che | encryption-at-rest theo hạ tầng, mask logs/analytics, không push payload |
| Money/points/order/receipts | PostgreSQL ledger+events | Owner/admin đúng quyền | constraints/transaction/idempotency/audit append-only |
| Admin password/session | Hash/secret store/backend | Không expose trên API | password hash, rate-limit, rotation/revoke session, không public signup/OTP |
| Provider keys/storage secrets | Backend/env/CI secrets | Server/service roles | tách môi trường, không settings public/Git/client bundle |

## Controls và abuse cases

1. Firebase verify ID token project/issuer/audience/expiry trước map user, kiểm tra local disabled; session admin audience khác customer. Không cho login social tạo quyền admin.
2. Web cookie HttpOnly/Secure và CSRF/Origin; allowlisted CORS; mobile secure token. Admin password rate-limit, hash; không yêu cầu thêm OTP/TOTP trái lựa chọn user.
3. Mọi resource owner check và permission server; ID guess của order/withdraw/refund trả404/403 phù hợp mà không leak. Role update/session revoke phải có hiệu lực API.
4. Link mới reauth cả user đang dùng và identity mới; không merge theo email/phone tự khai; Apple có thể email ẩn/thiếu không làm tài khoản mới bị buộc cùng email.
5. Money commands check bounds/version, rowlocks/conditional updates và unique operation keys. Retry không tạo tác dụng lặp; admin quyền full vẫn không được rút points hoặc sửa ledger posted.
6. Upload signed intent theo MIME/size/purpose, finalize kiểm tra object metadata/checksum; sanitize rich text/instructions/review; không render HTML/script tùy ý. CSV export escape cells có thể bị spreadsheet coi là formula.
7. Secrets, tokens, passwordhash, SĐT/địa chỉ/bank đầy đủ không vào analytics/stacktrace/log. Audit tài chính lưu actor/ref/reason và redacted before/after; kiểm tra quyền đọc audit.
8. Device token gắn đúnguser/env, detach khi logout/switch account; payload notification tối thiểu. Marketing consent riêng OSpermission, recheck ngay trước gửi.
9. Account deletion là request P-011: đang có đơn/withdraw/refund chưa giải quyết thì xử lý nghĩa vụ trước anonymization; không xóa giao dịch tài chính để làm số dư biến mất. Retention cần user quyết định trước release, không tự áp số ngày.
10. Backup/restore kiểm tra quyền và dữ liệu tách môi trường; staging không gửi Zalo/push thật cho khách production. Không đưa credentials thật vào seed/demo/tests.

## Verification bắt buộc

- Token giả/sai project/hết hạn, revoked session, customer→admin, ownerA→resourceB, stale role.
- Payload price/status/verified_phone giả; input negative/fraction VND, quantity sai step, amount vượt available.
- Concurrent checkout/withdraw, duplicate confirm/refund/complete, mutation mất response, bank outcome unknown.
- XSS content/review, upload sai loại, CSV injection; logs/traces không chứa secret/PII đã cấm.
- Consent revoke sau enqueue, push token rebind, unlinklast/identity-already-in-use, request xóa account còn liability.

Nguồn: [Firebase verify tokens](https://firebase.google.com/docs/auth/admin/verify-id-tokens), [Firebase link providers](https://firebase.google.com/docs/auth/flutter/account-linking), [PostgreSQL locks](https://www.postgresql.org/docs/current/explicit-locking.html). Các lựa chọn session/UX là đề xuất của TPX, không coi tài liệu hãng là quyết định business.
