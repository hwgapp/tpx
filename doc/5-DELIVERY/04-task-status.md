# Task Status

Status chuẩn:

```text
Todo -> Ready -> Running -> Review -> Done
Blocked
Deferred
```

| Task ID | Phase | Lane | Status | Size | Depends On | Blocks | Owner | Progress | Tests | Blocker | Notes |
| --- | --- | --- | --- | ---: | --- | --- | --- | ---: | --- | --- | --- |
| T-001 | P0 | Docs | Done | 1 | - | T-002 | Codex | 100% | Đối chiếu 6 câu trả lời G0 với intake, config, decision logs; kiểm tra template được copy đủ và không có source code mới | - | Khởi tạo hồ sơ và ghi nhận yêu cầu; không đồng nghĩa G0 đã được user review |
| T-002 | P0 | Discovery | Review | 1 | T-001 | BRD/PRD freeze | User + Codex | Draft ready | Review business/phạm vi; ghi nguồn và open questions | - | Chính sách cốt lõi đã tổng hợp, gồm giá trị điểm/admin; BRD sẵn review, PRD còn chi tiết; chưa freeze gate |
| T-003 | P0 | Docs | Done | 1 | T-001 | - | Codex | 100% | Đối chiếu tên và viết tắt trong README, status, intake và decision log | - | Cập nhật Thực phẩm xanh (TPX); đóng OQ-001; không phát sinh task được unblock |
| T-004 | P0 | Docs | Done | 1 | T-001 | - | Codex | 100% | Đối chiếu 9 câu trả lời với intake, decision log, config, brief và business rules; giá/trọng lượng vẫn TBD | - | Ghi G1 vòng đầu; đóng OQ-003/004/006, hoãn OQ-009; chưa unblock BRD freeze |
| T-005 | P0 | Docs | Done | 1 | T-001 | - | Codex | 100% | Đối chiếu 8 câu trả lời với intake, decision log, config, brief và business rules; mốc hủy chưa bị suy diễn | - | Ghi G1 vòng 2; mở OQ-015; cập nhật quyết định thủ công hiện tại và tự động hóa về sau; chưa unblock BRD freeze |
| T-006 | P0 | Docs | Done | 1 | T-001 | - | Codex | 100% | Kiểm tra mốc 22:00 nhất quán trong docs hiện hành; giữ raw notes/decision cũ; không thêm quota giao hoặc tự hủy đơn chưa thanh toán | - | Ghi G1 vòng 3 và scope nháp; đóng OQ-005/007/010/015; bổ sung OQ-016/017; chưa unblock BRD freeze |
| T-007 | P0 | Docs | Done | 1 | T-001 | - | Codex | 100% | Đối chiếu 5 câu trả lời với intake, decision log, rules, scope, config và brief; không tự chọn nhà cung cấp OTP/Zalo hoặc rule số dư | - | Ghi G1 vòng 4; đóng OQ-013/018/020; mở OQ-021, RBAC chi tiết còn mở; chưa unblock BRD freeze |
| T-008 | P0 | Docs | Done | 1 | T-001 | - | Codex | 100% | Đối chiếu chính xác hai mã màu trong brief, tokens, prompt và decision log | - | Ghi màu TPX #309953/#F9A01B; không có task được unblock; discovery số dư còn mở |
| T-009 | P0 | Docs | Done | 1 | T-001 | - | Codex | 100% | Đối chiếu 5 câu trả lời số dư; ghi rõ câu 4 chưa trả lời; không suy diễn quyền trừ thủ công hoặc hoàn ngân hàng tự động | - | Ghi G1 vòng 5 và cập nhật BRD nháp; OQ-021/022/023 còn mở; chưa unblock BRD freeze |
| T-010 | P0 | Docs | Done | 1 | T-001 | - | Codex | 100% | Đối chiếu loyalty với intake, decisions, rules, scope, config và monetization; không suy diễn tỷ lệ đổi hoặc coi ví dụ là mặc định | - | Ghi G1 vòng 6; mở OQ-024–028; chưa unblock BRD freeze |
| T-011 | P0 | Docs | Done | 1 | T-001 | - | Codex | 100% | Kiểm tra thời điểm tích là sau khi đơn hoàn thành; không tự thêm điều kiện thanh toán đủ; cơ sở tính vẫn mở | - | Ghi D-044, cập nhật BR-023 và OQ-026; chưa có task được unblock |
| T-012 | P0 | Docs | Done | 1 | T-001 | - | Codex | 100% | Kiểm tra docs hiện hành không có COD bản đầu; trần đổi điểm đồng thời, cơ sở tích/hạn điểm đúng; kỳ vọng đơn không bị tự đổi thành số cụ thể | - | Ghi D-045–051 và G1 vòng 7; hoàn thiện BRD nháp; chuẩn bị review được unblock, BRD freeze chưa được unblock |
| T-013 | P0 | Docs | Done | 1 | T-001 | - | Codex | 100% | Đối chiếu 6 phản hồi với D-052–057; kiểm tra hai nhóm trong BRD/PRD, feature ID và flow; không biến ví dụ ưu đãi/tỷ lệ điểm thành quyết định | - | Ghi nhận phạm vi 2026-10-21; PRD nháp/chuẩn bị trao đổi Technical được unblock; chưa freeze gate hoặc tạo skeleton |
| T-014 | P0 | Docs | Done | 1 | T-013 | - | Codex | 100% | Kiểm tra D-058–061 và TD-002–013; phân biệt stack user chọn với phần Proposed; kiểm tra không có code skeleton mới | - | Đóng OQ-029–031; soạn Technical để review; chưa unblock implementation |
| T-015 | P0 | Docs | Done | 1 | T-014 | - | Codex | 100% | Kiểm tra Flutter thay mobile cũ; không Docker trong phương án hiện hành; giữ lịch sử TD-008/012 với trạng thái bị thay | - | Ghi TD-014–017; cập nhật workspace/push/deploy đề xuất; chưa unblock implementation |
| T-016 | P0 | Docs | Done | 1 | T-013 | - | Codex | 100% | Đối chiếu D-062–066 với BRD/PRD/config; không coi 5 ngày là tối đa hoặc lời đang tìm nguồn là lệnh crawl | - | Ghi phạm vi sơ chế, menu, hướng dẫn và đặt trước; mở OQ-034–037; chưa unblock freeze/implementation |
| T-017 | P0 | Docs | Done | 1 | T-016 | - | Codex | 100% | Kiểm tra hủy theo cutoff tương ứng đơn và trả lúc đặt; không tự đặt timeout, xóa ngoại lệ D-026 hoặc chốt ngày cutoff | - | Ghi D-067/068; đóng OQ-016, cập nhật OQ-017/034/037; chưa unblock freeze/implementation |
| T-018 | P0 | Docs | Done | 1 | T-017 | - | Codex | 100% | Đối chiếu D-069–073; thứ tự tiền hoàn/điểm/thực trả; quyền ngoại lệ; rút thủ công; món auto-off; không suy diễn giá trị đổi điểm hoặc giữ tiền chờ rút | - | Đóng OQ-010/021 về chính sách, cập nhật OQ-017/022/024/028/032/036; chưa unblock freeze/implementation |
| T-019 | P0 | Docs | Done | 1 | T-018 | - | Codex | 100% | Kiểm tra D-074–077/TD-018, 1 điểm = 1.000đ, điểm không rút, ví dụ 50 điểm và một admin; không cố định 5% | - | Đóng OQ-024; có permission matrix bản đầu; T-002 chuyển Review, bước review business được unblock; chưa unblock implementation |
| T-020 | P0 | Docs | Done | 1 | T-019 | - | Codex | 100% | Đối chiếu D-078/BR-035 và AC-BAL-001–003: tổng 200.000đ, pending 150.000đ, available 50.000đ; checkout chỉ dùng available | - | Chốt chính sách giữ tiền chờ rút; cập nhật PRD/data model draft; review luồng số dư được unblock, chưa unblock implementation |
| T-021 | P0 | Docs | Done | 1 | T-020 | - | Codex | 100% | Đối chiếu D-079–085/BR-036–037; kiểm tra ngày +7, cutoff 22h trước giao, ví dụ dùng 50 điểm/tích 950, phí giao không tích và hoàn đúng nguồn | - | Đóng OQ-026/034, chốt chính sách OQ-028; chi tiết PRD lịch/loyalty được unblock; chưa unblock implementation |
| T-022 | P0 | Docs | Done | 1 | T-021 | - | Codex | 100% | Đối chiếu TD hiện hành, giữ Flutter/không Docker, sửa tham chiếu business đã đóng; tra docs chính thức cho ORM/queue/self-host/push/UI | - | Chuẩn bị vòng review Technical 1, không tự duyệt proposal; review kiến trúc và hạ tầng được unblock, chưa unblock skeleton/implementation |
| T-023 | P0 | Docs | Done | 1 | T-022 | - | Codex | 100% | Đối chiếu 5 trả lời với D-086–088/TD-019–024; kiểm tra auth/provider docs, phase và giữ RBAC/no Docker | - | Stack/module/auth design được unblock; Firebase Auth còn Proposed, chưa freeze schema/contracts hoặc tạo skeleton |
| T-024 | P0 | Docs | Done | 1 | T-023 | - | Codex | 100% | Kiểm tra links/IDs/21spec/63screens/118API/68tables/104featureAC/42QA/18NFR, dependency graph và ví dụ tiền/ngày; không claim product tests | - | PRD v0.1 toàn hệ thống sẵn review; Firebase Auth/contact đã duyệt, P-001–012 còn proposal; review/design preparation được unblock, implementation chưa mở |
| T-025 | P0 | Docs | Done | 1 | T-024 | - | Codex | 100% | Đối chiếu21stories/104AC,63screens,13flows,28scenarios,56CMP,190surface cells; kiểm tra links/IDs/hash snapshots/contrast/output status | - | Design brief/prompt/context pack ready để user gửi Claude Design; actual DS/UI Pending, chưa import hoặc unblock code |
| T-026 | P0 | Docs | Done | 1 | T-025 | Review flow gaps | Codex | 100% | Đối chiếu PRD/flow/state/API; kiểm IDs/refs/snapshot/J-FC coverage và standalone pack; không claim product tests | - | Flow audit v0.2:28findings/6Critical,25J/100FC,16AG; P-013–019 chưa duyệt. Detailed design/review được unblock, critical implementation chưa mở |
| T-027 | P0 | Docs | Done | 1 | T-026 | Clarify OQ-048/049/050/042 | Codex | 100% | python3 /tmp/tpx-review-round1-verify.py; source/AC/API/state/hold/links/snapshot checks, no product tests | - | Ghi D-093–100 theo6trả lời và2clarifiers, phân biệt phần chốt/mở; cập nhật PRD/schema draft/design context. Unblock đặc tả points/admin; cash/points cùng hold, không clawback ORDER_EARN; complete-unpaid/chênh lệch còn mở |
| T-028 | P0 | Docs | Done | 1 | T-027 | Claude Design handoff | Codex | 100% | python3 doc/4-DESIGN/tools/verify_handoff.py; consistency/coverage/snapshot/branch checks, không product tests | - | Brief v0.4 làm lại DS/UI requirements và current rules; context độc lập/generator/validator trong repo. Unblock gửi design; actual output Pending, OQ-050/042 còn mở |
| T-029 | P0 | Git | Running | 1 | T-028 | GitHub publication | Codex | Prepared | verify_handoff.py PASS; inspect staged files; verify remote HEAD after push | - | User yêu cầu push; origin hwgapp/tpx đang trống, chuẩn bị initial commit main; không thêm application skeleton |

## Rollup

| Phase | Done Points | Total Points | % | Forecast |
| --- | ---: | ---: | ---: | --- |
| P0 | 27 | 29 | 93% | Chờ review BRD/PRD/Technical; đây là tiến độ task hồ sơ, không phải tiến độ sản phẩm |
