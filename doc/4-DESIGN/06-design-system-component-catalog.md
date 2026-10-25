# Catalog được chọn cho TPX

> Bản chọn theo archetype thương mại thực phẩm/operations, thay catalog template đa ngành. Source of truth cho IDs là [56 components](04-component-inventory.md); contract fields tại [output contract](07-claude-design-output-contract.md).

## Nhóm cần thiết kế

| Nhóm | Component ID | Phạm vi |
| --- | --- | --- |
| Foundation/action/forms | CMP-001–013 | Typography/money, buttons/inputs/selects/quantity/date/filters/status/panels |
| Consumer commerce/content | CMP-014–019 | Product/meal/variant/supplied ingredients/cooking/cart/reorder |
| Tiền, loyalty và đơn | CMP-020–030 | Allocation/bank/points/timeline/cutoff/wallet/ledger/withdraw/refund |
| Feedback/overlay | CMP-031–034 | Error/loading/offline/access/conflict/unknown, confirmations/sheets/drawers |
| Admin operations/data | CMP-035–043 | Search/filter/tables/pagination/metrics/BOM/procurement/prep/delivery/case |
| Content/engagement | CMP-044–048 | Media/content/reviews/referral/notificationconsent |
| Platform shells/identity/adminutility | CMP-049–056 | Web/app/admin shells, social/accountaccess/audit/settings/address/attempts |

## Không bật từ catalog template chung

Không game/education/AI/OCR/chat, paywall/subscription/IAP/ads, map/GPS, shoppinglist tự do, COD/topup/rút points/OTP baseline. Locked/error phải theo domain TPX, không dùng banner “Nâng cấp gói” hoặc “Xem quảng cáo nhận điểm”.

## Component spec tối thiểu

ID/name/purpose; anatomy; properties/variants; states; tokens; dimensions/layoutconstraints; breakpoint/platform differences; accessibility; interaction/validation; usage/do/don’t; Screens/Flows/CMPdependencies; priority; source/frame/exportreference. Designer có thể đề xuất CMP mới nếu màn thực tế cần, nhưng ghi reason và mapping, không tự thêm feature business.
