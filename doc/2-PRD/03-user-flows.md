# User Flows

> PRD v0.1 — Draft review. Phương án [P] tại [review register](11-review-decisions.md); guard và trạng thái tại [domain states](12-domain-states.md).

## UF-001 — Đăng nhập và liên kết tài khoản

- Features: F-001.
- Luồng thành công: Đăng nhập Google/Facebook/Apple qua Firebase → backend xác minh → tạo hoặc trả user/phiên TPX → phục hồi giỏ và trang đang xem. Trong tài khoản, xác thực lại trước khi liên kết provider mới.
- Lỗi/ngoại lệ: Token sai project/hết hạn, người dùng đóng luồng, identity đã thuộc tài khoản khác hoặc gỡ phương thức cuối. Không gộp user chỉ do trùng email/SĐT.
- Kết quả/bất biến: User ID ổn định; giữ đơn hàng, số dư và loyalty. SĐT liên hệ chưa OTP không trở thành identity đăng nhập.
- Liên quan: [screens](02-screen-inventory.md), [routes](05-route-map.md), [API contracts](06-api-contract-map.md).

## UF-002 — Chọn nguyên liệu thô

- Features: F-002/F-004.
- Luồng thành công: Trang chủ/danh mục/tìm kiếm → xem sản phẩm → chọn quy cách và số gói → thêm vào giỏ.
- Lỗi/ngoại lệ: Hàng đang tắt bán, giá đổi hoặc số lượng không hợp lệ: hiển thị lý do và yêu cầu xử lý, không tự thay sản phẩm.
- Kết quả/bất biến: Giỏ chung chứa lựa chọn RAW theo catalog hiện tại.
- Liên quan: [screens](02-screen-inventory.md), [routes](05-route-map.md), [API contracts](06-api-contract-map.md).

## UF-003 — Chọn món sơ chế

- Features: F-003/F-004.
- Luồng thành công: Danh sách món → xem nguyên liệu chính/hướng dẫn nấu → chọn khẩu phần và giá gói → thêm vào giỏ chung.
- Lỗi/ngoại lệ: Tắt một nguyên liệu làm món liên quan không nhận đặt mới; không tự hủy đơn đã có.
- Kết quả/bất biến: Đúng BOM theo khẩu phần; gói không gồm gia vị/nước sốt, khách không sửa thành phần.
- Liên quan: [screens](02-screen-inventory.md), [routes](05-route-map.md), [API contracts](06-api-contract-map.md).

## UF-004 — Checkout và đặt đơn

- Features: F-004/F-005/F-008/F-012.
- Luồng thành công: Đăng nhập → nhập địa chỉ/SĐT nhận hàng → chọn ngày/khung → xem báo giá → tự áp available, chọn dùng điểm → xác nhận → tạo đơn và HOLD points trong transaction → màn đơn/thanh toán; CAPTURE points chỉ khi complete D-093.
- Lỗi/ngoại lệ: Báo giá hết hạn, giá/cấu hình thay đổi, qua cutoff, vùng tắt hoặc số dư vừa được dùng: rollback toàn bộ và báo giá lại. Mất phản hồi sau commit thì tra key/order trước khi gửi lại.
- Kết quả/bất biến: Một đơn và một lần giao cho hai nhóm; chưa báo đủ tiền nếu vẫn còn phần cần chuyển khoản.
- Liên quan: [screens](02-screen-inventory.md), [routes](05-route-map.md), [API contracts](06-api-contract-map.md).

## UF-005 — Chuyển khoản

- Features: F-005.
- Luồng thành công: Khách xem ngân hàng, nội dung và số tiền phải chuyển → chuyển ngay → báo đã chuyển [P] → admin đối soát → ghi tiền thực nhận/phân bổ → đủ nguồn mới FUNDED.
- Lỗi/ngoại lệ: Tiền thiếu/thừa, tham chiếu trùng hoặc tiền đến muộn: mở case/phần chưa phân bổ; không tự nạp ví hay đưa lại vào mua.
- Kết quả/bất biến: Receipt thực tế, nguồn nội bộ và quyết định thu mua luôn tách biệt.
- Liên quan: [screens](02-screen-inventory.md), [routes](05-route-map.md), [API contracts](06-api-contract-map.md).

## UF-006 — Cutoff và mua hàng

- Features: F-006/F-008.
- Luồng thành công: 22h ngày D−1: API khóa hủy → batch ngày D → đơn đủ tiền và quyết định thủ công cho đơn chưa trả → gom RAW/BOM snapshot → mua/nhận → ghi lượng, giá vốn, chất lượng và thiếu hàng.
- Lỗi/ngoại lệ: Job chậm/restart không mở lại quyền hủy. Đơn chưa trả chưa được duyệt không tự đưa đi mua. Thiếu hoặc không đạt phải mở case.
- Kết quả/bất biến: Tổng nhu cầu truy về từng đơn/dòng; giá vốn không đổi giá bán đã chốt.
- Liên quan: [screens](02-screen-inventory.md), [routes](05-route-map.md), [API contracts](06-api-contract-map.md).

## UF-007 — Sơ chế, đóng gói, giao và hoàn thành

- Features: F-007/F-012/F-017.
- Luồng thành công: Nhận hàng → làm sạch/cắt/chia → đóng gói → sẵn sàng → TPX giao → ghi nhận giao thành công → hoàn thành → tích điểm và xét referral một lần.
- Lỗi/ngoại lệ: Case hàng chưa thống nhất có thể chặn; refund bank pending không tự chặn phần hàng đã thống nhất D-097. Admin quyết định giao thiếu tiền D-095, không mandatory fully-funded dispatch; complete-unpaid OQ-050. Giao lỗi tạo case, không tự hoàn tiền, giao lại hoặc thu thêm phí.
- Kết quả/bất biến: Tiến trình rõ; không chuyển đi chuyển lại COMPLETED để tích điểm thêm.
- Liên quan: [screens](02-screen-inventory.md), [routes](05-route-map.md), [API contracts](06-api-contract-map.md).

## UF-008 — Hủy trước cutoff

- Features: F-021.
- Luồng thành công: Chi tiết đơn → API trả quyền hủy → xem ảnh hưởng tiền/điểm → gửi cancel với version → CANCELLED → RELEASE held points theo D-094, cash xử lý theo policy được chốt ở OQ-048 và lập phương án hoàn tiền đã nhận qua ngân hàng.
- Lỗi/ngoại lệ: Đúng 22h, đơn terminal hoặc version đã đổi bị từ chối. Giờ máy khách không quyết định quyền hủy.
- Kết quả/bất biến: Không hoàn hai lần; không tự chuyển ngân hàng; đơn đã hủy không còn được mua.
- Liên quan: [screens](02-screen-inventory.md), [routes](05-route-map.md), [API contracts](06-api-contract-map.md).

## UF-009 — Yêu cầu rút số dư

- Features: F-010/F-011.
- Luồng thành công: Xem available → nhập số tiền và tài khoản ngân hàng → tạo yêu cầu, chuyển available sang pending atomically → admin duyệt → nhận xử lý chuyển → chuyển ngân hàng → xác nhận đã chuyển có tham chiếu.
- Lỗi/ngoại lệ: Hủy/từ chối chỉ ở trạng thái cho phép P-002. Đang PROCESSING hoặc chưa rõ ngân hàng có chuyển chưa thì giữ pending; checkout cạnh tranh không tiêu được khoản này.
- Kết quả/bất biến: Ví 200k, rút 150k chỉ còn 50k mua hàng. Duyệt chưa giảm tổng; PAID mới giảm pending và tổng.
- Liên quan: [screens](02-screen-inventory.md), [routes](05-route-map.md), [API contracts](06-api-contract-map.md).

## UF-010 — Thiếu hàng, đổi món và hoàn một phần

- Features: F-021/F-012.
- Luồng thành công: Case ghi dòng bị ảnh hưởng → trao đổi khách → lưu phương án/split đã đồng ý → preview nguồn còn hoàn và hold-release/captured-return → xác nhận → từng phần tiền/điểm thực hiện nội bộ hoặc ngân hàng PROCESSING → SETTLED.
- Lỗi/ngoại lệ: Chưa có đồng ý thì không thay hàng. Hoàn vượt nguồn/cạnh tranh bị chặn. Ngân hàng chưa rõ kết quả giữ claim/cap. Earn đã tiêu khi hoàn sau complete cần OQ-049; không triển khai debt_points như policy đã duyệt.
- Kết quả/bất biến: Hoàn tiền theo thỏa thuận, điểm bằng điểm; giữ nguyên ORDER_EARN đã thưởng D-100, không sửa snapshot gốc.
- Liên quan: [screens](02-screen-inventory.md), [routes](05-route-map.md), [API contracts](06-api-contract-map.md).

## UF-011 — Referral, mua lại và thường mua

- Features: F-017/F-018/F-019.
- Luồng thành công: Mã/link referral → kiểm tra điều kiện P-006 → đơn đầu hoàn thành → thưởng đúng setting một lần. Mua lại/thường mua → preview giá và khả dụng hiện tại → giỏ mới → checkout mới.
- Lỗi/ngoại lệ: Tự giới thiệu, ghi nhận muộn, hoàn thành trùng; hàng cũ tắt/giá đổi hoặc giỏ đang có dữ liệu cần xử lý rõ.
- Kết quả/bất biến: Không tự đặt/thu tiền, không đổi lịch sử đơn cũ; reward không rút thành tiền.
- Liên quan: [screens](02-screen-inventory.md), [routes](05-route-map.md), [API contracts](06-api-contract-map.md).

## UF-012 — Đánh giá, thông báo và nhắc đặt

- Features: F-013/F-016/F-020.
- Luồng thành công: Dòng hoàn thành → gửi đánh giá → kiểm duyệt P-010 → công khai. Domain commit outbox → notification/attempt → Zalo/push → deep link có xác thực. Nhắc đặt kiểm tra lại đồng ý trước gửi và trước cutoff.
- Lỗi/ngoại lệ: Provider lỗi, quyền push bị từ chối, khách tắt đồng ý, token thuộc user trước hoặc job trễ: ghi fail/skip đúng, không rollback đơn hoặc tự gửi kênh khác.
- Kết quả/bất biến: Verified purchase từ DB; đồng ý marketing tách quyền OS; payload không lộ dữ liệu riêng.
- Liên quan: [screens](02-screen-inventory.md), [routes](05-route-map.md), [API contracts](06-api-contract-map.md).

## UF-013 — Quản trị và thay settings

- Features: F-009/F-014/F-015.
- Luồng thành công: Tài khoản cố định/mật khẩu → kiểm tra quyền → màn được phép → sửa draft → validate/publish version cấu hình/catalog/nội dung → audit → chỉ ảnh hưởng báo giá mới.
- Lỗi/ngoại lệ: 401/403, quyền đã thu hồi, version conflict, thiếu cấu hình hoặc nội dung không hợp lệ.
- Kết quả/bất biến: Không OTP admin, không đăng ký công khai; settings mới không sửa lại tiền/trạng thái đơn cũ.
- Liên quan: [screens](02-screen-inventory.md), [routes](05-route-map.md), [API contracts](06-api-contract-map.md).

## Thay đổi ngày/cutoff xuyên thiết bị

Khách mở checkout 21:59 nhưng xác nhận 22:00: backend từ chối ngày mai/báo giá cũ nếu không còn hợp lệ. Đơn giao xa giữ cutoff 22h trước ngày giao, không khóa ngay tối đặt. App trở lại sau khi chuyển khoản phải lấy trạng thái tiền mới; thao tác Back không gửi đơn mới.

## Mất phản hồi sau thao tác ngân hàng

Nếu admin đã chuyển tiền nhưng lưu kết quả bị timeout, không chuyển lại hoặc giải phóng pending. Tra request/state/reference và đối soát trước khi xác nhận PAID. Màn thành công chỉ phản ánh command đã commit; không chứng minh ngân hàng đã chuyển nếu chưa ghi nhận thực tế.

## Bổ sung audit ngày 2026-10-21

13 UF là core flows, không đủ chứng minh toàn bộ action/recovery. [Audit](../4-DESIGN/12-flow-audit.md) bổ sung25[Journeys](../4-DESIGN/13-detailed-journeys.md) và100[cases](../4-DESIGN/14-flow-case-matrix.md), giữ Screen/Feature IDs. Xem P-013–019 cho các branch chưa chốt; đọc [action gaps](../4-DESIGN/15-action-contract-gaps.md) trước khi implement controls chưa có contract.


Nguồn review mới nhất: [vòng1](16-review-round-1.md) ngày2026-10-25; các mô tả cũ phải đọc với HOLD/CAPTURE/RELEASE, admin cancel và admin quyết định giao, không tự suy ra cash hold/debit.
