# Screen, user-story và flow requirements — TPX

> Brief v0.4 — Planned, chưa có frame delivered. PRD có 21 feature/user-story groups, 63 Screen IDs, 13 core flows. US IDs là alias traceability trong handoff, không tạo feature/business mới. UC là scenario để designer thể hiện nhánh tương tác.

## 1. Definition of done cho coverage

- Mỗi Screen ID có default UI và navigation/interaction trên đúng surfaces. 32 screen khách × 4 surfaces + 31 screen admin × 2 surfaces = **190 coverage cells**.
- Default cần actual frame/source reference. iOS/Android có thể dùng shared frame nếu anatomy giống và có notes safe area/back/keyboard/typography/provider; mỗi cell vẫn có mapping và bằng chứng, không ghi trống hoặc chỉ “giống app”.
- Web desktop và mobile có layout cụ thể; admin compact có actual composed view giữ hành động/fields quan trọng, table chuyển list/detail khi cần. Shared component không được làm mất màn/context.
- Required states có thể dùng shared component frame + screen-specific copy/actions/placement nếu không đổi anatomy; state làm đổi quyết định tiền/date/quyền cần frame ví dụ gắn đúng Screen ID.
- Từng user story phải có flow entry→action→success/error/exit, gồm thao tác admin liên quan. P1 cũng phải đủ trong R1.

## 2. User-story coverage

| Story alias | PRD feature/spec | User story nguồn | Screens | Scenarios cần có |
| --- | --- | --- | --- | --- |
| US-001 | [F-001](../2-PRD/04-detailed-feature-specs/F-001.md) | Là khách, tôi muốn đăng nhập web/app và giữ cùng dữ liệu mua hàng để sử dụng TPX đúng quy tắc đã công bố. | S-009, S-010, S-011, S-032 | UC-004 |
| US-002 | [F-002](../2-PRD/04-detailed-feature-specs/F-002.md) | Là khách và admin, tôi muốn mua theo quy cách TPX công bố để sử dụng TPX đúng quy tắc đã công bố. | S-001, S-002, S-003, S-004, S-035, S-036 | UC-001, UC-017 |
| US-003 | [F-003](../2-PRD/04-detailed-feature-specs/F-003.md) | Là khách và admin, tôi muốn mua gói nguyên liệu chính đủ cho món theo khẩu phần để sử dụng TPX đúng quy tắc đã công bố. | S-001, S-003, S-005, S-006, S-007, S-037, S-038, S-039 | UC-002, UC-018 |
| US-004 | [F-004](../2-PRD/04-detailed-feature-specs/F-004.md) | Là khách, tôi muốn đặt cả hai nhóm trong một đơn và lần giao để sử dụng TPX đúng quy tắc đã công bố. | S-008, S-012, S-013, S-014, S-017, S-018, S-019, S-041, S-042 | UC-001, UC-002, UC-003, UC-005, UC-009, UC-020 |
| US-005 | [F-005](../2-PRD/04-detailed-feature-specs/F-005.md) | Là khách và admin, tôi muốn biết số phải chuyển và xác nhận tiền nhận thực tế để sử dụng TPX đúng quy tắc đã công bố. | S-014, S-016, S-017, S-042, S-043 | UC-006, UC-020 |
| US-006 | [F-006](../2-PRD/04-detailed-feature-specs/F-006.md) | Là admin, tôi muốn gom đúng đơn theo ngày giao và quyết ngoại lệ để sử dụng TPX đúng quy tắc đã công bố. | S-037, S-039, S-044, S-045, S-046 | UC-018, UC-021 |
| US-007 | [F-007](../2-PRD/04-detailed-feature-specs/F-007.md) | Là admin và khách, tôi muốn theo dõi từ nhận hàng đến giao hoàn thành để sử dụng TPX đúng quy tắc đã công bố. | S-019, S-042, S-046, S-047, S-048, S-049 | UC-022 |
| US-008 | [F-008](../2-PRD/04-detailed-feature-specs/F-008.md) | Là khách và admin, tôi muốn chọn lịch đúng cutoff và phạm vi phục vụ để sử dụng TPX đúng quy tắc đã công bố. | S-012, S-013, S-014, S-015, S-048 | UC-005 |
| US-009 | [F-009](../2-PRD/04-detailed-feature-specs/F-009.md) | Là admin cố định, tôi muốn vận hành theo quyền và truy vết từng thao tác để sử dụng TPX đúng quy tắc đã công bố. | S-033, S-034, S-035, S-036, S-038, S-055, S-056, S-057, S-058, S-063 | UC-016, UC-017, UC-020, UC-026 |
| US-010 | [F-010](../2-PRD/04-detailed-feature-specs/F-010.md) | Là khách và admin có quyền, tôi muốn dùng available và đối soát số dư để sử dụng TPX đúng quy tắc đã công bố. | S-022, S-052, S-055, S-056 | UC-003, UC-007, UC-023, UC-026 |
| US-011 | [F-011](../2-PRD/04-detailed-feature-specs/F-011.md) | Là khách và admin, tôi muốn giữ tiền rút và biết kết quả ngân hàng để sử dụng TPX đúng quy tắc đã công bố. | S-023, S-024, S-053, S-054 | UC-007, UC-024 |
| US-012 | [F-012](../2-PRD/04-detailed-feature-specs/F-012.md) | Là khách và admin, tôi muốn tích sau hoàn thành và dùng trong giới hạn để sử dụng TPX đúng quy tắc đã công bố. | S-014, S-021, S-025, S-052, S-055, S-056 | UC-003, UC-008, UC-022, UC-023, UC-026 |
| US-013 | [F-013](../2-PRD/04-detailed-feature-specs/F-013.md) | Là khách và admin, tôi muốn nhận đúng trạng thái và biết khi gửi lỗi để sử dụng TPX đúng quy tắc đã công bố. | S-029, S-030, S-060 | UC-015, UC-028 |
| US-014 | [F-014](../2-PRD/04-detailed-feature-specs/F-014.md) | Là admin, tôi muốn điều chỉnh chính sách có version không sửa đơn cũ để sử dụng TPX đúng quy tắc đã công bố. | S-059, S-063 | UC-025, UC-026 |
| US-015 | [F-015](../2-PRD/04-detailed-feature-specs/F-015.md) | Là khách và admin, tôi muốn xem thông tin hàng hóa/TPX đáng tin và đúng thực tế để sử dụng TPX đúng quy tắc đã công bố. | S-001, S-004, S-006, S-007, S-031, S-040, S-061 | UC-002, UC-019, UC-027 |
| US-016 | [F-016](../2-PRD/04-detailed-feature-specs/F-016.md) | Là khách đã mua và admin, tôi muốn đánh giá hàng đã nhận và quản lý nội dung để sử dụng TPX đúng quy tắc đã công bố. | S-004, S-006, S-028, S-062 | UC-014, UC-027 |
| US-017 | [F-017](../2-PRD/04-detailed-feature-specs/F-017.md) | Là khách mới/người giới thiệu và admin, tôi muốn giới thiệu bạn và nhận điểm theo setting để sử dụng TPX đúng quy tắc đã công bố. | S-026, S-056 | UC-011, UC-022 |
| US-018 | [F-018](../2-PRD/04-detailed-feature-specs/F-018.md) | Là khách, tôi muốn tạo giỏ mới nhanh từ đơn cũ để sử dụng TPX đúng quy tắc đã công bố. | S-018 | UC-012 |
| US-019 | [F-019](../2-PRD/04-detailed-feature-specs/F-019.md) | Là khách, tôi muốn tìm nhanh lựa chọn đã mua thường xuyên để sử dụng TPX đúng quy tắc đã công bố. | S-027 | UC-013 |
| US-020 | [F-020](../2-PRD/04-detailed-feature-specs/F-020.md) | Là khách và admin, tôi muốn nhận nhắc đúng đồng ý và trước cutoff để sử dụng TPX đúng quy tắc đã công bố. | S-030, S-060 | UC-015, UC-028 |
| US-021 | [F-021](../2-PRD/04-detailed-feature-specs/F-021.md) | Là khách và admin, tôi muốn xử lý ngoại lệ theo thỏa thuận và hoàn đúng nguồn để sử dụng TPX đúng quy tắc đã công bố. | S-019, S-020, S-021, S-041, S-042, S-049, S-050, S-051, S-052 | UC-009, UC-010, UC-023 |

## 3. Core flow map

| Flow ID | Flow nguồn PRD | Screens liên quan | Scenarios |
| --- | --- | --- | --- |
| UF-001 | Đăng nhập và liên kết tài khoản | S-009, S-010, S-011, S-032, S-008, S-014 | UC-004 |
| UF-002 | Chọn nguyên liệu thô | S-001, S-002, S-003, S-004, S-008, S-009, S-014, S-015, S-016, S-017, S-019 | UC-001 |
| UF-003 | Chọn món sơ chế | S-001, S-005, S-006, S-007, S-008, S-014, S-017, S-019 | UC-002 |
| UF-004 | Checkout và đặt đơn | S-001, S-002, S-003, S-004, S-008, S-009, S-014, S-015, S-016, S-017, S-019, S-005, S-006, S-007, S-022, S-025, S-012, S-013, S-021, S-052, S-056 | UC-001, UC-002, UC-003, UC-005, UC-008 |
| UF-005 | Chuyển khoản | S-016, S-017, S-018, S-019, S-042, S-043, S-041, S-050 | UC-006, UC-020 |
| UF-006 | Cutoff và mua hàng | S-037, S-038, S-039, S-045, S-044, S-046, S-042 | UC-018, UC-021 |
| UF-007 | Sơ chế, đóng gói, giao và hoàn thành | S-014, S-019, S-021, S-025, S-052, S-056, S-047, S-048, S-049, S-050, S-042 | UC-008, UC-022 |
| UF-008 | Hủy trước cutoff | S-018, S-019, S-020, S-021 | UC-009 |
| UF-009 | Yêu cầu rút số dư | S-022, S-023, S-024, S-053, S-054, S-056, S-058 | UC-007, UC-024 |
| UF-010 | Thiếu hàng, đổi món và hoàn một phần | S-014, S-019, S-021, S-025, S-052, S-056, S-031, S-050, S-042, S-051 | UC-008, UC-010, UC-023 |
| UF-011 | Referral, mua lại và thường mua | S-010, S-026, S-056, S-059, S-018, S-019, S-008, S-014, S-027, S-004, S-006 | UC-011, UC-012, UC-013 |
| UF-012 | Đánh giá, thông báo và nhắc đặt | S-004, S-006, S-019, S-028, S-062, S-029, S-030, S-024, S-060, S-034 | UC-014, UC-015, UC-027, UC-028 |
| UF-013 | Quản trị và thay settings | S-033, S-034, S-057, S-058, S-035, S-036, S-040, S-037, S-038, S-039, S-045, S-061, S-031, S-007, S-059, S-014, S-042, S-055, S-056, S-063, S-062, S-004, S-006, S-028, S-060, S-029, S-030 | UC-016, UC-017, UC-018, UC-019, UC-025, UC-026, UC-027, UC-028 |

## 4. Scenarios: paths, success và edge

| Scenario | Nhiệm vụ | Features | PRD flow | Screen path/coverage | Happy-path interaction | Nhánh lỗi/edge |
| --- | --- | --- | --- | --- | --- | --- |
| UC-001 | Mua nguyên liệu thô | F-002, F-004 | UF-002/UF-004 | S-001 → S-002 → S-003 → S-004 → S-008 → S-009 → S-014 → S-015 → S-016 → S-017 → S-019 | Tìm/chọn variant, pack count, giỏ, login, ngày giao, quote, đặt một đơn. | Variant tắt/giá đổi/không đúng qty; quote phải cập nhật trước confirm. |
| UC-002 | Mua nguyên liệu theo món | F-003, F-004, F-015 | UF-003/UF-004 | S-001 → S-005 → S-006 → S-007 → S-008 → S-014 → S-017 → S-019 | Xem thành phần/hướng dẫn, chọn khẩu phần giá sẵn, thêm giỏ và đặt. | Không gia vị/sốt; món thiếu ingredient, không sửa từng nguyên liệu. |
| UC-003 | Giỏ hỗn hợp và ba nguồn thanh toán | F-004, F-010, F-012 | UF-004 | S-008 → S-014 → S-015 → S-016 → S-017 → S-019 → S-022 → S-025 | RAW+MEAL cùng order; balance auto, points opt-in/caps, bank remainder. | T=0 không yêu cầu chuyển0đ; quote/account đổi, đang gửi hoặc response chưa rõ. |
| UC-004 | Social login, hồ sơ và linked identity | F-001 | UF-001 | S-009 → S-010 → S-011 → S-032 → S-008 → S-014 | Google/FB/Apple, trở lại giỏ, cập nhật profile, link provider cùng user. | Provider cancel/fail, email ẩn, identity conflict; contactphone không OTP, phone login chưa có. |
| UC-005 | Sổ địa chỉ và ngày giao tương lai | F-004, F-008 | UF-004 | S-012 → S-013 → S-014 → S-015 → S-019 | Chọn/thêm địa chỉ, SĐT và slot; đặt trước tối đa7 ngày. | Ngoài vùng, trước/sau 22h, quote qua mốc; đơn tương lai giữ deadline trước ngày giao. |
| UC-006 | Chờ xác nhận chuyển khoản | F-005 | UF-005 | S-016 → S-017 → S-018 → S-019 → S-042 → S-043 | Xem bank/amount/reference, báo đã chuyển [P], admin xác nhận thực nhận. | Client notice không PAID; thiếu/thừa/muộn, phần chưa phân bổ, copy lỗi. |
| UC-007 | Ví available/pending và yêu cầu rút | F-010, F-011 | UF-009 | S-022 → S-023 → S-024 → S-053 → S-054 | Xem50k available/150k pending, tạo rút, adminapprove/process/paid. | Vượt available, cancel/reject theo P-002, unknown bank outcome; không nạp/không rút points. |
| UC-008 | Điểm, giới hạn và điều chỉnh | F-012 | UF-004/UF-007/UF-010 | S-014 → S-019 → S-021 → S-025 → S-052 → S-056 | Chọn dùng, đọc cap/earn dự kiến, xem HOLD/CAPTURE/RELEASE/earn/return history. | Chưa complete không cộng; HOLD/CAPTURE/RELEASE theo D-093/094; hoàn sau complete giữ nguyên ORDER_EARN D-100, không tự dựng debt. |
| UC-009 | Xem đơn và hủy hợp lệ | F-004, F-021 | UF-008 | S-018 → S-019 → S-020 → S-021 | Theo dõi order, hạn hủy, preview tác động, hủy trước cutoff. | Đúng22h khóa, state đãđổi/đãhủy, không lặp hoàn nguồn nội bộ. |
| UC-010 | Khách theo dõi hoàn/đổi món | F-021 | UF-010 | S-019 → S-021 → S-031 → S-050 → S-052 | Hiển thị phương án đã thỏa thuận, tiền/points/kênh hoàn, tiến trình. | Partial/full/bank pending; thiếu hàng không tự đổi hoặc tự hủy cảđơn. |
| UC-011 | Giới thiệu và mốc thưởng | F-017 | UF-011 | S-010 → S-026 → S-056 → S-059 | Code/link share, điều kiện và trạng thái reward sau đơn đầu complete. | Mức reward demo settings, self/late attribution, reversal P-006, không cash. |
| UC-012 | Mua lại đơn | F-018 | UF-011 | S-018 → S-019 → S-008 → S-014 | Preview đơn cũ theo giá/quy cách mới, chọn thêm/thay giỏ, checkout mới. | Hàngtắt/giá đổi/giỏ có sẵn, không tự đặt hoặc giữgiá cũ. |
| UC-013 | Món thường mua | F-019 | UF-011 | S-027 → S-004 → S-006 → S-008 | Danh sách/pin-hide [P], chọn sản phẩm, thêm giỏ. | Khách mới empty, sản phẩm tắt bán, order hủy không tính tần suất. |
| UC-014 | Đánh giá từ khách đã mua | F-016 | UF-012 | S-004 → S-006 → S-019 → S-028 → S-062 | Từ itemcompleted viết rating/text, pendingmoderation, xem published. | Chưa mua/chưa complete, submit lặp, hidden; admin không sửa sao/text. |
| UC-015 | Notification/deeplink và consent | F-013, F-020 | UF-012 | S-029 → S-030 → S-019 → S-024 → S-060 | Xem thông báo, mở resource sauauth, bật/tắtnhắc theo kênh. | Pushdenied, token user cũ, unsubscribe sauqueue, jobquacutoff, provider fail/skip. |
| UC-016 | Admin login và access | F-009 | UF-013 | S-033 → S-034 → S-057 → S-058 | Fixedaccount/password, mở màn theo quyền, quản lýrole/status/phiên. | Không OTP; wrongpassword, expired/revoked, forbidden, dirty form. |
| UC-017 | Quản trị RAW/danh mục/variants | F-002, F-009 | UF-013 | S-035 → S-036 → S-040 | Tạo/sửa category/product/variant, giá/pack/mapping nguyên liệu, ảnh, publish. | Missingmapping/unit/price, versionconflict, variant tắt không sửa ordercũ. |
| UC-018 | Quản trị món/BOM/khả dụng | F-003, F-006 | UF-013/UF-006 | S-037 → S-038 → S-039 → S-045 | BOM theo portion và version, hướng dẫn nấu/source, tắt ingredient xem impact. | Món tự tắt, tái bật theo P-007, đơn cũ giữ snapshot, không auto replace. |
| UC-019 | Ảnh/nội dung/chính sách | F-015 | UF-013 | S-040 → S-061 → S-031 → S-007 | Uploadmetadata/source, edit/preview/publish version. | Uploadfail/invalid/unsaved, draft không public; không claimfarm/certification giả. |
| UC-020 | Admin đối soát tiền/đơn | F-004, F-005, F-009 | UF-005 | S-041 → S-042 → S-043 → S-050 | Filter/date/detail, receiptactual/reference, phần còn thu, excesscase. | Duplicate/partial/excess/late money; paid khác included procurement. |
| UC-021 | Chốt thu mua và chất lượng | F-006 | UF-006 | S-044 → S-045 → S-046 → S-037 → S-042 | Batch ngày giao, decideunpaid có reason, nhu cầu unit/source, ghi mua/đạt/thiếu/cost. | Jobchậm không mở hủy, retry không nhân đôi, thiếu/không đạt mởcase, không đổi giá bán. |
| UC-022 | Sơ chế/đóng gói/giao/complete | F-007, F-012, F-017 | UF-007 | S-047 → S-048 → S-049 → S-050 → S-042 | Checklist, sắp delivery date/slot, dispatch, outcome, complete/earn. | Chưa xong case, admin quyết định giao thiếu tiền D-095; complete-unpaid OQ-050, deliveryfailed→agreement, complete lặp không thưởng thêm. |
| UC-023 | Admin agreement và hoàn theo leg | F-021, F-010, F-012 | UF-010 | S-042 → S-050 → S-051 → S-052 → S-056 → S-021 | Agreement, preview split/caps/hold-release/captured-return, approveinternallegs, bankclaim/settle. | Whole/partial/excess, nguồn gốc khác payout method, pendingcap, D-100 giữ ORDER_EARN, không debt, no duplicate. |
| UC-024 | Admin duyệt/chuyển tiền rút | F-011 | UF-009 | S-053 → S-054 → S-056 → S-058 | Reviewbank/amount, approve, claimPROCESSING, markPAIDreference. | Haiadmin/race, unknownbank, cancel/reject chỉ state cho phép, no auto-release. |
| UC-025 | Cấu hình chính sách có version | F-014 | UF-013 | S-059 → S-036 → S-039 → S-014 → S-042 | Fee/minimum/vùng/slot/bank/cappoint/referral/reminder, validate và publish version. | Invalidconfig/missing data, examples không default, đơn cũ không đổi; secrets không UI public. |
| UC-026 | Khách, ledger, audit và reports | F-009, F-010, F-012, F-014 | UF-013 | S-055 → S-056 → S-058 → S-034 → S-063 | Customer detail, các ledger, actor/reason/ref, lọc metric theo basis. | Permission restricted, cash-in khácGMV/liability; pending không cộng 2 lần, costincomplete có label. |
| UC-027 | Admin moderation | F-016, F-015 | UF-012/UF-013 | S-062 → S-004 → S-006 → S-028 | Kiểmtra verifiedpurchase, publish/hide có reason, xemaverage. | Không sửa text/rating, denied/versionconflict, public chỉ published. |
| UC-028 | Admin notification operations | F-013, F-020 | UF-012/UF-013 | S-060 → S-029 → S-030 → S-034 | Queue/attempt/channelstatus/templateerror, retrytheoconsent. | SENT không READ, provider thiếu config/unknown, unsubscribedskip; không rollback order. |

Path trong bảng gồm cả các màn đối chiếu/role transition, không ép người dùng đi qua tất cả màn tuần tự. Designer tách persona swimlanes khách/admin và branch từ cùng entry; annotate cross-role events thay vì link khách trực tiếp vào admin.

## 5. State pattern library

| Pattern | Nhóm | States cần thể hiện | Lưu ý |
| --- | --- | --- | --- |
| ST-01 | Duyệt catalog | Default; loading; empty/filter-empty; network error/retry; offline cached; unavailable item | Màn public: no-permission N/A có giải thích; không giả số tồn kho |
| ST-02 | Chi tiết nội dung/sản phẩm | Default; loading; missing/not-found; network error; offline cached; variant unavailable | Giá/quy cách/ảnh/cooking dài; CTA cần đủ option |
| ST-03 | Giỏ/quote/checkout | Default; empty; validation; submitting; changed-price/quote; insufficient available/points; cutoff/date changed; offline blocked; unknown outcome; placed | Phân biệt báo giá với đã tạo đơn; giữ context khi login/Back |
| ST-04 | Authentication/identity | Default; provider/credential loading; cancelled; failed; expired; revoked; linked/conflict; return-to-context | Admin password không OTP; social3providers, emailoptional; không phone login baseline |
| ST-05 | Profile/address/settingsforms | Default; loading; empty when applicable; invalid; submitting; dirty; conflict; success; offlineblocked; permission | SĐT contact chưa OTP; validation/help luôn còn nhãn |
| ST-06 | Order/wallet/points/history | Default; loading; empty; error; offline/stale; permission/owner; pending/settled/locked; success | Không chỉ một badge xanh; timeline, đơn vị, deadline rõ |
| ST-07 | Mutation tài chính/approval | Review; validation; submitting; stale/conflict; insufficientsource/cap; unknown outcome; permission; locked; success | Có amount/source/destination; không replay mù khi unknown hoặc PROCESSING |
| ST-08 | Admin lists/boards | Default; loading; empty; filtered empty; error; stale; permission; selectable/sorted; compact overflow | Táchlọc trạng thái/payment/date; row actions có label |
| ST-09 | Admin publish/edit | Draft; dirty; invalid; uploading; preview; published; archived; conflict; permission; error | Version giữđơn cũ; có source/impact; không publish placeholdersecrets |
| ST-10 | Admin operations decisions | Undecided; included/excluded; in-progress; blocked/case; complete; invalidtransition; stale; permission; unknownmoney | Mua unpaid không PAID; no early-cutoff/no complete duplicate |
| ST-11 | Engagement/reviews/consent | Default; first use/empty; ineligible; opt-in/off/denied; submitted/pending; reward/published; error | Mức setting demo, marketingconsent riêngOS, no selfgrant |
| ST-12 | Read/policy/support | Published; loading; missing; error; offline cached; longtext | Không invent claims; screen reader và link navigation rõ |

## 6. Screen handoff target — đủ 63 IDs

| Screen ID | Màn hình | Features | Surface set | State pattern | Components yêu cầu | Prototype scenarios |
| --- | --- | --- | --- | --- | --- | --- |
| S-001 | Trang chủ | F-002, F-003, F-015 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-01 | CMP-001, CMP-002, CMP-003, CMP-013, CMP-014, CMP-026, CMP-031, CMP-032, CMP-049 | UC-001, UC-002 |
| S-002 | Danh sách nguyên liệu | F-002 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-01 | CMP-001, CMP-002, CMP-003, CMP-007, CMP-011, CMP-013, CMP-014, CMP-031, CMP-032, CMP-034, CMP-035, CMP-037, CMP-049 | UC-001 |
| S-003 | Tìm kiếm | F-002, F-003 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-01 | CMP-001, CMP-002, CMP-003, CMP-004, CMP-007, CMP-011, CMP-013, CMP-014, CMP-031, CMP-032, CMP-034, CMP-035, CMP-037, CMP-049 | UC-001 |
| S-004 | Chi tiết nguyên liệu | F-002, F-015, F-016 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-02 | CMP-001, CMP-002, CMP-003, CMP-006, CMP-012, CMP-013, CMP-015, CMP-016, CMP-031, CMP-032, CMP-034, CMP-046, CMP-049 | UC-001, UC-013, UC-014, UC-027 |
| S-005 | Danh sách món | F-003 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-01 | CMP-001, CMP-003, CMP-011, CMP-013, CMP-014, CMP-031, CMP-032, CMP-035, CMP-037, CMP-049 | UC-002 |
| S-006 | Chi tiết món và khẩu phần | F-003, F-015, F-016 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-02 | CMP-001, CMP-002, CMP-003, CMP-006, CMP-012, CMP-013, CMP-015, CMP-016, CMP-017, CMP-031, CMP-032, CMP-034, CMP-046, CMP-049 | UC-002, UC-013, UC-014, UC-027 |
| S-007 | Hướng dẫn nấu | F-003, F-015 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-02 | CMP-001, CMP-003, CMP-013, CMP-015, CMP-017, CMP-018, CMP-031, CMP-032, CMP-045, CMP-049 | UC-002, UC-019 |
| S-008 | Giỏ hàng chung | F-004 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-03 | CMP-001, CMP-002, CMP-003, CMP-006, CMP-013, CMP-014, CMP-016, CMP-019, CMP-020, CMP-026, CMP-031, CMP-032, CMP-034, CMP-049 | UC-001, UC-002, UC-003, UC-004, UC-012, UC-013 |
| S-009 | Đăng nhập social | F-001 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-04 | CMP-001, CMP-003, CMP-004, CMP-013, CMP-031, CMP-032, CMP-049, CMP-051 | UC-001, UC-004 |
| S-010 | Tài khoản | F-001 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-05 | CMP-001, CMP-002, CMP-003, CMP-004, CMP-008, CMP-010, CMP-013, CMP-031, CMP-032, CMP-047, CMP-048, CMP-049, CMP-051, CMP-052 | UC-004, UC-011 |
| S-011 | Liên kết đăng nhập | F-001 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-04 | CMP-001, CMP-003, CMP-013, CMP-031, CMP-032, CMP-033, CMP-049, CMP-051, CMP-052 | UC-004 |
| S-012 | Sổ địa chỉ | F-004, F-008 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-05 | CMP-001, CMP-002, CMP-003, CMP-013, CMP-031, CMP-032, CMP-034, CMP-049, CMP-055 | UC-005 |
| S-013 | Thêm/sửa địa chỉ | F-004, F-008 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-05 | CMP-001, CMP-003, CMP-004, CMP-007, CMP-009, CMP-010, CMP-013, CMP-031, CMP-032, CMP-034, CMP-049, CMP-055 | UC-005 |
| S-014 | Checkout | F-004, F-005, F-008, F-012 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-03 | CMP-001, CMP-003, CMP-004, CMP-006, CMP-007, CMP-008, CMP-009, CMP-010, CMP-013, CMP-016, CMP-019, CMP-020, CMP-021, CMP-022, CMP-026, CMP-031, CMP-032, CMP-034, CMP-049, CMP-055 | UC-001, UC-002, UC-003, UC-004, UC-005, UC-008, UC-012, UC-025 |
| S-015 | Chọn ngày/khung giao | F-008 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-03 | CMP-001, CMP-003, CMP-009, CMP-013, CMP-026, CMP-031, CMP-032, CMP-034, CMP-049 | UC-001, UC-003, UC-005 |
| S-016 | Hướng dẫn chuyển khoản | F-005 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-06 | CMP-001, CMP-003, CMP-012, CMP-013, CMP-020, CMP-023, CMP-031, CMP-032, CMP-049 | UC-001, UC-003, UC-006 |
| S-017 | Kết quả đặt đơn | F-004, F-005 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-03 | CMP-001, CMP-003, CMP-012, CMP-013, CMP-020, CMP-023, CMP-024, CMP-031, CMP-032, CMP-049 | UC-001, UC-002, UC-003, UC-006 |
| S-018 | Lịch sử đơn | F-004, F-018 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-06 | CMP-001, CMP-002, CMP-003, CMP-011, CMP-012, CMP-013, CMP-019, CMP-024, CMP-031, CMP-032, CMP-034, CMP-035, CMP-037, CMP-049 | UC-006, UC-009, UC-012 |
| S-019 | Chi tiết và tiến trình đơn | F-004, F-007, F-021 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-06 | CMP-001, CMP-002, CMP-003, CMP-012, CMP-013, CMP-019, CMP-020, CMP-021, CMP-022, CMP-023, CMP-024, CMP-025, CMP-026, CMP-031, CMP-032, CMP-034, CMP-049, CMP-055 | UC-001, UC-002, UC-003, UC-005, UC-006, UC-008, UC-009, UC-010, UC-012, UC-014, UC-015 |
| S-020 | Xác nhận hủy | F-021 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-07 | CMP-001, CMP-003, CMP-013, CMP-020, CMP-021, CMP-026, CMP-030, CMP-031, CMP-032, CMP-033, CMP-049 | UC-009 |
| S-021 | Chi tiết điều chỉnh/hoàn | F-021, F-012 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-06 | CMP-001, CMP-003, CMP-012, CMP-013, CMP-020, CMP-022, CMP-025, CMP-028, CMP-030, CMP-031, CMP-032, CMP-049 | UC-008, UC-009, UC-010, UC-023 |
| S-022 | Số dư tiền hoàn | F-010 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-06 | CMP-001, CMP-002, CMP-003, CMP-011, CMP-013, CMP-021, CMP-027, CMP-028, CMP-031, CMP-032, CMP-037, CMP-049 | UC-003, UC-007 |
| S-023 | Tạo yêu cầu rút | F-011 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-07 | CMP-001, CMP-003, CMP-004, CMP-005, CMP-007, CMP-010, CMP-013, CMP-027, CMP-029, CMP-031, CMP-032, CMP-033, CMP-034, CMP-049 | UC-007 |
| S-024 | Theo dõi yêu cầu rút | F-011 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-06 | CMP-001, CMP-003, CMP-012, CMP-013, CMP-025, CMP-027, CMP-028, CMP-029, CMP-031, CMP-032, CMP-033, CMP-049 | UC-007, UC-015 |
| S-025 | Điểm loyalty | F-012 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-06 | CMP-001, CMP-002, CMP-003, CMP-008, CMP-011, CMP-012, CMP-013, CMP-022, CMP-028, CMP-031, CMP-032, CMP-034, CMP-037, CMP-049 | UC-003, UC-008 |
| S-026 | Giới thiệu bạn bè | F-017 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-11 | CMP-001, CMP-002, CMP-003, CMP-013, CMP-022, CMP-031, CMP-032, CMP-047, CMP-049 | UC-011 |
| S-027 | Món thường mua | F-019 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-01 | CMP-001, CMP-003, CMP-006, CMP-011, CMP-013, CMP-014, CMP-019, CMP-031, CMP-032, CMP-035, CMP-037, CMP-049 | UC-013 |
| S-028 | Viết đánh giá | F-016 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-11 | CMP-001, CMP-003, CMP-004, CMP-010, CMP-013, CMP-031, CMP-032, CMP-046, CMP-049 | UC-014, UC-027 |
| S-029 | Thông báo trong tài khoản [P] | F-013 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-06 | CMP-001, CMP-002, CMP-003, CMP-011, CMP-012, CMP-013, CMP-031, CMP-032, CMP-034, CMP-037, CMP-048, CMP-049, CMP-056 | UC-015, UC-028 |
| S-030 | Tùy chọn thông báo/nhắc đặt | F-013, F-020 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-05 | CMP-001, CMP-003, CMP-008, CMP-013, CMP-031, CMP-032, CMP-033, CMP-048, CMP-049, CMP-056 | UC-015, UC-028 |
| S-031 | Thông tin TPX/chính sách/hỗ trợ | F-015 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-12 | CMP-001, CMP-003, CMP-013, CMP-031, CMP-032, CMP-049 | UC-010, UC-019 |
| S-032 | Kết quả xác thực/deep link | F-001 | WEB_DESKTOP/WEB_MOBILE/APP_IOS/APP_ANDROID | ST-04 | CMP-001, CMP-003, CMP-013, CMP-031, CMP-032, CMP-049, CMP-051 | UC-004 |
| S-033 | Đăng nhập admin | F-009 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-04 | CMP-001, CMP-003, CMP-004, CMP-010, CMP-013, CMP-031, CMP-032, CMP-050, CMP-052 | UC-016 |
| S-034 | Dashboard vận hành | F-009 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-08 | CMP-001, CMP-002, CMP-003, CMP-012, CMP-013, CMP-027, CMP-031, CMP-032, CMP-036, CMP-038, CMP-050, CMP-056 | UC-016, UC-026, UC-028 |
| S-035 | Catalog nguyên liệu | F-002, F-009 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-08 | CMP-001, CMP-002, CMP-003, CMP-004, CMP-007, CMP-008, CMP-011, CMP-012, CMP-013, CMP-014, CMP-031, CMP-032, CMP-034, CMP-035, CMP-036, CMP-037, CMP-050 | UC-017 |
| S-036 | Sản phẩm và variants | F-002, F-009 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-09 | CMP-001, CMP-003, CMP-004, CMP-005, CMP-006, CMP-007, CMP-008, CMP-010, CMP-013, CMP-015, CMP-016, CMP-031, CMP-032, CMP-034, CMP-036, CMP-039, CMP-044, CMP-045, CMP-050, CMP-054 | UC-017, UC-025 |
| S-037 | Nguyên liệu thị trường | F-003, F-006 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-08 | CMP-001, CMP-003, CMP-004, CMP-007, CMP-008, CMP-013, CMP-031, CMP-032, CMP-033, CMP-035, CMP-036, CMP-039, CMP-050 | UC-018, UC-021 |
| S-038 | Danh mục món | F-003, F-009 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-08 | CMP-001, CMP-003, CMP-011, CMP-012, CMP-013, CMP-014, CMP-031, CMP-032, CMP-035, CMP-036, CMP-037, CMP-050 | UC-018 |
| S-039 | Món, khẩu phần và công thức giao | F-003, F-006 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-09 | CMP-001, CMP-003, CMP-004, CMP-006, CMP-007, CMP-008, CMP-010, CMP-013, CMP-015, CMP-016, CMP-017, CMP-018, CMP-031, CMP-032, CMP-033, CMP-036, CMP-039, CMP-044, CMP-045, CMP-050, CMP-054 | UC-018, UC-025 |
| S-040 | Thư viện ảnh | F-015 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-08 | CMP-001, CMP-003, CMP-013, CMP-015, CMP-031, CMP-032, CMP-035, CMP-036, CMP-037, CMP-044, CMP-045, CMP-050 | UC-017, UC-019 |
| S-041 | Quản lý đơn | F-004, F-021 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-08 | CMP-001, CMP-002, CMP-003, CMP-007, CMP-009, CMP-011, CMP-012, CMP-013, CMP-024, CMP-031, CMP-032, CMP-034, CMP-035, CMP-036, CMP-037, CMP-050 | UC-020 |
| S-042 | Chi tiết đơn vận hành | F-004, F-005, F-007, F-021 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-10 | CMP-001, CMP-003, CMP-012, CMP-013, CMP-020, CMP-021, CMP-024, CMP-025, CMP-026, CMP-030, CMP-031, CMP-032, CMP-033, CMP-034, CMP-036, CMP-041, CMP-043, CMP-050, CMP-053, CMP-055 | UC-006, UC-020, UC-021, UC-022, UC-023, UC-025 |
| S-043 | Hàng đợi chuyển khoản | F-005 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-07 | CMP-001, CMP-003, CMP-005, CMP-010, CMP-011, CMP-012, CMP-013, CMP-020, CMP-023, CMP-031, CMP-032, CMP-033, CMP-035, CMP-036, CMP-037, CMP-050, CMP-053 | UC-006, UC-020 |
| S-044 | Danh sách đợt thu mua | F-006 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-08 | CMP-001, CMP-003, CMP-009, CMP-011, CMP-012, CMP-013, CMP-026, CMP-031, CMP-032, CMP-035, CMP-036, CMP-037, CMP-038, CMP-040, CMP-050 | UC-021 |
| S-045 | Chi tiết đợt và quyết định mua | F-006 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-10 | CMP-001, CMP-003, CMP-007, CMP-008, CMP-012, CMP-013, CMP-017, CMP-025, CMP-026, CMP-031, CMP-032, CMP-033, CMP-034, CMP-036, CMP-040, CMP-043, CMP-050, CMP-053 | UC-018, UC-021 |
| S-046 | Ghi nhận mua/nhận thực tế | F-006, F-007 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-10 | CMP-001, CMP-003, CMP-005, CMP-007, CMP-010, CMP-013, CMP-031, CMP-032, CMP-036, CMP-040, CMP-041, CMP-043, CMP-050 | UC-021 |
| S-047 | Bảng tập kết/sơ chế/đóng gói | F-007 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-10 | CMP-001, CMP-003, CMP-012, CMP-013, CMP-017, CMP-031, CMP-032, CMP-036, CMP-041, CMP-050 | UC-022 |
| S-048 | Bảng giao hàng | F-007, F-008 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-08 | CMP-001, CMP-002, CMP-003, CMP-007, CMP-009, CMP-011, CMP-012, CMP-013, CMP-031, CMP-032, CMP-034, CMP-035, CMP-036, CMP-037, CMP-038, CMP-042, CMP-050, CMP-055 | UC-022 |
| S-049 | Chi tiết giao/kết quả | F-007, F-021 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-10 | CMP-001, CMP-003, CMP-012, CMP-013, CMP-025, CMP-031, CMP-032, CMP-033, CMP-036, CMP-042, CMP-043, CMP-050, CMP-055 | UC-022 |
| S-050 | Ngoại lệ/thỏa thuận khách | F-021 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-10 | CMP-001, CMP-003, CMP-004, CMP-007, CMP-010, CMP-012, CMP-013, CMP-020, CMP-025, CMP-030, CMP-031, CMP-032, CMP-033, CMP-034, CMP-036, CMP-043, CMP-050, CMP-053 | UC-010, UC-020, UC-022, UC-023 |
| S-051 | Danh sách điều chỉnh/hoàn | F-021 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-08 | CMP-001, CMP-003, CMP-011, CMP-012, CMP-013, CMP-030, CMP-031, CMP-032, CMP-035, CMP-036, CMP-037, CMP-038, CMP-043, CMP-050 | UC-023 |
| S-052 | Lập/duyệt/thực hiện hoàn | F-021, F-010, F-012 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-07 | CMP-001, CMP-003, CMP-004, CMP-005, CMP-007, CMP-010, CMP-012, CMP-013, CMP-020, CMP-021, CMP-022, CMP-025, CMP-028, CMP-030, CMP-031, CMP-032, CMP-033, CMP-034, CMP-036, CMP-043, CMP-050, CMP-053 | UC-008, UC-010, UC-023 |
| S-053 | Danh sách yêu cầu rút | F-011 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-08 | CMP-001, CMP-003, CMP-011, CMP-012, CMP-013, CMP-027, CMP-029, CMP-031, CMP-032, CMP-035, CMP-036, CMP-037, CMP-038, CMP-050 | UC-007, UC-024 |
| S-054 | Duyệt/chuyển hoàn rút | F-011 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-07 | CMP-001, CMP-003, CMP-004, CMP-005, CMP-010, CMP-012, CMP-013, CMP-025, CMP-027, CMP-028, CMP-029, CMP-031, CMP-032, CMP-033, CMP-034, CMP-036, CMP-050, CMP-053 | UC-007, UC-024 |
| S-055 | Danh sách khách | F-009, F-010, F-012 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-08 | CMP-001, CMP-003, CMP-011, CMP-013, CMP-031, CMP-032, CMP-035, CMP-036, CMP-037, CMP-050, CMP-052 | UC-026 |
| S-056 | Chi tiết khách và sổ giao dịch | F-009, F-010, F-012, F-017 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-06 | CMP-001, CMP-003, CMP-012, CMP-013, CMP-021, CMP-022, CMP-025, CMP-027, CMP-028, CMP-030, CMP-031, CMP-032, CMP-036, CMP-047, CMP-050, CMP-052, CMP-055 | UC-008, UC-011, UC-023, UC-024, UC-026 |
| S-057 | Tài khoản admin/quyền | F-009 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-05 | CMP-001, CMP-003, CMP-004, CMP-007, CMP-008, CMP-010, CMP-013, CMP-031, CMP-032, CMP-033, CMP-036, CMP-050, CMP-052, CMP-053, CMP-054 | UC-016 |
| S-058 | Nhật ký thao tác | F-009 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-06 | CMP-001, CMP-002, CMP-003, CMP-011, CMP-013, CMP-025, CMP-028, CMP-031, CMP-032, CMP-035, CMP-036, CMP-037, CMP-050, CMP-052, CMP-053 | UC-016, UC-024, UC-026 |
| S-059 | Settings nghiệp vụ | F-014 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-05 | CMP-001, CMP-002, CMP-003, CMP-004, CMP-005, CMP-007, CMP-008, CMP-009, CMP-010, CMP-013, CMP-022, CMP-031, CMP-032, CMP-033, CMP-034, CMP-036, CMP-045, CMP-047, CMP-050, CMP-053, CMP-054 | UC-011, UC-025 |
| S-060 | Theo dõi gửi thông báo | F-013, F-020 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-08 | CMP-001, CMP-003, CMP-008, CMP-011, CMP-012, CMP-013, CMP-031, CMP-032, CMP-035, CMP-036, CMP-037, CMP-048, CMP-050, CMP-056 | UC-015, UC-028 |
| S-061 | Nội dung/chính sách | F-015 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-09 | CMP-001, CMP-003, CMP-004, CMP-010, CMP-013, CMP-015, CMP-018, CMP-031, CMP-032, CMP-036, CMP-044, CMP-045, CMP-050 | UC-019 |
| S-062 | Duyệt đánh giá | F-016 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-08 | CMP-001, CMP-003, CMP-011, CMP-012, CMP-013, CMP-031, CMP-032, CMP-033, CMP-035, CMP-036, CMP-037, CMP-046, CMP-050 | UC-014, UC-027 |
| S-063 | Báo cáo vận hành/tài chính [P] | F-009, F-014 | ADMIN_DESKTOP/ADMIN_COMPACT | ST-06 | CMP-001, CMP-003, CMP-007, CMP-009, CMP-011, CMP-012, CMP-013, CMP-020, CMP-027, CMP-028, CMP-031, CMP-032, CMP-035, CMP-036, CMP-038, CMP-050, CMP-054 | UC-026 |

## 7. Critical prototype fixtures và copy

| Fixture | Entry/state | Kết quả cần thể hiện |
| --- | --- | --- |
| F1 — cutoff | Clock21/10/2026 21:59→22:00 HCM | Min22/10→23/10; max vẫn28/10. Giao26/10 khóa self-cancel 22h25/10. UI stale phải yêu cầu chọn lại khi submit. |
| F2 — cash buckets | Wallet200k; rút150k; đặt dùng50k | Trước đặt available50k/pending-rút150k/held0/total200k. Sau đặt available0/held-đơn50k/pending-rút150k/total200k. |
| F3 — release/capture cash | Tiếp F2 | Cancel→available50k/held0/pending150k/total200k. Complete→available0/held0/pending150k/total150k trước sự kiện khác. Không credit/debit lại available. |
| F4 — points buckets | Có100points, dùng50 | Place→available50/held50/total100; cancel→100/0/100; complete→50/0/50 trước earn riêng. |
| F5 — allocation | G1m/cash200k/points50/fee0 hoặc20k | Bank750k hoặc770k; complete capture cash200k+50points, earn950 riêng. Opt-out points với fee20k: bank820k/earn1000. Caps chỉ demo. |
| F6 — refund sau complete | Order đã capture50points và earn950; earned points đã dùng ở B | Refund theo nguồn còn lại; RETURN50captured points khi full refund, giữ950ORDER_EARN, không debt/clawback/earn lại. |
| F7 — bank notice | Client báo đã chuyển hoặc admin duyệt mua/giao unpaid | Trạng thái chờ xác nhận/remaining due; chưa PAID. Admin cancel vận hành có actor/reason, customer cutoff không bị đổi. |
| F8 — financial unknown | Withdraw/refund BANK đang PROCESSING, save timeout | Giữ pending/claim, có hướng đối soát; approve khác settled, không chuyển lại mù hoặc release tiền. |

Dữ liệu demo phải ghi trong handoff; bank account/contact masked, không bịa credentials. Clock/scenario selector ngoài UI, khách không có nút đổi cutoff. Order/cash/points/refund/procurement tách status và timeline.

## 8. Navigation và behavior notes

Web: topnav danh mục/nguyên liệu/món, search/giỏ/account; mobile browser có nav đúng web, có thể bottomaction cho checkout. Flutter đề xuất bottomnav Trang chủ/Món ăn/Giỏ/Đơn/Tài khoản, appbar và Back theo OS. Admin: sidebar theo nhóm Catalog, Đơn/Thanh toán, Thu mua/Sơ chế/Giao, Tiền/Hoàn/Rút, Khách/Engagement, Nội dung, Cấu hình/Quyền/Audit.

Hiển thị return/login/guest, back/deeplink/reload, filter-retention, form dirty và keyboard/safe area. Modal/sheet không tạo action money khi dismiss; externalbank-appreturn lấy state mới. Offline cho xem cache cũ có nhãn, các money actions bị chặn/chờ on line, không hứa syncqueue.

## 9. Subviews/variants không được bỏ trong màn logic

| Screen ID | Variants/panels cần thiết kế |
| --- | --- |
| S-010 | Profile view/edit, logout và yêu cầu xóa tài khoản [P-011] |
| S-011 | Liên kết provider; thành công/cancel/conflict; phone tương lai là annotation, không nút baseline |
| S-013 | Add/edit/saved/outside-area, phone validation nhưng không OTP |
| S-014 | Points on/off/no points; available/pending; zero bank due; quote changed/22h crossed |
| S-020 | Preview cancel hợp lệ; blocked deadline; state vừa thay đổi; success/unknown outcome |
| S-021 | Full/partial/excess refund; tiền/điểm và nguồn gốc/kênh hoàn; pending/settled/held-release/captured-return |
| S-024 | Withdrawal PENDING/APPROVED/PROCESSING/PAID/REJECTED/CANCELLED, unknown bank theo P-002 |
| S-025 | Available/held/total; HOLD/CAPTURE/RELEASE/earn; thông tin cap; hoàn sau complete RETURN captured points, giữ ORDER_EARN D-100 |
| S-031 | Thông tin TPX/người bán, giao-hủy-hoàn, quyền riêng tư, hỗ trợ: layout/content variants |
| S-032 | Provider callback/deep link success, loading, cancelled, error, session cần đăng nhập lại |
| S-035 | Category management và RAW product list: create/edit/filter/archive references |
| S-036 | Create/edit RAW; variants/price/pack/ingredient mappings; validate/publish/availability |
| S-039 | Meal variants/portions; BOM units/version; cooking/source; publish/impact/restore proposal |
| S-043 | Receipt entry/confirmation, partial/excess/late/duplicate; đối soát chưa rõ kết quả |
| S-045 | Paid/unpaid/undecided/excluded tabs; quyết định có lý do; ingredient summary và sources |
| S-046 | Lượng mua/đạt/thiếu, chất lượng và actual cost; không sửa sales price snapshot |
| S-049 | Ready/dispatch/failure/retry-agreement/complete; unpaid guard theo P-008 |
| S-050 | Case list/detail, ảnh hưởng dòng hàng, agreement composer/version và trạng thái giải quyết |
| S-052 | Refund preview/approve/internal legs/bank claim/settle; partial/excess; release hold trước complete; sau complete RETURN captured points, giữ ORDER_EARN D-100 |
| S-054 | Approve/reject/claim processing/mark paid, bank reference, two-admin conflict và unknown outcome |
| S-056 | Customer profile/orders, money ledger, points ledger, referral; credit gắn adjustment đúng quyền |
| S-057 | Fixed accounts/status, role-permission matrix, sessions/revocation; không public signup/OTP |
| S-059 | Commerce/fee/minimum; vùng/slot; bank; loyalty caps; referral; reminders; version preview/validation |
| S-060 | Zalo/push/marketing/transactional attempts, missing-config/provider-fail/skip/retry |
| S-062 | Pending/published/hidden reviews; eligible purchase; reason moderation; read-only customer rating/text |
| S-063 | Orders/cash-in/refunds/wallet liability/points/cost-coverage modes, date basis và incomplete-data states |

## 10. Flow audit v0.2 là phần bắt buộc của handoff

28 UC ở trên là scenario groups, không phải tất cả action/case. Dùng thêm [25 journeys](13-detailed-journeys.md) và [100 FC](14-flow-case-matrix.md); map tới Screen IDs hiện có và actual prototype/frame. Không thêm63 màn mới, không coi190 default cells là đủ edge states. Với [16 action gaps](15-action-contract-gaps.md), dựng nhánh proposal và ghi capability thiếu; không tự biến thành policy/API đã duyệt.

Subviews bổ sung: S-008 merge/cart conflict; S-022/S-024 withdrawal history; S-026 recipient claim entry; S-028 my-review status; S-033/S-057 recovery capability/landing; S-043 unmatched/correction; S-045/S-046 allocation/delta; S-050 case fulfillment-vs-finance; S-056 deletion tracking; S-059 impacted-order/readiness. Các mutation còn thiếu contract phải được ghi rõ trong assumptions/fix-list.

## 11. Screen → journey/case bindings sau audit

Các FC dưới là case trọng tâm bổ sung; “UC/ST baseline” nghĩa là màn được bao phủ ở03 sections trước, chưa có FC mới riêng. Không suy ra Delivered từ mapping này.

| Screen ID | Journey | FC trọng tâm hoặc baseline |
| --- | --- | --- |
| S-001 | J-001, J-004 | UC/ST baseline; kiểm default/action states theo screen requirements |
| S-002 | J-001, J-004 | UC/ST baseline; kiểm default/action states theo screen requirements |
| S-003 | J-004 | FC-013 |
| S-004 | J-001, J-004, J-015, J-016 | FC-013, FC-014, FC-063 |
| S-005 | J-001, J-004 | UC/ST baseline; kiểm default/action states theo screen requirements |
| S-006 | J-001, J-004, J-015, J-016 | FC-013, FC-014, FC-015, FC-016 |
| S-007 | J-004 | FC-016 |
| S-008 | J-001, J-004, J-005, J-007, J-015 | FC-001, FC-002, FC-003, FC-004, FC-013, FC-015, FC-017, FC-018, FC-019, FC-020, FC-027, FC-057, FC-058, FC-059 |
| S-009 | J-001, J-002, J-014, J-017 | FC-001, FC-003, FC-005, FC-006, FC-008, FC-053 |
| S-010 | J-001, J-002, J-014, J-025 | FC-004, FC-008, FC-099, FC-100 |
| S-011 | J-002, J-025 | FC-007, FC-100 |
| S-012 | J-003 | FC-010 |
| S-013 | J-003 | FC-009, FC-010 |
| S-014 | J-003, J-005, J-006, J-007, J-012, J-013, J-015, J-020 | FC-009, FC-011, FC-019, FC-020, FC-021, FC-023, FC-024, FC-025, FC-026, FC-027, FC-028, FC-045, FC-049, FC-050, FC-077, FC-080 |
| S-015 | J-003, J-006, J-007, J-020 | FC-011, FC-021, FC-023, FC-024 |
| S-016 | J-007, J-008, J-010, J-020 | FC-029, FC-030, FC-031, FC-038, FC-079 |
| S-017 | J-007, J-008 | FC-025, FC-028 |
| S-018 | J-008, J-009, J-015 | FC-029, FC-057 |
| S-019 | J-003, J-006, J-007, J-008, J-009, J-010, J-011, J-013, J-015, J-016, J-017, J-023, J-025 | FC-010, FC-012, FC-022, FC-028, FC-029, FC-030, FC-032, FC-033, FC-034, FC-035, FC-036, FC-037, FC-038, FC-040, FC-057, FC-058, FC-061, FC-062, FC-064, FC-066, FC-090, FC-091, FC-097, FC-098 |
| S-020 | J-006, J-009 | FC-022, FC-033, FC-035 |
| S-021 | J-009, J-010, J-011, J-013, J-017, J-025 | FC-034, FC-041, FC-043, FC-044 |
| S-022 | J-007, J-009, J-011, J-012, J-025 | FC-033, FC-045, FC-099 |
| S-023 | J-012 | FC-045, FC-047 |
| S-024 | J-012, J-017, J-025 | FC-046, FC-047, FC-048, FC-099 |
| S-025 | J-007, J-009, J-011, J-013, J-023 | FC-033, FC-044, FC-049, FC-050, FC-051, FC-052, FC-092 |
| S-026 | J-014 | FC-053, FC-054, FC-055, FC-056 |
| S-027 | J-015 | FC-060 |
| S-028 | J-016 | FC-061, FC-062, FC-063, FC-064 |
| S-029 | J-017 | FC-066 |
| S-030 | J-017 | FC-065, FC-067 |
| S-031 | J-010, J-025 | FC-039, FC-097, FC-098 |
| S-032 | J-001, J-002, J-014, J-017 | FC-001, FC-005, FC-006, FC-053, FC-066 |
| S-033 | J-018 | FC-069, FC-072 |
| S-034 | J-018, J-020, J-021, J-024 | FC-069 |
| S-035 | J-019 | FC-075 |
| S-036 | J-019 | FC-073, FC-075, FC-076 |
| S-037 | J-019 | FC-074 |
| S-038 | J-019 | UC/ST baseline; kiểm default/action states theo screen requirements |
| S-039 | J-019, J-022 | FC-073, FC-076 |
| S-040 | J-019 | FC-073 |
| S-041 | J-021 | UC/ST baseline; kiểm default/action states theo screen requirements |
| S-042 | J-008, J-009, J-010, J-020, J-021, J-022, J-023, J-024 | FC-078, FC-079, FC-082, FC-083, FC-086, FC-089, FC-093 |
| S-043 | J-008, J-009, J-024 | FC-030, FC-031, FC-032, FC-036, FC-093, FC-094 |
| S-044 | J-006, J-021 | FC-081 |
| S-045 | J-006, J-010, J-019, J-021, J-022 | FC-022, FC-037, FC-074, FC-081, FC-082, FC-083, FC-084, FC-085, FC-088 |
| S-046 | J-010, J-021, J-022 | FC-084, FC-085, FC-086, FC-087, FC-088 |
| S-047 | J-022, J-023 | FC-088, FC-089 |
| S-048 | J-023 | UC/ST baseline; kiểm default/action states theo screen requirements |
| S-049 | J-023 | FC-089, FC-090, FC-091, FC-092 |
| S-050 | J-008, J-009, J-010, J-011, J-019, J-021, J-022, J-023, J-024, J-025 | FC-036, FC-037, FC-038, FC-039, FC-040, FC-074, FC-083, FC-086, FC-087, FC-090, FC-091, FC-092, FC-094, FC-097 |
| S-051 | J-011, J-024 | UC/ST baseline; kiểm default/action states theo screen requirements |
| S-052 | J-009, J-010, J-011, J-013, J-024, J-025 | FC-034, FC-040, FC-041, FC-042, FC-043, FC-044, FC-051 |
| S-053 | J-012, J-024 | UC/ST baseline; kiểm default/action states theo screen requirements |
| S-054 | J-012, J-024, J-025 | FC-046, FC-047, FC-048 |
| S-055 | J-025 | UC/ST baseline; kiểm default/action states theo screen requirements |
| S-056 | J-011, J-012, J-013, J-014, J-024, J-025 | FC-052, FC-055, FC-056, FC-095, FC-099, FC-100 |
| S-057 | J-018 | FC-070, FC-071, FC-072 |
| S-058 | J-012, J-018, J-024, J-025 | FC-070, FC-071, FC-093, FC-096 |
| S-059 | J-003, J-014, J-020 | FC-012, FC-056, FC-077, FC-078, FC-079, FC-080 |
| S-060 | J-017 | FC-067, FC-068 |
| S-061 | J-019 | UC/ST baseline; kiểm default/action states theo screen requirements |
| S-062 | J-016 | FC-063, FC-064 |
| S-063 | J-020, J-024 | FC-095, FC-096 |

## 12. Policy branches cần prototype, không tự duyệt

Quy tắc mới nhất: D-093–100. OQ-048/049 đã đóng: cả cash/points hold và refund sau complete giữ ORDER_EARN. **OQ-050/OQ-042 chưa có trả lời**, yêu cầu các variant dưới để review. A/B là tên branch thiết kế, không phải option user đã chọn hoặc setting tự tạo.

| Câu hỏi / màn | Branch A đề xuất | Branch B đề xuất | Bằng chứng thiết kế |
| --- | --- | --- | --- |
| OQ-050 · S-042/S-049/S-019/S-025 | Admin đã giao thiếu tiền nhưng complete đợi thu đủ; show delivered/remaining due, holds chưa capture và earn chưa cấp | Admin explicit complete khi còn thiếu; show confirm remaining due/audit, capture holds và earn chỉ khi completion được duyệt theo branch này; số phải thu còn giữ | Direct frames cho delivered-unpaid, quyết định complete/blocked, tiền/điểm trước-sau, cancel dialog/back; không auto PAID hoặc tự chọn default policy |
| OQ-042 · S-042/S-050/S-014/S-016/S-021 | Sau phương án khách đồng ý, re-quote nghĩa vụ mới và reserve/release delta cash/points theo nguồn khả dụng/caps/opt-in, bank phần thiếu | Phần tăng thêm chỉ bank transfer, không tự tăng holds nguồn nội bộ; phần giảm release holds/refund captured theo nguồn đã thống nhất | Before/after items/qty/total/fee/hold/due, khách đồng ý, admin preview/apply, quote changed/insufficient available/cancel/unknown; branch annotation ngoài UI |

Không biến việc “admin có chức năng update” thành mọi field/settlement đều đã được duyệt. Partial giảm chưa complete không vừa RELEASE hold vừa credit refund; sau complete không thu hồi ORDER_EARN. Refund bank pending không tự chặn phần hàng đã thống nhất. Nhánh nào công cụ không mô phỏng được phải có frame/state notes và limitation.

Các phần P-002/003/005/006/007/009/010/011/013/016/017/019 còn proposal theo từng phần: lifecycle rút/partial split/fee-first/referral restore/consent/recovery/allocation... cần label assumptions và hiện lý do disabled/error. Không hỏi lại hoặc dựng branch phủ nhận các phần đã chốt.
