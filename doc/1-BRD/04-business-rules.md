# Business Rules

> Draft từ yêu cầu trực tiếp của user; chưa freeze BRD. Các chi tiết TBD không được tự suy diễn khi implement.

| ID | Rule | Applies To | Source | Notes |
| --- | --- | --- | --- | --- |
| BR-001 | TPX trực tiếp bán toàn bộ sản phẩm | Người bán | D-009 | Phạm vi hiện tại có một đơn vị bán là TPX |
| BR-002 | Chốt gom mua lúc 22:00; trước mốc sớm nhất giao hôm sau, sau mốc sớm nhất D+2; khách có thể chọn ngày xa hơn | Đơn hàng | D-010, D-023, D-025, D-066, D-079/080 | Tối đa ngày đặt + 7 ngày; giao ngày D chốt mua lúc 22:00 ngày D−1, theo Asia/Ho_Chi_Minh |
| BR-003 | TPX tự đi mua, tập kết một điểm, sơ chế rồi tự giao | Vận hành | D-011 | Lịch và trách nhiệm từng bước chi tiết TBD |
| BR-004 | Khi thiếu hàng hoặc hàng không đạt, trao đổi với khách về hoàn tiền hoặc mua lại món khác; hoàn theo thỏa thuận | Ngoại lệ đơn hàng | D-012, D-049 | Quy trình ghi nhận phương án và thực hiện hoàn đặc tả ở PRD; không tự thêm thời hạn/tỷ lệ hoàn cố định |
| BR-005 | Khách thanh toán ngay khi đặt, kể cả đơn tương lai; bản đầu chuyển khoản, nhân viên xác nhận, không COD | Thanh toán | D-019, D-048, D-068, D-069 | Ngoại lệ mua khi chưa thanh toán do nhân viên được admin cấp quyền quyết thủ công; thời gian chờ/xác nhận cần đặc tả |
| BR-006 | Phạm vi ra mắt là các quận nội thành TP.HCM | Địa chỉ giao hàng | D-007 | Danh sách vùng giao cụ thể TBD |
| BR-007 | Web cung cấp khung giao cho khách chọn, không giới hạn số đơn mỗi khung | Giao hàng | D-016, D-028 | TPX tự sắp xếp việc giao; khung cụ thể và thao tác cấu hình đặc tả ở PRD |
| BR-008 | Bên thu mua đặt giá bán trước; giá đơn đã đặt không đổi theo giá chợ | Giá bán | D-017 | Không đồng nghĩa đã chốt cách tính tiền khi trọng lượng thực tế khác |
| BR-009 | TPX tạo trước thông tin/quy cách khối lượng theo loại sản phẩm trên web; khách chọn các lựa chọn đã công bố | Sản phẩm | D-018, D-027 | Chưa có yêu cầu tự động cân lại và thu/hoàn chênh lệch; chi tiết từng quy cách đặc tả ở PRD |
| BR-010 | Phí giao và đơn tối thiểu cấu hình trong admin | Checkout và admin | D-021 | Giá trị và cách áp dụng thay đổi đối với đơn đã đặt TBD |
| BR-011 | Khách được hủy trước giờ chốt mua của đợt tương ứng đơn; sau mốc này không được hủy | Hủy đơn | D-024, D-067, D-080 | Áp dụng cả đơn tương lai; trước 22:00 ngày trước giao được hủy, từ mốc này khóa hủy; hoàn theo thỏa thuận |
| BR-012 | Ngoại lệ mua/loại đơn chưa thanh toán do người có quyền quyết thủ công; bản đầu admin toàn quyền thực hiện | Duyệt mua và RBAC | D-026, D-068, D-069, D-074 | Khách vẫn trả khi đặt; duyệt mua không thay trạng thái thu tiền |
| BR-013 | Khách cá nhân và nhà hàng/quán ăn dùng chung flow hiện tại | Mua hàng | D-029 | Chưa yêu cầu luồng B2B riêng hoặc giá sỉ riêng |
| BR-014 | Khách bản đầu Google/Facebook/Apple; phone + OTP bổ sung khi dịch vụ sẵn sàng | Auth khách | D-030, D-087/088 | Firebase Auth đã duyệt TD-025; SĐT liên hệ checkout chưa cần OTP D-089 |
| BR-015 | Một số account admin cố định user tạo, tài khoản/mật khẩu không OTP; giữ RBAC | Quản trị | D-031, D-074, D-086 | Thay số lượng một admin; không OTP/TOTP; quyền không vượt nghiệp vụ |
| BR-016 | Thông báo qua Zalo và push trên app | Thông báo | D-032 | Sự kiện, nội dung, phương thức tích hợp và xử lý lỗi chưa chốt |
| BR-017 | Quản lý số dư để nhận hoàn tiền và dùng cho đơn sau | Hoàn tiền và thanh toán | D-033, D-035–D-039 | Không tự nạp; được yêu cầu hoàn ngân hàng; tự ưu tiên dùng số dư; không hết hạn; admin được cộng khi điều chỉnh đơn |
| BR-018 | Khách không tự nạp tiền vào số dư | Số dư | D-035 | Không có luồng khách tự nạp |
| BR-019 | Khách yêu cầu rút tiền hoàn; số tiền yêu cầu chuyển pending, admin quản lý/duyệt/chuyển ngân hàng | Rút hoàn | D-036, D-071, D-074, D-076, D-078 | Chỉ tiền hoàn, không điểm; pending không dùng thanh toán; lifecycle và thời gian xử lý cần đặc tả |
| BR-020 | Thứ tự: số dư tiền hoàn -> điểm trong giới hạn nếu khách chọn dùng -> thanh toán thực phần còn lại | Checkout | D-037, D-048, D-070 | Phần thực trả là chuyển khoản ở bản đầu; chỉ available được dùng; cơ sở trần theo D-081; thời điểm giữ/trừ cần đặc tả |
| BR-021 | Số dư không hết hạn | Số dư | D-038 | Không tự hết hạn số dư |
| BR-022 | Admin được thêm số dư khi điều chỉnh đơn hàng | Admin, RBAC và số dư | D-039 | Quyền cộng số dư gắn điều chỉnh đơn; chưa chốt quyền trừ thủ công hoặc cộng ngoài điều chỉnh đơn |
| BR-023 | Tích 1 điểm/1.000đ giá trị thanh toán sau cùng khi đơn hoàn thành; dùng 1 điểm giảm 1.000đ trong hạn mức; tạm không hết hạn | Loyalty | D-040, D-041, D-044, D-046, D-047, D-075, D-082 | Cơ sở tích là tiền hàng sau giảm giá, trừ phần trả bằng điểm; phần trả số dư vẫn tích; loại phí giao và làm tròn xuống mỗi 1.000đ |
| BR-024 | Admin cấu hình đồng thời trần phần trăm và trần tiền đổi điểm trên đơn, áp dụng mức thấp hơn | Loyalty settings | D-042, D-045, D-081 | Cơ sở % là tiền hàng sau giảm giá, không phí giao, trước trừ số dư; ví dụ 10% và 100.000đ không phải mặc định |
| BR-025 | Khách chọn dùng điểm sau số dư tiền hoàn, 1 điểm = 1.000đ, trong trần admin set | Checkout | D-043, D-070, D-075, D-077 | Ví dụ đơn 1.000.000đ, trần 5% thì tối đa 50 điểm; tỷ lệ/trần ví dụ không thay giá trị settings |
| BR-026 | Giao không thành công do vận hành trao đổi với khách rồi quyết định | Giao hàng | D-050 | Không tự áp số lần giao lại, phí phát sinh hoặc tự động hủy |
| BR-027 | Nguyên liệu thô từ catalog; món sơ chế chọn món/khẩu phần giá sẵn; dùng chung giỏ, đơn và lần giao | Catalog/mua hàng | D-052, D-058–D-061 | TPX định nghĩa quy cách/khẩu phần; không có nhập yêu cầu tự do hoặc sửa từng nguyên liệu |
| BR-028 | Thông tin sản phẩm và vận hành minh bạch; đánh giá từ khách đã mua | Nội dung/đánh giá | D-053 | Quyền đánh giá và nội dung cụ thể cần đặc tả |
| BR-029 | Thưởng referral bằng điểm loyalty sau đơn đầu hoàn thành của khách mới; mức điểm do admin set | Referral | D-054, D-073 | Phân bổ cho từng bên, điều kiện và thời điểm áp ưu đãi khách mới cần đặc tả; không tự đặt số điểm |
| BR-030 | Mua lại đơn, danh sách món thường mua; nhắc đặt qua kênh khách đồng ý nhận | Mua thường xuyên | D-055 | Lịch/kênh nhắc đặc tả sau; không gửi tin trong giai đoạn trao đổi |
| BR-031 | Sơ chế là làm sạch, cắt/chia sẵn; gói chỉ có nguyên liệu chính, không có gia vị/nước sốt ở bản đầu | Món sơ chế | D-062, D-063 | Thông tin món/gói phải thể hiện rõ thành phần được cung cấp |
| BR-032 | Món có hướng dẫn nấu | Nội dung món | D-064 | User đang tìm nguồn dữ liệu; chưa chốt website/cơ chế nhập và chưa thực hiện crawl |
| BR-033 | Thực đơn cố định; món liên kết nguyên liệu và tự tắt bán khi nguyên liệu bị tắt | Catalog | D-065, D-072 | Bật lại món và xử lý đơn đã đặt cần đặc tả; không tự hủy đơn đã có |
| BR-034 | Cho đặt trước tối đa 7 ngày; khi đến ngày mua không có nguyên liệu thì hoàn tiền | Đơn tương lai | D-066, D-049, D-079 | Hoàn theo thỏa thuận hiện hành; chưa tự quy định hoàn cả đơn hay từng dòng; giữ giá đơn đã đặt theo BR-008 |
| BR-035 | Số dư có available, held_order và pending_withdrawal; chỉ available được đặt/rút | Số dư/checkout | D-078/099 | Place chuyển available→held_order, complete capture giảm tổng, cancel release; pending rút tách riêng |
| BR-036 | Hoàn phần trả bằng điểm bằng điểm, không đổi thành tiền; phần số dư/chuyển khoản hoàn theo thỏa thuận | Hủy/hoàn đơn | D-083/084 | Theo dõi riêng từng nguồn thanh toán; phân bổ hoàn một phần cần đặc tả |
| BR-037 | Hoàn sau complete được phép, không thu hồi điểm ORDER_EARN đã thưởng | Loyalty/refund | D-100 thay D-085 | Không debt/offset; return điểm thanh toán là nguồn khác, không thay earned points đã cấp |

## Số dư tiền hoàn và điểm loyalty

- Số dư tiền hoàn: khách không tự nạp, được yêu cầu rút hoàn ngân hàng, ưu tiên tự dùng và không hết hạn theo D-033, D-035–D-039.
- Loyalty: tích trên giá trị thanh toán sau cùng khi đơn hoàn thành; khách chọn dùng; giới hạn phần trăm và trần tiền do admin set; bản đầu chưa làm hết hạn theo D-040–D-047.
- Thứ tự: tiền hoàn -> điểm (khách chọn, trong hạn mức) -> chuyển khoản phần còn lại. Tiền hoàn được yêu cầu rút ngân hàng; điểm không được rút. Giá trị dùng là 1 điểm = 1.000đ; hoàn phần điểm bằng điểm, phần tiền theo thỏa thuận và giữ nguyên ORDER_EARN đã thưởng (D-100 thay D-085).

Câu chuyện nông trại và đối soát chuyển khoản tự động để sau theo D-013/D-019. Toàn bộ COD hoãn khỏi giai đoạn đầu theo D-048.


## Review ngày2026-10-25 — nguồn mới nhất D-093–098

- Điểm HOLD ngay khi tạo đơn thành công, không sử dụng tiếp. Complete CAPTURE chính thức, cancel RELEASE; chưa tự áp cơ chế này cho số dư cash (OQ-048).
- TPX không thực hiện được: admin hủy đơn, hoàn tiền, mở held points; customer cutoff vẫn22h, admin cancellation có actor/reason riêng.
- Admin quyết định giao khi còn thiếu thanh toán, số phải thu không bị xóa; complete-unpaid còn OQ-050. Không tự thêm COD hoặc PAID giả.
- Admin có chức năng update đơn/thay đổi; nghĩa vụ chênh lệch chi tiết còn OQ-042.
- Giao phần hàng đã thống nhất không bị chặn chỉ do khoản hoàn đang pending.
- D-098 không đồng ý tiền đề case6; OQ-049 cần làm rõ hoàn sau complete/earn đã tiêu. Không coi debt_points đã được duyệt, chưa tự bỏ BR-037/D-085.

Nguồn làm rõ mới nhất D-099/100: cả cash/points hold; cho hoàn sau complete và không clawback ORDER_EARN. Những ghi chú OQ-048/049 ở lịch sử vòng hỏi trước đã được đóng; xem review vòng1 mới nhất.
