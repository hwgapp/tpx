# Route Map

> PRD v0.1 — 2026-10-21 — Draft sẵn review, chưa freeze. **[C]**: đã chốt trong decision log. **[P]**: phương án chi tiết cần review tại [sổ review](11-review-decisions.md). Không coi [P] là yêu cầu user đã duyệt.

Các path là đề xuất contract navigation. Admin thuộc origin riêng hoặc base `/admin` do deployment cấu hình; bảng dùng base `/admin`. Chỉ nhận return path thuộc allowlist nội bộ.

| Route ID | Web path | Flutter route | Screen ID | Auth/permission |
| --- | --- | --- | --- | --- |
| R-001 | / | /home | S-001 | Public |
| R-002 | /nguyen-lieu | /catalog/raw | S-002 | Public |
| R-003 | /tim-kiem | /search | S-003 | Public |
| R-004 | /san-pham/:slug | /products/:id | S-004 | Public |
| R-005 | /mon-an | /catalog/meals | S-005 | Public |
| R-006 | /mon-an/:slug | /meals/:id | S-006 | Public |
| R-007 | /mon-an/:slug/huong-dan | /meals/:id/instructions | S-007 | Public |
| R-008 | /gio-hang | /cart | S-008 | Public → Customer |
| R-009 | /dang-nhap | /sign-in | S-009 | Public |
| R-010 | /tai-khoan | /account | S-010 | Customer |
| R-011 | /tai-khoan/dang-nhap | /account/identities | S-011 | Customer |
| R-012 | /tai-khoan/dia-chi | /account/addresses | S-012 | Customer |
| R-013 | /tai-khoan/dia-chi/:id | /account/addresses/:id | S-013 | Customer |
| R-014 | /thanh-toan | /checkout | S-014 | Customer |
| R-015 | /thanh-toan#lich-giao | /checkout/delivery | S-015 | Customer |
| R-016 | /don-hang/:id/thanh-toan | /orders/:id/payment | S-016 | Customer |
| R-017 | /don-hang/:id/da-dat | /orders/:id/placed | S-017 | Customer |
| R-018 | /tai-khoan/don-hang | /orders | S-018 | Customer |
| R-019 | /don-hang/:id | /orders/:id | S-019 | Customer |
| R-020 | /don-hang/:id/huy | /orders/:id/cancel | S-020 | Customer |
| R-021 | /don-hang/:id/hoan/:refundId | /orders/:id/refunds/:refundId | S-021 | Customer |
| R-022 | /tai-khoan/so-du | /account/balance | S-022 | Customer |
| R-023 | /tai-khoan/rut-tien | /account/withdrawals/new | S-023 | Customer |
| R-024 | /tai-khoan/rut-tien/:id | /account/withdrawals/:id | S-024 | Customer |
| R-025 | /tai-khoan/diem | /account/loyalty | S-025 | Customer |
| R-026 | /tai-khoan/gioi-thieu | /account/referral | S-026 | Customer |
| R-027 | /tai-khoan/thuong-mua | /account/frequent | S-027 | Customer |
| R-028 | /don-hang/:id/danh-gia/:itemId | /orders/:id/reviews/:itemId | S-028 | Customer |
| R-029 | /tai-khoan/thong-bao | /account/notifications | S-029 | Customer |
| R-030 | /tai-khoan/thong-bao/cai-dat | /account/notification-preferences | S-030 | Customer |
| R-031 | /thong-tin/:slug | /content/:slug | S-031 | Public |
| R-032 | /auth/callback | /auth/callback | S-032 | Public |
| R-033 | /admin/login | — | S-033 | Admin public entry |
| R-034 | /admin | — | S-034 | dashboard.read |
| R-035 | /admin/products | — | S-035 | catalog.manage |
| R-036 | /admin/products/:id | — | S-036 | catalog.manage |
| R-037 | /admin/ingredients | — | S-037 | catalog.manage |
| R-038 | /admin/meals | — | S-038 | catalog.manage |
| R-039 | /admin/meals/:id | — | S-039 | catalog.manage |
| R-040 | /admin/media | — | S-040 | content.manage |
| R-041 | /admin/orders | — | S-041 | orders.read |
| R-042 | /admin/orders/:id | — | S-042 | orders.read |
| R-043 | /admin/payments | — | S-043 | payments.confirm |
| R-044 | /admin/procurement/batches | — | S-044 | procurement.manage |
| R-045 | /admin/procurement/batches/:id | — | S-045 | procurement.manage |
| R-046 | /admin/procurement/batches/:id/purchases | — | S-046 | procurement.manage |
| R-047 | /admin/fulfillment | — | S-047 | fulfillment.manage |
| R-048 | /admin/deliveries | — | S-048 | delivery.manage |
| R-049 | /admin/deliveries/:id | — | S-049 | delivery.manage |
| R-050 | /admin/cases | — | S-050 | adjustments.manage |
| R-051 | /admin/refunds | — | S-051 | refunds.manage |
| R-052 | /admin/refunds/:id | — | S-052 | refunds.manage |
| R-053 | /admin/withdrawals | — | S-053 | withdrawals.manage |
| R-054 | /admin/withdrawals/:id | — | S-054 | withdrawals.manage |
| R-055 | /admin/customers | — | S-055 | customers.read |
| R-056 | /admin/customers/:id | — | S-056 | customers.read |
| R-057 | /admin/accounts | — | S-057 | access.manage |
| R-058 | /admin/audit | — | S-058 | audit.read |
| R-059 | /admin/settings | — | S-059 | settings.manage |
| R-060 | /admin/notifications | — | S-060 | notifications.manage |
| R-061 | /admin/content | — | S-061 | content.manage |
| R-062 | /admin/reviews | — | S-062 | reviews.moderate |
| R-063 | /admin/reports | — | S-063 | reports.read |

## Navigation và deep link

- Web: home → catalog/món → chi tiết → giỏ → checkout → thanh toán/đơn. Account menu dẫn đơn/tiền/điểm/referral/địa chỉ/tùy chọn.
- Flutter đề xuất bottom navigation: Trang chủ / Món ăn / Giỏ / Đơn hàng / Tài khoản. Search mở từ header; không tạo app admin.
- Push chỉ mang entity type/id và route được allowlist; mở app cần xác thực/ownership lại. Không đưa token/ngân hàng/số dư vào URL hoặc preview push.
- Link referral chỉ mở nội dung/ghi nhận mã, không tự đăng nhập/đặt đơn. OAuth callback và deep link xử lý state/nonce theo SDK.
- Refresh web trực tiếp một route phải hoạt động; Flutter back không submit lại checkout hoặc giao dịch. Route sử dụng ID nội bộ, slug chỉ phục vụ nội dung public.
