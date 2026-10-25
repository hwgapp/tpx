# Prompt gửi Claude Design — TPX

> v0.4 · 2026-10-25. Copy phần dưới dấu phân cách và đính kèm **08-claude-design-context.md**. Chỉ cần hai file này khi Claude Design không có repo access.

---

Bạn là lead product designer cho **Thực phẩm xanh (TPX)**. Đọc context đính kèm và tạo **hai package thiết kế hoàn chỉnh**:

1. **Design System Package**: foundations/tokens, thư viện component có anatomy/variants/states, responsive/native behavior, accessibility và mapping sang web/Flutter.
2. **UI Workflow Package**: UI high fidelity và prototype flows cho web bán hàng, app Flutter iOS/Android và admin, gồm success, error, edge cases và recovery.

Phạm vi phải giữ: **21 nhóm user story, 116 AC, 63 Screen IDs, 56 CMP, 25 journeys J-001–025 và 100 cases FC-001–100**;13 UF/28 UC là nhóm flow nguồn. P1 vẫn thuộc R1. 32 màn khách có WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID;31 màn admin có ADMIN_DESKTOP/ADMIN_COMPACT: **190 screen×surface cells** phải map evidence default. Native shared frame được nếu có nguồn thật và platform notes; web mobile/admin compact cần layout cụ thể.

### Sản phẩm và visual direction

TPX tự bán thực phẩm tươi, khách đặt trước rồi TPX gom đơn, mua chợ đầu mối, tập kết/sơ chế và tự giao. RAW theo quy cách/số gói và MEAL theo món/khẩu phần chung giỏ/đơn/lần giao. MEAL chỉ nguyên liệu chính, không gia vị/sốt/nấu sẵn/tẩm ướp; có hướng dẫn nấu. Gia đình/người đi làm/nhà hàng dùng chung flow.

Brand **#309953**, accent **#F9A01B**. Đề xuất giao diện sáng, sạch, gần gũi, ảnh thực phẩm tự nhiên. Consumer dễ đọc giá/quy cách/ngày giao; admin dễ quét dữ liệu và thực hiện thao tác tiền/đơn. Designer chọn typography Việt, bố cục và semantic shades đủ contrast, giữ đúng hai brand primitives. Không tự tạo claim nông trại/organic/chứng nhận.

### Quy tắc mới nhất phải đúng

- 22h HCM chốt mua; trước 22h sớm nhất giao hôm sau, từ 22h ngày kia; tối đa ngày đặt+7. Đơn giao ngày D khóa self-cancel 22h D−1. Hiển thị ngày giờ cụ thể, không theo clock của thiết bị.
- Bank transfer, admin xác nhận thực nhận; không COD. “Đã báo chuyển khoản” chưa PAID. Admin được quyết định mua/giao chưa đủ tiền, nhưng khoản còn phải thu và audit vẫn giữ.
- Tiền hoàn available → points opt-in/caps → bank remainder. **Cash và points cùng HOLD khi tạo đơn thành công, CAPTURE khi complete, RELEASE khi hủy**; không tiêu/rút khoản đang giữ. Không giữ nguồn chỉ vì đang xem quote, không trừ available lần hai khi capture.
- Cash hiển thị **available / held_order / pending_withdrawal / total**; points hiển thị available/held/total riêng, không CTA rút/nạp/expiry. Approve rút chưa là đã chuyển, unknown bank outcome vẫn chờ đối soát.
- Earn 1điểm/1.000đ đủ điều kiện sau complete, floor; redeem 1điểm=1.000đ; cap% trên hàng trước số dư, không phí giao, đồng thời cap VND. Phần trả bằng cash balance vẫn earn, phần points/phí giao không earn.
- **Refund sau complete được phép và giữ nguyên ORDER_EARN đã cấp**, kể cả khách đã dùng points thưởng. RETURN points đã dùng khác RELEASE hold, không debt/clawback. Hoàn tiền theo nguồn/thỏa thuận, bank pending khác settled.
- Admin dùng CANCELLED/hủy vận hành khi không thực hiện được; không NOT_FULFILLED/fake complete. Có admin update đơn, phương án khách đã đồng ý và audit; refund pending không tự chặn giao phần hàng còn lại đã thống nhất.
- Khách Google/Facebook/Apple, contact phone checkout chưa OTP; admin fixed/password/RBAC không OTP. Zalo và push app, consent marketing khác OS permission.

### Flow và tương tác

Với mỗi J/FC: entry → precondition → actor action → system result → success/error → recovery/exit. Khách/admin có swimlane riêng; chuyển vai trò bằng domain event, không link khách vào admin. Mỗi required cell có default layout; loading/empty/validation/offline/access/conflict/cutoff/locked/submitting/unknown/success phải map evidence hoặc N/A có lý do. Critical money/cutoff/unknown cần frame trực tiếp; shared component state phải có copy/action/placement trong context màn.

Đủ các subviews catalog/category/variants/BOM/ảnh, settings, receipt/refund legs/withdrawal history, my-review, referral recipient, role/access/audit/report. App cần cold/warm start, back/keyboard/safe area, OAuth/bank return/deeplink; web có refresh/Back/multi-tab; admin compact giữ action/số tiền/bank destination quan trọng.

### Phần còn review

Ưu tiên các quyết định D-093–100 trong context. P-001–019 có trạng thái từng phần; không coi tất cả unapproved. OQ-048/049 đã đóng. OQ-050 complete-unpaid và OQ-042 settlement/hold delta chưa chốt: **dựng cả các branch ghi rõ trong context**, annotate ngoài product UI, không chọn một branch thành policy chính thức. Các proposal khác cũng cần assumptions/capability notes, không fake backend success.

### Output

Bàn giao đúng hai packages theo Output Contract: source/editable artifacts, token JSON, component/state matrix, contrast/assets/font provenance; screen/flow/story map, **journey-case-map**, state/surface coverage, prototype links, assumptions/fix-list và manifest. Có gallery foundations/components và entry hub customer/admin/scenario selector bên ngoài UI.

Tên frame `<ScreenID>__<Surface>__<State>__v01`; giữ nguyên US/UF/UC/J/FC/S/CMP IDs. Báo expected/delivered/missing bằng evidence thật. Không chỉ viết tài liệu hoặc một số màn đẹp; thiếu export format thì ghi limitation và bàn giao artifact thực, giữ Missing/Needs-fix cho phần thiếu. Có thể chia artifacts theo nhóm nhưng dùng một manifest chung.

Copy sản phẩm tiếng Việt; technical IDs/API/SQL/Firebase nằm trong annotations. Prototype dùng data demo, không OAuth/bank thật. Không thêm COD/top-up/rút points/expiry/phone OTP/marketplace/GPS/chat/AI/crawler/voucher/paywall. Tiếp tục thực hiện toàn bộ phần có thể thiết kế, không coi brief là gate approval hoặc production code đã có.
