# Intake Answers

Nơi ghi câu trả lời đã chọn trong quá trình Codex phỏng vấn.

## Format Nhanh

```text
G1:
1:A
2:A,C
3:khác: ...
```

## Current Answers

> Quy tắc hiện hành: mốc chốt mua và khóa hủy là **22:00**, thay cho 21:00/“9h” ở các vòng cũ. Các vòng dưới giữ lịch sử trả lời; đọc vòng mới nhất và decision log khi có thay đổi.

> Thanh toán hiện hành ở bản đầu: **bắt buộc chuyển khoản, chưa có COD** (D-048). Các câu trả lời trước về duyệt COD được giữ làm lịch sử, không phải phạm vi hiện hành.

### G0 — 2026-10-20

| Chủ đề | Câu trả lời của user |
| --- | --- |
| Ý tưởng | Platform thương mại điện tử thực phẩm tươi: rau, củ, quả, thịt, cá, trứng |
| Mô hình vận hành | Khách đặt trước; mỗi tối gom đơn rồi mua hàng tại chợ đầu mối |
| Giá trị mong muốn | Giảm giá thành, hàng tươi ngon và chất lượng được đảm bảo; tiêu chuẩn và cách đo chưa chốt |
| Nội dung truyền thông | Kể câu chuyện sản phẩm từ nông trại; cần làm rõ nguồn gốc và bằng chứng tương ứng khi mua qua chợ đầu mối |
| Loại sản phẩm | Thương mại điện tử |
| Nền tảng | iOS, Android, Web app, Admin/CMS, Backend/API |
| Mục tiêu | Bản production đầy đủ dùng được; phạm vi chức năng cụ thể cần discovery |
| Doanh thu | Chênh lệch giữa giá mua và giá bán thực phẩm |
| Backend | Node.js, kiến trúc modular; các lựa chọn công nghệ khác chưa chốt |

Tên dự án được user chốt ngày 2026-10-20: **Thực phẩm xanh**. Viết tắt khi cần: **TPX**. Hồ sơ hiện nằm trực tiếp tại workspace `/Users/vod/Documents/TPX/code`; `fresh-market` là tên folder khi khởi tạo, không còn là đường dẫn hiện hành.

### G1 — 2026-10-20, đã nhận vòng trả lời đầu

| Chủ đề | Câu trả lời của user |
| --- | --- |
| Khu vực ra mắt | Các quận nội thành TP.HCM; danh sách vùng giao cụ thể chưa chốt |
| Khách hàng | Gia đình, người đi làm; có thể phục vụ thêm nhà hàng/quán ăn; ưu tiên giữa các nhóm chưa chốt |
| Người bán | TPX trực tiếp bán toàn bộ |
| Chu kỳ | Nhận đơn hằng ngày, giao hôm sau; giờ chốt và khung giờ mua/sơ chế/giao chưa chốt |
| Vận hành | TPX tự đi mua và giao; tập kết về một điểm, sơ chế trước khi giao |
| Thiếu hàng hoặc không đạt | Trao đổi với khách để hoàn tiền hoặc mua lại món khác; chưa chốt quy trình khi không liên lạc được |
| Câu chuyện nông trại | Để tính sau; chưa đưa thành cam kết nguồn gốc đã xác minh hoặc yêu cầu triển khai ngay |
| Thanh toán | Chuyển khoản thu trước; khách quen mới có thể được COD; tiêu chí khách quen và xác nhận chuyển khoản chưa chốt |

Các câu 4–6 của user ở vòng đầu mô tả chu kỳ đặt, giao và vận hành, không phải quyết định về giá. Giá và trọng lượng được làm rõ thêm ở vòng 2 bên dưới.

### G1 — 2026-10-20, vòng 2

| Chủ đề | Câu trả lời của user |
| --- | --- |
| Giờ chốt đơn | 21:00 hằng ngày; xử lý đơn sau mốc này chưa chốt |
| Khung giờ giao | Trên web có khung giờ cho khách chọn; khung cụ thể, sức chứa và cấu hình chưa chốt |
| Giá bán | Bên thu mua nghiên cứu và đặt giá trước; giá bán không thay đổi theo giá chợ đối với đơn đã đặt |
| Trọng lượng | Tùy loại sản phẩm; đơn vị bán, quy cách và chênh lệch cân thực tế cần đặc tả tiếp |
| Chuyển khoản | Nhân viên kiểm tra/xác nhận ở bản đầu; tự động hóa để sau |
| COD | Nhân viên duyệt từng khách ở bản đầu; rule tự động để sau |
| Phí giao và đơn tối thiểu | Làm settings trong admin; giá trị ban đầu và cách áp dụng khi thay đổi chưa chốt |
| Hủy đơn | User nói: “khách chỉ được hủy trước 9h”; chưa rõ 09:00 hay 21:00 và ngày áp dụng; chưa chuẩn hóa thành giờ cụ thể |

### G1 — 2026-10-20, vòng 3

| Chủ đề | Câu trả lời của user |
| --- | --- |
| Chốt mua và hủy đơn | Đổi mốc từ 21:00 sang 22:00; sau khi TPX chốt lên đơn đi mua thì khách không hủy được nữa |
| Ngày giao | Đơn sau 22:00 không được chọn giao ngày hôm sau; sớm nhất là ngày hôm sau nữa. Ví dụ đặt sau 22:00 ngày D thì sớm nhất giao D+2 |
| Đơn chưa thanh toán lúc 22:00 | Nhân viên quyết định duyệt mua nếu chấp nhận rủi ro khách không nhận, hoặc loại khỏi đợt mua; không tự động hủy toàn bộ đơn chưa thanh toán |
| Quy cách sản phẩm | TPX tạo trước thông tin/quy cách khối lượng trên web theo từng loại sản phẩm; khách chọn các lựa chọn đã công bố |
| Khung giao | Chỉ để khách chọn; không giới hạn số đơn mỗi khung; TPX tự sắp xếp giao hàng |

### G1 — 2026-10-20, vòng 4

| Chủ đề | Câu trả lời của user |
| --- | --- |
| Khách cá nhân và nhà hàng/quán ăn | Hiện tại dùng chung một flow; chưa yêu cầu luồng B2B riêng |
| Đăng nhập | Số điện thoại + OTP; nhà cung cấp và cách gửi OTP chưa chọn |
| Nhân viên | Phân quyền đầy đủ RBAC; danh sách role và permission chi tiết cần đặc tả |
| Thông báo | Zalo và push notification qua app; cách tích hợp, sự kiện và mẫu thông báo cần đặc tả |
| Hoàn tiền/số dư | Có phần quản lý số dư để dùng cho đơn sau; chưa chốt nạp tiền, rút tiền, cách trừ, thời hạn hoặc quyền điều chỉnh |

### Bổ sung — Màu thương hiệu, 2026-10-20

- Màu chủ đạo: **#309953**.
- Màu nhấn ở một số vị trí cần thu hút: **#F9A01B**.
- Ghi nhận ở D-034 và `../4-DESIGN/00-design-brief.md`; không thay thế phần discovery số dư đang chờ trả lời.

### G1 — 2026-10-20, vòng 5: số dư

| Chủ đề | Câu trả lời của user |
| --- | --- |
| Nạp thêm | Khách không chủ động nạp tiền |
| Rút hoàn | Khách được yêu cầu rút hoàn về tài khoản ngân hàng; quy trình duyệt/chuyển tiền chưa chốt |
| Sử dụng | Ưu tiên tự động trừ số dư khi mua hàng |
| Thanh toán kết hợp | User chưa trả lời câu 4: số dư không đủ thì kết hợp chuyển khoản/COD như thế nào |
| Thời hạn | Không hết hạn |
| Điều chỉnh | Admin được thêm số dư khi điều chỉnh đơn hàng; chưa có quyết định cấp thêm quyền trừ thủ công hoặc cộng ngoài điều chỉnh đơn |

### G1 — 2026-10-20, vòng 6: loyalty

| Chủ đề | Câu trả lời của user |
| --- | --- |
| Thời điểm triển khai | Loyalty có ngay từ bản đầu |
| Tích điểm | Cứ 1.000đ chi tiêu tích 1 điểm; cơ sở tính, thời điểm ghi nhận và cách làm tròn chưa chốt |
| Dùng điểm | Khách chọn dùng điểm hoặc không khi mua hàng |
| Giới hạn đổi điểm | Admin cấu hình giới hạn tối đa trong settings; user đưa ví dụ “10% - 100k”, chưa chốt cách kết hợp hai giới hạn hoặc giá trị mặc định |
| Giá trị đổi điểm | Chưa chốt 1 điểm được đổi thành bao nhiêu tiền; tỷ lệ tích điểm không tự xác định tỷ lệ đổi |

Số dư tiền hoàn và điểm loyalty được ghi riêng vì quy tắc sử dụng khác nhau: tiền hoàn ưu tiên tự dùng, còn điểm do khách chọn. Chưa có quyết định áp dụng quyền rút ngân hàng hoặc quy tắc không hết hạn của tiền hoàn sang điểm loyalty. Câu 4 về thanh toán phần thiếu khi số dư không đủ vẫn chưa được trả lời.

### G1 — 2026-10-20, bổ sung thời điểm tích loyalty

- User chốt: tích điểm **sau khi đơn hàng hoàn thành** (D-044).
- Tỷ lệ đổi sang tiền, cách kết hợp giới hạn, cơ sở tính/làm tròn và hạn điểm vẫn còn mở.
- Tiêu chí trạng thái Hoàn thành sẽ đặc tả ở PRD; chưa có câu trả lời riêng xác nhận điều kiện thanh toán đủ.

### G1 — 2026-10-20, vòng 7: tổng hợp business

| Chủ đề | Câu trả lời của user |
| --- | --- |
| Trần đổi điểm | Đồng thời giới hạn theo phần trăm và số tiền; ví dụ 10%, tối đa 100.000đ; admin cấu hình các giá trị |
| Cơ sở tích điểm | Giá trị thanh toán sau cùng; thành phần số tiền và cách làm tròn cần đặc tả tiếp |
| Hạn loyalty | Tạm thời không làm hết hạn |
| Thanh toán giai đoạn đầu | Bắt buộc chuyển khoản; tạm chưa làm COD, thay phạm vi COD trước đó |
| Hoàn tiền | Theo thỏa thuận với khách |
| Giao không thành công | Vận hành trao đổi với khách rồi quyết định |
| Thử nghiệm | Nội thành TP.HCM, kỳ vọng vài chục đơn/ngày; chưa có ngày ra mắt cụ thể |

Tỷ lệ đổi **1 điểm = bao nhiêu đồng** chưa được trả lời. Không coi tỷ lệ tích 1.000đ/điểm là tỷ lệ đổi. Cách kết hợp điểm, số dư và chuyển khoản vẫn cần đặc tả; user mới xác nhận hoãn COD ở câu 3.

### 2026-10-21 — Phạm vi chức năng và đầu vào PRD

- Hai nhóm mua hàng: nguyên liệu thô theo yêu cầu; nguyên liệu đã sơ chế theo món.
- Đồng ý minh bạch/đánh giá, referral, mua lại/món thường mua/nhắc đặt.
- Tiếp cận cụm dân cư và chọn ưu đãi mua thử thuộc vận hành.
- Tập trung chốt business, technical, design và implementation theo template.
- Tỷ lệ đổi điểm chưa chốt, kể cả ví dụ 1 điểm = 10đ trước đó.

### 2026-10-21 — Hai luồng mua hàng và Technical

- Nguyên liệu thô: chọn từ catalog TPX theo sản phẩm/quy cách/số lượng.
- Món sơ chế: chọn món và khẩu phần TPX cung cấp; giá sẵn cho từng gói/khẩu phần.
- Hai nhóm trong một giỏ, một đơn và cùng lần giao.
- Stack user chọn: NestJS, React, Next.js, PostgreSQL.
- User yêu cầu gợi ý thêm. Các đề xuất TypeScript/monorepo, admin Vite, Expo, Prisma, BullMQ/Redis, UI web, storage và Docker được ghi ở TD-005–013; chưa được user chốt.

### 2026-10-21 — Điều chỉnh mobile/deployment

- Mobile dùng **Flutter/Dart**, không React Native/Expo (TD-014).
- **Không dùng Docker** (TD-015), bao gồm local/CI/deployment.
- TD-008 và TD-012 cũ đã được thay; đề xuất push mới là FCM (TD-017), triển khai Node.js trực tiếp (TD-016), chưa được user chốt phương án cụ thể.
- pnpm/TypeScript chỉ áp dụng các app JS/TS; Flutter dùng toolchain riêng và theo cùng contract API.

### 2026-10-21 — Sơ chế, menu và đặt trước

- Sơ chế: chỉ làm sạch, cắt/chia sẵn nguyên liệu chính; ban đầu không gia vị/nước sốt.
- Có hướng dẫn nấu; user đang tìm nguồn crawl menu/hướng dẫn, chưa xác định nguồn hoặc giao thực hiện crawl.
- Thực đơn cố định, tắt món/nguyên liệu khi thị trường hết.
- Khách được đặt trước nhiều ngày; ví dụ 5 ngày, không phải tối đa đã chốt.
- Đến ngày mua thiếu nguyên liệu thì hoàn theo thỏa thuận; chưa chốt hoàn theo dòng/món hay cả đơn, lịch gom mua/khóa hủy và thời điểm thu tiền cho đơn tương lai.

### 2026-10-21 — Hủy và thanh toán đơn đặt trước

- Khách được hủy khi chưa tới cutoff đợt mua của đơn, kể cả đơn đặt trước nhiều ngày (D-067).
- Khách phải thanh toán ngay lúc đặt, không đợi sát ngày giao hoặc đợt mua (D-068); nhân viên vẫn xác nhận chuyển khoản thủ công.
- Chưa có timeout cụ thể hoặc quyết định giữ/bỏ ngoại lệ D-026. Mapping ngày giao sang ngày cutoff vẫn cần đặc tả, không tự coi là đã chốt chính xác ngày trước giao.

### 2026-10-21 — Bổ sung quy tắc cuối business

- Admin cấp quyền để nhân viên quyết thủ công ngoại lệ đơn chưa thanh toán; yêu cầu khách trả khi đặt vẫn giữ.
- User nhắc “1.000đ -> 1 điểm”; tỷ lệ tích đã rõ, giá trị tiền khi đổi một điểm vẫn cần xác nhận bằng ví dụ cụ thể.
- Thứ tự: tự ưu tiên số dư tiền hoàn -> điểm trong hạn mức nếu khách chọn -> chuyển khoản thực phần còn lại.
- Có quản lý yêu cầu rút; nhân viên duyệt và chuyển hoàn ngân hàng. User chưa trả lời riêng việc giữ tiền đang chờ rút.
- Món link nguyên liệu để tự tắt bán khi nguyên liệu tắt; không tự suy diễn bật lại/hủy đơn đã đặt.
- Referral thưởng loyalty; mức điểm để admin cấu hình sau, không có số điểm mặc định đã chốt.

### 2026-10-21 — Admin bản đầu và giá trị dùng điểm đã xác nhận

- Bước đầu một admin toàn quyền cho quản trị/vận hành (D-074); nền quyền có thể mở rộng về sau.
- User xác nhận thứ tự tiền hoàn -> điểm trong giới hạn -> chuyển khoản phần còn lại và quy trình quản lý/duyệt/chuyển rút hoàn.
- Dùng 1 điểm giảm 1.000đ trong hạn mức; điểm không được yêu cầu rút tiền (D-075/076). OQ-024 đã đóng.
- Ví dụ đơn 1.000.000đ, trần 5% dùng tối đa 50 điểm = 50.000đ. Không coi 5% là mặc định thay cho cấu hình admin (D-077).
- Các mốc chờ chuyển khoản, giữ tiền rút, công thức cơ sở/làm tròn, hoàn/hủy và dữ liệu nội dung còn được đặc tả ở PRD.

### 2026-10-21 — Available và pending khi rút số dư

- Tạo yêu cầu rút sẽ giữ đúng số tiền yêu cầu ở pending; checkout chỉ được dùng available (D-078).
- Ví dụ tổng số dư 200.000đ, yêu cầu rút 150.000đ: pending 150.000đ, available 50.000đ; tổng vẫn 200.000đ khi yêu cầu đang chờ xử lý.
- Chính sách giữ tiền đã rõ; lifecycle duyệt, chuyển hoàn, hủy/từ chối tiếp tục đặc tả ở PRD.

### 2026-10-21 — Chốt lịch đặt trước và công thức loyalty/hoàn

- Tối đa 1 tuần = 7 ngày. User đồng ý lịch đề xuất: giao ngày D chốt mua/khóa hủy 22:00 ngày D−1 (D-079/080).
- Đồng ý trần % trên tiền hàng sau giảm giá, không phí giao, trước trừ số dư (D-081).
- Tích trên tiền hàng sau giảm giá trừ phần trả bằng điểm; số dư vẫn tích, phí giao không tích, làm tròn xuống mỗi 1.000đ được 1 điểm (D-082). User nhấn mạnh không tích tiếp trên phần trả bằng điểm.
- Đồng ý cả ba ý: trả phần điểm bằng điểm; tiền theo thỏa thuận; hoàn sau hoàn thành thu hồi điểm tích tương ứng phần hoàn (D-083–085).
- Ví dụ đã đồng ý: tiền hàng 1 triệu, số dư 200k, dùng 50 điểm, chuyển khoản 750k nếu không phí giao; hoàn thành tích 950 điểm. Tỷ lệ 5% vẫn là ví dụ.
- Đóng OQ-026/034, đóng chính sách OQ-028; phân bổ hoàn một phần/trường hợp điểm đã tiêu vẫn cần đặc tả PRD.

### 2026-10-21 — Technical vòng 1 được trả lời

- Đồng ý gói stack/kiến trúc TD-019; không đồng nghĩa freeze toàn bộ Technical.
- Admin cố định một số account user tạo, không OTP/TOTP D-086/TD-020; thay số lượng một admin trước đây, giữ RBAC.
- Server user có sẵn, không cần tiếp tục hỏi mua máy/ngân sách TD-022. GitHub TD-023.
- Chưa có account dịch vụ OTP/Zalo/Firebase; Google/Facebook/Apple bản đầu D-087/TD-021; phone login sau khi OTP sẵn sàng D-088.
- Firebase Authentication là đề xuất TD-024, chưa phải user chọn; SĐT nhận hàng/identity linking tiếp tục đặc tả.

### 2026-10-21 — Duyệt Firebase Auth/contact và giao chuẩn bị PRD

- User đồng ý Firebase Authentication cho Google/Facebook/Apple web/Flutter, backend verify token/map user TPX: TD-025.
- Đồng ý nhập SĐT nhận hàng ở checkout chưa OTP; phone login sau liên kết tài khoản hiện có: D-089.
- Giao phân tích và chuẩn bị PRD toàn hệ thống web/app/admin/DB/backend: D-090. Chưa phải user duyệt toàn bộ các policy chi tiết mới hoặc freeze gate.
- Đã soạn PRD v0.1 đủ21feature,63screen,118API,68bảng logic; các chi tiết tiền/state chưa chốt có P-001–012 để review theo flow.

### 2026-10-21 — Design handoff

- User yêu cầu viết brief trong4-DESIGN để tự giao Claude Design: design system và UI flows toàn bộ user story web/app/admin (D-091).
- Chuẩn bị prompt và context pack độc lập, đầy đủ story/screen/flow/state/component mapping và output contract. Không tạo actual design artifacts hoặc tự gửi request sang công cụ bên ngoài.
- Input coverage:21story groups/63Screen IDs/13coreflows/28scenarios,56components,190screen×surface cells. Output vẫn Pending; cácPbusiness không tự được duyệt.

Open questions nằm trong `04-open-questions.md`. BRD/PRD/Technical là draft, chưa freeze. Không tự suy diễn quy tắc còn thiếu hoặc coi phần đề xuất là đã được duyệt.

## 2026-10-21 — Rà soát flow completeness

- User yêu cầu tìm flow/case thiếu trên web/app/admin và cập nhật brief.
- Chưa có câu trả lời phê duyệt policy mới; giữ P-001–019 review. Design có thể tiếp tục với annotated branches; module tiền/terminal cần chốt gaps trước code.

## 2026-10-25 — Review vòng1

- Điểm hold khi tạo đơn thành công; complete mới trừ, hủy mở hold.
- Admin hủy/hoàn đơn không thực hiện được, quyết định giao khi còn thiếu và có chức năng cập nhật thay đổi.
- Đồng ý giao phần hàng đã thống nhất trong khi tiền hoàn pending.
- User nói case6 không xảy ra; chưa tự chốt debt, cấm hoàn sau complete hoặc bỏ thu hồi điểm.
- Timing số dư tiền hoàn chưa được suy ra từ câu chỉ nói điểm.

## 2026-10-25 — Bổ sung trả lời

- Cash và points reserve khi đặt thành công, complete mới tiêu, cancel mở hold; order_hold khác pending_withdrawal.
- Hoàn sau complete được phép, điểm ORDER_EARN đã thưởng giữ nguyên. Không thu hồi/điểm âm/debt để xử lý refund.

## 2026-10-25 — Yêu cầu hoàn thiện brief

Phạm vi: design system + UI flows app/web/admin. Tiếp tục design inputs với annotated OQ-050/042, không tự chọn câu trả lời vì user chuyển sang yêu cầu hoàn thiện brief.
