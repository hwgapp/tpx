# Open Questions

| ID | Câu hỏi | Mức độ | Owner | Cần chốt trước gate/task | Trạng thái |
| --- | --- | --- | --- | --- | --- |
| OQ-001 | Tên dự án và viết tắt? | Low | User | G2 | Closed — Thực phẩm xanh (TPX), 2026-10-20; folder hiện tại giữ nguyên |
| OQ-002 | Danh sách vùng giao cụ thể trong nội thành TP.HCM? | High | User | G2 | Partial — đã chốt nội thành TP.HCM |
| OQ-003 | Nhóm khách hàng phục vụ? | High | User | G1 | Closed — gia đình, người đi làm; có thể thêm nhà hàng/quán ăn |
| OQ-004 | Đội mình trực tiếp bán toàn bộ hay có nhà bán khác tự đăng hàng, nhận đơn? | High | User | G2 | Closed — TPX trực tiếp bán toàn bộ |
| OQ-005 | Mốc chốt, ngày giao cho đơn muộn và giới hạn số đơn theo khung? | High | User | G2 | Closed — chốt 22:00; sau mốc này sớm nhất giao D+2; khách chọn khung, không giới hạn số đơn; chi tiết lịch vận hành đặc tả ở PRD |
| OQ-006 | Ai mua và giao; có điểm tập kết và sơ chế không? | High | User | G2 | Closed — TPX tự mua/giao, một điểm tập kết, có sơ chế; chi tiết quy trình sẽ làm rõ ở PRD |
| OQ-007 | Cách công bố giá và quy cách khối lượng? | High | User | G2 | Closed — bên thu mua đặt giá trước, không đổi theo giá chợ; TPX tạo quy cách theo sản phẩm trên web cho khách chọn; chưa có yêu cầu tự động cân lại/thu chênh lệch |
| OQ-008 | Cơ chế quyết định hoàn tiền và giao không thành công? | High | User | G2 | Closed về chính sách — hoàn theo thỏa thuận; vận hành trao đổi với khách rồi quyết; thao tác ghi nhận/chi trả đặc tả ở PRD |
| OQ-009 | Câu chuyện và bằng chứng nguồn gốc nông trại sẽ triển khai ra sao? | Medium | User | Trước khi triển khai nội dung nông trại | Deferred — user để tính sau; không chặn discovery hiện tại |
| OQ-010 | Có giữ ngoại lệ xử lý đơn chưa thanh toán? | High | User | G3 | Closed — admin cấp quyền nhân viên quyết thủ công, D-069; không COD |
| OQ-011 | Sửa đơn và áp dụng settings mới đối với đơn đã đặt? | High | User | G3 | Partial — phương án version/snapshot, khách hủy-đặt lại và admin agreement ở P-009; chưa coi đã duyệt |
| OQ-012 | Ngày ra mắt và định nghĩa báo cáo? | Medium | User | Release | Partial — chưa chốt ngày; định nghĩa metrics và targets tại PRD14/P-010/012 để review. Server user có sẵn, không hỏi lại mua máy/ngân sách TD-022 |
| OQ-013 | Cá nhân và nhà hàng/quán ăn có flow riêng không? | High | User | G2 | Closed — hiện tại dùng chung một flow; chưa yêu cầu giá sỉ riêng |
| OQ-014 | Danh mục ban đầu, đơn vị bán và khẩu phần cụ thể? | High | User | G3 | Partial — món sơ chế làm sạch/cắt/chia nguyên liệu chính, không gia vị/sốt; có hướng dẫn nấu; menu cố định, tắt khi hết; nội dung cụ thể TPX cung cấp |
| OQ-015 | “Khách chỉ được hủy trước 9h” nghĩa là gì? | High | User | G2 | Closed — sau mốc TPX chốt lên đơn mua thì không hủy được; user đổi mốc chốt sang 22:00 |
| OQ-016 | Hạn hủy của đơn đặt trước/đơn muộn? | Medium | User | G3 | Closed — hủy trước cutoff đợt mua D-067; giao ngày D khóa hủy 22:00 ngày D−1, D-080 |
| OQ-017 | Thời gian chờ chuyển khoản/xác nhận và xử lý quá hạn? | High | User | G3 | Partial — phải trả khi đặt; ngoại lệ thủ công do nhân viên được admin cho phép đã chốt D-069; timeout chưa chốt |
| OQ-018 | Cách đăng nhập khách hàng? | High | User | G3 | Closed — D-087/088: Google/Facebook/Apple bản đầu; phone + OTP khi dịch vụ sẵn sàng, thay D-030 về giai đoạn |
| OQ-019 | Auth admin và quyền cụ thể? | High | User | G3 | Closed về phương thức — account cố định user tạo, tài khoản/mật khẩu không OTP/TOTP D-086/TD-020; giữ RBAC/audit, session/recovery còn đặc tả |
| OQ-020 | Các kênh thông báo đơn hàng cần có ngay bản đầu? | Medium | User | G3 | Closed — Zalo và push trên app; sự kiện/tích hợp đặc tả ở PRD/Technical |
| OQ-021 | Thứ tự kết hợp các nguồn thanh toán? | High | User | G3 | Closed — số dư tiền hoàn -> điểm trong giới hạn nếu khách chọn -> thanh toán thực phần còn lại bằng chuyển khoản, D-070; cơ sở hạn mức đã chốt D-081, thời điểm ghi sổ còn OQ-023 |
| OQ-022 | Lifecycle xử lý rút và hạn mức/SLA cụ thể? | High | User | G3 | Partial — giữ pending đã chốt; P-002 đề xuất transitions/cancel/reject/processing/paid và đối soát; không đặt SLA/amount default |
| OQ-023 | Thời điểm trừ số dư/điểm và xử lý hủy/điều chỉnh? | High | User | G3 | Closed timing — D-093/099: cash/points HOLD lúc place, CAPTURE lúc complete, RELEASE khi hủy; chỉnh số hold theo update còn OQ-042 |
| OQ-024 | Giá trị sử dụng điểm và quyền rút? | High | User | G2 | Closed — 1 điểm = 1.000đ giá trị thanh toán, không rút tiền; đơn 1.000.000đ trần 5% tối đa 50 điểm (D-075–077) |
| OQ-025 | Cách kết hợp trần phần trăm và tiền khi đổi điểm? | High | User | G2 | Closed về cách kết hợp — áp đồng thời, lấy mức thấp hơn; ví dụ 10%, tối đa 100.000đ; giá trị admin set; mẫu số là tiền hàng sau giảm giá, không phí giao, trước trừ số dư D-081 |
| OQ-026 | Thành phần giá trị thanh toán sau cùng và cách làm tròn tích điểm; cơ sở phần trăm khi đổi điểm? | High | User | G3 | Closed — D-081/082: trần % tính trên tiền hàng sau giảm giá trước trừ số dư, không phí giao; tích trên tiền hàng sau giảm giá trừ điểm dùng, tính cả phần số dư, loại phí giao; làm tròn xuống mỗi 1.000đ |
| OQ-027 | Điểm loyalty có hết hạn không? | Medium | User | G2 | Closed — tạm thời chưa làm hết hạn điểm ở bản đầu (D-047) |
| OQ-028 | Phân bổ hoàn một phần và điểm đã được dùng? | High | User | G3 | Partial — D-100 không clawback ORDER_EARN, không debt; split partial P-003 vẫn review. D-099 phân biệt hold release trước complete và captured points return sau complete |
| OQ-029 | Nguyên liệu thô chọn bằng cách nào? | High | User | G3 | Closed — catalog TPX, chọn quy cách/số lượng (D-058) |
| OQ-030 | Cấu hình và giá món sơ chế? | High | User | G3 | Closed — món/khẩu phần định nghĩa trước, giá sẵn theo gói/khẩu phần (D-059/060) |
| OQ-031 | Hai nhóm có giỏ/đơn/lần giao chung? | High | User | G3 | Closed — được phép (D-061) |
| OQ-032 | Referral: phân bổ, điều kiện và xử lý hoàn? | High | User | G3 | Partial — reward points/settings đã chốt; P-006 đề xuất first-valid attribution, từng bên, mốc đủ điều kiện và reversal; mức cụ thể là config |
| OQ-033 | ORM, queue, push, deployment và dịch vụ tích hợp? | High | User | G4 | Closed về gói stack — TD-019 duyệt; server user có sẵn TD-022, GitHub TD-023. Credentials chưa có; Firebase Auth riêng còn OQ-038 |
| OQ-034 | Mapping ngày giao tương lai sang cutoff 22:00 ngày nào; tối đa đặt trước bao lâu? | High | User | G3 | Closed — D-079/080: tối đa 7 ngày; giao ngày D chốt mua/khóa hủy 22:00 ngày D−1, theo Asia/Ho_Chi_Minh |
| OQ-035 | Nguồn menu/hướng dẫn và nhập nội dung? | Medium | User | Release content | Partial — P-010 soạn phương án nhập tay có source; nguồn thực tế user còn tìm; chưa crawl hoặc chọn website thay user |
| OQ-036 | Tái bật món và tác động order đã có? | High | User | G3 | Partial — auto-off đã chốt; P-007 đề xuất effective availability giữ manual-off, snapshot order không đổi; chưa duyệt tái bật |
| OQ-037 | Thiếu hàng hoàn theo phần nào và thời điểm thực hiện? | High | User | G3 | Partial — trả khi đặt/hoàn theo thỏa thuận đã chốt; P-003/008 có case/agreement/refund legs, partial/full theo thỏa thuận chứ không tự áp toàn đơn |
| OQ-038 | Firebase Authentication cho Google/Facebook/Apple? | High | User | G4 | Closed — user đồng ý, TD-025 duyệt TD-024; credentials chưa tạo |
| OQ-039 | SĐT nhận hàng nhập checkout chưa OTP? | Medium | User | G3 | Closed — user đồng ý D-089; phone login sau link user cũ, contact không tự verified |
| OQ-040 | Quy tắc merge giỏ guest/account, đồng bộ nhiều thiết bị và phục hồi order sau mất phản hồi? | High | User + Codex | G3/G4, trước implementation module liên quan | Proposed — P-013; chưa duyệt, có thể design branch có annotation |
| OQ-041 | Đơn EXCLUDED hoặc TPX không thể thực hiện sau cutoff kết thúc bằng trạng thái nào và giải quyết nguồn tiền/điểm ra sao? | High | User + Codex | G3/G4, trước implementation module liên quan | Closed về hướng business — D-094: hủy/hoàn/mở hold, dùng CANCELLED thay đề xuất NOT_FULFILLED; transitions còn cần đặc tả |
| OQ-042 | Thực thi thay hàng/sửa lịch-người nhận và thu thêm/giảm nghĩa vụ, cập nhật demand/loyalty thế nào? | High | User + Codex | G3/G4, trước implementation module liên quan | Proposed — P-015; chưa duyệt, có thể design branch có annotation |
| OQ-043 | Receipt nhầm/unmatched và payout được xác nhận bank thất bại được sửa/retry bằng workflow nào? | High | User + Codex | G3/G4, trước implementation module liên quan | Proposed — P-016; chưa duyệt, có thể design branch có annotation |
| OQ-044 | Phân bổ hàng thiếu theo nguồn order/RAW/BOM và quản lý demand revision khi đã đi mua thế nào? | High | User + Codex | G3/G4, trước implementation module liên quan | Proposed — P-017; chưa duyệt, có thể design branch có annotation |
| OQ-045 | Kênh hỗ trợ/bằng chứng đồng ý và guard tách phần hàng đã giải quyết khỏi tiền hoàn ngân hàng còn chờ? | High | User + Codex | G3/G4, trước implementation module liên quan | Proposed — P-018; chưa duyệt, có thể design branch có annotation |
| OQ-046 | Runbook/capabilities quản trị cố định và lifecycle theo dõi yêu cầu xóa tài khoản còn nghĩa vụ? | High | User + Codex | G3/G4, trước implementation module liên quan | Proposed — P-019; chưa duyệt, có thể design branch có annotation |
| OQ-047 | Lịch ngày nghỉ/tạm ngừng nhận đơn, slot theo ngày và xử lý đơn đã đặt bị ảnh hưởng? | High | User + Codex | G3, trước delivery options/settings implementation | Proposed — bổ sung P-009/AG-014; chưa chốt lịch hoặc mặc định mở7ngày |
| OQ-048 | Hold đến complete áp dụng chỉ điểm hay cả số dư tiền hoàn? | High | User | G3, trước implementation module liên quan | Closed — D-099: cả cash và points đều HOLD đến complete; cancel RELEASE, không dùng tiếp/rút |
| OQ-049 | Đơn đã complete còn được hoàn không; nếu earned points đã tiêu thì xử lý thế nào để case6 không xảy ra? | High | User | G3, trước implementation module liên quan | Closed — D-100: được hoàn sau complete, không thu hồi ORDER_EARN; thay D-085, không debt/offset |
| OQ-050 | Admin cho giao thiếu tiền có được complete khi vẫn còn phải thu và tích điểm ngay lúc đó không? | High | User | G3, trước implementation module liên quan | Open — D-095 quyết định giao; chưa tự coi quyền complete-unpaid đã được duyệt |
