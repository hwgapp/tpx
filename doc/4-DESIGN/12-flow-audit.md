# Audit flows web, Flutter app và admin — TPX

> v0.2 — 2026-10-21. Rà soát semantic flow sau brief v0.1. **Có nhánh thiếu và nhánh mới chỉ được mô tả khái quát.** Kiểm tra IDs/links/coverage trước đây không chứng minh một hành trình đã xử lý đến cuối. Chưa có UI thực tế để nghiệm thu.

## Cập nhật trạng thái ngày2026-10-25

Findings bên dưới là snapshot audit2026-10-21, không phải tất cả còn chưa chốt. [Review vòng1](../2-PRD/16-review-round-1.md) chọn CANCELLED cho admin cancel, hold/capture/release points, admin quyết định giao thiếu tiền, update đơn và tách giao phần còn lại khỏi refund pending. Những phần business này đã rõ hơn; contracts/code chưa implement. Cash timing/hoàn sau complete/complete-unpaid và settlement adjustment còn mở. Không dùng câu “6Critical cần review” của snapshot cũ để phủ nhận các quyết định mới.

## Kết luận audit ban đầu và mức độ sẵn sàng

Giữ21 feature groups,63 màn logic và190 cặp screen×surface làm baseline. Bổ sung25 hành trình chi tiết và100 case có entry/action/result/recovery; không coi “đủ màn” là “đủ flow”. Các yêu cầu mới về trạng thái/contract dưới đây vẫn là đề xuất, không tự chốt business thay user.

- **Critical**: thiếu đường kết thúc đơn không thể thực hiện; đơn EXCLUDED treo; substitution/thu thêm không có execution chain; receipt correction/unmatched; payout known-failed; guard case/refund có thể kẹt giao.
- **High/Medium**: cart merge/sync, recovery theo platform, my-review và withdrawal history, referral recipient route, admin/deletion recovery, impact queue và support handoff.
- Có thể tiếp tục thiết kế các luồng đã xác định và các branch có nhãn proposal. Chưa đủ điều kiện freeze money/terminal contracts hoặc coi prototype là implementation đã chạy.

## Cách rà soát

Đối chiếu trực tiếp21 spec/104 AC,13 UF,63 screens/routes,118 API, permission/state/financial rules và28 UC/12 ST của brief. Mỗi action được kiểm qua: entry/actor; prerequisite/allowed action; dữ liệu/mutation; success; validation/conflict; interruption/retry; cross-role handoff; terminal/recovery. Các case hiện đã có trong nguồn được ghi “đã có, cần frame riêng”, không báo sai là thiếu nghiệp vụ.

## Finding register

| Finding | Mức / loại | Khoảng trống và bằng chứng hiện tại | Journey / policy / action gap |
| --- | --- | --- | --- |
| FG-001 | High · Thiếu flow/contract | Guest cart merge sau login — 03/UC-004 chỉ nói trở lại giỏ; API-019–021 chỉ giỏ authenticated, không có quy tắc merge. | J-001, J-005; P-013; AG-001 |
| FG-002 | High · Cần cụ thể hóa | Cold start/refresh/link/unlink/logout mọi phiên — UF-001 có token/conflict, nhưng chưa có kết quả UI khi app bị đóng, callback lặp hoặc cache user cũ. Unlink đã nêu ở F-001 nhưng chưa mô tả Firebase→TPX sync. | J-002; P-011; AG-002 |
| FG-003 | Medium · Cần cụ thể hóa | CRUD địa chỉ và quote sau đổi vùng — API-008–011 có CRUD; UC-005 chỉ tóm tắt chọn/thêm, chưa gắn delete/default/contact snapshot và invalidate slot/fee. | J-003; P-009 P-015; — |
| FG-004 | Medium · Cần cụ thể hóa | Chọn variant, search rỗng và Back từ hướng dẫn — UC-001/002 có happy path; cần return context và missing/archive/quy cách đổi để không tự thay hàng. | J-004; PRD; — |
| FG-005 | High · Thiếu quy tắc | Giỏ nhiều thiết bị và clear sau order — F-004 có version nhưng chưa nói hàng thêm đồng thời có bị xóa khi order commit hay merge guest/user ra sao. | J-005; P-013; AG-001 |
| FG-006 | Medium · Đã có, cần frame riêng | Boundary22h, max+7 và đơn giao xa — F-008/UF-004 đã có rule; thêm test clock/timezone/midnight và chọn lại có chủ đích, không coi là thiếu business rule. | J-006; PRD; — |
| FG-007 | High · Đã có, cần frame riêng | Caps, pending, minimum, zero-bank và unknown order — P-001/005/009 và công thức đã có; UC-003/008 đang gộp, cần chứng minh từng nhánh thay vì generic error. | J-007, J-013; P-001 P-004 P-005 P-009; — |
| FG-008 | High · Cần cụ thể hóa | Quay lại từ ngân hàng/cold start — 03 có một câu external bank return, chưa có điểm phục hồi khi app chết, receipt partial hoặc bank instructions đổi. | J-008; P-016; AG-004 |
| FG-009 | High · Đã có, cần frame riêng | Cancel vs receipt vs cutoff — UF-008/AC đã nêu; cần hủy xong nhưng hoàn chưa xong, giữ order terminal khi nhận bank muộn. | J-009; P-001 P-003 P-006; — |
| FG-010 | Critical · Thiếu action chain | Đổi món làm tăng tiền/đổi nhu cầu — P-009 nêu phải thu thêm, API-109 chỉ lưu agreement; chưa có execution revision/thu thêm/re-price eligibility và demand delta. | J-010, J-022; P-015 P-017; AG-007 |
| FG-011 | Critical · Thiếu trạng thái kết thúc | Không có gì giao sau cutoff/giao thất bại cuối — 12-domain-states chỉ CANCELLED bởi customer trước cutoff và COMPLETED sau giao; không có terminal cho TPX không thực hiện được. | J-010, J-023; P-014; AG-005 |
| FG-012 | Critical · Thiếu resolution | EXCLUDED còn order/tiền/điểm treo — Domain2 ghi EXCLUDED không tự cancel/refund; chưa có đường giải quyết sau loại đơn, nhất là đã áp nguồn nội bộ. | J-021; P-014; AG-005 |
| FG-013 | High · Thiếu quy tắc/contract | Thiếu hàng phân bổ về từng order — F-006 có nguồn RAW/BOM nhưng không có cách phân bổ accepted qty khi không đủ hoặc cập nhật kế hoạch sau thay hàng. | J-022; P-017; AG-008 |
| FG-014 | Critical · Thiếu action/contract | Receipt nhầm order/amount hoặc chưa biết order — Có enum REVERSED, API-077 yêu cầu order cụ thể nhưng không có reversal/unmatched allocation workflow. Không thể coi refund là sửa xác nhận nhầm. | J-024; P-016; AG-004 |
| FG-015 | Critical · Thiếu recovery | Bank payout PROCESSING đã xác nhận thất bại — P-002/003 xử lý unknown tốt, nhưng hiện chỉ có mark-paid/settle sau processing; thiếu nhánh known-failed/correction/retry có bằng chứng. | J-011, J-012; P-016; AG-006 |
| FG-016 | High · Thiếu navigation subview | Danh sách yêu cầu rút của khách — API-032 có list nhưng S-024 chỉ detail, route không có list entry; cần history/list trong S-022/S-024 và đường quay lại. | J-012; P-002; AG-009 |
| FG-017 | High · Thiếu read contract | Xem lại review của tôi pending/hidden — API-049 chỉ submit, API-018 chỉ public published; chưa có my-review/status/read path đủ dựng flow quay lại. | J-016; P-010; AG-010 |
| FG-018 | Medium · Thiếu entry route | Referral recipient claim — API-044 có claim, S-026 chỉ link của tôi; chưa có URL nhận mã, giữ mã qua login và fallback web khi không có app. | J-014; P-006 P-013; AG-011 |
| FG-019 | High · Cần cụ thể hóa | OS permission vs consent và private deep link — UF-012 đã có denied/ownership; cần foreground/background/cold start, đổi user và quay lại OS settings. Không thêm yêu cầu web push. | J-017; PRD; — |
| FG-020 | High · Cần cụ thể hóa | Admin không quyền dashboard/mất quyền đang thao tác — RBAC có guard; UC-016 chưa có landing đầu tiên được phép và interrupted action khi role/session đổi. | J-018; P-019; AG-012 |
| FG-021 | High · Thiếu operational recovery | Fixed admin provisioning/reset/last access — API-056–059 chỉ list/update roles; session controls trong brief vượt khả năng endpoints hiện tại. Cần runbook hoặc contract thực cho recovery. | J-018; P-019; AG-012 |
| FG-022 | High · Thiếu owner/readback | Xóa tài khoản còn đơn/tiền/payout — API-007 nhận request nhưng không có progress/readback/admin resolution đầy đủ. P-011 đúng ý định, chưa đủ UI flow xử lý đến cuối. | J-025; P-011 P-019; AG-013 |
| FG-023 | High · Thiếu impact queue cụ thể | Tắt ingredient ảnh hưởng prepaid orders tương lai — API-069 trả affected products/meals, domain nói cần case order cũ; chưa có query/entry tìm đủ order bị ảnh hưởng theo snapshot. | J-019, J-020; P-007 P-009 P-017; AG-014 |
| FG-024 | High · Cần cụ thể hóa | Settings readiness theo feature và bank snapshot — UC-025 có validate, chưa nêu bank cũ/slot tắt/thiếu reward khác thiếu checkout config; cần tránh chặn sai module. | J-020; P-009 P-016; AG-014 |
| FG-025 | High · Thiếu handoff/queue contract | Trách nhiệm xử lý việc đang treo — Các API list có status nhưng dashboard/queue chưa cam kết đủ unmatched, excluded, no-contact, payout unknown và deletion. Không tự thêm task-management suite. | J-021, J-024, J-025; P-014 P-016 P-018 P-019; AG-015 |
| FG-026 | Critical · Mâu thuẫn guard/liên kết state | Case còn hoàn bank làm kẹt giao phần hàng đã thống nhất — UF-007 và domain1 chặn case chưa xử lý; domain2a/close đợi financial legs. Chưa định nghĩa agreed fulfillment đã resolved trong khi refund còn pending. | J-010, J-011, J-023; P-018; AG-016 |
| FG-027 | High · Thiếu support handoff | Khách báo lỗi sau complete/chưa liên hệ được — S-031 support và admin cases có, nhưng chưa có entry từ order/refund/withdraw, bằng chứng đồng ý và nhánh không trả lời; không mặc định in-app ticket. | J-025, J-010, J-023; P-018; AG-016 |
| FG-028 | High · Đã có, thiếu chứng minh xuyên vai trò | Generic states chưa chứng minh hành trình kết thúc — 28 UC +12 ST bao phủ tên nhưng không có preconditions→mutation→result→recovery cho từng action và platform. Coverage190cell chỉ default, không đủ edge. | J-001, J-007, J-011, J-018, J-024; PRD; — |

## Những nhánh phải review trước khi code

1. P-014: kết thúc đơn không thể giao hoặc EXCLUDED, hoàn phần nội bộ/bank và không tích điểm sai.
2. P-015: thực thi thay hàng/sửa ngày-người nhận, nghĩa vụ tăng/giảm và nguồn phải thu thêm.
3. P-016: sửa sai receipt/payout, tiền chưa biết order, bank đã xác nhận thất bại; bảo toàn ledger/audit.
4. P-017: phân bổ thiếu hàng theo nguồn đơn và sửa demand khi thay hàng.
5. P-018: tách fulfillment resolution khỏi bank refund pending, support và bằng chứng thỏa thuận.
6. P-013/P-019: quy tắc giỏ khách/đa thiết bị và admin/account/deletion recovery.

Các rule đã chốt như 22h/+7 ngày, không COD, không nạp, không rút điểm, thứ tự nguồn tiền và tỷ lệ loyalty không bị mở lại.

## Bàn giao tiếp theo

- [25 detailed journeys](13-detailed-journeys.md): ai làm gì, state/result và điểm kết thúc.
- [100 case matrix](14-flow-case-matrix.md): scenario yêu cầu thiết kế, toàn bộ Expected.
- [Action/contract gaps](15-action-contract-gaps.md): thiếu capability nào, prototype được thể hiện đến đâu.
- [Review register](../2-PRD/11-review-decisions.md): P-001–019 chưa được user duyệt; không bịa API/state đã có.

Khi Claude Design giao lại, cần map J/FC tới actual frame/prototype và review các path này. Hiện mới hoàn thiện đầu vào audit, chưa có sản phẩm hoặc test pass về hành vi.
