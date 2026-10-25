# Events và metrics

> PRD v0.1 — Draft. Đề xuất first-party domain events trong hệ thống; không tự thêm Google Analytics, Firebase Analytics hoặc marketing SDK chỉ vì đã dùng Firebase Auth/FCM. `[P]` là telemetry/UX policy cần review.

| Event | Feature | Trigger | Properties allowlist | Nguồn | Lưu ý |
| --- | --- | --- | --- | --- | --- |
| auth.signed_in | F-001 | Sau verify Firebase và tạo/map phiên thành công | provider,platform,is_new_user | Backend | Không token/email; đếm phiên khác số user |
| catalog.item_viewed | F-002/F-003/F-015 | Chi tiết sản phẩm/món hiển thị | product_id,kind,variant_id?,platform | Client [P] | Không dùng như chứng cứ mua |
| cart.item_changed | F-004 | Thay giỏ thành công | variant_id,pack_count,action,platform | Backend/client event ID [P] | Không include địa chỉ/ghi chú |
| checkout.quoted | F-004/F-008/F-012 | Quote được tính | quote_id,config_version,date_offset,use_points,has_balance | Backend | Không ghi số tài khoản hoặc địa chỉ |
| order.placed | F-004/F-005 | Order transaction commit | order_id,kind_mix,G,F,B,D,T,delivery_date | Backend outbox | Event ID duy nhất; money string, không contact |
| payment.receipt_confirmed | F-005 | Actual bank receipt matched | order_id,receipt_id,matched_amount_vnd,funding_state | Backend outbox | Không raw bank reference/number |
| procurement.decided | F-006 | Quyết định included/excluded commit | batch_id,order_id,decision,unpaid_override | Backend/audit | Reason chi tiết ở audit, không analytics tự do |
| fulfillment.stage_changed | F-007 | Prep/pack/dispatch command commit | order_id,stage | Backend outbox | Không GPS/contact |
| order.completed | F-007/F-012/F-017 | Complete một lần | order_id,completed_at,eligible_goods_vnd | Backend outbox | Source xác định hoàn thành và eligible earn |
| order.cancelled | F-021 | Cancel hợp lệ commit | order_id,reason_code,before_cutoff | Backend outbox | Không free-text khách |
| case.agreed | F-021 | Agreement version được lưu | order_id,case_id,plan_kind | Backend/audit | Thông tin trao đổi chi tiết riêng |
| refund.leg_settled | F-021/F-012 | Từng leg hoàn thực hiện | refund_id,leg_id,original_source,payout_method,amount_vnd,points | Backend outbox | Pending không tính đã chuyển |
| balance.entry_posted | F-010 | Money ledger commit | entry_id,type,order_id?,withdrawal_id? | Backend/audit | Đối soát từ ledger, không client |
| withdrawal.created | F-011 | Available sang pending commit | withdrawal_id,amount_vnd | Backend outbox | Không bank details |
| withdrawal.state_changed | F-011 | Approve/process/paid/reject/cancel commit | withdrawal_id,from_state,to_state | Backend outbox | PAID mới là cash payout |
| loyalty.entry_posted | F-012 | Earn/redeem/return/revoke/reward commit | entry_id,type,points,order_id? | Backend outbox | Debt proposal tách loại, không coi là cash |
| referral.rewarded | F-017 | Reward entry posted | referral_id,reward_id,qualifying_order_id,points | Backend outbox | Một reward/beneficiary, không thưởng register |
| order.reorder_previewed | F-018 | Preview mua lại | source_order_id,eligible_count,unavailable_count | Backend [P] | Không tự coi là doanh thu |
| frequent.item_used | F-019 | Thêm giỏ từ danh sách thường mua | variant_id,action | Client [P] | Không cross-user profile |
| review.submitted | F-016 | Eligible review lưu | review_id,product_id,rating,moderation_state | Backend [P] | Không đưa text review vào analytics |
| content.published | F-015 | Admin publish nội dung | content_id,version | Backend/audit | Không toàn bộ body |
| settings.published | F-014 | Version active | section,version | Backend/audit | Không secret hoặc toàn bộ config |
| notification.attempted | F-013 | Provider attempt được ghi | notification_id,channel,status,error_code? | Worker | SENT không đồng nghĩa đã đọc |
| reminder.skipped | F-020 | Không gửi do consent/cutoff/provider | schedule_id,channel,reason_code | Worker [P] | Không tự gửi kênh thay thế |
| consent.changed | F-013/F-020 | Khách thay tùy chọn | channel,purpose,enabled,version | Backend/audit | Không lấy OS permission làm consent |

## Envelope và ownership

Mỗi event có event_id UUID/dedupe_key, occurred_at UTC, aggregate_type/id/version, actor_type và user_id/admin_id nội bộ khi cần, platform, correlation_id/request_id. PII và dữ liệu tự do không thuộc properties allowlist. Backend transaction/outbox là nguồn cho giao dịch; client analytics không xác nhận paid/earn/refund.

Đếm revenue/points theo durable entries với unique business keys; ingestion có thể retry nên consumer dedupe event_id. Với UI event cần dùng sampling/consent phù hợp, không dùng để sửa state giao dịch.

## Báo cáo cần có [P-010]

- Đơn đặt/đơn hoàn thành/hủy theo created date hoặc delivery date có nhãn; RAW/MEAL/mixed và giá trị đơn.
- Tiền bank nhận thực/matched/excess, balance applied, points discount; không cộng lại tiền hoàn dùng như bank cash-in.
- Refund pending/settled theo từng nguồn; withdrawals pending/processing/paid; liability available+pending một lần.
- Repeat customer/reorder, referral qualifying/rewarded; review published và reminder opt-in/skipped; không cam kết KPI chưa có baseline.
- Cost coverage và chênh lệch gộp tham khảo, không gọi lợi nhuận ròng khi chưa đủ chi phí. Định nghĩa tại [NFR/metrics](14-non-functional-requirements.md).
