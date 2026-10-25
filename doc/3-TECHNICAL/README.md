# Technical appendix — TPX

Stack đã được user chọn/duyệt; schema/contract và policy chi tiết vẫn review. Không tạo code skeleton trước Technical gate.

- [Technical brief](00-technical-brief.md) và [architecture](01-architecture.md).
- [Data dictionary: 68 bảng logic](02-data-model.md).
- [API design: DTO, auth, errors và concurrency](03-api-design.md); danh mục 118 operations tại [PRD API map](../2-PRD/06-api-contract-map.md).
- [Client state/cache](04-state-management.md), [integrations](05-integrations.md), [security/privacy](06-security-privacy.md), [deployment](07-deployment.md).
- [Decisions](08-technical-decisions.md), [PRD overview](../2-PRD/00-prd-overview.md), [review register](../2-PRD/11-review-decisions.md).

Không dùng Docker; server user có sẵn; GitHub, Flutter, Firebase Auth/FCM, NestJS/Next/React/PostgreSQL theo các quyết định đã ghi. Credentials chưa được tạo và không lưu trong tài liệu.
