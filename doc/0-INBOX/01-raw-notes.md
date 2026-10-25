# Raw Notes

Ghi nhanh ý tưởng, yêu cầu thô, link tham khảo, đối thủ, ghi chú họp.

Không cần format đẹp. Khi đủ thông tin, Codex sẽ tổng hợp sang BRD/PRD.

## 2026-10-20 — Câu trả lời G0 của user (nguyên văn)

> 1. mình muốn làm 1 platform thương mại điện tử, có app web, với các sản phẩm rau củ qua, thịt cá trứng,  sẽ kể câu chuyện truyền thông sản phẩm được lấy từ nông trại, hình thức khác hàng đặt, mỗi tối sẽ gom đơn đi mua ở chợ đầu mối -> giúp giảm giá thành, hàng tươi ngon dẳm báo
> 2. thương mại điện tử
> 3. A,B,C,D,E
> 4. làm bản đầy đủ dùng được
> 5. bán hàng, doanh thu từ việc chênh lệch mua đi bán lại
> 6. back-end nodejs modular đầy đủ

## 2026-10-20 — Tên dự án (nguyên văn)

> tên dự án là Thực phẩm xanh
> viết tắt nếu có TPX

## 2026-10-20 — Câu trả lời vận hành G1 (nguyên văn)

> 1. ra mắt ở các quận nội thành HCM
> 2. khách hàng: gia định, người đi làm, cũng có thể là nhà hàng quán ăn
> 3. A, tự bán
> 4. đặt hằng ngày
> 5. giao hôm sau
> 6. TPX tự đi mua, giao hàng, tập kết về một điểm, sơ chế xong hôm sau giao
> 7. thiếu hàng hoặc ko đạt -> trao đổi với khách về việc hoàn tiền, hoặc mua lại món khác
> 8. câu chuyện nông trại chắc tính sau
> 9. thanh toán chuyển khoản, thu trước, khi nào khách quen mới cho COD

## 2026-10-20 — Quy tắc vận hành G1, vòng 2 (nguyên văn)

> 1. Chốt đơn lúc mấy giờ? 21h
> 2. trên web có khung giờ cho khách chọn
> 3. giá bán được bên thu mua nghiên cứu và set giá trước, ko thay đổi theo giá chợ
> 4. trọng lượng tùy theo loại sản phẩm
> 5. A. nhân viên kiểm tra, sau này làm tự động sau
> 6. nhân viên duyệt từng khách, sau này có rule tự động sau
> 7. làm seting trong admin đi
> 8. khách chỉ được hủy trước 9h

## 2026-10-20 — Quy tắc vận hành G1, vòng 3 (nguyên văn)

> 1. nghĩa là tại ngày đặt hàng, sau 21h, sau khi TPX chốt lên don đi mua hàng, thì ko hủy được nữa -> đổi lại 22h nhé
> 2. Đặt sau 21h, thì ko thể chọn giao ngày hôm sau, phải là ngày hôm sau nữa -> đổi lại 22h nhe
> 3. đến 22h nếu chưa thanh toán, nhân viên sẽ quyết định có duyệt để mua đơn đó hay ko, nếu chấp nhận rủi ro bom hàng thì vẫn mua, ko thì loại ra
> 4. quy cách khối lượng sản phẩm thì tùy theo loại sản phẩm, TPX sẽ tạo thông tin trước trên web, cho khách chọn
> 5. ko, chỉ đưa khung giờ cho khách chọn, TPX tự sắp xếp việc giao

## 2026-10-20 — Phạm vi bản đầu G1, vòng 4 (nguyên văn)

> 1. hiện tại dùng chung 1 flows thôi
> 2. đăng nhập bằng sdt + OTP
> 3. phân quyền đầy đủ RBAC
> 4. thông báo zalo, push noti qua app
> 5. mình muốn làm phần quản lý số dư, để kích thích dùng cho đơn sau

## 2026-10-20 — Màu thương hiệu (nguyên văn)

> tông màu chính : #309953
> màu để tạo điểm nhấn ở một số chỗ cần thu hút: #F9A01B

## 2026-10-20 — Quản lý số dư G1, vòng 5 (nguyên văn)

> 1. khách ko chủ động nạp
> 2. khách được yêu cầu rút hoàn về tài khoản ngân hàng
> 3. ưu tiên tự động trừ hết số dư
>
> 5) ko hết hạn
> 6) admin được thêm số dư khi điều chính đơn hàng

## 2026-10-20 — Loyalty từ bản đầu (nguyên văn)

> để uy tín có thể làm chương trình tích lũy điểm loyalty luôn từ ban đầu
> cứ 1.000d -> 1 điểm
> đơn hàng sẽ được mua quy đổi từ điểm với một mức giới hạn tối đa được quy định trong seting, ví dụ tối đa 10% - 100k, do admin set, khi mua hàng khách hang được chọn dùng điểm hay ko

## 2026-10-20 — Thời điểm tích loyalty (nguyên văn)

> thực hiện tích điểm sau khi đơn hoàn thành

## 2026-10-20 — Business G1, vòng 7 (nguyên văn)

> 1. ví dụ 10% tối đa 100k, con số này được seting
> 2. tính trên giá trị thanh toán sau cùng, tạm thời ko làm hết hạn
> 3. tạm thời chưa làm thanh toán COD, giai đoạn đầu bắt buộc bank transfer
> 4. hoàn tiền theo thỏa thuận
> 5. cái này bên vận hành trao đổi với khách rồi quyết
> 6. thử nghiệm các quận nội thành trước, hy vọng vài chục đơn mỗi ngày là ok

## 2026-10-21 — Phạm vi và trọng tâm (nguyên văn)

> 1. **Bắt đầu từ vài cụm chung cư hoặc khu dân cư -> ok nha, cái này ở bước vận hành**
> 2. phần này ok, mình sẽ làm 2 nhóm chức năng chính. - Mua nguyên liệu thô theo yêu cầu. - Mua nguyên liệu đã sơ chế theo món.
> 3. phần này về vận hành, bây giờ cần trao đổi để chốt busines, technical, design và implementation
> 4. ok
> 5. ok, sure
> 6. ok

Ngữ cảnh mục 4–6: đồng ý thông tin thực tế/đánh giá, referral và mua lại/nhắc đặt trong đề xuất trước. User chưa xác nhận riêng ví dụ 1 điểm đổi 10đ.

## 2026-10-21 — Hai luồng mua hàng và stack (nguyên văn)

> 1. A.
> 2. B
> 3. A
> 4. được phép
> 5. nestjs, reactjs, nextjs, postgres, bạn gợi ý thêm

Ngữ cảnh: câu 1 chọn nguyên liệu thô từ catalog; câu 2 chọn món/khẩu phần; câu 3 giá sẵn theo gói/khẩu phần; câu 4 giỏ/đơn/lần giao chung; câu 5 chọn công nghệ và yêu cầu đề xuất bổ sung.

## 2026-10-21 — Điều chỉnh mobile/deployment (nguyên văn)

> flutter, ko dùng react native
> ko dùng docker,

## 2026-10-21 — Sơ chế, hướng dẫn và đặt trước (nguyên văn)

> 1. A.
> 2. A, ban đầu mình chỉ cung cấp nguyên liệu, ko cung cấp gia vị, nước sốt vì cần có đầu bếp, khá phức tạp.
> 3. có, mình đang tìm crawl các menu món ăn, hướng dẫn
> 4. thực đơn cố định, chỉ tắt món, nguyên liệu khi thị trường hết
> 5. khách được phép đặt trước nhiều ngày. thực tế cũng có thể xảy ra đặt trước 5 ngày, nhưng tới ngày đó thị trường ko có nguyên liệu -> hoàn. tiền

Ngữ cảnh 1:A: chỉ làm sạch, cắt/chia sẵn; 2:A: chỉ nguyên liệu chính. Không coi lời user đang tìm nguồn là yêu cầu triển khai crawler ngay.

## 2026-10-21 — Hủy và thanh toán đơn đặt trước (nguyên văn)

> 1. chưa tới giờ chốt mua thì khách được hủy
> 2. khi đặt phải thanh toán luôn

## 2026-10-21 — Quyền ngoại lệ, thanh toán, rút hoàn và referral (nguyên văn)

> 1. Ngoại lệ chưa thanh toán: -> ok, admin cho phép nhân viên quyết phần này một cách thủ công
> 2. 1.000 d -> 1 điểm
> 3. ưu tiên dùng tiền còn trong số dư -> dùng điểm, nhưng có rule giới hạn -> phần còn lại thanh toán thực
> 4. khách yêu cầu rút tiền -> có phần quản lý này -> nhân viên duyệt và chuyển hoàn
> 5. có, món cần link tới nguyên liệu để tự động tắt
> 6. thưởng điểm loyalty, bao nhiêu thì setting sau

## 2026-10-21 — Admin ban đầu và xác nhận giá trị dùng điểm (nguyên văn)

> - Admin cấp quyền cho nhân viên quyết ngoại lệ đơn chưa thanh toán. -> bước đầu làm 1 tài khoản admin full tất cả quyền
>
> * Thanh toán theo thứ tự: **số dư tiền hoàn → điểm trong giới hạn → chuyển khoản phần còn lại**. -> ok
> * Nhân viên quản lý, duyệt và chuyển hoàn các yêu cầu rút. -> ok
> * &#x20;ok
> * ok
>
> ví dụ khách có 100 điểm (tương đương 100.000), nhưng khách sẽ ko được yêu cầu rút ra tiền 100.000 đ
>
> giả sử khi khách có đơn hàng 1.000.000, sẽ được thanh toán tối đa 5% băng điểm -> sẽ dùng 50 điểm để thanh toán

## 2026-10-21 — Giữ số dư khi yêu cầu rút (nguyên văn)

> nếu khách có 200.000 số dư
> khách tạo yêu cầu rút 150.000 -> sẽ bị pending 150.000
> khách chỉ được thanh toán cho 50.000 đang available

## 2026-10-21 — Chốt lịch đặt trước, loyalty và hoàn (nguyên văn)

> 1. cho đặt trước 1 tuần
> 2. đúng, làm theo bạn nói, thanh toán bằng điểm thì phần điểm ko được tích điểm tiếp
> 3. đồng ý với 3 ý của bạn

## 2026-10-21 — Bắt đầu trao đổi Technical (nguyên văn)

> trao đổi về technical nhé

## 2026-10-21 — Technical vòng 1 (nguyên văn)

> 1. ok
> 2. mình sẽ tạo 1 số account admin cố định, ko cần OTP
> 3. mình có server ok, ko cần quan tâm
> 4. chưa có, chắc bước đầu sẽ có login google, fb, apple account trước, sau khi đăng ký OTP ok thì thêm login phone
> 5. github

## 2026-10-21 — Duyệt auth/contact và yêu cầu PRD (nguyên văn)

> ok, bạn phân tích và chuẩn bị PRD cho toàn bộ hệ thống từ web, app, admin, DB....

## 2026-10-21 — Yêu cầu brief Claude Design (nguyên văn)

> bạn viết brief fho 4-DESIGN đi
>
> để mình yêu cầu claude design làm&#x20;
>
> - design system
> - ui flows for all user story từ web , app, admin

## 2026-10-21 — Yêu cầu rà soát flows (nguyên văn)

> mình nghĩ bạn nên phân tích lại các flows trên app, web, admin cho kỹ càng
> xem có thiếu flows nào, case nào ko

## 2026-10-25 — Trả lời review PRD vòng1 (nguyên văn)

> 1. ngay khi đơn tạo thành công, điểm sẽ bị hold lại, ko được dùng tiếp, đến khi đơn hoàn thành, chính thức trừ
> 2. hủy đơn, hoàn tiền, điểm bị hold trước đó sẽ open lại
> 3. do admin quyết dịnh
> 4. admin có chức năng để update thay đổi
> 5. ok
> 6. ko xảy ra tình trạng này

## 2026-10-25 — Hai câu làm rõ (nguyên văn)

> Cả điểm và số dư tiền hoàn đều hold đến hoàn thành
>
> Vẫn cho hoàn, không thu hồi điểm đã thưởng

## 2026-10-25 — Hoàn thiện design brief (nguyên văn)

> check lại và hoàn thiện design brief cho
>
> - design system
> - ui flows cho app, web, admin
