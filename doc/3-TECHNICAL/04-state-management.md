# Client state, cache và đồng bộ

> Technical appendix PRD v0.1 — Draft. Các thư viện state cụ thể chưa được tự chốt thêm; contract state độc lập React/Flutter. Không tạo code skeleton.

## Web storefront Next.js

- Public catalog/content có thể render server/cache theo product/version; invalidation khi publish/tắt nguyên liệu/giá. Không cache personalized balance/loyalty/order vào shared CDN.
- Giỏ guest ở local storage chứa variant/count, không giữ giá như nguồn sự thật. Sau login đề xuất merge preview nếu có server cart; không ghi đè giỏ cũ âm thầm P-010.
- Server data qua API; query state tách form state/use_points/date/slot. Quote là immutable result có expiry/version; thay bất kỳ input → invalidate quote. Không submit stale totals.
- Customer session cookie HttpOnly; form CSRF/Origin guard; frontend chỉ giữ profile/permissions tối thiểu. SSR không serialize tokens vào HTML.
- Mutation optimistic chỉ cho UI vô hại có rollback (lọc, đọc notification); không optimistic số dư, rút, paid, cancel, points hay complete.

## Flutter iOS/Android

- Tách presentation/viewstate, application use cases, API repository và DTO mapping; không share package TypeScript. API client từ contract được generate sau khi OpenAPI freeze.
- Firebase SDK xử lý social flow, TPX session/tokens dùng secure storage; push/deeplink mở resource sau kiểm tra auth. Tách installation_id vớiuser_id, rebind token trên switch account.
- Viewstates loading/data/empty/error/offline/submitting/conflict/permission-denied. Giỏ cache xem được offline, giao dịch cần online; không lưu hàng đợi rút/đặt đơn sẽ tự gửi khi reconnect.
- Resume app/refocus sau22h hoặc trở về từ bank app → refetch order/quote/options. Countdown chỉ hiển thị dựa server offset, không thay guard API.
- OS push permission và marketing consent riêng. Chặn quyền push không chặn mua hàng. Không hard-code default selected use_points=true nếu khách chưa chọn.

## Admin React/Vite

- Auth/session riêng, query keys gồm filters/date/version. Disable action khi đang gửi; table context giữ khi trở lại chi tiết.
- Dữ liệu tài chính chỉ refetch sau server commit; race version409 mở lại preview. Không cho sửa state bằng input dropdown không có transition guard.
- Procurement/delivery board refresh có `generated_at` và thông báo dữ liệu cũ; có thể polling theo cấu hình, chưa cần WebSocket/live GPS.
- Form settings/recipe có draft và validation; thay đổi chưa lưu nhắc khi rời; publish bất biến theo version.

## Cache ownership

| Dữ liệu | Nguồn sự thật | Cache | Invalidation |
| --- | --- | --- | --- |
| Giá/khả dụng/BOM | PostgreSQL | CDN/Redis public catalog [P] | catalog/settings event + revalidate checkout |
| Ngày sớm nhất/cutoff | Backend current time+policy | chỉ hiển thị ngắn | boundary22h/refocus/input date |
| Balance/loyalty | PostgreSQL ledger+projection | private UI ngắn, không cache authority | mọi giao dịch/refund/withdraw |
| Orders/funding | PostgreSQL | private query cache | command success/push/refocus |
| Notification jobs | DB outbox/attempts | Redis queue | consumer trạng thái durable |
| Filter/forms | Client local | in-memory/local khi phù hợp | user reset/logout |

Logout/switch account xóa cache personalized, detach token cần thiết và revoke session; không hiển thị wallet user trước. Back/reload sau đặt không submit order mới, dùng order_id/idempotency result.
