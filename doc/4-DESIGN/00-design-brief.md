# Design brief — Thực phẩm xanh (TPX)

> v0.4 · 2026-10-25 · Đầu vào thiết kế, chưa phải design output. Nguồn mới nhất D-001–100 và review PRD vòng1. Visual choices ngoài hai màu là đề xuất của designer; business chưa chốt phải có annotation riêng.

## 1. Kết quả cần có

**Design System Package** và **UI Workflow Package** cho toàn bộ R1. Thiết kế high fidelity, component library tái sử dụng và prototype có thể đi hết hành trình. Bàn giao source/editable artifact, tokens, asset provenance và mapping thực, theo [output contract](07-claude-design-output-contract.md).

Phạm vi: **21 nhóm user story, 116 acceptance criteria, 63 màn logic, 56 components, 25 journeys và 100 cases**. 13 UF/28 UC là flow groups trong PRD; J/FC là chi tiết tương tác bổ sung, không phải màn mới. P1 vẫn thuộc R1. Đếm màn/default frame không thay việc thiết kế success/error/recovery.

## 2. Sản phẩm và người sử dụng

TPX trực tiếp bán rau củ quả, thịt cá trứng. Khách đặt trước → TPX gom đơn → mua chợ đầu mối → tập kết một điểm → làm sạch/cắt/chia → TPX tự giao. Khách gia đình, người đi làm, nhà hàng dùng chung flow, thử nghiệm nội thành TP.HCM.

Hai lối mua dùng cùng giỏ/đơn/lần giao: RAW theo quy cách và số gói; MEAL là gói nguyên liệu chính theo món/khẩu phần, giá sẵn, có hướng dẫn nấu. Gói không gồm gia vị/nước sốt, không nấu hoặc tẩm ướp, không cho tùy biến từng nguyên liệu. Trình bày rõ TPX giao gì và khách cần tự chuẩn bị gì.

Trải nghiệm khách ưu tiên dễ chọn món/hàng, đọc quy cách/giá/ngày giao và biết tiền nào còn có thể sử dụng. Admin ưu tiên xử lý đúng đơn/tiền/thu mua, tra được quyết định và biết việc gì còn chờ.

## 3. Hướng thị giác

Giữ primary **#309953**, accent **#F9A01B**, tên Thực phẩm xanh/TPX. Đề xuất light theme, nền trung tính sáng, typography Việt rõ, ảnh thực phẩm tự nhiên; orange nhấn vừa đủ. Consumer ưu tiên ảnh và quyết định mua, admin ưu tiên bảng/form và phân cấp số liệu; cùng ngôn ngữ tokens, khác mật độ/chrome phù hợp tác vụ.

Chưa có logo/ảnh/catalog chính thức: dùng wordmark đơn giản, dữ liệu và asset demo có ghi nguồn. Designer tự chọn font/icon/layout và đề xuất semantic shades đủ contrast. Không gắn claim nông trại/organic/chứng nhận khi chưa có bằng chứng. Không thêm logo redesign, dark theme hoặc animation phức tạp thành điều kiện làm chậm flow chính.

## 4. Surfaces và mức bao phủ

| Nhóm | Yêu cầu |
| --- | --- |
| 32 màn khách | WEB_DESKTOP, WEB_MOBILE, APP_IOS, APP_ANDROID |
| 31 màn admin | ADMIN_DESKTOP, ADMIN_COMPACT; browser responsive, không app admin/shipper riêng |
| Tổng | 190 cặp screen × surface, tất cả cần evidence default layout |

Web mobile phải có layout của màn đó; app Flutter có native navigation/back/keyboard/safe area. iOS/Android có thể dùng shared frame nếu có source thật và notes khác biệt. Admin compact cần thể hiện thông tin và action trọng yếu, không chỉ thu nhỏ bảng desktop. Chi tiết viewport/adaptive tại [design system requirements](02-design-system-requirements.md).

## 5. Business đã chốt phải thể hiện đúng

- Chốt mua 22h HCM. Trước 22h sớm nhất ngày mai, từ 22h ngày kia, tối đa ngày đặt+7. Giao ngày D thì khách hủy trước 22h D−1; admin có nhánh hủy vận hành riêng khi không thực hiện được.
- Giá bán công bố, snapshot đơn không đổi theo giá chợ. Hết/không đạt: TPX trao đổi khách và ghi phương án, không tự thay hàng. Giao phần còn lại đã thống nhất không bị chặn chỉ vì bank refund pending.
- Bank transfer, xác nhận thực nhận thủ công; không COD. Client notice hoặc admin duyệt mua/giao không làm PAID. Admin quyết định giao khi chưa thu đủ, số còn phải thu vẫn hiển thị/audit. Complete-unpaid còn OQ-050.
- Thứ tự: tiền hoàn available → điểm nếu khách chọn trong caps → bank remainder. **Cả cash và points HOLD khi tạo đơn thành công; complete mới CAPTURE, hủy RELEASE.** Không dùng hold của đơn khác hoặc pending rút; quote chưa commit không hold. Capture không trừ available lần hai.
- Cash: total=available+held_order+pending_withdrawal. Points: total=available+held. Không top-up/rút điểm/expiry. Duyệt rút không đồng nghĩa đã chuyển tiền; processing unknown chưa được tự giải phóng.
- Tích1điểm/1.000đ tiền hàng đủ điều kiện sau complete, floor; dùng 1điểm giảm1.000đ. Trần% trên hàng sau giảm giá trước cash, không phí giao, đồng thời có trần VND. Phần cash vẫn tích, phần trả points/phí giao không tích.
- **Cho hoàn sau complete, giữ nguyên ORDER_EARN đã thưởng** (D-100 thay D-085). Hoàn points đã thanh toán là RETURN captured points, khác earned points; trước complete chỉ RELEASE holds. Không debt/clawback/offset hoặc lấy cash bù điểm.
- Khách đăng nhập Google/Facebook/Apple; SĐT nhận hàng chưa OTP, phone login sau. Admin fixed accounts/password, không OTP/TOTP, có RBAC/audit. Zalo và push app; consent nhắc đặt khác quyền OS.

## 6. Phần chưa chốt: thiết kế nhánh có annotation

Đọc trạng thái từng phần [P-001–019](../2-PRD/11-review-decisions.md), không đánh đồng tất cả còn pending. OQ-048/049 đã đóng bằng D-099/100. **OQ-050** (complete/earn khi admin giao chưa đủ tiền) và **OQ-042** (settlement/hold delta khi admin update) chưa có câu trả lời. Các chi tiết P-002/003/005/006/007/009/010/011/013/016/017/019 cũng có phần proposal.

Designer thể hiện branch/variant và assumptions ngoài product UI; không tự chốt policy, fake API hoặc để technical IDs vào copy khách. Hai nhánh ưu tiên có mẫu cụ thể tại [flow requirements](03-screen-flow-requirements.md). Không cần chờ mọi proposal được duyệt để thiết kế các phần đã rõ.

## 7. Cách dùng bộ brief

Có repo: đọc02/03/04/07, journeys13 và cases14. Không có repo: gửi [prompt](01-claude-design-prompt.md) kèm [context pack độc lập](08-claude-design-context.md), pack đã nhúng nguồn cần thiết. Audit12 là snapshot lịch sử có disposition mới, không phải policy hiện tại.

Ngoài scope: COD, tự nạp, rút điểm, expiry, phone OTP bản đầu, marketplace, gia vị/sốt, GPS, chat/AI/OCR/crawler, voucher/subscription/paywall. Prototype chỉ mô phỏng; không kết nối ngân hàng/OAuth/server thật. Chưa tạo/import design artifacts; actual DS/UI output vẫn Pending.
