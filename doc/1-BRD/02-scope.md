# Scope

> Draft từ các yêu cầu đã nhận; chưa freeze BRD. Nguồn: `01-decision-log.md`. Các câu hỏi còn mở nằm trong `../0-INBOX/04-open-questions.md`.

## In Scope - Phase 1

- iOS, Android, Web app, Admin/CMS và Backend/API; backend Node.js modular.
- TPX trực tiếp bán rau, củ, quả, thịt, cá, trứng; ra mắt tại nội thành TP.HCM.
- Hai nhóm dùng chung giỏ, một đơn và lần giao: nguyên liệu thô chọn catalog theo quy cách/số lượng; món sơ chế chọn món/khẩu phần có giá TPX đặt sẵn.
- Catalog có giá bán đặt trước và quy cách theo sản phẩm cho khách chọn.
- Cho đặt trước tối đa 7 ngày; ngày giao sớm nhất theo cutoff 22:00. Giao ngày D chốt mua/khóa hủy lúc 22:00 ngày D−1; thiếu nguyên liệu ngày mua thì hoàn theo thỏa thuận.
- Món sơ chế chỉ làm sạch, cắt/chia sẵn, chỉ nguyên liệu chính; có hướng dẫn nấu. Thực đơn cố định và có thao tác tắt món/nguyên liệu khi hết thị trường.
- Khách chọn khung giao, TPX tự điều phối; không giới hạn số đơn mỗi khung.
- Khách thanh toán ngay khi đặt, cả đơn tương lai; bản đầu chuyển khoản được nhân viên xác nhận, chưa COD.
- Admin cấp quyền để nhân viên quyết thủ công ngoại lệ mua/loại đơn chưa thanh toán.
- Admin settings phí giao và đơn tối thiểu.
- TPX tự mua, tập kết một điểm, sơ chế và giao; hoàn tiền theo thỏa thuận; giao không thành công do vận hành trao đổi với khách để quyết định.
- Khách hủy được trước cutoff đợt mua tương ứng đơn, kể cả đặt trước nhiều ngày; khóa hủy sau cutoff; hoàn theo thỏa thuận.
- Khách cá nhân và nhà hàng/quán ăn dùng chung flow mua hàng hiện tại.
- Khách bản đầu Google/Facebook/Apple; phone + OTP sau.
- Một số account admin cố định user tạo, tài khoản/mật khẩu không OTP; giữ nền RBAC.
- Thông báo qua Zalo và push trên app; chưa chọn dịch vụ tích hợp.
- Quản lý số dư cho hoàn tiền và sử dụng ở đơn sau: ưu tiên tự động dùng, không hết hạn; admin được thêm số dư khi điều chỉnh đơn.
- Khách tạo yêu cầu rút hoàn ngân hàng: khoản yêu cầu sang pending, chỉ phần available dùng mua hàng; bản đầu admin duyệt/chuyển hoàn. Lifecycle và SLA cần đặc tả.
- Thứ tự thanh toán: số dư tiền hoàn trước, điểm trong hạn mức nếu khách chọn, chuyển khoản phần còn lại.
- Món liên kết nguyên liệu và tự tắt bán khi nguyên liệu tắt. Thưởng referral bằng loyalty, mức điểm settings.
- Loyalty ngay bản đầu: 1.000đ giá trị thanh toán cuối tích 1 điểm khi hoàn thành; dùng 1 điểm giảm 1.000đ; không rút điểm ra tiền, tạm không hết hạn. Khách chọn dùng; admin set trần phần trăm và tiền. Công thức chi tiết và hoàn/hủy cần đặc tả.

- Thông tin minh bạch/đánh giá từ khách đã mua; referral; mua lại đơn, món thường mua và nhắc đặt qua kênh khách đồng ý nhận. Điều kiện, phần thưởng và thao tác chi tiết cần đặc tả (D-053–D-055).

## Out Of Scope - Phase 1

- COD, duyệt khách COD và tự mở COD theo rule: tạm thời chưa làm ở giai đoạn đầu.
- Tự động đối soát chuyển khoản: user đã để sau.
- Quota số đơn theo khung giao: user xác nhận không cần.
- Nhà bán khác tự đăng bán: mô hình hiện tại TPX tự bán toàn bộ.
- Khách chủ động nạp tiền vào số dư: user xác nhận không có.
- Cung cấp gia vị/nước sốt hoặc tẩm ướp trong gói món sơ chế: chưa có ở bản đầu.

## Later Phases

- Phone login + OTP khi dịch vụ sẵn sàng.

- Đối soát chuyển khoản tự động.
- COD và các quy tắc duyệt: đánh giá lại khi mở giai đoạn sau.
- Câu chuyện truyền thông nông trại: để tính sau; chưa chốt nội dung hoặc yêu cầu truy xuất.

## Hạng Mục Vận Hành

- Tiếp cận các cụm chung cư/khu dân cư trong vùng thử nghiệm.
- Chọn ưu đãi mua thử, ngưỡng hỗ trợ phí giao và ngân sách thu hút khách.
- Sản xuất nội dung thực tế về hàng hóa và hoạt động TPX.
- Các con số ưu đãi được đề xuất trước chỉ là ví dụ, chưa thành cấu hình mặc định hoặc yêu cầu phần mềm được chốt.

## Non-Goals

- Chưa chốt thêm ngoài các giới hạn trên; không coi mong muốn “bản đầy đủ” là cho phép tự thêm tính năng chưa được trao đổi.
