# Design system requirements — TPX

> v0.4 · 2026-10-25. Đây là yêu cầu đầu vào, chưa có library delivered. Hai brand colors đã chốt; font/scale/shades/layout là phương án designer cụ thể hóa và review.

## 1. Foundation boards và token architecture

Primitive → semantic → component tokens, alias resolve được, không cycle. Dùng tên ổn định, giá trị có type/unit/description. Mapping web CSS variables/React và Flutter theme cùng semantic intent, không yêu cầu Flutter import CSS.

| Nhóm token | Nội dung phải xuất | Mẫu kiểm tra |
| --- | --- | --- |
| Color | Brand #309953/#F9A01B; neutral/text/surface/border/action/status/focus/disabled/overlay | Default/hover/pressed/focus/disabled và contrast table cho actual pairs |
| Typography | Font Việt/license/fallback, weights, heading/body/label/caption/numeric, line-height/tracking | Tên món nhiều dấu, địa chỉ dài, 1.000.000đ, điểm/qty; đề xuất consumer 16–18px/admin 14–16px |
| Spacing/sizing | Insets/gaps, heights, hit areas, max-width, density | Đề xuất base 4px, scale 4/8/12/16/24/32/48; actual layout constraints |
| Shape/border/elevation | Radius, strokes, shadows, focus rings | Cards/input/dialog/sheet có hierarchy, không dựa shadow để nhận biết state |
| Layout/breakpoints | Columns/gutters/containers, overflow, sticky header/CTA, safe area/keyboard | Nêu layout rule giữa widths, không chỉ liệt kê breakpoints |
| Motion | Timing/easing cho press/transition/loading, reduced-motion | Đề xuất 120–240ms; animation không che số tiền hoặc khẳng định success sớm |
| Assets/icons | Một icon family, sizes/strokes/labels; image ratio/placeholder/source/alt | Product RAW/MEAL, cooking instructions, social identity assets |
| Domain | Cash available/held-order/pending-withdrawal; points available/held; order/payment/refund/procurement | Mỗi bucket/status có label/icon/text, không gom mọi pending thành một màu hoặc một con số |

Gallery phải cho xem foundations và component instances đủ states, không chỉ bảng token chữ. Đề xuất light theme; dark theme ngoài phạm vi bắt buộc. Logo chưa chốt dùng wordmark tạm, không chặn flow design.

## 2. Color và accessibility

Brand primitive giữ nguyên, semantic action/text có thể dùng shade khác. Phép tính sRGB: trắng trên #309953≈3,62:1; trắng trên #F9A01B≈2,08:1. Ví dụ shade đề xuất #237B3F/trắng≈5,28:1; #F9A01B/chữ #142118≈7,99:1. Designer đo lại tất cả actual foreground/background pairs, không suy ra brand color mặc nhiên phù hợp chữ trắng.

Target text 4,5:1 và large text 3:1 theo [W3C contrast guidance](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). TPX đề xuất hit area chính 44CSSpx web và 48logicalpx Flutter; đây là project target, khác minimum 24CSSpx và exceptions của [W3C target size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).

Focus-visible/keyboard/read order, label/help/error/required, screen-reader announcements, text scale 200%, reduced motion và thông tin không chỉ bằng màu. Critical examples: checkout, wallet, withdraw, admin receipt/refund/delivery. Đo actual design, không gắn badge accessibility-pass chỉ vì dùng thư viện.

Social buttons dùng provider assets/branding: [Google guidance](https://developers.google.com/identity/branding-guidelines), [Apple guidance](https://developer.apple.com/design/human-interface-guidelines/sign-in-with-apple). Không recolor logo provider thành xanh TPX; nội dung tiếng Việt và phương án provider unavailable/cancel phải rõ.

## 3. Layout và interaction theo platform

| Surface | Viewport mẫu đề xuất | Behavior phải bàn giao |
| --- | --- | --- |
| WEB_DESKTOP | 1440CSSpx | Header/search/catalog, grid, checkout summary; keyboard/focus, direct URL/refresh, browser Back/multi-tab |
| WEB_MOBILE | 390CSSpx; check320/360 | Nav mobile, filter sheets, sticky CTA không che tổng/field error, keyboard/scroll, bank-app return |
| APP_IOS | 390logicalpx | Native shell, safe area, keyboard, sheet dismissal/back gesture, cold/warm start, auth/push/deep link |
| APP_ANDROID | 412logicalpx | System Back/activity resume, keyboard, native surfaces, provider/push return; khác biệt có notes |
| ADMIN_DESKTOP | 1440CSSpx | Sidebar, breadcrumbs, filter/table/detail, row actions, unsaved changes và reason confirmations |
| ADMIN_COMPACT | 390CSSpx | Prioritized fields/list-detail, readable totals/destination, sticky action vừa đủ; không thu nhỏ toàn bảng |

Tablet 768–1024 cần adaptive rules; hỗ trợ text dài và desktop zoom. Breakpoints/viewports là đề xuất thiết kế, không phải giới hạn thiết bị production đã chốt. Web không ép cài app để hoàn tất đơn; admin không có app nhân viên riêng.

## 4. Component contract

56 CMP trong [inventory](04-component-inventory.md), gồm primitives và domain patterns. Mỗi CMP bàn giao purpose/anatomy/properties; variants/sizes/states; semantic tokens; dimensions/constraints; responsive/native behavior; interaction/validation/accessibility; usage/do-don’t; Screens/J/FC refs và actual source/frame.

Default/hover(web)/pressed/focus-visible/selected/disabled/submitting/loading/empty/invalid/network/offline/access/locked/stale/conflict/unknown/success phải được xác định theo loại component. N/A có lý do; không nhân mọi state lên mọi component một cách máy móc. State reused cần instance/context rõ.

Form giữ input khi lỗi, focus field sai, pending không tạo success. Confirmation nêu action/amount/source/destination/reason và hậu quả. Table có filters/sort/pagination/selection/empty/stale, compact drilldown và action permission. Multi-select/bulk chỉ là pattern; không tự thêm bulk financial commands ngoài PRD.

## 5. Domain patterns ưu tiên

- CMP-020 price allocation: hàng/fee, cash hold, points hold, bank remaining và earn dự kiến; quote khác order đã tạo.
- CMP-021/CMP-027/CMP-028: cash available/held_order/pending_withdrawal/total; points available/held/total. HOLD chuyển bucket, CAPTURE chỉ giảm held, RELEASE mở lại; không dùng cùng nhãn cho tiền và điểm.
- CMP-022: points opt-in/caps, held/captured/released/earned/returned; refund sau complete giữ earned points, không debt/clawback.
- CMP-024/025/026: order, funding, procurement, refund tách trục; absolute cutoff22h D−1, admin cancel khác customer cancel.
- CMP-029/030: request/review/process/unknown/settle, source cash vs payout bank/points, hold-release khác refund captured; pending chưa settled.
- CMP-040/041/042/043: nguồn RAW/BOM, quantity/unit/demand revision, shortage/allocation, agreement, delivery outcome, admin dispatch thiếu tiền và refund pending không tự block phần hàng đã thống nhất.
- CMP-051/052/053/054: provider/session/access, version conflict/recovery/audit; chỉ expose capabilities có contract hoặc annotation proposal.

Thông tin OQ-050 và OQ-042 thể hiện theo branch requirements ở03, không bake một policy chưa chốt vào default component. UI copy không chứa HOLD/CAPTURE/ORDER_EARN/enum/API/P-ID; dùng “Đang giữ cho đơn”, “Đã sử dụng”, “Đã mở giữ”, “Điểm đã tích” phù hợp context.

## 6. Chất lượng và bàn giao

Font có license/provenance và glyph tiếng Việt; images có actual source/license/demo flag/alt; icon style thống nhất. Không giả ảnh trang trại là nguồn gốc hàng. Bàn giao token JSON thực có đầy đủ giá trị, aliases và unit mapping; component gallery/states/source refs cùng accessibility report theo [output contract](07-claude-design-output-contract.md).
