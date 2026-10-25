# Output contract — Design System và UI Workflow TPX

> v0.4 · 2026-10-25. Các file/path dưới là định dạng cần giao và vị trí import dự kiến; chưa phải artifacts đã tạo. Source thực có thể là công cụ thiết kế/prototype/editorial export; không tạo fake links hoặc tự đánh dấu Delivered.

## 1. Hai packages

**Design System Package** và **UI Workflow Package** cùng brand/token/CMP IDs. Mỗi package phải có actual editable/source artifacts, visual gallery/frames và tài liệu handoff. Chỉ một bản mô tả chữ chưa đủ. Nếu công cụ thiếu export format, giữ actual artifact hiện có và ghi limitation/Missing phần còn thiếu; không giả đã export.

Có thể chia artifacts: foundations/components → customer commerce → account/engagement → admin catalog → admin operations → admin finance/settings. Mọi phần dùng một manifest chung, không bỏ các nhóm sau vì công cụ có giới hạn.

## 2. Design System Package

Import vào `doc/4-DESIGN/system/` khi có output thật:

| Output | Nội dung bắt buộc |
| --- | --- |
| README / source refs | Project/brief version, source tool, editable artifact, gallery links, capabilities/limitations |
| tokens.json | color, typography, spacing, sizing, radius, border, shadow, motion, zIndex, breakpoint, asset, status/domain; type/unit/value/description, alias resolution |
| design-system / component inventory |56 CMP IDs, purpose/anatomy/properties/variants, platforms, token refs, Screen/J/FC usage, actual source/frame và status |
| component-state-matrix | CMP/variant/state, visual/behavior/a11y, actual frame/source hoặc inheritance proof; N/A có lý do |
| accessibility | Actual contrast pairs, focus/keyboard/labels/text scale/targets/safe area/reduced motion; unresolved findings |
| implementation notes | Semantic tokens→CSS/React/Flutter, units/font bundle/density, interaction/state contracts; không yêu cầu backend |
| asset manifest | AST ID, actual asset/source/license/demo flag, dimensions/ratio, alt text, Screen/CMP usage |

Token library thật phải có values đầy đủ; không giao các nhóm rỗng hoặc một brand palette thay cả hệ thống. Primitives #309953/#F9A01B giữ nguyên, semantic actions có shade đủ contrast. Designer chọn schema JSON nhất quán và ghi mapping, không cần theo một token standard mới chưa chốt.

## 3. UI Workflow Package

Import vào `doc/4-DESIGN/mockups/` khi có output thật:

| Output | Fields/content bắt buộc |
| --- | --- |
| README / prototype hub | Source/editable artifact, entry customer/admin và scenario selector ngoài product UI |
| screen-map | Screen ID/name, Feature/US/UC/J, required surfaces, default actual frames, states, CMP IDs, status |
| surface-coverage |190required Screen×Surface rows, viewport, actual default/source, Delivered/Shared-with-proof/Missing/Needs-fix, shared_from và platform notes |
| state-coverage | Screen/surface/state, Required hoặc N/A-with-reason, actual frame/CMP inheritance+copy/action/placement, status |
| user-story-map | US/Feature, source story/AC IDs, relevant J/FC/UC, entry→steps→exit, platform evidence/missing |
| flow-map | UF/UC/J, actor lanes, entry/trigger, success/failure/recovery/return/exit, actual prototype links |
| journey-case-map | J/FC, source Feature/AC, actor, Screen/Surface, precondition/action/result/recovery, actual frame/prototype, evidence status |
| design-assumptions | DA ID, source P/OQ/AG, policy state, branch/variant, proposal/confirmed scope, impact/review status |
| fix-list | DF ID, Screen/CMP/J/FC/Surface/State, issue/severity, Missing/Needs-fix/Resolved, evidence |
| manifest.json | Brief/source versions, actual artifacts/links/files, counts expected/delivered/missing, tool/export capabilities, limitations and asset refs |

Default layout phải được composed cho mỗi required cell, không thay bằng tên màn hoặc “same as desktop”. Shared iOS/Android được khi có actual frame và notes; web mobile/admin compact cần layout cụ thể.190 cells là coverage, không nhất thiết190 layout khác nhau.

State inherited chỉ hợp lệ nếu có actual CMP state và screen-specific copy/action/placement. Financial holds/refund/unknown/cutoff và các decision branches cần frame trực tiếp gắn Screen ID; không dùng generic error toast để bỏ nhánh. J/FC là planned cases, hiện chưa Delivered hoặc test passed.

## 4. Naming và prototype behavior

```text
<ScreenID>__<Surface>__<State-or-Variant>__v01
S-014__WEB_MOBILE__holds-created__v01
S-022__APP_IOS__available-order-hold-withdraw-pending__v01
S-052__ADMIN_DESKTOP__refund-keeps-earned-points__v01
S-042__ADMIN_COMPACT__oq050-option-a__v01
CMP-027__wallet-summary__states
```

Surface enums: WEB_DESKTOP, WEB_MOBILE, APP_IOS, APP_ANDROID, ADMIN_DESKTOP, ADMIN_COMPACT. Source tool stable IDs khác naming thì map đầy đủ, không giả filename đã export. Giữ US/UF/UC/J/FC/S/CMP nghĩa cũ.

Navigation/CTA/back có destination hoặc transition; lists/forms/dialogs có tương tác theo khả năng công cụ. Khách/admin tách lane, không link khách vào admin. Scenario selector mô phỏng clock/caps/balance/permission/unknown, đặt ngoài product UI. Không dùng OAuth/ngân hàng/API thật; mark demo trong handoff. Permission/version/cutoff guard có state alternative và limitation nếu prototype engine không thực hiện được.

## 5. Policy chưa chốt và tính trung thực của evidence

D-093–100 đã xác định joint holds và refund giữ ORDER_EARN; không dùng giả định debit ngay/clawback/debt cũ. OQ-048/049 đã đóng. OQ-050/OQ-042 vẫn pending: dựng các branches theo03, label assumption ngoài product UI, không chọn một branch thành chính sách đã được duyệt. Các P khác giữ trạng thái từng phần trong review register.

Thiết kế branch không đóng AG/backend gap, không chứng minh production integration. Không gắn Imported/Ready khi mới có prompt. Chỉ actual output mới được review bằng [checklist](05-design-review-checklist.md), import raw/reference và update maps/traceability/fix-list. Task implementation và gate không tự freeze bởi design brief.
