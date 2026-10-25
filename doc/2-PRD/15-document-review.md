# Báo cáo kiểm tra hồ sơ PRD v0.1

> Ngày 2026-10-21 — kiểm tra tài liệu và công thức, **không phải kết quả kiểm thử phần mềm**. Chưa có implementation hoặc deployment.

## Kết quả

- PASS 145 kiểm tra nhất quán tự động: local Markdown links, ID liên tục/duy nhất, tham chiếu feature/screen/route/API/table/AC/QA, dependency graph và các ví dụ tính toán.
- Phạm vi kiểm tra:55 file tài liệu liên quan, gồm báo cáo này. Script thực chạy trong phiên: `python3 /tmp/tpx-prd-verify.py`.
- Nguyên tắc đã đối chiếu: Firebase Auth đã duyệt, SĐT checkout không OTP, admin cố định không OTP/TOTP, phone login sau, không Docker, đủ R1 gồm cả P1; các gate vẫn chưa freeze.

| Hạng mục | Số lượng | Chi tiết |
| --- | --- | --- |
| Feature specs | 21 | F-001–021, mỗi feature có story/inputs/behavior/states/AC |
| Screens/routes | 63 | 32 màn web/app khách + 31 màn admin; có route web và Flutter |
| API operations | 118 | Quyền/input/output/error và DTO/transaction/idempotency |
| Bảng logic | 68 | Fields, FK, constraint/index và transaction notes; chưa tạo migration |
| Feature AC | 104 | Cộng các regression AC-BAL/DATE/LOY/REF/AUTH đã chốt |
| QA scenarios | 42 | Domain/API/DB/security/web/app/worker/ops |
| NFR | 18 | Performance/backup/session targets là proposal cần benchmark |
| Nhóm policy review | 12 | P-001–012 chưa được user duyệt |

## Ví dụ kiểm tra số học và ngày

- Tiền hàng 1.000.000đ, số dư 200.000đ, điểm 50, phí 0: chuyển 750.000đ, tích 950 sau hoàn thành.
- Phí giao 20.000đ: chuyển 770.000đ, earn vẫn 950; opt-out points: chuyển 820.000đ, tích 1000.
- Balance trả hết hoặc gần hết: không âm số phải chuyển, không tiêu points vượt tiền hàng còn lại theo P-005.
- Lưới768 tổ hợp số tiền/phí/số dư/trần giữ tổng nguồn, không âm và không vượt caps; đây là kiểm tra công thức trong PRD.
- Ví 200k/rút 150k: available 50k+pending 150k=total 200k; chỉ available được tiêu.
- Ngày 21/10/2026 xa nhất 28/10; tại 22:00 không còn quyền hủy trước cutoff đó; công thức clawback cumulative tránh thu hồi trùng do làm tròn nhiều lần.

## Review và công việc tiếp theo

- [Review register](11-review-decisions.md) giữ các phương án debit timing, rút, hoàn một phần, điểm cần thu hồi, fee allocation, referral, tái bật món, điều kiện complete, settings, UX/session/NFR. Không được coi PASS tài liệu là đã duyệt các phương án này.
- [Financial rules](13-financial-rules.md) tách nguồn gốc tiền và kênh hoàn; receipt thừa/đến muộn xử lý riêng, không giả funding/earn. Parent/leg refunds và pending cap có guard.
- [Traceability](../5-DELIVERY/12-traceability-matrix.md) nối toàn bộ feature sang AC/QA; review PRD và chuẩn bị design đã có tài liệu đầu vào.
- Chưa tạo skeleton/app/DB migration/account/repository hoặc tài nguyên ngoài hệ thống. Product tests, tích hợp thật và backup restore phải thực hiện sau implementation theo [test plan](../5-DELIVERY/08-test-plan.md).

## Flow review bổ sung ngày 2026-10-21

Review consistency v0.1 không phải review semantic completeness. Audit mới phát hiện28 findings, gồm6 Critical, và16 action/capability gaps. Đã bổ sung25 journeys/100 cases cùng P-013–019; [báo cáo audit](../4-DESIGN/12-flow-audit.md). Đã ghi rõ các nhánh chưa giải quyết state/contract, không tự duyệt hoặc đổi số baseline63 screens/118 API. Chưa thể coi critical money/terminal flows ready để code.

## Review vòng1 ngày2026-10-25

Các kiểm tra số lượng bên trên là snapshot2026-10-21. Hiện có111featureAC và119API draft (thêm admin cancel API-119); D-093–098 đã chốt một phần review. Không còn coi points debit ngay hoặc mandatory full-funded dispatch/debt_points là policy active. Chi tiết nguồn tại [review vòng1](16-review-round-1.md); chưa đủ để freeze các điểm còn OQ-048/049/050/042.

## Kết quả mới nhất 2026-10-25

Hai clarifiers đóng OQ-048/049: D-099 cash+points hold, D-100 cho refund sau complete và không thu hồi ORDER_EARN. Detailed feature AC và consolidated index hiện116AC;119API draft (admin cancel mới), chưa code. `python3 /tmp/tpx-review-round1-verify.py` PASS về hồ sơ; OQ-050/OQ-042 còn mở, không claim đầy đủ acceptance/implementation. Các kết quả104/111AC hoặc118API ở snapshot cũ giữ nghĩa lịch sử.
