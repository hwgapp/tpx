# Handoff input validation — TPX

> **v0.4 · 2026-10-25 · PASS về tài liệu đầu vào.** Design System Package/UI Workflow Package chưa được tạo hoặc import; đây không phải nghiệm thu giao diện hoặc test phần mềm.

| Kiểm tra | Kết quả |
| --- | --- |
| Nguồn PRD |21feature specs/116AC, source stories và nội dung AC nhúng trong context |
| Screens/components |63Screen IDs,56CMP IDs, usage mapping hai chiều khớp; admin login không cần data table nội bộ |
| Flow groups |21US aliases,13UF,28UC,25journeys/100cases; actor/screen/trigger/result/recovery và case refs hợp lệ |
| Surface coverage |190unique required screen×surface cells, tất cả Expected |
| Rules mới | Cash/points joint HOLD→CAPTURE hoặc RELEASE; cash held_order khác pending rút; refund sau complete giữ ORDER_EARN |
| Policy chưa chốt | OQ-050/OQ-042 có BranchA/B/frame requirements; OQ-048/049 đã đóng; các P khác có trạng thái từng phần |
| Mâu thuẫn cũ | Đã bỏ các assertions clawback/debt, cash total chỉ available+pending, OQ-049 chưa chốt và blanket P-013–019 chưa duyệt khỏi active design inputs |
| Source snapshots |44SHA-256 của nguồn PRD/BRD/Technical và các file design inputs; pack generated khớp sources |
| Context độc lập | Dưới256KiB, không cần repo access; đủ brief/DS/screens/stories/AC/journeys/cases/contract/policies |
| Links và trạng thái | Local links tồn tại; checklist actual-output unchecked; system/mockups chỉ placeholders; không application skeleton |

Lệnh đã chạy thành công:

```sh
python3 doc/4-DESIGN/tools/build_context.py
python3 doc/4-DESIGN/tools/build_context.py --check
python3 doc/4-DESIGN/tools/verify_handoff.py
```

Các script nằm trong repo, không cần metadata hoặc script trong `/tmp`. Generator đọc sources và rebuild08; verifier kiểm consistency/coverage/freshness và một số assertions về policy. Đây là kiểm tài liệu; không chứng minh100case đã chạy trong app hoặc actual design đã đạt accessibility/interaction.

Báo cáo audit2026-10-21 ở12 giữ nghĩa lịch sử và có disposition mới; không coi mọi finding cũ còn open. Các quyết định D-093–100 và review PRD vòng1 là nguồn mới hơn. Các kết quả v0.1–v0.3 trước đây không thay bản kiểm v0.4 hiện tại.

**Đã unblock:** gửi [prompt](01-claude-design-prompt.md) kèm [context](08-claude-design-context.md) để làm hai packages và review các branches. **Còn mở:** OQ-050 complete-unpaid/OQ-042 settlement-update cùng các phần proposal chưa duyệt; không freeze PRD/Technical hoặc mở implementation chỉ vì brief đã được kiểm tra. Dùng [checklist](05-design-review-checklist.md) khi có actual designs.
