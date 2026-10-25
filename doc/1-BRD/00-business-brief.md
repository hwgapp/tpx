# Business Brief

> Draft cập nhật ngày 2026-10-21; chưa freeze BRD. Nguồn: `01-decision-log.md`, D-001–D-088. Mốc hiện hành 22:00; COD hoãn khỏi bản đầu.

## Tóm Tắt

Thực phẩm xanh (TPX) là platform thương mại điện tử thực phẩm tươi, gồm rau, củ, quả, thịt, cá, trứng. TPX trực tiếp bán, nhận đơn hằng ngày, gom đơn mỗi tối để mua tại chợ đầu mối và giao hôm sau. Thử nghiệm tại các quận nội thành TP.HCM với kỳ vọng vài chục đơn/ngày; vùng giao cụ thể và ngày ra mắt chưa chốt.

## Vấn Đề

Giá trị user muốn cung cấp là thực phẩm giá tốt, tươi ngon và chất lượng đảm bảo. Nhu cầu cụ thể và tiêu chuẩn đánh giá chất lượng còn cần làm rõ với user.

## Giải Pháp

Hai nhóm mua hàng: **nguyên liệu thô** chọn từ catalog TPX theo quy cách/số lượng và **nguyên liệu đã sơ chế theo món** chọn món/khẩu phần có giá đặt sẵn. Hai nhóm dùng chung giỏ, một đơn và cùng lần giao (D-052, D-058–D-061).

TPX tự đi mua, tập kết về một điểm, sơ chế và tự giao. Sơ chế chỉ làm sạch, cắt/chia sẵn nguyên liệu chính; ban đầu không có gia vị/nước sốt. Món có hướng dẫn nấu, thực đơn cố định và tắt món/nguyên liệu khi thị trường hết. User đang tìm nguồn crawl menu/hướng dẫn, chưa giao thực hiện crawler.

Chốt 22:00; trước mốc sớm nhất giao hôm sau, sau mốc sớm nhất ngày hôm sau nữa. Khách được đặt trước tối đa 7 ngày. Giao ngày D thì chốt mua và khóa hủy lúc 22:00 ngày D−1, theo Asia/Ho_Chi_Minh. Nếu đến ngày mua thiếu nguyên liệu thì hoàn theo thỏa thuận. Khách chọn khung giao, không quota số đơn mỗi khung. Giá bán được đặt trước và không đổi theo giá chợ đối với đơn đã đặt.

## User Chính

Gia đình, người đi làm và có thể thêm nhà hàng/quán ăn dùng chung flow, chưa có luồng B2B/giá sỉ riêng. Khách bản đầu Google/Facebook/Apple; phone + OTP sau. Một số admin cố định user tạo, tài khoản/mật khẩu không OTP, giữ nền RBAC (D-086–088).

## Giá Trị Khác Biệt

Thông tin hàng hóa/quy trình minh bạch, đánh giá từ khách đã mua; giới thiệu bạn bè với ưu đãi khách mới và thưởng sau đơn đầu hoàn thành; mua lại đơn, món thường mua và nhắc đặt trên kênh khách đồng ý nhận. Các điều kiện/phần thưởng cụ thể chưa chốt (D-053–D-055).

Định hướng: gom nhu cầu để giảm giá thành và cung cấp hàng tươi. Hiệu quả chi phí và tiêu chí chất lượng chưa được kiểm chứng. Câu chuyện nông trại được user hoãn để tính sau.

Thông báo qua Zalo và push app. Số dư tiền hoàn không hết hạn, không tự nạp; admin cộng khi điều chỉnh đơn. Khách yêu cầu rút ngân hàng, admin duyệt/chuyển hoàn; tiền yêu cầu rút sang pending, chỉ available được dùng mua hàng. Thứ tự: số dư available -> điểm trong hạn mức nếu chọn -> chuyển khoản phần còn lại. Món tự tắt theo nguyên liệu; referral thưởng điểm settings. Lifecycle xử lý yêu cầu rút cần đặc tả ở PRD.

Loyalty từ bản đầu: 1.000đ giá trị thanh toán sau cùng tích 1 điểm khi đơn hoàn thành, chưa hết hạn; dùng 1 điểm giảm 1.000đ trong hạn mức và không rút điểm thành tiền. Khách chọn dùng sau tiền hoàn; admin cấu hình trần phần trăm và tiền. Ví dụ đơn 1.000.000đ với trần 5% dùng tối đa 50 điểm. Các tỷ lệ/trần ví dụ chưa phải mặc định. Trần % tính trên tiền hàng sau giảm giá, không phí giao, trước trừ số dư. Tích điểm trên tiền hàng sau giảm giá và trừ điểm đã dùng; phần trả bằng số dư vẫn tích, phí giao không tích, làm tròn xuống mỗi 1.000đ. Hoàn phần điểm bằng điểm, phần tiền theo thỏa thuận; hoàn sau hoàn thành thu hồi điểm đã tích tương ứng phần hoàn (D-081–085).

## Business Model

Doanh thu từ chênh lệch mua-bán; mức giá/biên lợi nhuận mục tiêu chưa chốt. Khách thanh toán ngay khi đặt, kể cả đơn tương lai; phần thực trả chuyển khoản được nhân viên xác nhận, không COD. Nhân viên có quyền admin cấp được quyết thủ công ngoại lệ mua đơn chưa thanh toán; duyệt mua không ghi thành đã thu tiền. Thời gian chờ/xác nhận còn mở, đối soát tự động để sau. Phí giao/đơn tối thiểu cấu hình admin. Hủy được trước cutoff đợt mua của đơn; sau cutoff khóa hủy. Hoàn theo thỏa thuận, giao thất bại do vận hành trao đổi quyết định. Mapping cutoff đã chốt D-080; lifecycle tài chính, phân bổ hoàn một phần và trường hợp điểm đã dùng cần đặc tả ở PRD.
