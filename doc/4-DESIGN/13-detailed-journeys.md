# Hành trình chi tiết web, app và admin — TPX

> Design brief v0.4 — 2026-10-25. Cập nhật theo D-093–100. J là hành trình xuyên vai trò, FC là tình huống cần thiết kế; không thay ID US/UF/UC/S hiện có. P-xxx đọc theo trạng thái từng phần trong review register; chỉ phần còn mở dựng branch có annotation, không coi backend đã hỗ trợ.

Mỗi bước ghi rõ khách/admin/hệ thống; sự kiện giữa hai vai trò không phải link điều hướng từ khách vào admin. Các hành trình dùng màn/subview hiện có; số màn logic vẫn63. Bao phủ màn không chứng minh đã bao phủ từng action/state.

## Index

| Journey | Mục tiêu | Feature nguồn | UC liên quan | Cases |
| --- | --- | --- | --- | --- |
| J-001 | Duyệt chưa đăng nhập → đăng nhập → giữ giỏ | F-001, F-002, F-003, F-004 | UC-001, UC-002, UC-004 | FC-001, FC-002, FC-003, FC-004 |
| J-002 | Khởi động app, phiên đăng nhập và liên kết identity | F-001 | UC-004 | FC-005, FC-006, FC-007, FC-008 |
| J-003 | Địa chỉ, người nhận và thay vùng giao | F-004, F-008 | UC-005, UC-025 | FC-009, FC-010, FC-011, FC-012 |
| J-004 | Chọn RAW/MEAL, quy cách và nội dung món | F-002, F-003, F-015 | UC-001, UC-002 | FC-013, FC-014, FC-015, FC-016 |
| J-005 | Giỏ hàng, sửa số lượng và đồng bộ nhiều thiết bị | F-004 | UC-003 | FC-017, FC-018, FC-019, FC-020 |
| J-006 | Ngày giao, 22h và đơn đặt xa | F-004, F-008 | UC-005, UC-009, UC-021 | FC-021, FC-022, FC-023, FC-024 |
| J-007 | Checkout tiền/điểm, quote và kết quả chưa rõ | F-004, F-010, F-012 | UC-003, UC-008 | FC-025, FC-026, FC-027, FC-028 |
| J-008 | Chuyển khoản và quay lại web/app | F-005 | UC-006, UC-020 | FC-029, FC-030, FC-031, FC-032 |
| J-009 | Theo dõi đơn và hủy trước cutoff | F-004, F-021 | UC-009, UC-010 | FC-033, FC-034, FC-035, FC-036 |
| J-010 | Thiếu hàng → liên hệ → đổi món/giảm đơn/tăng phải thu | F-006, F-007, F-021, F-005 | UC-010, UC-021, UC-023 | FC-037, FC-038, FC-039, FC-040 |
| J-011 | Hoàn hỗn hợp tiền/điểm và đối soát từng phần | F-021, F-010, F-012 | UC-008, UC-010, UC-023 | FC-041, FC-042, FC-043, FC-044 |
| J-012 | Ví → rút tiền → duyệt/chuyển/reject/cancel | F-010, F-011 | UC-007, UC-024 | FC-045, FC-046, FC-047, FC-048 |
| J-013 | Loyalty: tích, dùng, hoàn và thu hồi đã tiêu | F-012, F-017, F-021 | UC-008, UC-011, UC-023 | FC-049, FC-050, FC-051, FC-052 |
| J-014 | Referral từ link/mã đến đơn đủ điều kiện | F-001, F-017, F-012 | UC-004, UC-011 | FC-053, FC-054, FC-055, FC-056 |
| J-015 | Mua lại và thường mua → giỏ mới | F-018, F-019, F-004 | UC-012, UC-013 | FC-057, FC-058, FC-059, FC-060 |
| J-016 | Đánh giá của tôi và kiểm duyệt | F-016, F-015 | UC-014, UC-027 | FC-061, FC-062, FC-063, FC-064 |
| J-017 | Thông báo, quyền OS, consent và deep link | F-013, F-020 | UC-015, UC-028 | FC-065, FC-066, FC-067, FC-068 |
| J-018 | Admin: login, quyền, mất phiên và tài khoản cố định | F-009 | UC-016 | FC-069, FC-070, FC-071, FC-072 |
| J-019 | Admin catalog, ảnh, BOM và tác động đơn tương lai | F-002, F-003, F-015 | UC-017, UC-018, UC-019 | FC-073, FC-074, FC-075, FC-076 |
| J-020 | Settings readiness, hiệu lực và thay cấu hình | F-014, F-008, F-005, F-012, F-017, F-020 | UC-025 | FC-077, FC-078, FC-079, FC-080 |
| J-021 | Cutoff → batch → quyết unpaid → loại/mua | F-006, F-004, F-005 | UC-020, UC-021 | FC-081, FC-082, FC-083, FC-084 |
| J-022 | Mua/nhận thực tế → phân bổ shortage → nhu cầu sửa | F-006, F-007, F-021 | UC-018, UC-021, UC-023 | FC-085, FC-086, FC-087, FC-088 |
| J-023 | Sơ chế/đóng gói → giao thành công/thất bại → kết thúc | F-007, F-012, F-017, F-021 | UC-022, UC-023 | FC-089, FC-090, FC-091, FC-092 |
| J-024 | Đối soát, xác nhận nhầm và báo cáo tiền thật | F-005, F-009, F-010, F-011, F-012, F-014, F-021 | UC-020, UC-024, UC-026 | FC-093, FC-094, FC-095, FC-096 |
| J-025 | Hỗ trợ, agreement evidence và xóa tài khoản còn nghĩa vụ | F-001, F-009, F-021 | UC-004, UC-010, UC-016, UC-023, UC-026 | FC-097, FC-098, FC-099, FC-100 |

## J-001 — Duyệt chưa đăng nhập → đăng nhập → giữ giỏ

Màn: S-001, S-002, S-004, S-005, S-006, S-008, S-009, S-032, S-010. Scenario nguồn: UC-001, UC-002, UC-004.

1. Khách duyệt public; thêm RAW/MEAL vào giỏ tạm [P-013], chưa tạo đơn hoặc giữ tiền.
2. Từ giỏ chọn thanh toán → đăng nhập; lưu route nội bộ và lựa chọn trước khi mở provider.
3. Callback thành công → lấy giỏ tài khoản; nếu đã có giỏ khác, cho xem chênh lệch trước gộp/thay [P-013].
4. Sau xác nhận giỏ, tính lại giá/khả dụng; quay lại giỏ hoặc checkout, không tự đặt đơn.

Điểm kết thúc / recovery: Có một giỏ tài khoản được khách hiểu và xác nhận; cancel/fail provider vẫn giữ giỏ tạm, không ghi tiền.

Cases cần thể hiện: FC-001, FC-002, FC-003, FC-004.

## J-002 — Khởi động app, phiên đăng nhập và liên kết identity

Màn: S-009, S-010, S-011, S-032. Scenario nguồn: UC-004.

1. Web refresh hoặc app cold start → kiểm tra phiên trước khi hiển thị dữ liệu riêng.
2. Refresh thành công → lấy user/current state; thất bại → đăng nhập rồi trở lại route được phép.
3. Trong tài khoản chọn link provider → xác thực lại → link qua provider → đồng bộ identities cùng user.
4. Logout current/all theo P-011; gỡ binding thiết bị và dữ liệu riêng được cache; không tự gộp theo email.

Điểm kết thúc / recovery: User ID không đổi khi link; phiên mất hiệu lực không để action cũ thực hiện; thao tác tiền không tự replay sau login.

Cases cần thể hiện: FC-005, FC-006, FC-007, FC-008.

## J-003 — Địa chỉ, người nhận và thay vùng giao

Màn: S-012, S-013, S-014, S-015, S-019, S-059. Scenario nguồn: UC-005, UC-025.

1. Khách chọn địa chỉ lưu hoặc nhập người nhận/SĐT/địa chỉ tại checkout; không cần OTP/định vị.
2. Lưu/sửa/xóa/default address có xác nhận và validation; địa chỉ chỉ là nguồn cho đơn mới.
3. Đổi vùng → lấy lại slots/fee/minimum/quote; xóa lựa chọn không còn hợp lệ và yêu cầu chọn lại.
4. Đơn đã đặt hiển thị contact snapshot; sửa sổ địa chỉ không đổi nơi giao của đơn cũ.

Điểm kết thúc / recovery: Checkout có địa chỉ hợp lệ trong vùng đang mở; đơn cũ chỉ đổi qua agreement P-009/P-015.

Cases cần thể hiện: FC-009, FC-010, FC-011, FC-012.

## J-004 — Chọn RAW/MEAL, quy cách và nội dung món

Màn: S-001, S-002, S-003, S-004, S-005, S-006, S-007, S-008. Scenario nguồn: UC-001, UC-002.

1. Tìm/lọc riêng RAW/MEAL hoặc kết quả phân nhóm; chọn sản phẩm published.
2. RAW chọn pack/step qty; MEAL chọn khẩu phần/giá và xem nguyên liệu được giao, phần tự chuẩn bị.
3. Mở hướng dẫn rồi Back về đúng khẩu phần/scroll; thêm giỏ với phản hồi variant/qty cụ thể.
4. Khả dụng thay đổi giữa xem và thêm → báo dòng bị ảnh hưởng, giữ các lựa chọn khác, không tự thay hàng.

Điểm kết thúc / recovery: Giỏ chỉ có lựa chọn TPX cung cấp; ảnh/hướng dẫn không có không được thành lời khẳng định sai.

Cases cần thể hiện: FC-013, FC-014, FC-015, FC-016.

## J-005 — Giỏ hàng, sửa số lượng và đồng bộ nhiều thiết bị

Màn: S-008, S-014. Scenario nguồn: UC-003.

1. Xem giỏ mixed; tăng/giảm/xóa variant, xác nhận xóa cả giỏ nếu có [P-013].
2. Mỗi thay đổi cập nhật cart version; đang gửi thì không cộng nhiều lần từ một lần chạm.
3. Giỏ server thay đổi từ thiết bị khác → hiển thị trạng thái hiện tại/diff và cho tiếp tục với version mới.
4. Checkout chỉ dùng giỏ được xác nhận; khi đã tạo đơn, chỉ loại các dòng đã mua, không làm mất dòng thêm từ phiên khác [P-013].

Điểm kết thúc / recovery: Qty và tiền khớp server; lỗi cập nhật giữ dữ liệu gần nhất và hành động retry có chủ đích.

Cases cần thể hiện: FC-017, FC-018, FC-019, FC-020.

## J-006 — Ngày giao, 22h và đơn đặt xa

Màn: S-014, S-015, S-019, S-020, S-044, S-045. Scenario nguồn: UC-005, UC-009, UC-021.

1. Lấy clock/date range từ server theo HCM; hiển thị ngày cụ thể, một ngày/slot cho toàn đơn.
2. Ngày 21/10 trước 22h chọn 22..28/10; từ 22h chọn 23..28/10; không trượt max thành 29/10.
3. Khách giữ checkout qua 22h hoặc qua ngày → lấy range/quote mới trước commit, không tự chuyển ngày đã chọn.
4. Đơn giao 26/10 hiển thị khóa hủy lúc 22h 25/10; chỉ vào batch ngày 26/10.

Điểm kết thúc / recovery: Ngày hợp lệ tại commit; cùng một order có một lần giao; không tạo quota slot hoặc tự chuyển ngày.

Cases cần thể hiện: FC-021, FC-022, FC-023, FC-024.

## J-007 — Checkout tiền/điểm, quote và kết quả chưa rõ

Màn: S-008, S-014, S-015, S-016, S-017, S-019, S-022, S-025. Scenario nguồn: UC-003, UC-008.

1. Review hàng/địa chỉ/ngày/fee/minimum; server tự áp available, points opt-in trong caps, bank remainder.
2. Quote hiển thị nguồn tiền, điểm dùng và earn dự kiến; điểm chưa tích khi tạo đơn.
3. Đổi giỏ/slot/settings hoặc ví bị dùng ở phiên khác → invalid quote, trình bày diff và yêu cầu review lại.
4. Submit một lần; transaction tạo order và HOLD points D-093. Timeout → tra order/key; complete mới CAPTURE points, không trừ available lần nữa. D-099: cash cũng HOLD/CAPTURE/RELEASE; held_order tách pending rút.

Điểm kết thúc / recovery: Một order hoặc không order; không giữ tiền một nửa, không gửi lại tự động, zero bank due bỏ bước chuyển khoản.

Cases cần thể hiện: FC-025, FC-026, FC-027, FC-028.

## J-008 — Chuyển khoản và quay lại web/app

Màn: S-016, S-017, S-018, S-019, S-042, S-043, S-050. Scenario nguồn: UC-006, UC-020.

1. Khách thấy đúng bank/amount/reference của order, copy từng trường; QR hoặc mở app bank chỉ là tiện ích nếu có cấu hình, không giả tích hợp.
2. Khách rời TPX để chuyển; quay lại hoặc cold start → mở lại order và lấy funding mới.
3. Báo đã chuyển [P] chỉ tạo notice; admin kiểm tra actual receipt/reference và confirm phần thực nhận.
4. Thiếu → còn phải trả; đủ → funded; thừa/muộn/sai nội dung → queue case đối soát, không tự nạp ví.

Điểm kết thúc / recovery: Hướng dẫn và trạng thái tiền thật không mâu thuẫn; thông báo gửi lỗi không làm đổi funding.

Cases cần thể hiện: FC-029, FC-030, FC-031, FC-032.

## J-009 — Theo dõi đơn và hủy trước cutoff

Màn: S-018, S-019, S-020, S-021, S-022, S-025, S-042, S-050, S-052, S-043. Scenario nguồn: UC-009, UC-010.

1. Danh sách đơn phân biệt tiến trình giao, funding và refund; vào detail xem deadline và allowed actions.
2. Hủy hợp lệ → preview order/dòng và tác động nội bộ/bank đã nhận; xác nhận với version.
3. Commit CANCELLED → RELEASE cash/points holds một lần; tiền đã thực nhận/áp hoàn theo agreement, chưa hoàn thì vẫn pending. Admin cancel vận hành được dùng sau cutoff, không giả khách hủy trước hạn.
4. Race cancel/receipt/cutoff → lấy lại trạng thái; tiền tới muộn vào case, không khôi phục mua.

Điểm kết thúc / recovery: Đơn hủy không vào thu mua; lịch sử hoàn còn truy cập được; không hủy/hoàn hai lần.

Cases cần thể hiện: FC-033, FC-034, FC-035, FC-036.

## J-010 — Thiếu hàng → liên hệ → đổi món/giảm đơn/tăng phải thu

Màn: S-019, S-021, S-031, S-042, S-045, S-046, S-050, S-052, S-016. Scenario nguồn: UC-010, UC-021, UC-023.

1. Từ đơn tương lai bị ảnh hưởng hoặc nhận hàng không đạt → admin mở case gắn order item/qty cụ thể.
2. Liên hệ khách theo kênh cấu hình → ghi phương án và bằng chứng đã đồng ý; chưa liên hệ được giữ OPEN/blocked.
3. Preview thay hàng/giảm hàng: before/after, quantity, net obligation, refund hoặc tiền cần thu thêm; không ghi sửa snapshot gốc.
4. Admin dùng chức năng update theo D-096; execution/repricing/chênh lệch OQ-042 còn cần chốt. Nếu không thực hiện được thì admin CANCELLED, hoàn tiền và release held points; case financial theo dõi riêng.

Điểm kết thúc / recovery: Hàng giao khớp phương án khách đồng ý; không còn action tài chính treo bị che sau case CLOSED.

Cases cần thể hiện: FC-037, FC-038, FC-039, FC-040.

## J-011 — Hoàn hỗn hợp tiền/điểm và đối soát từng phần

Màn: S-019, S-021, S-022, S-025, S-050, S-051, S-052, S-056. Scenario nguồn: UC-008, UC-010, UC-023.

1. Admin chọn agreement/affected items; refund preview lấy nguồn còn hoàn trừ các plan đang giữ cap.
2. Review cash_goods/shipping/excess và points; original source khác payout method; hiển thị ORDER_EARN được giữ nguyên D-100.
3. Approve → internal legs settle theo P-003; BANK legs chờ chuyển; nhóm chuyển phải cùng destination và tổng bằng legs được claim.
4. Xác nhận bank thật → legs settled; parent settled khi đủ; order refund projection có thể vẫn PARTIAL dù case đã xong.

Điểm kết thúc / recovery: Không hoàn vượt tiền đã thu hoặc cap còn lại; tiền/points không bị lặp; khách thấy từng phần đã nhận và còn chờ.

Cases cần thể hiện: FC-041, FC-042, FC-043, FC-044.

## J-012 — Ví → rút tiền → duyệt/chuyển/reject/cancel

Màn: S-022, S-023, S-024, S-053, S-054, S-056, S-058, S-014. Scenario nguồn: UC-007, UC-024.

1. Khách xem available/pending/total và lịch sử các yêu cầu; chọn tạo rút, nhập bank/name/account/amount.
2. Review masked destination → tạo: chuyển available sang pending trong cùng operation; details/withdrawal history có entry quay lại.
3. Admin review → approve → claim processing → chuyển thực → mark paid có reference; APPROVED chưa phải đã chuyển.
4. Cancel/reject chỉ các trạng thái P-002 cho phép; unknown giữ pending; sửa bank/known failure cần P-016, không chỉnh request đang chuyển.

Điểm kết thúc / recovery: Ví 200k/rút 150k còn 50k available; paid làm tổng còn 50k; cancel/reject release một lần; không rút loyalty.

Cases cần thể hiện: FC-045, FC-046, FC-047, FC-048.

## J-013 — Loyalty: tích, dùng, hoàn và thu hồi đã tiêu

Màn: S-014, S-019, S-021, S-025, S-052, S-056. Scenario nguồn: UC-008, UC-011, UC-023.

1. Checkout cho thấy available/held/total points và cash available/held_order/pending rút. Place HOLD cả hai nguồn, không dùng tiếp.
2. Complete CAPTURE cả hai holds một lần, không trừ available lại; earn riêng theo nội dung cuối, history có các entry nguồn.
3. Cancel trước complete RELEASE holds. Sau complete RETURN captured points/hoàn cash theo nguồn và agreement; giữ nguyên ORDER_EARN đã cấp.
4. D-100 cho hoàn sau complete dù earned points đã tiêu; không debt/offset/clawback hoặc lấy cash bù.

Điểm kết thúc / recovery: Cash/points có bucket rõ; hoàn sau complete giữ ORDER_EARN; không duplicate hold/capture/release/return/earn.

Cases cần thể hiện: FC-049, FC-050, FC-051, FC-052.

## J-014 — Referral từ link/mã đến đơn đủ điều kiện

Màn: S-009, S-010, S-026, S-056, S-059, S-032. Scenario nguồn: UC-004, UC-011.

1. Người giới thiệu xem link/code và điều kiện reward từ settings, copy/share có kết quả.
2. Người nhận mở link: web hoặc app khi link được cấu hình; chưa có app vẫn dùng web, không hứa deferred attribution qua cài đặt.
3. Giữ mã qua login và yêu cầu claim theo P-006; nhập mã thủ công khi link không giữ được, không tự ghi nhận theo email.
4. Đơn đầu đủ điều kiện complete → reward một lần; hoàn qualifying order hiển thị reversal proposal và liên hệ hỗ trợ nếu chưa quyết.

Điểm kết thúc / recovery: Cả hai phía biết trạng thái chờ/đủ/không đủ/thưởng; không thưởng đăng ký hoặc order chưa complete.

Cases cần thể hiện: FC-053, FC-054, FC-055, FC-056.

## J-015 — Mua lại và thường mua → giỏ mới

Màn: S-018, S-019, S-027, S-004, S-006, S-008, S-014. Scenario nguồn: UC-012, UC-013.

1. Khách từ order history/detail chọn mua lại hoặc mở danh sách thường mua.
2. Preview từng variant với giá/quy cách/khả dụng hiện tại; đánh dấu dòng không còn.
3. Giỏ đang có dữ liệu → chọn thêm/thay theo P-010, xác nhận trước mutation; version cũ phải reload diff.
4. Giỏ mới chọn ngày/slot/points lại, không dùng receipt/khuyến khích/địa chỉ cũ để tự đặt.

Điểm kết thúc / recovery: Lịch sử đơn gốc bất biến; lựa chọn hiện tại được khách xác nhận, không auto-checkout.

Cases cần thể hiện: FC-057, FC-058, FC-059, FC-060.

## J-016 — Đánh giá của tôi và kiểm duyệt

Màn: S-004, S-006, S-019, S-028, S-062. Scenario nguồn: UC-014, UC-027.

1. Từ dòng order completed của mình → mở form đánh giá hoặc review đã gửi.
2. Gửi rating/text hợp lệ → PENDING moderation; retry không tạo review trùng.
3. Admin mở review và purchase evidence → publish/hide với reason, không sửa rating/text.
4. Public average chỉ published; khách có nơi xem review pending/hidden; edit/delete review chưa được chốt thì không dựng CTA khả dụng.

Điểm kết thúc / recovery: Không có ngõ cụt sau submit; trạng thái của tôi khác public; eligibility cho hàng không giao/hoàn cần P-010/P-018.

Cases cần thể hiện: FC-061, FC-062, FC-063, FC-064.

## J-017 — Thông báo, quyền OS, consent và deep link

Màn: S-009, S-019, S-021, S-024, S-029, S-030, S-032, S-060. Scenario nguồn: UC-015, UC-028.

1. Khách chọn nhận push/reminder theo kênh; giải thích trước OS prompt; từ chối không chặn mua.
2. Consent marketing/reminder tách OS permission; Zalo cần khả năng gửi hợp lệ, SĐT contact chưa OTP không đồng nghĩa nhận được Zalo.
3. Nhận link khi app foreground/background/cold start hoặc web → kiểm tra session/ownership → tải entity mới.
4. Logout/account switch gỡ binding; user có thể mở OS settings và quay lại để refresh; retry admin kiểm tra consent/sự kiện còn hiệu lực.

Điểm kết thúc / recovery: Khách tới đúng resource và state hiện tại; SENT không phải READ; không gửi kênh khác khi chưa đồng ý.

Cases cần thể hiện: FC-065, FC-066, FC-067, FC-068.

## J-018 — Admin: login, quyền, mất phiên và tài khoản cố định

Màn: S-033, S-034, S-057, S-058. Scenario nguồn: UC-016.

1. Admin dùng fixed account/password, không signup hoặc OTP; login sai/rate limit có recovery message.
2. Load permissions → landing vào màn đầu được phép; không bắt vào dashboard nếu không dashboard.read.
3. Đổi roles/status có impact preview và guard P-019; action đang mở revalidate quyền khi submit.
4. Provision/reset password/revoke phiên theo P-019 bằng runbook hoặc contract được duyệt; không dựng nút backend chưa có.

Điểm kết thúc / recovery: Mỗi thao tác có actor riêng; không khóa mất quản trị cuối, không nâng quyền qua UI ẩn hoặc dùng phiên cũ.

Cases cần thể hiện: FC-069, FC-070, FC-071, FC-072.

## J-019 — Admin catalog, ảnh, BOM và tác động đơn tương lai

Màn: S-035, S-036, S-037, S-038, S-039, S-040, S-045, S-050, S-061. Scenario nguồn: UC-017, UC-018, UC-019.

1. Tạo category/ingredient và variant RAW hoặc meal/portion; nhập giá, units, BOM, nội dung/ảnh/source.
2. Validate draft → preview consumer → publish; upload/finalize chưa xong không được coi asset ready.
3. Tắt ingredient → xem impacted variants và orders tương lai cần case; không chỉ đổi badge catalog.
4. Sửa giá/BOM/archive giữ snapshot order và recipe nguồn; bật lại theo manual flags P-007.

Điểm kết thúc / recovery: Catalog mới hợp lệ; đơn cũ không mất nội dung và tác động order có người xử lý, không chỉ toast thành công.

Cases cần thể hiện: FC-073, FC-074, FC-075, FC-076.

## J-020 — Settings readiness, hiệu lực và thay cấu hình

Màn: S-059, S-014, S-015, S-016, S-034, S-042, S-063. Scenario nguồn: UC-025.

1. Admin mở từng section với active version/thiếu cấu hình; policies 22h/+7 đã chốt không tự thành slider đổi tùy ý.
2. Nhập fee/minimum/vùng/slot/bank/caps/rewards/reminder; review units và reason.
3. Validate/publish version → affected quotes reload; đơn giữ snapshot; đổi bank/vùng có affected old-order queue.
4. Readiness theo chức năng: thiếu bắt buộc cho checkout thì chặn checkout; thiếu reward/reminder không được tự bịa default hoặc chặn mọi giao dịch không liên quan.

Điểm kết thúc / recovery: Cấu hình có hiệu lực rõ, không âm thầm sửa nghĩa vụ đơn cũ; không giả tất cả tích hợp sẵn sàng.

Cases cần thể hiện: FC-077, FC-078, FC-079, FC-080.

## J-021 — Cutoff → batch → quyết unpaid → loại/mua

Màn: S-034, S-041, S-042, S-044, S-045, S-046, S-050. Scenario nguồn: UC-020, UC-021.

1. Trước cutoff chỉ preview nhu cầu; phân biệt ngày tạo đơn và ngày giao để không mua đơn đặt xa sớm.
2. Từ 22h build/rebuild batch → actual source order lines; unpaid có tabs undecided/included/excluded, cần reason đúng quyền.
3. Chốt quyết định → xem delta nhu cầu và version; không giữ một bản export cũ như kế hoạch hiện tại.
4. EXCLUDED/không thể thực hiện → admin quyết CANCELLED có reason, release held points và hoàn tiền theo D-094; receipt muộn vẫn vào case, không tự include lại.

Điểm kết thúc / recovery: Mọi order đến cutoff có quyết định hoặc exception owner; không treo PLACED vô hạn, không tự cancel theo timer chưa duyệt.

Cases cần thể hiện: FC-081, FC-082, FC-083, FC-084.

## J-022 — Mua/nhận thực tế → phân bổ shortage → nhu cầu sửa

Màn: S-039, S-042, S-045, S-046, S-047, S-050. Scenario nguồn: UC-018, UC-021, UC-023.

1. Từ procurement line xem từng nguồn RAW/MEAL order và unit conversion theo snapshot.
2. Ghi mua nhiều đợt/lô nhỏ, quantity/cost/quality và lượng đạt; phân biệt cumulative đã nhận với lần nhập thêm.
3. Nếu thiếu/hỏng, ops phân bổ rõ về order/items theo P-017, lưu quyết định; tạo case cho đúng khách bị ảnh hưởng.
4. Agreement thay hàng → demand revision; ghi mua bổ sung/delta và chuyển prep đúng lượng cuối; dư mua/cost không tự thành hàng khách phải trả.

Điểm kết thúc / recovery: Tổng accepted phân bổ không vượt thực nhận; không dùng cùng hàng cho hai đơn, trace được nguồn/chi phí còn thiếu.

Cases cần thể hiện: FC-085, FC-086, FC-087, FC-088.

## J-023 — Sơ chế/đóng gói → giao thành công/thất bại → kết thúc

Màn: S-019, S-042, S-047, S-048, S-049, S-050, S-025. Scenario nguồn: UC-022, UC-023.

1. Prep theo order/item checklist; nhận/đạt/sơ chế/đóng gói có guard; không tick đủ khi shortage chưa giải quyết.
2. READY→dispatch theo quyết định admin D-095 kể cả khi còn phải thu; ghi actor/reason, không đổi payment thành PAID. Bank refund pending không tự block phần hàng đã thống nhất.
3. Giao thành công→complete theo guard được chốt, CAPTURE cash/points holds và earn/reward riêng; complete-unpaid còn OQ-050: dựng cả A/B theo03 section12, không tự chọn default. Giao fail→case, admin có thể quyết hủy/CANCELLED theo D-094.
4. Đơn chỉ giao phần còn lại sau điều chỉnh: cập nhật agreed composition trước ready; không tự tạo split deliveries hoặc mark full complete cho phần chưa giao.

Điểm kết thúc / recovery: Mọi failed delivery có người xử lý và nhánh cuối; terminal không mở lại tùy ý; notification lỗi không rollback completion.

Cases cần thể hiện: FC-089, FC-090, FC-091, FC-092.

## J-024 — Đối soát, xác nhận nhầm và báo cáo tiền thật

Màn: S-034, S-042, S-043, S-051, S-052, S-053, S-054, S-056, S-058, S-063, S-050. Scenario nguồn: UC-020, UC-024, UC-026.

1. Queue theo business day: chưa xác nhận bank, unmatched/excess, payout pending/processing, refund legs dở và case chưa đóng.
2. Receipt sai order/amount hoặc entry sai → mở correction proposal P-016, show before/after và downstream effects; không edit ledger đã posted.
3. Đối soát funding/ledger/payout references và liabilities; mismatch phải có record xử lý, không dùng nút credit để làm khớp số.
4. Báo cáo phân biệt created/delivery/payment date; doanh thu/thu tiền/hoàn/rút/liability/points và cost completeness, export đúng filter/quyền.

Điểm kết thúc / recovery: Queue không bỏ sót nghĩa vụ; correction có audit và không chuyển ngân hàng giả; report không coi pending là đã chi.

Cases cần thể hiện: FC-093, FC-094, FC-095, FC-096.

## J-025 — Hỗ trợ, agreement evidence và xóa tài khoản còn nghĩa vụ

Màn: S-010, S-011, S-019, S-021, S-022, S-024, S-031, S-050, S-052, S-054, S-055, S-056, S-058. Scenario nguồn: UC-004, UC-010, UC-016, UC-023, UC-026.

1. Khách từ order/payment/refund/withdraw hoặc policy mở liên hệ TPX theo kênh đã cấu hình, kèm mã tham chiếu được copy; không tự thêm in-app chat/ticket upload.
2. Ops tạo case từ liên hệ, chọn order/items, ghi issue và bằng chứng thỏa thuận; pending contact không đồng nghĩa AGREED.
3. Khách yêu cầu xóa account → reauth → thấy outstanding orders/money/withdraw/refund; request có trạng thái và đích liên hệ.
4. Ops xử lý nghĩa vụ trước anonymize theo P-011/P-019; không xóa ledger, tự forfeiture ví hoặc xóa identity làm khách mất đường nhận hoàn.

Điểm kết thúc / recovery: Khách có lối tìm trợ giúp ở trạng thái lỗi; deletion có owner/status/recovery, không chỉ toast đã nhận rồi biến mất.

Cases cần thể hiện: FC-097, FC-098, FC-099, FC-100.

## Khác biệt platform phải thể hiện trong từng journey

| Surface | Interaction và recovery |
| --- | --- |
| Web desktop/mobile | Direct URL/refresh, provider popup blocked/redirect, browser Back không resubmit, nhiều tab, dirty form, bàn phím/focus, quay từ app bank bằng history. Không ép cài app để hoàn tất đơn. |
| Flutter iOS | Cold/warm start, provider cancel/callback, OS back/swipe và sheet dismissal, safe area/keyboard/text scale; bank-app return và push sau logout. Không coi đóng app là hủy order. |
| Flutter Android | Cold/warm start và activity bị OS dừng, system Back/keyboard, provider cancel/callback, push permission/state, link sau đổi user; không replay mutation khi resume. |
| Admin desktop/compact | List→detail→back giữ filter/ngày; dirty form, multi-tab/two-admin conflict; partial permission, masked PII, processing unknown; compact vẫn đọc được số tiền/destination và action confirm, không chỉ thu nhỏ bảng. |

Quyền push/native provider thực tế phụ thuộc cấu hình/SDK; thiết kế mô tả states và capability, không cam kết provider operation đã chạy. Các OS paths là tình huống kiểm tra thiết kế, không phải thay đổi stack.

## Cách chứng minh một journey hoàn chỉnh

Mỗi journey có entry cụ thể, actor lane, preconditions, trigger, result được xác nhận, actions còn được phép, lỗi/recovery và exit. Mỗi FC map tới source/frame thật cho các surfaces có liên quan; N/A có lý do. Case tài chính/terminal/cutoff phải có frame trực tiếp. Không đánh dấu đạt chỉ vì component có một generic error state.
