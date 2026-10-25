# Permission Matrix

> PRD v0.1 — Fixed admin accounts user tạo, không OTP/TOTP D-086/TD-020. RBAC giữ đầy đủ, không suy diễn cơ cấu nhân viên mới. Có thể gán full permissions cho các account ban đầu; audit luôn actor riêng. Permission names là thiết kếđềxuất.

| Principal | Permission/action | Cho phép | Giới hạn/không cho phép |
| --- | --- | --- | --- |
| Public | catalog/content.read | Đọc published catalog/món/content và deliveryoptions | Không đọc PII/đơn/ví/điểm hoặc admin |
| Customer | profile/identities/addresses/cart.manage_own | Hồ sơ/identity/sổđịa chỉ/giỏ của mình | Không merge user theoemail; không tự OTP-verify contact |
| Customer | orders.create/read/cancel_own | Đặt vàxemđơn; cancel trước cutoff | Không tự set paid, sửa giá hoặc cancel sau cutoff |
| Customer | balance.read/withdrawals.create/read_own | Available/pending/ledger/rút của mình | Không tựnạp, dùng pending hoặc rút points |
| Customer | loyalty.read/redeem_own | Opt-inpoints trongcaps | Không selfgrant/revoke arbitrary |
| Customer | reviews/referral/reorder/frequent/preferences_own | Các feature đãxác định theoeligibility | Không review đơnngười khác, spamnhắc hoặc tự đặtqua reorder |
| Admin | dashboard.read | Xem overview vận hành | Không suy diễn full access tới PII |
| Admin | catalog.manage | Catalog/variants/ingredients/BOM/price | Không sửa giá snapshotorder cũ |
| Admin | orders.read | Xem orders theo quyền | Không tự ghi receipt/refund |
| Admin | orders.cancel | Hủy vận hành order không thực hiện được theo D-094, actor/reason và financial resolution riêng | Không giả khách hủy trước cutoff, không tự refund tiền chưa thu hoặc capture points |
| Admin | orders.complete | Complete bằng command vàguard | Không tạo earn lặp lại |
| Admin | payments.confirm | Record/confirm actual bankreceipt | Không coi customer notice làđã thu |
| Admin | procurement.manage | Batch/paid include/purchases | Unpaid cần quyền override riêng |
| Admin | procurement.unpaid_override | Duyệt/loại unpaid có reason | Không đổi trạng thái đã thu hoặc tựgiao nợ |
| Admin | fulfillment.manage | Checklistreceive/prep/pack | Không tự thay hàng khi chưa có agreement |
| Admin | delivery.manage | Dispatch/kết quảgiao | Không tựhoàn/cancel khifail |
| Admin | balance.read | Xem customer ledger tiền | Không arbitrary credit/debit |
| Admin | balance.adjust | Credit gắn adjustment hợp lệ | Không mở nạp/cộng ngoài scope |
| Admin | withdrawals.manage | Approve/reject/claim/paidwithdraw | Không release PROCESSING khi outcomeunknown |
| Admin | loyalty.read | Xem point ledger/referral | Không rút points hoặc tùy ý grant |
| Admin | refunds.manage | Preview/approve/thực hiện refundplan | Không vượt remaining caps hoặc quy đổi point thành cash |
| Admin | adjustments.manage | Case/agreement/revision | Không tự thu bổ sung khi khách chưađồng ý |
| Admin | customers.read | Xemcustomerprofile/summary đúng scope | Money/pointsdetail còn kiểm tra quyền riêng |
| Admin | access.manage | Account/role/status theo quyền | Không public signup; không tự vượt business |
| Admin | audit.read | Đọc redacted audit | Không password/token/bankfull |
| Admin | settings.manage | Versionconfigvalidate | Không tựthay đơnđã đặt |
| Admin | content.manage | Media/content/instructions | Không publishscript/draft public |
| Admin | reviews.moderate | Publish/hide có reason | Không sửa rating/text khách |
| Admin | notifications.manage | Queueattempt/retry theo current consent | Không spam/unsubscribed hoặc fake delivery success |
| Admin | reports.read | Báo cáo/export [P] | Không lộ PII người khácvà tínhcash/GMV lẫn |

## Guards chung

- Customer routes luôn `resource.user_id == authenticated TPX user_id`, kể cả id đã thấy qua link/push. Không nhận role/verified flags từ client.
- Admin route kiểm tra active account/session + permission + domain guard + expectedversion. Role full không được rút points/dùng pending/ghi đã thu giả. Admin cancel vận hành D-094 là action riêng, không giả khách hủy trước cutoff.
- Thao tác tiền/state require actor/reason/reference tươngứng; hệ thống/worker có service identity cho audit, không dùng adminaccount chung.
- Account/role change revoke/refresh permissioncontext tạiAPI. Không cache full access vôthời hạn.
- Module balance/loyalty không mở nút arbitrary grant/debit ngoài yêu cầu; credits gắn adjustment, reward/earn/revoke qua domaincommand. Phân quyền phêduyệt nhiều bước/4-eyes chưa được useryêu cầu.
