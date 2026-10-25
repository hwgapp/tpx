# Interview Log

| Ngày | Gate | Câu hỏi / Chủ đề | Câu trả lời ngắn | Follow-up |
| --- | --- | --- | --- | --- |
| 2026-10-20 | G0 | Ý tưởng, nền tảng, release, doanh thu, backend | Thực phẩm tươi; gom đơn buổi tối, mua ở chợ đầu mối; iOS/Android/Web/Admin/API; production; lãi mua-bán; Node.js modular | Review tổng hợp G0, tiếp tục discovery vận hành G1 |
| 2026-10-20 | G0 | Tên dự án | Thực phẩm xanh; viết tắt TPX | Đã cập nhật tên trong hồ sơ; tiếp tục các câu hỏi vận hành G1 |
| 2026-10-20 | G1 | Khách hàng, vùng giao, người bán, vận hành và thanh toán | Nội thành TP.HCM; gia đình/người đi làm, có thể thêm quán ăn; TPX tự bán/mua/giao; một điểm tập kết và sơ chế; đặt hằng ngày giao hôm sau; chuyển khoản trước, COD cho khách quen; trao đổi khi thiếu hoặc hàng không đạt; câu chuyện nông trại để sau | Chốt giờ chốt đơn, khung giao, giá và trọng lượng, xác nhận thanh toán, tiêu chí COD, phí giao và hủy đơn |
| 2026-10-20 | G1 | Quy tắc vận hành vòng 2 | Chốt 21h; web cho chọn khung giao; thu mua đặt giá trước; trọng lượng theo sản phẩm; xác nhận chuyển khoản và duyệt COD thủ công; phí giao/đơn tối thiểu cấu hình admin; hủy “trước 9h” | Làm rõ 9h sáng/tối và ngày áp dụng; đơn sau giờ chốt/chưa thanh toán; quy cách hàng và xử lý chênh lệch cân; khung giao |
| 2026-10-20 | G1 | Quy tắc vận hành vòng 3 | Đổi mốc chốt/khóa hủy sang 22h; sau 22h sớm nhất giao D+2; nhân viên quyết định mua đơn chưa thanh toán; TPX tạo quy cách trước cho khách chọn; khung giao không giới hạn số đơn | Cập nhật quy tắc hiện hành, giữ lịch sử 21h; tiếp tục phạm vi sản phẩm, ngoại lệ hoàn tiền và chăm sóc khách |
| 2026-10-20 | G1 | Phạm vi bản đầu vòng 4 | Chung flow cá nhân/quán ăn; SĐT + OTP; RBAC đầy đủ; Zalo và push qua app; quản lý số dư để dùng cho đơn sau | Làm rõ nguồn số dư, quyền rút, cách sử dụng/thanh toán kết hợp, thời hạn và quyền điều chỉnh; chưa chọn dịch vụ tích hợp |
| 2026-10-20 | G1 — bổ sung đầu vào Design | Màu thương hiệu | Chủ đạo #309953, nhấn #F9A01B ở một số vị trí cần thu hút | Đã ghi design brief/tokens/handoff prompt; các câu hỏi số dư còn mở |
| 2026-10-20 | G1 | Số dư vòng 5 | Không tự nạp; yêu cầu rút về ngân hàng; ưu tiên tự trừ; không hết hạn; admin thêm số dư khi điều chỉnh đơn | Câu 4 thanh toán kết hợp chưa được trả lời; chuẩn bị BRD nháp, giữ quy trình rút và quyền chi tiết là open questions |
| 2026-10-20 | G1 | Loyalty vòng 6 | Có từ bản đầu; 1.000đ chi tiêu tích 1 điểm; khách chọn dùng điểm; giới hạn đổi điểm do admin set, ví dụ 10% - 100k | Chốt tỷ lệ đổi, cách kết hợp hạn mức, thời điểm/cơ sở tích và hạn điểm; tiền hoàn và loyalty có quy tắc riêng |
| 2026-10-20 | G1 | Bổ sung thời điểm tích loyalty | Sau khi đơn hoàn thành | Cập nhật D-044; tỷ lệ đổi, giới hạn, cơ sở tính và hạn điểm còn mở |
| 2026-10-20 | G1 | Business vòng 7 | Trần % và tiền đồng thời, admin set; tích trên giá trị thanh toán cuối, chưa hết hạn; chỉ bank transfer ở bản đầu; hoàn theo thỏa thuận; vận hành quyết khi giao lỗi; kỳ vọng vài chục đơn/ngày nội thành | Hoàn thiện BRD draft; còn tỷ lệ đổi điểm và các chi tiết checkout/ngoại lệ ở PRD; COD được hoãn |
| 2026-10-21 | G1/G2 — đầu vào PRD | Phạm vi hai nhóm mua hàng | Nguyên liệu thô theo yêu cầu và sơ chế theo món; đồng ý minh bạch/đánh giá, referral và mua lại/nhắc đặt; chiến dịch thuộc vận hành | Làm rõ hai luồng, giá và giỏ; chuẩn bị Technical sau BRD/PRD; tỷ lệ đổi điểm còn mở |
| 2026-10-21 | PRD/Technical draft | Cách mua, giá và stack | Catalog thô; món/khẩu phần giá sẵn; giỏ/đơn/giao chung; NestJS/React/Next.js/PostgreSQL | Đóng OQ-029–031; soạn đề xuất phần bổ sung TD-005–013; chưa freeze hoặc tạo skeleton |
| 2026-10-21 | Technical draft | Mobile/deployment | User chọn Flutter, không React Native và không Docker | Ghi TD-014/015; thay push/deployment và workspace proposal; FCM và chạy Node.js trực tiếp còn Proposed |
| 2026-10-21 | Business/PRD draft | Sơ chế, menu, hướng dẫn và đặt trước | Làm sạch/cắt/chia nguyên liệu chính, không gia vị/sốt; có hướng dẫn; menu cố định, tắt khi hết; được đặt nhiều ngày, thiếu nguyên liệu ngày mua thì hoàn | Ghi D-062–066; làm rõ batch/khóa hủy/thanh toán đơn tương lai, nguồn nội dung và tác động tắt nguyên liệu |
| 2026-10-21 | Business/PRD draft | Hủy và thanh toán | Hủy được khi chưa tới cutoff mua của đơn; thanh toán ngay lúc đặt | Ghi D-067/068; đóng OQ-016, cập nhật OQ-017/034/037; không tự chốt timeout, mapping ngày cutoff hoặc bỏ ngoại lệ cũ |
| 2026-10-21 | Business/PRD draft | Quyền ngoại lệ, thứ tự tiền/điểm, rút hoàn, availability và referral | Admin cấp quyền quyết thủ công; số dư -> điểm có hạn mức -> thực trả; nhân viên duyệt/chuyển rút; tự tắt món theo nguyên liệu; referral thưởng điểm settings | Ghi D-069–073; đóng OQ-010/021 về chính sách; loại thưởng, bước rút và auto-off đã rõ; tỷ lệ đổi điểm/tiền chờ rút còn mở |
| 2026-10-21 | Business/PRD review | Admin bản đầu và quy đổi loyalty | Một admin toàn quyền; 100 điểm = 100.000đ giá trị dùng, không rút tiền; đơn 1.000.000đ trần 5% dùng 50 điểm; xác nhận thứ tự nguồn và rút tiền hoàn | Ghi D-074–077/TD-018; đóng OQ-024; cập nhật permission matrix và hồ sơ sẵn review, không tự chốt mặc định 5% |
| 2026-10-21 | Business/PRD review | Giữ tiền yêu cầu rút | Tổng 200.000đ, rút 150.000đ chuyển pending; chỉ 50.000đ available được thanh toán | Ghi D-078/BR-035, AC-BAL-001–003; chính sách giữ tiền đã chốt, lifecycle xử lý rút còn ở PRD |
| 2026-10-21 | Business/PRD review | Lịch đặt trước, cơ sở loyalty và hoàn | Đặt trước 7 ngày; đồng ý cutoff 22h ngày trước giao, cơ sở trần/tích và làm tròn xuống; hoàn điểm bằng điểm, tiền theo thỏa thuận, thu hồi điểm tích tương ứng | Ghi D-079–085; đóng OQ-026/034 và chính sách OQ-028; cập nhật acceptance criteria, chưa freeze gate |

| 2026-10-21 | Technical draft/review | User yêu cầu trao đổi Technical | Giữ stack đã chọn và không Docker; chưa có xác nhận mới cho các đề xuất | Chuẩn bị review kiến trúc, tooling, auth admin, hạ tầng, tích hợp và repository/CI tại technical brief |

| 2026-10-21 | Technical draft/review | Trả lời vòng 1 | Duyệt stack; admin cố định không OTP; server có sẵn; Google/Facebook/Apple trước phone OTP; GitHub | D-086–088/TD-019–024; cập nhật auth/RBAC/phase, Firebase Auth Proposed OQ-038 |

| 2026-10-21 | PRD toàn hệ thống draft review | User đồng ý Firebase Auth/contact, yêu cầu PRD web/app/admin/DB | Chốt D-089/090 và TD-025; chuẩn bị PRD v0.1, API/data/state/security/AC/QA đủ toàn hệ thống | P-001–012 là phương án chi tiết còn review; OQ-038/039 đóng; chưa freeze hoặc tạo code |

| 2026-10-21 | Design handoff input | Brief cho Claude Design | User sẽ giao design system và UI flows cho toàn bộ stories web/app/admin | Ghi D-091; chuẩn bị prompt/context pack, coverage/CMP/state/output contract; chưa có actual design/import |

## 2026-10-21 — Flow audit sau design brief

User yêu cầu rà kỹ flows/cases app/web/admin. Đối chiếu hành trình, cross-role và recovery thay vì chỉ đếm screens. Kết quả28findings/6Critical,25journeys/100cases,16action gaps; P-013–019/OQ-040–046 là proposal chưa duyệt. D-092/T-026 ghi việc audit, không approval nghiệp vụ hay implementation.

## 2026-10-25 — Review PRD vòng1

Ghi D-093–098 và [review vòng1](../2-PRD/16-review-round-1.md). Điểm chuyển sang hold→capture khi complete/release khi cancel. Admin quyết giao thiếu tiền, có chức năng sửa đơn; refund pending không tự chặn giao phần còn lại. Câu6 chưa xác định cách loại trừ earned-points clawback; không triển khai debt proposal như đã duyệt. OQ-048/049 cần trả lời; OQ-050/OQ-042 còn chi tiết.

## 2026-10-25 — Làm rõ cash hold và earn sau hoàn

D-099 đóng OQ-048: cash và points cùng hold đến complete. D-100 đóng OQ-049: vẫn hoàn sau complete, không thu hồi ORDER_EARN; thay D-085. Không còn debt/offset hoặc blanket cấm hoàn sau complete. OQ-050 complete-unpaid và OQ-042 settlement update còn mở.

## 2026-10-25 — Design handoff v0.4

User yêu cầu kiểm tra/hoàn thiện design system và UI flows. D-101/T-028 ghi task; không có câu trả lời mới cho OQ-050/042. Đồng bộ quy tắc mới D-093–100, gỡ policy cũ mâu thuẫn, cụ thể hóa gallery/tokens/evidence/platform branches; chưa tạo designs hoặc implementation.
