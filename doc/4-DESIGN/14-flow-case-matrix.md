# Ma trận case cần thiết kế — TPX

> v0.4 — 2026-10-25. 100 case để review thiết kế, **chưa chạy test sản phẩm**. Đây là yêu cầu scenario bổ sung trong21 feature hiện có, không phải100 feature mới hoặc100 layout độc lập. P-xxx cần review; “PRD” dẫn lại nghĩa vụ trong PRD hiện hành, gồm các chi tiết [P] đã ghi ở nguồn.

Đọc cùng [journeys](13-detailed-journeys.md) và [action gaps](15-action-contract-gaps.md). Với mỗi case cần ghi actual frame/prototype, actor, screen/surface, start state, thao tác, result, recovery và trạng thái Delivered/Needs-fix/Missing. Hiện toàn bộ là **Expected**. Case chỉ có admin thì APP_IOS/APP_ANDROID là N/A; case khách có đủ web/app; flow xuyên vai trò có bằng chứng ở cả hai phía, không cho khách truy cập màn admin.

## J-001 — Duyệt chưa đăng nhập → đăng nhập → giữ giỏ

Màn dùng làm nơi thể hiện: S-001, S-002, S-004, S-005, S-006, S-008, S-009, S-032, S-010.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-001 | Khách/hệ thống · S-008, S-009, S-032 | Khách mới không có giỏ server | Thêm 2 loại hàng khi guest rồi đăng nhập | Khôi phục đúng variant/qty; thông báo giỏ đã lưu; không thêm bản sao khi callback lặp. | P-013 · Expected |
| FC-002 | Khách/hệ thống · S-008 | Guest và tài khoản đều có giỏ | Hai giỏ có cùng variant hoặc khác qty | So sánh và xác nhận quy tắc gộp/thay; không xóa giỏ server hoặc tự cộng qty âm thầm. | P-013 · Expected |
| FC-003 | Khách/hệ thống · S-009, S-008 | Đóng provider hoặc chặn popup | Đang checkout rồi hủy đăng nhập | Trở lại giỏ với lựa chọn còn nguyên và CTA thử lại; không mất form hoặc hiện đặt thành công. | PRD · Expected |
| FC-004 | Khách/hệ thống · S-010, S-008 | Đăng xuất rồi người khác đăng nhập | Thiết bị dùng chung, user A có giỏ riêng | Không đưa giỏ/đơn/ví của A sang B; việc giữ guest cart sau logout phải theo P-013, không tự merge dữ liệu riêng. | P-013 · Expected |

## J-002 — Khởi động app, phiên đăng nhập và liên kết identity

Màn dùng làm nơi thể hiện: S-009, S-010, S-011, S-032.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-005 | Khách/hệ thống · S-032, S-009 | App bị đóng giữa callback | Mở lại app sau OAuth redirect | Có loading/recover route; chỉ tạo một phiên/user phù hợp; nếu callback không khôi phục được, quay lại login an toàn. | PRD · Expected |
| FC-006 | Khách/hệ thống · S-009, S-032 | Phiên hết hạn ở trang riêng | Push hoặc reload chi tiết đơn khi session expired | Đăng nhập rồi kiểm tra ownership lại; giữ destination an toàn, không chớp nội dung tài khoản cũ. | P-011 · Expected |
| FC-007 | Khách/hệ thống · S-011 | Provider thuộc user khác | Link Apple/Google đã được dùng ở tài khoản khác | Báo conflict và lối liên hệ hỗ trợ; không merge tiền/điểm. Gỡ phương thức cuối bị chặn. | P-011 · Expected |
| FC-008 | Khách/hệ thống · S-010, S-009 | Đăng xuất mọi thiết bị/khóa account | Máy khác đang giữ màn checkout | Máy khác nhận lỗi phiên/refresh, về login với giải thích; chưa tạo đơn thì không giữ tiền; không tự gửi lại POST sau login. | P-011 · Expected |

## J-003 — Địa chỉ, người nhận và thay vùng giao

Màn dùng làm nơi thể hiện: S-012, S-013, S-014, S-015, S-019, S-059.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-009 | Khách/hệ thống · S-013, S-014 | Ngoài vùng hoặc chưa có slot | Chọn địa chỉ không phục vụ | Nêu vùng chưa hỗ trợ, giữ giỏ, cho đổi địa chỉ; không tự chọn quận/slot thay khách. Ngày nghỉ/tạm dừng phục vụ phải theo cấu hình ngày hợp lệ, không mặc định mở đủ7ngày; chưa có lịch thì ghi gap AG-014/P-009. | P-009 · Expected |
| FC-010 | Khách/hệ thống · S-012, S-013, S-019 | Xóa địa chỉ mặc định | Địa chỉ đó đang có đơn đặt trước | Bỏ địa chỉ lưu nhưng không xóa snapshot đơn; checkout đang mở phải revalidate trước submit. | P-009 · Expected |
| FC-011 | Khách/hệ thống · S-014, S-015 | Đổi vùng làm thay phí | Đã chọn ngày/slot và tính tiền | Hiển thị phí/tổng mới và slot không còn hợp lệ; cần xác nhận quote mới; không giữ tổng cũ. | P-009 · Expected |
| FC-012 | Khách + admin/hệ thống · S-019, S-059 | Sửa người nhận sau đặt | Khách sửa SĐT trong hồ sơ | Đơn vẫn dùng thông tin đã chốt; có lối liên hệ TPX theo mã đơn để xin sửa, không hứa thay tự động. | P-015 P-018 · Expected |

## J-004 — Chọn RAW/MEAL, quy cách và nội dung món

Màn dùng làm nơi thể hiện: S-001, S-002, S-003, S-004, S-005, S-006, S-007, S-008.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-013 | Khách/hệ thống · S-003, S-004, S-006, S-008 | Không có kết quả/variant biến mất | Search hoặc mở link sản phẩm đã archive | Phân biệt không tìm thấy với lỗi mạng; quay lại danh mục; giỏ cũ hiển thị dòng cần xử lý, không crash. | PRD · Expected |
| FC-014 | Khách/hệ thống · S-004, S-006 | Thiếu lựa chọn khẩu phần/qty sai step | Bấm thêm giỏ khi form chưa hợp lệ | Nêu lỗi tại selector/qty, giữ focus và giá tương ứng; không làm tròn qty âm thầm. | PRD · Expected |
| FC-015 | Khách/hệ thống · S-006, S-008 | Ingredient vừa bị tắt | MEAL đang hiển thị còn bán nhưng server đã tắt | Chặn add/checkout mới; chỉ rõ món tạm ngừng; đơn đã trả không tự hủy. | PRD · Expected |
| FC-016 | Khách/hệ thống · S-006, S-007 | Gia vị/hướng dẫn dài/ảnh thiếu | Mở món và hướng dẫn trên màn nhỏ | Nhãn nguyên liệu cung cấp và tự chuẩn bị rõ; placeholder ảnh; Back giữ khẩu phần; không thêm customization/gia vị vào giỏ. | PRD · Expected |

## J-005 — Giỏ hàng, sửa số lượng và đồng bộ nhiều thiết bị

Màn dùng làm nơi thể hiện: S-008, S-014.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-017 | Khách/hệ thống · S-008 | Qty chạm 0/xóa dòng cuối | Khách giảm số gói cuối cùng | Xóa có phản hồi rõ; empty state dẫn về catalog; không mở checkout với giỏ rỗng. | PRD · Expected |
| FC-018 | Khách/hệ thống · S-008 | Thêm nhanh nhiều lần khi mạng chậm | Hai lần chạm +/- trước phản hồi | Cho thấy đang cập nhật và qty đã xác nhận; không hiện tổng chắc chắn khi request chưa commit. | P-013 · Expected |
| FC-019 | Khách/hệ thống · S-008, S-014 | Hai thiết bị sửa cùng giỏ | Máy B sửa khi máy A đang checkout | 409/diff → lấy giỏ mới, vô hiệu quote cũ; khách xác nhận lại, không last-write mất dòng mà không báo. | P-013 · Expected |
| FC-020 | Khách/hệ thống · S-008, S-014 | Đã đặt xong nhưng giỏ đổi đồng thời | Máy khác thêm hàng trong lúc đặt | Không xóa hàng chưa thuộc order; refresh giỏ có giải thích; Back vào checkout cũ không đặt lại order. | P-013 · Expected |

## J-006 — Ngày giao, 22h và đơn đặt xa

Màn dùng làm nơi thể hiện: S-014, S-015, S-019, S-020, S-044, S-045.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-021 | Khách/hệ thống · S-014, S-015 | 21:59:59 → 22:00:00 | Chọn giao ngày mai rồi xác nhận đúng 22h | Chặn ngày không hợp lệ, thông báo mốc đã qua và yêu cầu chọn lại; không tự đặt ngày kia. | PRD · Expected |
| FC-022 | Khách + admin/hệ thống · S-019, S-020, S-045 | Giao xa và hủy sớm | Đặt 21/10 giao 26/10; hủy tối 21/10 | Vẫn được hủy trước 22h 25/10; không khóa vào tối đặt hoặc cho vào batch ngày 22/10. | PRD · Expected |
| FC-023 | Khách/hệ thống · S-015, S-014 | Máy để timezone khác/qua nửa đêm | Mở lịch ở múi giờ khác HCM hoặc app trở lại ngày mới | Hiển thị lịch HCM và lấy lại min/max từ server; lịch cũ không dùng để commit. | PRD · Expected |
| FC-024 | Khách/hệ thống · S-014, S-015 | Chọn hai ngày trong một giỏ | Khách muốn RAW ngày mai, MEAL ngày khác | Giải thích một đơn một ngày/slot; muốn ngày khác cần các lần đặt riêng và báo giá riêng, không tự tách/thu tiền nhiều đơn. | P-015 · Expected |

## J-007 — Checkout tiền/điểm, quote và kết quả chưa rõ

Màn dùng làm nơi thể hiện: S-008, S-014, S-015, S-016, S-017, S-019, S-022, S-025.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-025 | Khách/hệ thống · S-014, S-017 | Available đủ cả hàng/phí | Ví trả hết đơn và points đang bật | Bank due 0, points không bị tiêu thêm theo P-005; CTA đặt đơn không dẫn hướng dẫn chuyển 0đ. | P-001 P-005 · Expected |
| FC-026 | Khách/hệ thống · S-014 | Có pending và caps không tròn nghìn | Ví tổng 200k, pending 150k; caps ra 12.500đ | Chỉ dùng available 50k; tối đa 12 điểm nếu các giới hạn khác cho phép; nêu lý do giới hạn/điểm không đủ. | P-005 · Expected |
| FC-027 | Khách/hệ thống · S-008, S-014 | Nhỏ hơn đơn tối thiểu sau thay giỏ | Bỏ một dòng làm G thấp hơn minimum | Hiển thị còn thiếu bao nhiêu theo cơ sở P-009; không tính pending/điểm như hàng hoặc thêm phí giả. | P-009 · Expected |
| FC-028 | Khách/hệ thống · S-014, S-017, S-019 | Submit timeout hoặc login hết hạn | Bấm đặt xong mất mạng rồi mở lại | Place reserve cash/points atomically theo D-099; lost response tra operation/order trước retry. Complete mới capture, cancel mở hold; không hold mồ côi hoặc debit hai lần. | P-001 P-011 P-013 · Expected |

## J-008 — Chuyển khoản và quay lại web/app

Màn dùng làm nơi thể hiện: S-016, S-017, S-018, S-019, S-042, S-043, S-050.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-029 | Khách/hệ thống · S-016, S-018, S-019 | Rời app và app bị kill | Chuyển ngân hàng rồi mở lại TPX | Từ lịch sử đơn mở lại số còn thiếu/hướng dẫn; re-fetch trước hiển thị; không tạo đơn mới hay báo PAID vì quay lại. | PRD · Expected |
| FC-030 | Khách + admin/hệ thống · S-016, S-019, S-043 | Chuyển nhiều lần còn thiếu | Nhận 300k rồi 450k cho nghĩa vụ750k | Hiển thị từng receipt và remaining; chỉ đủ nguồn sau confirm đủ 750k, không yêu cầu khách chuyển lại cả 750k. | PRD · Expected |
| FC-031 | Khách + admin/hệ thống · S-016, S-043 | Bank TPX đổi sau lúc đặt | Admin đổi tài khoản nhận tiền khi đơn còn chờ | Đối chiếu hướng dẫn snapshot/cảnh báo tài khoản cũ; không âm thầm đổi reference; ghi nhận tiền đến bank cũ cần quy tắc P-016. | P-016 · Expected |
| FC-032 | Khách + admin/hệ thống · S-019, S-043 | Thông báo xác nhận đến trước refresh | Push đến khi đang ở màn chờ | Refresh cùng order; show confirmed amount/remaining; notice khách không hiển thị như receipt admin. | PRD · Expected |

## J-009 — Theo dõi đơn và hủy trước cutoff

Màn dùng làm nơi thể hiện: S-018, S-019, S-020, S-021, S-022, S-025, S-042, S-050, S-052, S-043.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-033 | Khách/hệ thống · S-020, S-019, S-022, S-025 | Hủy đơn chưa nhận bank | Đã áp balance/points theo P-001 | Cancel RELEASE cả cash/points hold đúng một lần; total ví không tăng giả. Bank chưa nhận không tạo refund; không vừa release cash hold vừa credit refund cùng khoản. | P-001 · Expected |
| FC-034 | Khách + admin/hệ thống · S-019, S-021, S-052 | Hủy đơn đã nhận bank | Trước cutoff, đơn đã funded | CANCELLED mở cả cash/points holds; bank refund thực nhận có thể pending riêng. Chưa complete thì chưa earn, không gọi release hold là RETURN đã capture. | P-003 · Expected |
| FC-035 | Khách/hệ thống · S-020, S-019 | Preview trước 22h, confirm sau 22h | Modal hủy giữ mở qua mốc | Server chặn; đóng/refresh preview với deadline cụ thể; không tự gửi lại hoặc đề nghị đổi giờ máy. | PRD · Expected |
| FC-036 | Khách + admin/hệ thống · S-019, S-043, S-050 | Receipt tới sau hủy | Khách vẫn chuyển theo hướng dẫn cũ | Đơn vẫn hủy; admin thấy receipt muộn và phương án hoàn; không auto đưa vào batch. | P-006 P-016 · Expected |

## J-010 — Thiếu hàng → liên hệ → đổi món/giảm đơn/tăng phải thu

Màn dùng làm nơi thể hiện: S-019, S-021, S-031, S-042, S-045, S-046, S-050, S-052, S-016.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-037 | Khách + admin/hệ thống · S-050, S-019, S-045 | Đổi món cùng giá | Thiếu một dòng, khách đồng ý hàng khác | Show old/new và audit; cập nhật nhu cầu mua/prep, không vừa mua món cũ vừa món mới. | P-015 P-017 · Expected |
| FC-038 | Khách + admin/hệ thống · S-050, S-016, S-019 | Đổi sang món đắt hơn | Chênh tăng 50k sau đã funded | Admin update đã chốt về capability. Dựng OQ-042 A re-quote/hold delta và B bank-only top-up theo03 section12; cùng before/after, customer agreement, cancel/conflict/unknown. Không tự chọn settlement policy. | P-015 · Expected |
| FC-039 | Khách + admin/hệ thống · S-050, S-031 | Khách không trả lời | Thiếu hàng sau cutoff, đang tới giờ giao | Giữ case cần xử lý/nhắc ops; không auto chọn món, auto đồng ý hoặc auto hoàn sau thời gian tự đặt. | P-018 · Expected |
| FC-040 | Khách + admin/hệ thống · S-050, S-019, S-052 | Hết tất cả hàng, khách chọn hoàn | Không có phần nào giao sau 22h | Admin hủy/CANCELLED có reason theo D-094, release cash/points holds, hoàn tiền thật theo agreement; không NOT_FULFILLED hoặc fake COMPLETED để thoát. | P-014 · Expected |

## J-011 — Hoàn hỗn hợp tiền/điểm và đối soát từng phần

Màn dùng làm nơi thể hiện: S-019, S-021, S-022, S-025, S-050, S-051, S-052, S-056.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-041 | Khách + admin/hệ thống · S-052, S-021 | Một phần ví xong, bank đang chờ | Refund có BALANCE + BANK + POINTS | Trước complete release cash/points holds, không duplicate credit. Sau complete hoàn captured sources theo plan, giữ nguyên ORDER_EARN D-100. Bank pending khác settled. | P-003 · Expected |
| FC-042 | Admin/hệ thống · S-052 | Hai admin lập refund cùng đơn | Plan A giữ cap, B preview số cũ | B nhận conflict/remaining mới; không chấp nhận tổng vượt nguồn; reject trước execution mới release cap đúng phần. | P-003 · Expected |
| FC-043 | Khách + admin/hệ thống · S-052, S-021 | Ngân hàng không rõ hoặc đã xác nhận thất bại | Đã claim BANK leg rồi timeout/reject từ bank | Unknown giữ claim, không chuyển lại; known failure mở review/correction theo P-016, không dùng nút settle để thoát. | P-016 · Expected |
| FC-044 | Khách + admin/hệ thống · S-052, S-021, S-025 | Full refund sau partial nhiều lần | Order đã có hai phương án hoàn | Full refund chỉ remaining captured/actual received sources; không vượt cap đang giữ. Giữ nguyên ORDER_EARN đã cấp, không debt/clawback hoặc lặp RETURN. | P-003 P-004 · Expected |

## J-012 — Ví → rút tiền → duyệt/chuyển/reject/cancel

Màn dùng làm nơi thể hiện: S-022, S-023, S-024, S-053, S-054, S-056, S-058, S-014.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-045 | Khách/hệ thống · S-023, S-022, S-014 | Hai yêu cầu rút/checkout cùng lúc | Available200k, hai request150k | Chỉ operation đủ nguồn thành công; operation còn lại nhận số dư mới để review, không âm available. | P-002 · Expected |
| FC-046 | Khách + admin/hệ thống · S-024, S-054 | Khách cancel cạnh tranh admin approve | Màn khách còn PENDING nhưng admin vừa APPROVED | Refresh allowed actions; không release nếu trạng thái không cho cancel; giải thích kết quả thực. | P-002 · Expected |
| FC-047 | Khách + admin/hệ thống · S-023, S-024, S-054 | Bank sai trước hoặc sau processing | Khách muốn sửa số tài khoản | Trước xử lý dùng cancel/recreate nếu được phép; processing khóa sửa và mở đối soát, không đổi nơi nhận sau khi chuyển. | P-002 P-016 · Expected |
| FC-048 | Khách + admin/hệ thống · S-054, S-024 | Đã chuyển nhưng lưu timeout | Admin mark-paid không nhận phản hồi | Tra request/reference trước thao tác tiếp; tuyệt đối không chuyển lần nữa; paid đã có thì chỉ show kết quả đó. | P-002 · Expected |

## J-013 — Loyalty: tích, dùng, hoàn và thu hồi đã tiêu

Màn dùng làm nơi thể hiện: S-014, S-019, S-021, S-025, S-052, S-056.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-049 | Khách/hệ thống · S-014, S-025 | Balance trả hàng vẫn tích | G1m, F20k, balance200k, redeem50 | Bank770k; place HOLD200k cash và50points, complete CAPTURE cả hai một lần và earn950 riêng. Available giảm khi hold, total wallet chỉ giảm khi capture. | PRD · Expected |
| FC-050 | Khách/hệ thống · S-014, S-025 | Không dùng điểm, phí giao cao | G1m, F20k, balance200k, opt-out | Bank 820k, earn 1000 khi complete; fee không earn; toggle không biến thành mặc định bắt buộc. | PRD · Expected |
| FC-051 | Khách + admin/hệ thống · S-025, S-052 | Hoàn sau complete, điểm thưởng đã tiêu | A đã earn950, dùng ở B rồi hoàn A | D-100: cho hoàn sau complete, giữ nguyên ORDER_EARN đã thưởng dù đã dùng ở đơn B. RETURN points dùng trả đơn là phần riêng; không thu hồi950earn, không debt/offset/cash bù. | C D-100 · Expected |
| FC-052 | Khách + admin/hệ thống · S-025, S-056 | Complete/refund worker chạy lại | Cùng sự kiện được retry hoặc thông báo trễ | Complete retry không CAPTURE hold hoặc earn/referral hai lần. Khi earn worker còn chờ, UI hiển thị đang cập nhật thay vì tự cộng; capture không giảm available lần hai. | PRD · Expected |

## J-014 — Referral từ link/mã đến đơn đủ điều kiện

Màn dùng làm nơi thể hiện: S-009, S-010, S-026, S-056, S-059, S-032.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-053 | Khách/hệ thống · S-026, S-009, S-032 | Chưa cài app/chưa login | Mở referral URL trên mobile browser | Có đích web dùng được và mã đọc/copy được; không ép store hoặc làm mất mã qua login; route link phải bổ sung contract. | P-006 P-013 · Expected |
| FC-054 | Khách/hệ thống · S-026 | Mã sai/self/attribution muộn | Claim sau đã có đơn hoặc mã của chính mình | Giải thích điều kiện/reason; không tự chuyển referrer hoặc hard-block chỉ do trùng email/SĐT. | P-006 · Expected |
| FC-055 | Khách + admin/hệ thống · S-026, S-056 | Hai đơn đầu complete gần đồng thời | Cùng referred user có hai completion | Một qualifying order/reward; trạng thái rõ, không dùng mỗi order để thưởng lại. | P-006 · Expected |
| FC-056 | Khách + admin/hệ thống · S-026, S-059, S-056 | Chưa cấu hình reward hoặc hoàn một phần | Settings reward thiếu hoặc qualifying order partial refund | Không hiện số thưởng bịa; reward program chưa ready không ảnh hưởng mua hàng; partial reversal để review, không tự áp tỷ lệ. | P-006 · Expected |

## J-015 — Mua lại và thường mua → giỏ mới

Màn dùng làm nơi thể hiện: S-018, S-019, S-027, S-004, S-006, S-008, S-014.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-057 | Khách/hệ thống · S-018, S-019, S-008 | Tất cả dòng cũ hết bán | Mua lại order có các variant đã archive | Không tạo giỏ rỗng dẫn thanh toán; giải thích và dẫn catalog; không tự substitute. | PRD · Expected |
| FC-058 | Khách/hệ thống · S-019, S-008 | Một dòng đổi pack/giá | Variant cũ khác quy cách hoặc đã có variant mới | Show old vs current, không coi ID mới là lựa chọn khách đã đồng ý; chỉ thêm dòng hợp lệ được chọn. | P-010 · Expected |
| FC-059 | Khách/hệ thống · S-008 | Chọn replace khi giỏ có dữ liệu | Khách Back/cancel modal xác nhận | Giữ nguyên giỏ hiện tại; confirm mới replace; thao tác lặp không nhân đôi. | P-010 · Expected |
| FC-060 | Khách/hệ thống · S-027 | Khách mới/ẩn món thường mua | Chưa có completed hoặc hide toàn bộ | Empty state có catalog và lối quản lý hidden/pinned [P]; không dùng lịch sử user trước trên thiết bị. | P-010 · Expected |

## J-016 — Đánh giá của tôi và kiểm duyệt

Màn dùng làm nơi thể hiện: S-004, S-006, S-019, S-028, S-062.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-061 | Khách/hệ thống · S-028, S-019 | Đã gửi rồi mở lại | Mở review cùng order_item | Hiện review/status thay vì form gửi mới; nếu API hiện chưa trả my-review/status thì ghi contract gap. | P-010 · Expected |
| FC-062 | Khách/hệ thống · S-019, S-028 | Một order có nhiều dòng giống sản phẩm | Hai order_item cùng sản phẩm hoặc mua nhiều lần | Chọn đúng dòng eligible, không nhầm review thuộc order khác; chống trùng theo item proposal. | P-010 · Expected |
| FC-063 | Khách + admin/hệ thống · S-062, S-028, S-004 | Ẩn sau khi đã public | Admin hide review có reason | Public average cập nhật; khách không thấy review biến mất vô cớ trong lịch sử của mình; không tự sửa sao. | P-010 · Expected |
| FC-064 | Khách + admin/hệ thống · S-028, S-062, S-019 | Hoàn hàng sau complete | Item hoàn/không giao nhưng order terminal | Giữ lịch sử purchase thật; eligibility/review tồn tại sau refund phải được review, không invent tự xóa hoặc vẫn verified theo cờ client. | P-010 P-018 · Expected |

## J-017 — Thông báo, quyền OS, consent và deep link

Màn dùng làm nơi thể hiện: S-009, S-019, S-021, S-024, S-029, S-030, S-032, S-060.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-065 | Khách/hệ thống · S-030 | OS denied rồi bật lại trong Settings | Bật reminder nhưng OS từ chối push | Show consent và trạng thái permission riêng; nút mở OS settings có fallback; trở lại refresh, không lặp prompt vô hạn. | PRD · Expected |
| FC-066 | Khách/hệ thống · S-029, S-032, S-019 | Deep link user khác/resource đã xóa | Push cũ sau account switch hoặc private ID | Đăng nhập/ownership guard; không lộ số dư/địa chỉ; quay notifications/list an toàn khi không truy cập được. | PRD · Expected |
| FC-067 | Khách + admin/hệ thống · S-030, S-060 | Unsubscribe sau enqueue/job trễ | Tắt nhận nhắc trước lúc worker gửi hoặc worker chạy sau 22h | SKIPPED có reason, không retry ép gửi; transactional notification không bị hiểu nhầm là reminder marketing. | PRD · Expected |
| FC-068 | Admin/hệ thống · S-060 | Provider nhận nhưng timeout | Admin thấy notification unknown rồi chọn retry | Show risk/attempt hiện tại, dedupe logic và reason; không giả đúng một lần ngoài mạng hoặc đổi order state. | PRD · Expected |

## J-018 — Admin: login, quyền, mất phiên và tài khoản cố định

Màn dùng làm nơi thể hiện: S-033, S-034, S-057, S-058.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-069 | Admin/hệ thống · S-033, S-034 | Không có dashboard.read | Account chỉ có procurement.manage | Landing hợp lệ vào thu mua; không loop login/403 và không show dashboard dữ liệu ngoài quyền. | PRD · Expected |
| FC-070 | Admin/hệ thống · S-057, S-058 | Thu hồi quyền khi đang mở dialog | Admin khác bỏ payments.confirm | Submit bị chặn, giữ context an toàn và thông báo quyền đổi; không replay khi refresh quyền. | PRD · Expected |
| FC-071 | Admin/hệ thống · S-057, S-058 | Tự disable/role cuối full access | Thay role của tài khoản quản trị cuối | Impact preview/guard proposal; không cho tự lockout nếu P-019 được duyệt; chưa coi một shared admin là giải pháp. | P-019 · Expected |
| FC-072 | Admin/hệ thống · S-033, S-057 | Quên password/cần account mới | Fixed account không đăng nhập được | Hiện hướng dẫn liên hệ người quản trị đã cấu hình; provision/reset qua runbook có audit proposal; không tự mở signup/email OTP. | P-019 · Expected |

## J-019 — Admin catalog, ảnh, BOM và tác động đơn tương lai

Màn dùng làm nơi thể hiện: S-035, S-036, S-037, S-038, S-039, S-040, S-045, S-050, S-061.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-073 | Admin/hệ thống · S-036, S-039, S-040 | Thiếu mapping/unit/ảnh upload lỗi | Publish meal có BOM sai đơn vị hoặc asset chưa finalize | Show field errors và link sửa; giữ draft; không publish ảnh giả thành ready hay tính kg như g. | PRD · Expected |
| FC-074 | Admin/hệ thống · S-037, S-045, S-050 | Tắt ingredient dùng chung RAW/MEAL | Nhiều món và đơn giao 5 ngày nữa bị ảnh hưởng | Impact list phân biệt new-sales blocked và existing-order needs-contact; link batch/cases; không tự hoàn/hủy tất cả. | P-007 P-017 · Expected |
| FC-075 | Admin/hệ thống · S-035, S-036 | Archive category còn product active | Sửa/xóa danh mục hoặc variant từng có đơn | Chặn/giải thích dependencies, giữ history; không xóa physical; product cũ public 404 vẫn có order snapshot đọc được. | PRD · Expected |
| FC-076 | Admin/hệ thống · S-039, S-036 | Hai admin sửa BOM/giá | Admin B publish version khi A đang dirty | Show conflict/diff, không overwrite âm thầm; báo đơn/quotes nào chịu version mới, không đổi đơn đã đặt. | P-007 P-009 · Expected |

## J-020 — Settings readiness, hiệu lực và thay cấu hình

Màn dùng làm nơi thể hiện: S-059, S-014, S-015, S-016, S-034, S-042, S-063.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-077 | Khách + admin/hệ thống · S-059, S-014 | Loyalty cap bằng0/không đủ điểm | Settings hợp lệ nhưng redeem không khả dụng | UI giải thích points không dùng được, vẫn thanh toán bằng nguồn khác; missing config khác giá trị0 đã cấu hình. | P-005 P-009 · Expected |
| FC-078 | Admin/hệ thống · S-059, S-042 | Đóng vùng hoặc slot đang có đơn | Publish vùng/slot inactive | Đơn cũ vào impact/case list, vẫn xem địa chỉ/lịch cũ; không xóa slot hoặc tự dời lịch. | P-009 P-018 · Expected |
| FC-079 | Khách + admin/hệ thống · S-059, S-016, S-042 | Thay bank active | Có khách đang chuyển theo bank snapshot cũ | Preview affected orders và policy handling; không đánh dấu chưa thu chỉ vì bank cũ inactive; xử lý theo P-016. | P-016 · Expected |
| FC-080 | Khách + admin/hệ thống · S-059, S-014 | Cấu hình thiếu hoặc version conflict | Thiếu bank/caps bắt buộc hoặc admin khác publish | Validation chỉ rõ trường; không apply nửa cấu hình; checkout hiển thị tạm chưa đặt được và giữ giỏ. | PRD · Expected |

## J-021 — Cutoff → batch → quyết unpaid → loại/mua

Màn dùng làm nơi thể hiện: S-034, S-041, S-042, S-044, S-045, S-046, S-050.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-081 | Admin/hệ thống · S-044, S-045 | Batch rỗng/job restart/chạy muộn | Không có order hoặc scheduler chạy sau 22h | Empty có thời điểm/cơ sở ngày; retry không nhân nhu cầu; khóa hủy theo server vẫn đúng 22h. | PRD · Expected |
| FC-082 | Admin/hệ thống · S-045, S-042 | Chưa quyết unpaid | Admin chưa duyệt mua cho một đơn thiếu bank | Hiển thị exception queue và không đưa vào total mua; không tự approve hoặc auto timeout cancel. | PRD · Expected |
| FC-083 | Admin/hệ thống · S-045, S-042, S-050 | Loại đơn đã dùng balance/points | Partial-funded order bị EXCLUDED | EXCLUDED cần admin quyết CANCELLED: release cash/points hold, bank refund theo thực nhận/thỏa thuận. Không giữ nguồn nội bộ vô hạn hoặc giả đã trả bank. | P-014 · Expected |
| FC-084 | Admin/hệ thống · S-045, S-046 | Rebuild sau thay quyết định/tiền muộn | Đã export mua rồi có revision | Show delta và preserve decision; đã bắt đầu mua thì cần revision/reason, không âm thầm rebuild overwrite kế hoạch. | P-006 P-017 · Expected |

## J-022 — Mua/nhận thực tế → phân bổ shortage → nhu cầu sửa

Màn dùng làm nơi thể hiện: S-039, S-042, S-045, S-046, S-047, S-050.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-085 | Admin/hệ thống · S-046, S-045 | Nhận nhiều lần cùng ingredient | Cần 10kg, lần đầu 6kg, lần sau 4kg | UI phân biệt lần nhập và cumulative 10kg; retry receipt không thêm 4kg lần nữa; không làm total 20kg. | P-017 · Expected |
| FC-086 | Admin/hệ thống · S-046, S-050, S-042 | Thiếu ingredient dùng cả RAW/MEAL | Cần 10kg, chỉ 8kg đạt, nhiều order cùng phụ thuộc | Ops xem impacted sources và quyết phân bổ 8kg; tạo shortages đúng 2kg theo order, không tự ưu tiên khách hoặc cắt đều mọi đơn. | P-017 · Expected |
| FC-087 | Admin/hệ thống · S-046, S-050 | Pack thực cân lệch/không đạt | 500g công bố nhưng phần nhận không đáp ứng | Mở quality/agreement cho phần bị ảnh hưởng; không auto thu cân chênh hoặc mặc định vẫn đạt để tick pack. | PRD · Expected |
| FC-088 | Admin/hệ thống · S-045, S-046, S-047 | Đổi món sau khi đã gom mua | Case đồng ý ingredient mới khi đã có kế hoạch cũ | Giữ demand gốc và delta/revision; không cộng cả cũ+lẫn mới làm nhu cầu hiện tại; cost thiếu có label. | P-015 P-017 · Expected |

## J-023 — Sơ chế/đóng gói → giao thành công/thất bại → kết thúc

Màn dùng làm nơi thể hiện: S-019, S-042, S-047, S-048, S-049, S-050, S-025.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-089 | Admin/hệ thống · S-047, S-049, S-042 | Thiếu tiền: admin dispatch và complete branches | Đã duyệt mua unpaid nhưng muốn dispatch | Admin quyết dispatch D-095, remaining due/audit giữ riêng. OQ-050 A đợi funded mới complete và B explicit complete-unpaid cần frames theo03 section12; không PAID giả/COD. Refund pending không tự block hàng đã thống nhất. | P-008 · Expected |
| FC-090 | Khách + admin/hệ thống · S-049, S-050, S-019 | Khách không nghe máy/giao lỗi | Order OUT_FOR_DELIVERY không giao được | Ghi reason/time và case; không autocharge retry, không auto refund; liên hệ và ghi quyết định P-018. | PRD · Expected |
| FC-091 | Khách + admin/hệ thống · S-049, S-050, S-019 | Giao lại hoặc không thể giao nữa | Khách đồng ý retry hoặc hủy thực hiện sau fail | Giao lại theo agreement giữ lịch sử fail; nếu admin quyết không giao nữa thì CANCELLED và RELEASE held points, hoàn tiền theo thỏa thuận D-094; không fake complete. | P-014 P-018 · Expected |
| FC-092 | Khách + admin/hệ thống · S-049, S-025, S-050 | Complete lặp hoặc phát hiện giao sai sau complete | Đã earn rồi có complaint mới | Complete retry không capture/earn lại. Complaint sau complete được xử lý refund theo agreement; giữ earned points, không mở lại status hoặc thưởng lần nữa. | PRD · Expected |

## J-024 — Đối soát, xác nhận nhầm và báo cáo tiền thật

Màn dùng làm nơi thể hiện: S-034, S-042, S-043, S-051, S-052, S-053, S-054, S-056, S-058, S-063, S-050.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-093 | Admin/hệ thống · S-043, S-042, S-058 | Receipt ghi nhầm đơn/nhập sai amount | Admin đã confirm vào order A nhưng thuộc B | Không xóa/edit receipt trực tiếp; correction có quyền/reason và guard khi A đã giao/hoàn; contract hiện thiếu, giữ P-016. | P-016 · Expected |
| FC-094 | Admin/hệ thống · S-043, S-050 | Có tiền nhưng không xác định order | Bank reference không nhận diện được đơn | Unmatched queue có lối ghi nhận/tra/allocate; không buộc gán đại order để nhập receipt; API hiện cần bổ sung. | P-016 · Expected |
| FC-095 | Admin/hệ thống · S-063, S-056 | Report thấy200k wallet pending 150k | Muốn xem tiền thực đã hoàn/rút trong ngày | Liability200k đến khi payout paid; pending 150k không tính chi thực; GMV/cash-in/refunds/withdrawals không cộng lẫn. | PRD · Expected |
| FC-096 | Admin/hệ thống · S-063, S-058 | Export stale/thiếu giá vốn/không đủ quyền | Filter đổi hoặc chỉ được xem summary | Timestamp/basis/filter/cost coverage rõ; không xuất PII ngoài quyền hoặc gọi gross margin đã chính xác khi cost thiếu. | PRD · Expected |

## J-025 — Hỗ trợ, agreement evidence và xóa tài khoản còn nghĩa vụ

Màn dùng làm nơi thể hiện: S-010, S-011, S-019, S-021, S-022, S-024, S-031, S-050, S-052, S-054, S-055, S-056, S-058.

| Case | Actor / màn trọng tâm | Tình huống | Điểm bắt đầu / thao tác | UI và recovery phải có | Policy / trạng thái |
| --- | --- | --- | --- | --- | --- |
| FC-097 | Khách + admin/hệ thống · S-019, S-031, S-050 | Complaint sau completed | Khách báo hàng kém chất lượng/giao nhầm | Complaint sau complete từ đúng order→ops case→refund theo agreement, giữ ORDER_EARN D-100; không mở lại completion để tích điểm thêm. | P-018 · Expected |
| FC-098 | Khách/hệ thống · S-031, S-019 | Chưa có kênh contact hoặc Zalo không mở | Bấm hỗ trợ trên desktop/app không có Zalo | Hiện phone/copy/contact web có cấu hình thực; không dead CTA, không bịa hotline hoặc mặc định mở ticket hệ thống chưa có. | P-018 · Expected |
| FC-099 | Khách + admin/hệ thống · S-010, S-022, S-024, S-056 | Yêu cầu xóa khi còn tiền/rút processing | Available50k/pending 150k hoặc có đơn tương lai | Show nghĩa vụ cần giải quyết và trạng thái request P-019; không xóa ví, tự rút, tự hủy đơn hoặc bỏ quyền theo dõi payout. | P-011 P-019 · Expected |
| FC-100 | Khách + admin/hệ thống · S-010, S-011, S-056 | Deletion request/recovery bị gián đoạn | Mất phiên sau gửi hoặc provider đã bị gỡ ở ngoài | Có cách tra request và liên hệ người xử lý theo P-019; recovery xác minh đúng user, không merge email hoặc lấy phone contact chưa OTP làm đăng nhập. | P-019 · Expected |

## Những tổ hợp phải cross-check, không chỉ demo từng case riêng

- Hủy ↔ receipt đến ↔ qua 22h; cancel chỉ được quyết theo server và state mới, tiền muộn không mở lại order.
- Checkout ↔ rút ↔ checkout thiết bị khác; available/points chỉ dùng một lần, pending rút không bao giờ tham gia quote.
- Ingredient off ↔ đơn tương lai ↔ demand đang mua ↔ substitution; catalog availability và fulfillment case là hai trục.
- Refund ↔ refund khác ↔ withdrawal từ tiền vừa hoàn; phần đã posted và cap đang giữ phải còn đúng khi client mở đồng thời.
- Complete ↔ referral reward ↔ refund toàn bộ/partial; không lặp earn/reward, việc thu hồi reward chưa chốt không được giả là đã duyệt.
- Role/session revoke ↔ modal submit ↔ unknown response; đọc lại kết quả với quyền hiện tại, không tự submit bằng quyền cũ.
- Settings/bank/slot change ↔ quote ↔ order snapshot; phân biệt đơn mới với nghĩa vụ đã có.
- Logout/account switch ↔ push/deep link ↔ cached screen; không hiện PII user trước hoặc dùng token user trước.

Các tổ hợp trên là review obligations, không khẳng định đã liệt kê mọi hoán vị hoặc sản phẩm đã an toàn tài chính. Giữ exploratory review và đối chiếu contract/state trước implementation.
