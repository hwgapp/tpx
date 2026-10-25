# Design handoff — Thực phẩm xanh (TPX)

> **v0.4 · 2026-10-25 · Ready to send for design.** Đây là brief hoàn thiện theo các quyết định hiện có; actual Design System/UI Workflow vẫn **Pending design output**. Các nhánh policy chưa chốt được chỉ rõ, không tự coi đã duyệt.

## Gửi cho Claude Design

1. Copy phần yêu cầu trong [01 — Prompt](01-claude-design-prompt.md).
2. Đính kèm [08 — Context pack độc lập](08-claude-design-context.md). Pack đã nhúng brief, DS/flow/component requirements,21source stories/116AC,25journeys/100cases, policy mới nhất và output contract. Không cần repo access hoặc đính kèm toàn thư mục.
3. Yêu cầu bàn giao **Design System Package** và **UI Workflow Package**, có editable source/artifacts/prototype và coverage evidence thực.

## Phạm vi và quyết định hiện tại

21nhóm story,63màn logic,56components;32màn khách trên web desktop/mobile + Flutter iOS/Android,31màn admin desktop/compact. Tổng190required screen×surface cells;25journeys/100cases thêm chiều hành vi/error/recovery. Shared native frames được nếu có proof/notes, không bỏ web mobile/admin compact.

D-093–100 đã xác định: cash/points HOLD lúc place, CAPTURE khi complete, RELEASE khi cancel; cash held_order khác pending rút. Cho hoàn sau complete, giữ ORDER_EARN; không debt/clawback. Admin quyết giao thiếu tiền và được hủy vận hành/update đơn. Refund pending không tự chặn phần hàng đã thống nhất.

**OQ-050** complete-unpaid và **OQ-042** settlement update chưa có câu trả lời. Brief yêu cầu prototype cả các branch cụ thể trong03section12 với annotation. OQ-048/049 đã đóng, không hỏi lại.19topics P có trạng thái từng phần; audit12 là snapshot lịch sử, không ghi đè nguồn mới.

## Tài liệu chính

| File | Dùng để |
| --- | --- |
| [00 — Design brief](00-design-brief.md) | Product, audience, brand, scope, confirmed rules |
| [01 — Prompt](01-claude-design-prompt.md) | Copy sang Claude Design |
| [02 — Design system requirements](02-design-system-requirements.md) | Foundations/tokens,56CMP, domain patterns, accessibility/platform rules |
| [03 — Screen/flow requirements](03-screen-flow-requirements.md) | Story/screen/state maps, fixtures và pending branch frames |
| [04 — Component inventory](04-component-inventory.md) | CMP IDs, variants/states và screen usage |
| [05 — Review checklist](05-design-review-checklist.md) | Review actual output sau khi có thiết kế |
| [06 — Selected catalog](06-design-system-component-catalog.md) | Component groups và scope exclusions |
| [07 — Output contract](07-claude-design-output-contract.md) | Hai packages, formats, naming và evidence |
| [08 — Standalone context](08-claude-design-context.md) | Attachment duy nhất cùng prompt |
| [09 — Surface coverage](09-design-coverage-plan.md) |190Expected screen/surface cells |
| [10 — Implementation mapping](10-implementation-mapping.md) |56DS +95UI targets, chưa Ready tasks |
| [11 — Handoff validation](11-handoff-validation.md) | Kết quả kiểm brief, khác nghiệm thu thiết kế |
| [12 — Audit history](12-flow-audit.md) | Findings2026-10-21 và disposition sau review |
| [13 — Detailed journeys](13-detailed-journeys.md) |25hành trình entry/action/result/recovery/exit |
| [14 — Case matrix](14-flow-case-matrix.md) |100cases và các tổ hợp cần review |
| [15 — Action gaps](15-action-contract-gaps.md) | Capability/contract gaps; prototype chưa đóng backend gaps |

## Refresh và kiểm tra

```sh
python3 doc/4-DESIGN/tools/build_context.py
python3 doc/4-DESIGN/tools/verify_handoff.py
```

Generator/validator chỉ phục vụ tài liệu, không tạo app/schema/prototype. Context phải khớp sources trước khi gửi; thay nguồn thì rebuild, không sửa pack generated bằng tay. Chưa import hoặc tạo output giả trong `system/`/`mockups/`; hai thư mục giữ placeholder template tới khi có artifacts thật. Design ready không tự freeze PRD/Technical hoặc hoàn tất implementation.
