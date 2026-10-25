# TPX — Product Requirements Document v0.1

> Thực phẩm xanh (TPX) — 2026-10-21 — **Draft hoàn chỉnh để review**, chưa freeze BRD/PRD/Technical. Đây là bộ đặc tả sản phẩm và phụ lục hệ thống; chưa có implementation, DB migration, account hoặc hạ tầng được tạo.

## Mục tiêu và phạm vi

TPX trực tiếp bán rau củ quả, thịt cá trứng theo mô hình khách đặt trước → gom đơn → mua chợ đầu mối → tập kết một điểm → làm sạch/cắt/chia → TPX giao. Khách gia đình/người đi làm/nhà hàng dùng chung flow; thử nghiệm nội thành TP.HCM, kỳ vọng vài chục đơn/ngày. Thu nhập từ chênh lệch mua-bán, không marketplace.

Hai nhóm trong cùng giỏ/đơn/lần giao: nguyên liệu thô chọn catalog/quy cách; món sơ chế chọn món/khẩu phần có giá sẵn, chỉ nguyên liệu chính, không gia vị/nước sốt. Có hướng dẫn nấu; menu cố định, tắt theo nguyên liệu. Chưa xây câu chuyện truy xuất nông trại hoặc crawler tự động.

| Surface | Công nghệ đã chọn | Phạm vi nghiệp vụ |
| --- | --- | --- |
| Web khách | Next.js; responsive | Catalog public/SEO nội dung, social login, checkout, đơn, số dư/rút, loyalty, referral, reviews, mua lại và preferences |
| App khách | Flutter iOS/Android | Nghiệp vụ ngang web; native navigation, Firebase login, secure session, push/deep link; không yêu cầu dùng app để mua |
| Admin | React/Vite; responsive đề xuất | Fixed accounts/password không OTP; RBAC; catalog/BOM, tiền/đơn, gom mua, sơ chế/giao, case/refund/rút, nội dung, settings, audit/reports |
| API/worker | NestJS modular monolith REST/OpenAPI | Giá/cutoff/ownership/ledgers ở server; worker outbox/BullMQ; không worker quyết cutoff |
| Database | PostgreSQL/Prisma | 68 bảng logic; snapshots, append-only ledgers, indexes/constraints; chưa generate migration |
| Dịch vụ | Firebase Auth/FCM, Zalo, S3-compatible | Social login đã duyệt TD-025, credentials/config chưa tạo; phone login sau OTP |

## Quy tắc đã chốt [C]

1. Chốt đơn lúc **22:00, Asia/Ho_Chi_Minh**. Trước mốc này, sớm nhất giao hôm sau; từ mốc này, sớm nhất giao ngày kia. Ngày giao xa nhất là ngày đặt + 7 ngày. Giao ngày D thì chốt mua và khóa hủy lúc 22h ngày D−1.
2. Khách thanh toán ngay khi đặt; bản đầu chuyển khoản, admin xác nhận thủ công, không COD. Admin có quyền quyết định mua đơn chưa thanh toán tại cutoff; việc duyệt mua không xác nhận đã nhận tiền.
3. Thứ tự thanh toán: tự dùng số dư tiền hoàn available → dùng điểm nếu khách chọn và trong giới hạn → chuyển khoản phần còn lại. Pending rút không được tiêu; khách không tự nạp tiền, số dư không hết hạn.
4. Ví có 200.000đ, yêu cầu rút 150.000đ: pending 150.000đ, available 50.000đ. Admin duyệt và chuyển ngân hàng thủ công; duyệt chưa đồng nghĩa đã chuyển tiền.
5. Mỗi 1.000đ tiền hàng đủ điều kiện tích 1 điểm khi hoàn thành, làm tròn xuống. Một điểm sử dụng giảm 1.000đ; không rút điểm thành tiền, không hết hạn điểm ở bản đầu. Trần phần trăm tính trên tiền hàng sau giảm giá trước số dư, không gồm phí giao, đồng thời áp trần VND. Phần trả bằng số dư vẫn tích; phần trả bằng điểm và phí giao không tích.
6. Hoàn phần thanh toán bằng điểm bằng điểm, tiền theo thỏa thuận. Sau complete vẫn cho hoàn, không thu hồi ORDER_EARN đã thưởng D-100 (thay D-085).
7. Khách đăng nhập Google/Facebook/Apple qua Firebase Authentication; backend xác minh token và dùng user TPX trong PostgreSQL. SĐT nhận hàng nhập ở checkout, chưa cần OTP. Phone login bổ sung sau và liên kết vào tài khoản hiện có. Admin dùng các tài khoản cố định/mật khẩu, không OTP, giữ RBAC. Dùng GitHub, server user đã có và không Docker.
8. Thông báo Zalo và push; referral thưởng điểm theo setting, người giới thiệu được thưởng sau đơn đầu hoàn thành. Có đánh giá từ khách đã mua, mua lại đơn, món thường mua và nhắc đặt qua kênh khách đồng ý nhận.

Nguồn chốt: [business decisions](../1-BRD/01-decision-log.md) D-001–100; [technical decisions](../3-TECHNICAL/08-technical-decisions.md) TD-001–025. Mọi quy tắc [P] chỉ là phương án để review, không ghi đè các nguồn này.

## Cấu trúc bộ hồ sơ

| Đọc theo thứ tự | Nội dung |
| --- | --- |
| [Feature inventory](01-feature-inventory.md) | 21 feature, priority/dependencies và 21 spec chi tiết |
| [Screen inventory](02-screen-inventory.md) / [Routes](05-route-map.md) | 63 màn: 32 web/app khách, 31 admin; web path và Flutter route rõ |
| [User flows](03-user-flows.md) / [Domain states](12-domain-states.md) | Happy/error/edge, guard và state từng domain |
| [Product API map](06-api-contract-map.md) / [API design](../3-TECHNICAL/03-api-design.md) | 119 operations, quyền, DTO/error/idempotency |
| [Permissions](07-permission-matrix.md) | Customer ownership, admin permissions và các hành động bị cấm |
| [Financial rules](13-financial-rules.md) | Công thức nguồn tiền, withdraw, partial refund và clawback |
| [Data dictionary](../3-TECHNICAL/02-data-model.md) | 68 bảng logic, fields/FKs/indexes, snapshots và transactions |
| [Analytics](08-analytics-events.md) / [NFR](14-non-functional-requirements.md) | Event/metric, an toàn dữ liệu, performance/backup target |
| [Acceptance criteria](09-acceptance-criteria.md) / [Test plan](../5-DELIVERY/08-test-plan.md) | 116 feature AC + regression, QA scenario, verification cần thực hiện |
| [Release scope](10-release-scope.md) / [Traceability](../5-DELIVERY/12-traceability-matrix.md) | R1 đầy đủ, dependencies/config và mapping end-to-end |
| [Review register](11-review-decisions.md) | 19 nhóm phương án còn review, đặc biệt money/points/state |

## Tiêu chí thành công

- Khách đặt được RAW+MEAL, tự biết ngày giao/cutoff/số phải chuyển và theo dõi một đơn xuyên web/app.
- Admin có đủ dữ liệu thu mua/BOM và quy trình từ nhận tiền đến giao/hoàn/rút, có audit và phân quyền; không cần thao tác SQL để vận hành thường ngày.
- Tiền/points không bị dùng trùng/hoàn trùng khi retry hoặc concurrency; pending không bị chi tiêu; không đánh đồng receipt/decision/state.
- Full R1 đi qua các AC và release readiness; mục tiêu doanh thu/tỷ lệ giữ chân số cụ thể chưa được user cung cấp, không tự đặt KPI cam kết.

## Kiểm tra hồ sơ

[Báo cáo kiểm tra](15-document-review.md) ghi rõ phạm vi consistency/số học và các việc chưa test ở sản phẩm. Không dùng kết quả kiểm tra tài liệu thay nghiệm thu implementation.

## Những gì chưa coi đã chốt

P-001–019 đưa phương án cụ thể cho debit timing, lifecycle rút, partial refund/khoản điểm cần thu hồi, fee allocation, referral, tái bật món, complete unpaid, config version/minimum, chính sách UI, session/retention và mục tiêu NFR. Chúng được gắn nhãn tại spec/AC. Danh sách địa bàn, khung giờ, fees/caps/rewards, catalog/BOM và credentials là dữ liệu cần trước mở bán.

Bước tiếp theo là review các phương án này và hoàn thiện Technical freeze; design handoff và delivery tasks dùng spec/ID này. Không đánh dấu gate freeze hay tạo code skeleton chỉ vì PRD đã soạn xong.

## Flow audit bổ sung — v0.2 của design handoff

[Audit flows](../4-DESIGN/12-flow-audit.md) phát hiện28 findings/6 Critical và16 action gaps, bổ sung25 journeys/100 cases. Đặc biệt cần chốt terminal resolution cho đơn không thực hiện được/EXCLUDED, adjustment execution/thu thêm, receipt/payout correction và fulfillment guard khi refund còn pending. P-013–019 chưa được user duyệt; các diagram/119 API baseline chưa tự có những capabilities này. Xem register và gap report trước implementation.

## Quyết định mới nhất — 2026-10-25

[Review vòng1](16-review-round-1.md) cập nhật D-093–100: points hold→capture/release, admin hủy vận hành, admin quyết giao thiếu thanh toán, admin update đơn và tách phần hàng đã thống nhất khỏi hoàn bank pending. API-119 admin cancel là draft mới, chưa implementation; tổng116featureAC.19chủ đề review có phần đã chốt, không còn đồng loạt chưa duyệt. OQ-048/049 đang hỏi về cash timing và hoàn sau complete; OQ-050 complete-unpaid và OQ-042 chênh lệch update còn mở. Chưa freeze PRD/Technical/design.
