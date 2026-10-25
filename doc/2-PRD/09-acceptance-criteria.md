# Acceptance Criteria

> Draft theo các quyết định đã nhận; chưa freeze PRD. Giữ các regression đã chốt và bổ sung104 featureAC cho đủ21 feature; [P] cần review trước implementation.

## Product-Level AC

- AC-PROD-001: Checkout chỉ sử dụng tiền hoàn available; không sử dụng khoản pending của yêu cầu rút.

## Feature-Level AC

| Feature | AC | Notes |
| --- | --- | --- |
| F-010/F-011 | AC-BAL-001: Với tổng 200.000đ, available 200.000đ và pending 0đ, tạo yêu cầu rút 150.000đ phải cho available 50.000đ, pending 150.000đ; tổng vẫn 200.000đ | D-078, BR-035 |
| F-010/F-004 | AC-BAL-002: Với available 50.000đ và pending 150.000đ, checkout dùng tối đa 50.000đ tiền hoàn; sau đó mới áp điểm nếu chọn và thanh toán phần còn lại | D-070, D-078 |
| F-011 | AC-BAL-003: Tạo yêu cầu rút hoặc duyệt yêu cầu không được hiển thị như đã chuyển tiền ngân hàng | Quy trình chuyển hoàn thủ công; trạng thái cụ thể còn cần review |
| F-008 | AC-DATE-001: Đặt ngày 21/10/2026 trước 22:00, được chọn giao từ 22/10 đến 28/10; không được chọn 29/10 | D-079; theo Asia/Ho_Chi_Minh |
| F-008/F-006 | AC-DATE-002: Đặt ngày 21/10/2026 từ 22:00, sớm nhất giao 23/10, xa nhất vẫn 28/10 | D-025, D-079/080; tối đa theo ngày đặt, không cộng 7 vào ngày sớm nhất |
| F-021/F-006 | AC-DATE-003: Đơn giao 26/10/2026 cho hủy trước 22:00 ngày 25/10; từ 22:00 khóa hủy và thuộc batch chốt mua đó | D-080; không khóa ngay ngày tạo đơn |
| F-004/F-012 | AC-LOY-001: Tiền hàng sau giảm giá 1.000.000đ, available dùng 200.000đ, khách đủ điểm và chọn dùng, trần 5%, trần tiền ít nhất 50.000đ, không phí giao -> dùng 50 điểm, chuyển khoản 750.000đ | D-081/082; trần % trước trừ số dư, 5% là ví dụ |
| F-012 | AC-LOY-002: Hoàn thành đơn AC-LOY-001 tích 950 điểm; chưa hoàn thành chưa tích | D-044, D-082; phần số dư vẫn tích, phần điểm không tích tiếp |
| F-004/F-012 | AC-LOY-003: Thêm phí giao 20.000đ vào ví dụ AC-LOY-001 -> chuyển khoản 770.000đ, vẫn dùng 50 điểm và tích 950 điểm khi hoàn thành | D-081/082; phí giao không tăng cơ sở trần hoặc tích |
| F-012 | AC-LOY-004: Cơ sở tích hợp lệ 12.999đ -> 12 điểm; 999đ -> 0 điểm | D-082; làm tròn xuống |
| F-012/F-021 | AC-REF-001: Hủy/hoàn toàn bộ đơn đã dùng 50 điểm -> hoàn lại đúng 50 điểm, không ghi 50.000đ thành tiền hoàn | D-083; phần tiền xử lý theo thỏa thuận D-084 |
| F-012/F-021 | AC-REF-002: Full refund đơn G1m/dùng50points/đã earn950: RETURN50captured points, giữ nguyên950ORDER_EARN dù đã dùng, cash hoàn theo nguồn | D-100 thay D-085 |

## Auth — phạm vi đã chốt

- AC-AUTH-001: Khách có các phương thức Google/Facebook/Apple ở bản đầu; không bắt buộc SMS OTP để đăng nhập social. Bổ sung phone login sau khi dịch vụ sẵn sàng.
- AC-AUTH-002: Admin chỉ dùng account cố định user tạo, tài khoản/mật khẩu không OTP/TOTP; không có đăng ký admin công khai. Phân quyền/ownership vẫn kiểm tra ở API.
- AC-AUTH-003: Việc đăng nhập social không tự cấp quyền admin; danh tính client tự khai không đủ để xem đơn/số dư/loyalty của người khác.

## Feature AC index — toàn hệ thống

Nguồn mới nhất D-093–100; mỗi AC giữ ID và được đồng bộ từ feature spec.

| AC ID | Feature/spec | Tiêu chí |
| --- | --- | --- |
| AC-F-001-01 | [F-001](04-detailed-feature-specs/F-001.md) | [C] Login ba provider trên web/iOS/Android tạo hoặc trả cùng user TPX khi đã link, không tạo ví/điểm mới. |
| AC-F-001-02 | [F-001](04-detailed-feature-specs/F-001.md) | [C] Token giả/hết hạn/sai project không được truy cập đơn/tiền/điểm. |
| AC-F-001-03 | [F-001](04-detailed-feature-specs/F-001.md) | [C] Hủy provider flow không tạo đơn hoặc mất giỏ. |
| AC-F-001-04 | [F-001](04-detailed-feature-specs/F-001.md) | [C] SĐT checkout lưu chưa OTP-verified; không tự cho login bằng số đó. |
| AC-F-001-05 | [F-001](04-detailed-feature-specs/F-001.md) | [P] Không unlink phương thức cuối, identity thuộc user khác báo conflict; không gộp số dư. |
| AC-F-002-01 | [F-002](04-detailed-feature-specs/F-002.md) | [C] Khách chỉ đặt variant TPX cung cấp; không gửi giá tùy ý lên API. |
| AC-F-002-02 | [F-002](04-detailed-feature-specs/F-002.md) | [C] Giá thị trường/giá vốn thay đổi không sửa đơn đã tạo. |
| AC-F-002-03 | [F-002](04-detailed-feature-specs/F-002.md) | [C] Sản phẩm tắt không thêm/đặt mới; giỏ cũ hiển thị lỗi cần xử lý. |
| AC-F-002-04 | [F-002](04-detailed-feature-specs/F-002.md) | [P] Mapping nguyên liệu/đơn vị thiếu làm variant chưa publish; admin thấy trường thiếu. |
| AC-F-002-05 | [F-002](04-detailed-feature-specs/F-002.md) | [P] Qty không đúng step hoặc ≤0 bị từ chối. |
| AC-F-003-01 | [F-003](04-detailed-feature-specs/F-003.md) | [C] Chọn khẩu phần hiển thị đúng giá gói, thành phần chính và không gia vị/sốt. |
| AC-F-003-02 | [F-003](04-detailed-feature-specs/F-003.md) | [C] Tắt một nguyên liệu khiến mọi món phụ thuộc không checkout được. |
| AC-F-003-03 | [F-003](04-detailed-feature-specs/F-003.md) | [C] Tắt món/nguyên liệu không tự hủy đơn tương lai đã trả. |
| AC-F-003-04 | [F-003](04-detailed-feature-specs/F-003.md) | [P] Sửa BOM không thay nhu cầu/giá snapshot đơn cũ. |
| AC-F-003-05 | [F-003](04-detailed-feature-specs/F-003.md) | [P] Nguyên liệu bật lại chỉ khôi phục nếu món không bị tắt tay. |
| AC-F-004-01 | [F-004](04-detailed-feature-specs/F-004.md) | [C] Giỏ RAW+MEAL tạo một order và một delivery, snapshot đúng từng variant. |
| AC-F-004-02 | [F-004](04-detailed-feature-specs/F-004.md) | [C] Pending rút không được checkout sử dụng. |
| AC-F-004-03 | [F-004](04-detailed-feature-specs/F-004.md) | [C] Ví dụ 1 triệu, available 200k, đủ điểm, trần5% → 50 điểm, chuyển 750k; complete tích950. |
| AC-F-004-04 | [F-004](04-detailed-feature-specs/F-004.md) | [P] Hai request cùng key trả cùng order; key khác payload báo conflict. |
| AC-F-004-05 | [F-004](04-detailed-feature-specs/F-004.md) | [P] Hai checkout/rút đồng thời không dùng trùng available/points; thiếu tiền hoàn quote mới, không âm. |
| AC-F-004-06 | [F-004](04-detailed-feature-specs/F-004.md) | [P] Đơn chưa trả ngoài nội bộ không tự hủy bằng timeout chưa chốt. |
| AC-F-004-07 | [F-004](04-detailed-feature-specs/F-004.md) | [C] Order commit giữ điểm theo D-093; thất bại tạo đơn không để hold mồ côi. D-099 cash cũng HOLD đến complete, cancel RELEASE. |
| AC-F-004-08 | [F-004](04-detailed-feature-specs/F-004.md) | [C] Place reserve cash/points atomically theo available mới nhất. Không có order commit thì không để hold mồ côi một nguồn; checkout/rút đồng thời không tiêu hold hoặc pending. |
| AC-F-005-01 | [F-005](04-detailed-feature-specs/F-005.md) | [C] Khách bấm đã chuyển vẫn thấy đang chờ admin xác nhận. |
| AC-F-005-02 | [F-005](04-detailed-feature-specs/F-005.md) | [C] Duyệt mua unpaid không làm payment=PAID. |
| AC-F-005-03 | [F-005](04-detailed-feature-specs/F-005.md) | [P] Receipt được confirm lại cùng key/reference không cộng tiền lần hai. |
| AC-F-005-04 | [F-005](04-detailed-feature-specs/F-005.md) | [P] Nhận thiếu hiển thị phần còn thiếu; nhận thừa ghi unmatched/excess và case thỏa thuận. |
| AC-F-005-05 | [F-005](04-detailed-feature-specs/F-005.md) | [P] Số phải chuyển0 không yêu cầu receipt; internal allocation hoàn tất là đủ nguồn. |
| AC-F-006-01 | [F-006](04-detailed-feature-specs/F-006.md) | [C] Đơn đặt trước5 ngày không đi mua ngay ngày tạo, chỉ đợt trước ngày giao. |
| AC-F-006-02 | [F-006](04-detailed-feature-specs/F-006.md) | [C] Từ22h không hủy dù job chưa chạy. |
| AC-F-006-03 | [F-006](04-detailed-feature-specs/F-006.md) | [C] Admin lựa chọn unpaid mua/loại riêng, có lịch sử. |
| AC-F-006-04 | [F-006](04-detailed-feature-specs/F-006.md) | [P] Retry tổng hợp không nhân đôi nhu cầu/order trong batch. |
| AC-F-006-05 | [F-006](04-detailed-feature-specs/F-006.md) | [P] Chạy lại batch giữ quyết định tay, báo delta nếu admin thay đổi kế hoạch được phép. |
| AC-F-007-01 | [F-007](04-detailed-feature-specs/F-007.md) | [C] Khách thấy tiến trình từ cùng một đơn, chưa cần app shipper riêng. |
| AC-F-007-02 | [F-007](04-detailed-feature-specs/F-007.md) | [C] Giao lỗi chuyển sang xử lý thủ công, không tự trừ/hoàn tiền. |
| AC-F-007-03 | [F-007](04-detailed-feature-specs/F-007.md) | [C] Chỉ complete mới tích loyalty. |
| AC-F-007-04 | [F-007](04-detailed-feature-specs/F-007.md) | [P] Complete lặp không cộng điểm/thưởng referral hai lần. |
| AC-F-007-05 | [F-007](04-detailed-feature-specs/F-007.md) | [P] Không complete order CANCELLED hoặc còn case hàng chưa giải quyết; xuất lỗi guard. |
| AC-F-007-06 | [F-007](04-detailed-feature-specs/F-007.md) | [C] Khi funding PARTIAL/UNFUNDED, admin được quyết định giao với actor/reason và số còn phải thu; dispatch không tự confirm receipt hoặc đổi FUNDED/PAID. |
| AC-F-007-07 | [F-007](04-detailed-feature-specs/F-007.md) | [C] Refund bank pending không tự chặn phần hàng còn lại đã thống nhất; fulfillment resolution và finance status thể hiện riêng, không falsely settled. |
| AC-F-008-01 | [F-008](04-detailed-feature-specs/F-008.md) | [C] Ngày21/10 trước22h chọn22..28/10; từ22h chọn23..28/10, không29/10. |
| AC-F-008-02 | [F-008](04-detailed-feature-specs/F-008.md) | [C] Giao26/10 được hủy trước 22h 25/10, đúng22h bị khóa. |
| AC-F-008-03 | [F-008](04-detailed-feature-specs/F-008.md) | [C] Không áp số đơn tối đa theo slot. |
| AC-F-008-04 | [F-008](04-detailed-feature-specs/F-008.md) | [P] Tắt vùng/slot không tự xóa/hủy đơn cũ. |
| AC-F-008-05 | [F-008](04-detailed-feature-specs/F-008.md) | [C] SĐT nhận hàng không bắt OTP trong R1. |
| AC-F-009-01 | [F-009](04-detailed-feature-specs/F-009.md) | [C] Các account user tạo login không cần OTP và có quyền phù hợp. |
| AC-F-009-02 | [F-009](04-detailed-feature-specs/F-009.md) | [C] Customer token không truy cập /admin dù biết URL. |
| AC-F-009-03 | [F-009](04-detailed-feature-specs/F-009.md) | [P] Disable account/role update có hiệu lực ở API, action cũ không được dùng tiếp qua cache lâu. |
| AC-F-009-04 | [F-009](04-detailed-feature-specs/F-009.md) | [P] Audit xác nhận tiền/withdraw/refund lưu actor+reason+reference, không secret. |
| AC-F-009-05 | [F-009](04-detailed-feature-specs/F-009.md) | [P] Báo cáo tách tiền nhận thực, tiền hoàn và giá trị đơn, không gọi GMV là tiền thu. |
| AC-F-010-01 | [F-010](04-detailed-feature-specs/F-010.md) | [C] 200k tạo rút150k → pending150k, available50k, total200k. |
| AC-F-010-02 | [F-010](04-detailed-feature-specs/F-010.md) | [C] Checkout chỉ dùng tối đa50k trong ví dụ, không pending150k. |
| AC-F-010-03 | [F-010](04-detailed-feature-specs/F-010.md) | [C] Không có API/CTA tự nạp tiền hoặc expiry. |
| AC-F-010-04 | [F-010](04-detailed-feature-specs/F-010.md) | [P] Hai admin retry credit cùng adjustment chỉ cộng một lần. |
| AC-F-010-05 | [F-010](04-detailed-feature-specs/F-010.md) | [P] Tổng ledger theo user đối soát bằng projection; không xóa entry để sửa số. |
| AC-F-010-06 | [F-010](04-detailed-feature-specs/F-010.md) | [C] Ví200k, place dùng50k: available150k/held_order50k/total200k; không cash capture ngay, held_order không được dùng/rút. |
| AC-F-010-07 | [F-010](04-detailed-feature-specs/F-010.md) | [C] Ví200k đã pending rút150k, place dùng50k: available0/held_order50k/pending150k/total200k; không gom hai loại giữ tiền vào cùng trạng thái. |
| AC-F-010-08 | [F-010](04-detailed-feature-specs/F-010.md) | [C] Cancel release held_order một lần; complete capture chỉ giảm held_order/total, không trừ available lại. Retry không tác dụng hai lần. |
| AC-F-011-01 | [F-011](04-detailed-feature-specs/F-011.md) | [C] Tạo rút150k trong ví200k giữ150k ngay; không trừ tổng cho tới khi chuyển. |
| AC-F-011-02 | [F-011](04-detailed-feature-specs/F-011.md) | [P] Duyệt không làm tiền ra khỏi pending và không hiện đã chuyển. |
| AC-F-011-03 | [F-011](04-detailed-feature-specs/F-011.md) | [P] PAID trừ pending150k, total còn50k; retry không trừ lại. |
| AC-F-011-04 | [F-011](04-detailed-feature-specs/F-011.md) | [P] REJECTED/CANCELLED trả available150k, tổng vẫn200k. |
| AC-F-011-05 | [F-011](04-detailed-feature-specs/F-011.md) | [P] Hai admin cùng claim/chuyển chỉ một tiến trình; unknown bank outcome không được trả tiền available tự động. |
| AC-F-012-01 | [F-012](04-detailed-feature-specs/F-012.md) | [C] Đơn1m, balance200k, point50 → earn950 khi complete. |
| AC-F-012-02 | [F-012](04-detailed-feature-specs/F-012.md) | [C] Phí giao20k không thay earn950 hoặc trần point50 trong ví dụ. |
| AC-F-012-03 | [F-012](04-detailed-feature-specs/F-012.md) | [C] Điểm không đổi thành tiền rút và không hết hạn bản đầu. |
| AC-F-012-04 | [F-012](04-detailed-feature-specs/F-012.md) | [P] Dùng điểm không vượt phần hàng còn sau balance và hạn mức, không chi trả phí giao. |
| AC-F-012-05 | [F-012](04-detailed-feature-specs/F-012.md) | [C] Đơn chọn50điểm đang hold bị hủy: release50 về available đúng một lần, không capture hoặc earn; sau complete RETURN captured points theo nguồn, không thu hồi ORDER_EARN D-100. |
| AC-F-012-06 | [F-012](04-detailed-feature-specs/F-012.md) | [C] Refund sau complete không thu hồi ORDER_EARN dù đã tiêu ở đơn khác; không tạo debt, không trừ cash để bù điểm. RETURN redeemed points giữ ledger riêng. |
| AC-F-012-07 | [F-012](04-detailed-feature-specs/F-012.md) | [C] Có100points, chọn50: place thành công available50/held50/total100; đơn khác chỉ dùng available50. |
| AC-F-012-08 | [F-012](04-detailed-feature-specs/F-012.md) | [C] Complete capture50held đúng một lần, available không giảm thêm; earned points là entry riêng chỉ phát sinh khi complete. |
| AC-F-012-09 | [F-012](04-detailed-feature-specs/F-012.md) | [C] Place/cancel/complete retry không hold/capture/release hai lần; quote chưa commit không hold, hold không thể rút thành tiền. |
| AC-F-013-01 | [F-013](04-detailed-feature-specs/F-013.md) | [C] Thiết kế có cả Zalo và push app; phone login chưa có không bỏ yêu cầu thông báo. |
| AC-F-013-02 | [F-013](04-detailed-feature-specs/F-013.md) | [P] Cùng event retry không tạo hai notification logic; gửi trùng do provider timeout được đánh dấu không khẳng định exactly-once mạng. |
| AC-F-013-03 | [F-013](04-detailed-feature-specs/F-013.md) | [P] Push denied/invalid token không chặn đặt đơn; cập nhật trạng thái gửi. |
| AC-F-013-04 | [F-013](04-detailed-feature-specs/F-013.md) | [P] Logout không để thiết bị nhận thông báo nhạy cảm user trước. |
| AC-F-013-05 | [F-013](04-detailed-feature-specs/F-013.md) | [P] Sửa/gửi lại notification không sửa trạng thái payment/order. |
| AC-F-014-01 | [F-014](04-detailed-feature-specs/F-014.md) | [C] Admin đổi trần % và VND cùng lúc; checkout áp mức thấp hơn. |
| AC-F-014-02 | [F-014](04-detailed-feature-specs/F-014.md) | [C] Giá trị ví dụ không tự trở thành production settings. |
| AC-F-014-03 | [F-014](04-detailed-feature-specs/F-014.md) | [P] Publish config invalid bị từ chối, có message từng field. |
| AC-F-014-04 | [F-014](04-detailed-feature-specs/F-014.md) | [P] Config update không thay shipping/pricing/points của order đã tạo. |
| AC-F-014-05 | [F-014](04-detailed-feature-specs/F-014.md) | [P] Không mở bán khi vùng/khung/ngân hàng và loyalty caps bắt buộc chưa được thiết lập. |
| AC-F-015-01 | [F-015](04-detailed-feature-specs/F-015.md) | [C] Trang bán phân biệt nguyên liệu cung cấp và gia vị khách tự chuẩn bị. |
| AC-F-015-02 | [F-015](04-detailed-feature-specs/F-015.md) | [C] Không yêu cầu module truy xuất nông trại trong R1. |
| AC-F-015-03 | [F-015](04-detailed-feature-specs/F-015.md) | [P] Nội dung nhúng script/file không hợp lệ bị từ chối hoặc sanitize. |
| AC-F-015-04 | [F-015](04-detailed-feature-specs/F-015.md) | [P] Ảnh thiếu không làm crash catalog, có placeholder và alt. |
| AC-F-015-05 | [F-015](04-detailed-feature-specs/F-015.md) | [P] Draft không lộ public, publish được kiểm tra quyền. |
| AC-F-016-01 | [F-016](04-detailed-feature-specs/F-016.md) | [C] Người chưa mua không tự gắn nhãn verified purchase. |
| AC-F-016-02 | [F-016](04-detailed-feature-specs/F-016.md) | [P] Dòng chưa complete hoặc của người khác bị từ chối review. |
| AC-F-016-03 | [F-016](04-detailed-feature-specs/F-016.md) | [P] Rating ngoài1..5 báo validation, output nội dung không chạy HTML/script. |
| AC-F-016-04 | [F-016](04-detailed-feature-specs/F-016.md) | [P] Review hidden không tính vào average công khai; lịch sử moderation còn audit. |
| AC-F-017-01 | [F-017](04-detailed-feature-specs/F-017.md) | [C] Không thưởng chỉ vì đăng ký/đặt chưa complete. |
| AC-F-017-02 | [F-017](04-detailed-feature-specs/F-017.md) | [C] Mức thưởng admin set và loại thưởng loyalty, không tiền rút. |
| AC-F-017-03 | [F-017](04-detailed-feature-specs/F-017.md) | [P] Complete retry hoặc hai job cùng chạy không thưởng hai lần cho một referred user. |
| AC-F-017-04 | [F-017](04-detailed-feature-specs/F-017.md) | [P] Self-referral bị từ chối; trùng email/phone không đủ để tự gộp/chặn khách hợp lệ. |
| AC-F-017-05 | [F-017](04-detailed-feature-specs/F-017.md) | [P] Reward preview cho cả hai bên rõ mức/điều kiện trước khi enable chiến dịch. |
| AC-F-018-01 | [F-018](04-detailed-feature-specs/F-018.md) | [C] Mua lại dùng thao tác mới, không sửa đơn cũ. |
| AC-F-018-02 | [F-018](04-detailed-feature-specs/F-018.md) | [P] Variant tắt/không còn có cảnh báo, không tự thay sản phẩm. |
| AC-F-018-03 | [F-018](04-detailed-feature-specs/F-018.md) | [P] Giá mới hiển thị và khách xác nhận; không giữ giá cũ trái catalog mới. |
| AC-F-018-04 | [F-018](04-detailed-feature-specs/F-018.md) | [P] Giỏ có sẵn không bị xóa âm thầm. |
| AC-F-019-01 | [F-019](04-detailed-feature-specs/F-019.md) | [C] Có lối vào món thường mua ở web/app. |
| AC-F-019-02 | [F-019](04-detailed-feature-specs/F-019.md) | [P] Khách mới thấy empty state dẫn catalog. |
| AC-F-019-03 | [F-019](04-detailed-feature-specs/F-019.md) | [P] Đơn hủy không làm tăng completed_count. |
| AC-F-019-04 | [F-019](04-detailed-feature-specs/F-019.md) | [P] Variant thay giá/hết bán cập nhật thông tin trước thêm giỏ. |
| AC-F-020-01 | [F-020](04-detailed-feature-specs/F-020.md) | [C] Chỉ nhắc qua kênh khách đồng ý nhận. |
| AC-F-020-02 | [F-020](04-detailed-feature-specs/F-020.md) | [P] Tắt consent sau enqueue nhưng trước gửi thì không gửi. |
| AC-F-020-03 | [F-020](04-detailed-feature-specs/F-020.md) | [P] Retry scheduler không tạo nhắc logic trùng cùng ngày/kênh. |
| AC-F-020-04 | [F-020](04-detailed-feature-specs/F-020.md) | [P] Job chạy sau22h bỏ nhắc của đợt đó, không đổi ngày giao hoặc trạng thái đơn. |
| AC-F-021-01 | [F-021](04-detailed-feature-specs/F-021.md) | [C] Cancel ngay trước cutoff được, đúng cutoff bị khóa. |
| AC-F-021-02 | [F-021](04-detailed-feature-specs/F-021.md) | [C] Thiếu nguyên liệu ngày mua không tự thay/hủy toàn bộ khi chưa thỏa thuận. |
| AC-F-021-03 | [F-021](04-detailed-feature-specs/F-021.md) | [C] Full refund đã dùng 50 point trả 50 point, không đổi thành50k withdrawable. |
| AC-F-021-04 | [F-021](04-detailed-feature-specs/F-021.md) | [P] Tổng cash/points hoàn nhiều lần không vượt nguồn thật đã thu/dùng; excess receipt hoàn riêng, không vừa hoàn vừa match lại. |
| AC-F-021-05 | [F-021](04-detailed-feature-specs/F-021.md) | [P] Bank refund pending không hiện settled; retry settle không double-credit/debit. |
| AC-F-021-06 | [F-021](04-detailed-feature-specs/F-021.md) | [C] Partial/full sau complete giữ nguyên ORDER_EARN đã cấp theo D-100; tiền/điểm thanh toán hoàn theo nguồn, preview/audit không tạo clawback. |
| AC-F-021-07 | [F-021](04-detailed-feature-specs/F-021.md) | [C] Admin hủy vận hành đơn không thực hiện được: CANCELLED có actor/reason, release held points một lần, hoàn tiền thực đã nhận/áp theo thỏa thuận, không earn. Customer cutoff guard vẫn nguyên. |
| AC-F-021-08 | [F-021](04-detailed-feature-specs/F-021.md) | [C] Before complete RELEASE cash/points còn hold, không duplicate credit bằng refund leg; after complete chỉ hoàn nguồn đã capture/thực thu, giữ nguyên ORDER_EARN đã cấp. |

## QA scenario matrix

| Scenario | Features | Kích hoạt | Kỳ vọng | Layer | Policy |
| --- | --- | --- | --- | --- | --- |
| QA-001 | F-001 | Google/FB/Apple trên web/iOS/Android; login lại và link | Cùng user TPX khi đã link; email thiếu/ẩn không làm lỗi; giữ đơn/ví/điểm | Contract + thiết bị thật | C/technical |
| QA-002 | F-001/F-009 | Token giả, project sai, session revoked, customer vào admin | 401/403/404 phù hợp, không lộ dữ liệu; không tự tạo role | API security | C/technical |
| QA-003 | F-001 | SĐT checkout chưa OTP; link phone về sau | Mua được không SMS OTP; không dùng contact làm login identity | API/E2E | C/technical |
| QA-004 | F-002/F-003 | Chọn variant/khẩu phần, gói RAW+MEAL | Giá/pack/BOM đúng, không gia vị/sốt, chung giỏ và order | Web/app E2E | C/technical |
| QA-005 | F-002/F-003 | Tắt ingredient giữa xem và checkout; bật lại manual-off meal | Checkout reject, order cũ giữ; bật lại không vượt manual-off | Domain/API | P-007 |
| QA-006 | F-003/F-006 | Sửa recipe sau order tương lai; gom mua | Dùng BOM snapshot order, không version catalog mới | DB integration | P-007 |
| QA-007 | F-004/F-012 | G1m/F0/A200k/cap5%/đủ points, opt-in | B200k/P50/T750k, complete earn950 | Domain + E2E | C/technical |
| QA-008 | F-004/F-012 | Thêm F20k hoặc opt-out | F20k→T770k/earn950; opt-out→P0/T820k/earn1000 | Domain | C/technical |
| QA-009 | F-004/F-012 | Balance đủ hoặc gần đủ đơn | Không âm T/không tiêu điểm dư/không giảm phí bằng điểm | Domain/property checks | P-005 |
| QA-010 | F-004 | Quote đổi giá/config/date/account sau tính | 409 và không tạo order/debit nửa chừng, requote cần xác nhận | API/DB | P-001/P-009 |
| QA-011 | F-004 | Double click, mất response, retry cùng key hoặc key khác body | Một order/funding/ledger; mismatch409, đọc lại resource | DB integration/E2E | P-001 |
| QA-012 | F-004/F-011 | Hai checkout/rút dùng cùng available và points | Không double spend, account không âm, request thua được quote lại | Concurrent DB integration | P-001/P-002 |
| QA-013 | F-008/F-021 | 21:59:59→22:00; thiết bị sai giờ; job cutoff chậm | Trước/sau22h đúng earliest/cancel guard tại server | Clock-controlled domain/API | C/technical |
| QA-014 | F-008 | Ngày21/10 chọn22..28 trước22h,23..28 từ22h | Không29/10; cutoff theo delivery D−1; vùng/slot active | Domain/API | C/technical |
| QA-015 | F-005 | Khách báo đã chuyển, admin nhận thiếu/thừa/duplicate | Notice không PAID; partial đúng, excess case; không credit lần hai | API/DB | P-001/P-006 |
| QA-016 | F-005/F-006 | Unpaid tại cutoff được admin duyệt mua | Included có actor/reason/quyền; funding vẫn thiếu | API/admin E2E | C/technical |
| QA-017 | F-006 | Batch build retry/restart và quyết định tay trước đó | Không nhân đôi quantities/order; giữ manual decision, trace sources | Worker/DB | P-006/P-007 |
| QA-018 | F-006/F-007 | RAW 500g×2 + MEAL cần300g cùng ingredient | Tổng 1300g base; không cộng500g với0.3kg như khác đơn vị | Domain/DB | P-007 |
| QA-019 | F-007/F-021 | Thiếu/không đạt/giao lỗi | Mở case, không tự thay/charge/refund/cancel; cần agreement | Admin/customer E2E | C/technical |
| QA-020 | F-007/F-012/F-017 | Complete retry và hai worker referral đồng thời | Một earned entry/referral qualifying reward; không reopen để earn | Concurrent DB integration | P-006/P-008 |
| QA-021 | F-009 | Fixed admin password không OTP, disable account/role change | Login đúng; action quyền bị thu hồi không tiếp tục qua cache | Security/E2E | C/technical |
| QA-022 | F-010/F-011 | Ví200k/rút150k, checkout sau đó | Available50k/pending150k/total200k; chỉ50k dùng được | Domain/API | C/technical |
| QA-023 | F-011 | Approve rồi paid, retry paid; reject/cancel | Approve không giảm total; paid pending0/total50k; reject/cancel trả available đúng1 lần | DB integration | P-002 |
| QA-024 | F-011 | Hai admin claim chuyển, timeout khi bank đã gửi | Một PROCESSING claim; không auto-release/chuyển lại khi chưa đối soát | Concurrent API/manual checklist | P-002 |
| QA-025 | F-010 | Admin credit adjustment retry, không gắn order/không quyền | Một credit có reference; thiếu adjustment/quyền bị chặn | API/DB | C/technical |
| QA-026 | F-012 | Earn12.999/999 eligible; refund trước complete | Earn12/0; chỉ tính phần còn eligible sau refund | Domain | P-003 phần refund |
| QA-027 | F-012/F-021 | Full refund G1m/point50/earn950 đã cấp, kể cả đã tiêu earn | Return50captured points, giữ950earned, không debt/clawback; cash theo nguồn | Domain/DB | C D-100 |
| QA-028 | F-021 | Partial nhiều lần + hai refund song song + bank leg pending | Cumulative không vượt source, pending giữ cap, không làm tròn lặp sai | Concurrent DB integration | P-003 |
| QA-029 | F-021/F-012 | Refund sau khi points earned đã tiêu | Debt projection/offset minh bạch, không trừ cash; chỉ khi P-004 được duyệt | Domain/DB | P-004 |
| QA-030 | F-021/F-005 | Bank receipt đến sau cancel/excluded | Unmatched/case; không auto mua lại/ghi thu hộ lần hai | API/DB | P-006 |
| QA-031 | F-013 | Firebase/Zalo/push unavailable, token invalid, logout/switch user | Fail/skip đúng; không rollback order; không gửi dữ liệu user cũ | Provider contract + thiết bị thật | C/technical |
| QA-032 | F-014 | Settings cap%,VND,minimum/fee đổi sau quote/order | Quote revalidate; order snapshot không đổi; invalid config reject | API/DB | P-009 |
| QA-033 | F-015 | Upload MIME/size sai, script trong content, draft | Reject/sanitize; draft không public; nguồn ảnh/hướng dẫn rõ | API/security | C/technical |
| QA-034 | F-016 | Review không mua, chưa complete, review lặp, hidden | Không forged verified; unique, published-only aggregate | API/DB | P-010 |
| QA-035 | F-017 | Referral register-only/self/duplicate first-complete/full refund | Không thưởng sớm/self; reward once theo config; reversal theo P-006 | Domain/worker | P-006 |
| QA-036 | F-018/F-019 | Reorder giỏ có sẵn, đổi giá/hết variant; frequent khách mới | Preview/confirm; không mất giỏ/đặt đơn ngầm; empty state rõ | Web/app E2E | P-010 |
| QA-037 | F-020 | Unsubscribe sau enqueue; job gửi trễ22h; provider cấm template | Skip theo consent/cutoff/policy, không fallback SMS/marketing trái consent | Worker/contract | P-010 |
| QA-038 | F-009/F-014 | Báo cáo cash/GMV/wallet liability/cost thiếu | Không cộng pending2 lần hoặc balance applied thành cash-in; incomplete cost có nhãn | Query integration | P-010 |
| QA-039 | F-001/F-009 | Browser cookie/CSRF, bearer mobile, session rotation | CSRF/Origin và audience guard; replay refresh bị chặn, không token log | Security integration | P-011 |
| QA-040 | F-004/F-010/F-011/F-012/F-021 | DB fail, lock deadlock, Redis restart, worker retry | Không partial money; bounded retry; outbox recover; account projections reconcile | Fault-injection DB/worker | C/technical |
| QA-041 | F-001/F-010 | Deletion request khi còn order/pending withdrawals | Không xóa ledger hoặc nghĩa vụ; anonymization sau resolution theo policy | API/privacy | P-011 |
| QA-042 | F-009/F-014 | Backup→restore, migration dry-run, load profile | Restore đọc được ledger/order, projection khớp; benchmark target trước release | Ops/staging | P-012 |

## Nghiệm thu phi chức năng

NFR-001–018 tại [NFR](14-non-functional-requirements.md) là phần release criteria. Performance/backup/session targets là proposal, không là test đã pass. Mỗi platform cần smoke và critical E2E; social providers/push phải test thật trước release.

Chưa có implementation nên các tiêu chí và QA trên là **test specification**, không phải kết quả kiểm thử sản phẩm. Kết quả kiểm tra hiện tại chỉ xác nhận tính nhất quán tài liệu, tham chiếu và ví dụ số học.
