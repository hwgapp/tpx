# Yêu cầu phi chức năng và vận hành

> PRD v0.1 — Draft. Các mức định lượng bên dưới là **target đề xuất P-012**, chưa benchmark/chưa là SLA. Server user đã có; không yêu cầu mua hạ tầng hay Docker.

| ID | Nhóm | Yêu cầu/tiêu chí nghiệm thu |
| --- | --- | --- |
| NFR-001 | Giao dịch | Không âm available/pending; không duplicate debit/credit/earn/revoke khi retry; concurrency tests dùng DB thật |
| NFR-002 | Thời gian | Server enforce Asia/Ho_Chi_Minh; đúng22:00 chuyển earliest và khóa cancel; UTC lưu event, business date riêng |
| NFR-003 | Quyền | Ownership mọi me/resource endpoint; admin permission mỗi action; không tạo admin từ social; test horizontal/vertical access |
| NFR-004 | Phiên | Cookie HttpOnly/Secure/CSRF web, mobile secure token; disable/revoke chặn request sau; không admin OTP/TOTP |
| NFR-005 | Privacy/log | Không token/password/OTP/bank number đầy đủ/contact/address trong analytics/log; audit tài chính có actor/ref/reason, mask thông tin khi xem không cần thiết |
| NFR-006 | Performance [P] | Dataset 1.000 variants/10.000 orders,20 khách và2 admin đồng thời: P95 read API≤500ms, quote/commit≤1.500ms, không gồm provider/network ngoài; benchmark trên staging trước chốt |
| NFR-007 | UX performance [P] | Web catalog có phân trang/image sizes, app list lazy-load; checkout không đóng băng khi network chậm; đo và xử lý các slow query thực tế |
| NFR-008 | Availability [P] | Native processes có health/readiness/restart; PostgreSQL hỏng thì fail closed cho money actions, không dựa cache để cấp tiền |
| NFR-009 | Jobs | Outbox retry/idempotency; retry bounded/backoff, queue failed có admin view; job outage không thay cutoff hoặc rollback domain đã commit |
| NFR-010 | Backup [P] | Backup DB hàng ngày ra vị trí tách server; target RPO24h/RTO 4h cho thử nghiệm; phải chạy restore và đối soát trước mở bán; chỉ target chưa đo |
| NFR-011 | Audit/reconcile | Daily checks tổng account/entries, pending withdrawals, refund remaining, point debt, receipt unmatched; sai lệch tạo cảnh báo vận hành, không tự sửa ledger |
| NFR-012 | Observability | request_id/command_id, latency/error rates, job backlog, cutoff batch status, provider fail; audit khác analytics/log kỹ thuật |
| NFR-013 | Compatibility [P] | Responsive web/mobile; matrix iOS/Android/browsers chốt theo bản Flutter/Next được pin. Social login/push phải test thiết bị thật và web Safari/Chrome |
| NFR-014 | Accessibility [P] | Keyboard/focus/labels web/admin, touch target/semantics Flutter; trạng thái không chỉ nhờ màu; lỗi form và số tiền đọc được |
| NFR-015 | Data types | VND BIGINT/string API; điểm nguyên; quantity NUMERIC+unit; không float hoặc tự quy đổi đơn vị không có conversion |
| NFR-016 | Recovery | Không đoán tác dụng giao dịch từ HTTP timeout; tra idempotency/resource state; bank outcome chưa rõ giữ PROCESSING và đối soát |
| NFR-017 | Secrets/environments | Dev/staging/prod tách DB/bucket/Firebase configs/device tokens; secrets backend/CI; không seed credentials thật vào Git |
| NFR-018 | Test/release | Không release khi chưa test critical flows, native DB migrations/backup restore, Firebase3 providers/FCM/Zalo thực; mocks chỉ dùng kiểm thử không coi tích hợp production đã xong |

## Báo cáo và định nghĩa chỉ số [P-010]

- Giá trị đơn: tổngG+F theo snapshot, lọc created_at hoặc delivery_date có nhãn. Không coi toàn bộ là tiền đã nhận.
- Tiền thu thực: bank receipts confirmed matched trong kỳ; balance applied là giảm nghĩa vụ số dư, không cộng lại thành bank cash-in; points discount là giảm giá trị thu.
- Hoàn tiền: settled bank refunds, credited balance refunds, points returned riêng; approved/pending thể hiện nghĩa vụ, không gọi đã chuyển.
- Nghĩa vụ số dư: tổng available+pending của account; pending tách riêng, không cộng lần hai vào total. Loyalty liability theo points/debt riêng, không hiển thị như tiền được rút.
- Chênh lệch gộp tham khảo: net merchandise money entitlement sau point discount/refunds − giá vốn đã nhập/phân bổ; hiển thị thiếu dữ liệu nếu chưa có cost. Không gọi đây là lợi nhuận ròng vì chưa đủ giao/sơ chế/chi phí khác.
- Đơn hoàn thành: completed event trong kỳ; hoàn một phần/full là trục refund riêng. Repeat/referral dùng user_id nội bộ, không dùng email/phone làm định danh analytics.

## Dữ liệu production cần cung cấp trước mở bán

Địa bàn và khung giao, ngân hàng nhận tiền, giá/quy cách/BOM/menu/ảnh/hướng dẫn đã duyệt, caps loyalty/minimum/fee/reward/reminder settings, fixed admin accounts, OAuth/Firebase/FCM/Zalo/S3 credentials và callback/domain. Không cần những secret này để review PRD; không ghi chúng vào tài liệu.
