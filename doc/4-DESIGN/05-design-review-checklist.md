# Checklist review design output — TPX

> v0.4 · 2026-10-25. Chỉ dùng nghiệm thu actual output; các ô vẫn unchecked. Kiểm brief có báo cáo riêng tại11.

## Hai packages và source

- [ ] Có Design System Package và UI Workflow Package, nguồn editable/artifact/prototype thật và capabilities/limitations.
- [ ] Có foundation/component gallery, token JSON đầy đủ, component/state matrix, assets/fonts/source và implementation notes.
- [ ] Có21story/116 AC,63 Screen IDs,56 CMP,25 J/100 FC và đủ190 screen×surface default evidence; P1 không bị bỏ.
- [ ] Screen/flow/story/journey-case/state/surface maps link actual frame/prototype; Delivered không dùng expected counts thay evidence.

## Visual system và platform

- [ ] Giữ #309953/#F9A01B; actual contrast pairs được đo, không trắng chữ nhỏ trên brand pair thiếu contrast.
- [ ] Typography Việt/tabular money, spacing/layout/density/shapes/motion đủ spec, aliases resolve và CSS/Flutter unit mapping.
- [ ] Component anatomy/properties/variants/states, usage, source/frame, responsive/native behavior đủ cho56 CMP.
- [ ] Web desktop/mobile, iOS/Android và admin desktop/compact có layout/navigation phù hợp; shared frame có proof/notes.
- [ ] Keyboard/focus/labels/read order/text scale/touch targets/keyboard-safe area/reduced motion; social assets đúng branding.

## Business-critical states

- [ ] RAW/MEAL mixed order, variants/portions/BOM/instructions, không gia vị/sốt/custom ingredient hoặc claim nông trại giả.
- [ ] Trước/đúng/sau22h, ngày +7, cutoff D−1, future order và checkout qua mốc được thể hiện.
- [ ] Cash available/held_order/pending_withdrawal/total và points available/held/total khác nhau; chỉ available được dùng/rút.
- [ ] Place giữ cash+points; complete capture không trừ available lần hai; cancel release một lần; quote/mutation unknown không nhân holds.
- [ ] Full/partial refund trước complete không vừa release vừa credit cùng nguồn; sau complete RETURN nguồn đã capture và giữ ORDER_EARN.
- [ ] Bank receipt/remaining/excess/late/unmatched, customer notice khác PAID, zero due không yêu cầu transfer0đ.
- [ ] Admin mua/giao thiếu tiền có decision/remaining/audit; không PAID giả/COD; OQ-050 complete branches có annotation.
- [ ] Admin cancel dùng CANCELLED/actor/reason; self-cancel cutoff giữ nguyên; không NOT_FULFILLED/fake complete.
- [ ] Admin update before/after/hold delta/remaining/refund; OQ-042 branches không tự chốt settlement.
- [ ] Bank refund pending không tự chặn phần hàng đã thống nhất; unknown payout giữ pending và không chuyển lại mù.

## Flow, recovery và nội dung

- [ ] Mỗi J/FC có entry/precondition/action/result/success/exception/recovery/exit, actor lanes và source/frame evidence.
- [ ] Guest/cart merge/multi-device, OAuth/bank-app return/cold start, private deep link/account switch/logout, ownership và expired session đủ state.
- [ ] Loading/empty/validation/offline/access/locked/submitting/conflict/unknown/success đúng màn; critical states có frame trực tiếp.
- [ ] Withdraw history/my-review/referral recipient/support/deletion/admin recovery, catalog/content/settings/roles/reports subviews có entry/back.
- [ ] Các nguồn config/fee/caps/reward demo không thành default; provider unavailable không giả gửi/login thành công; consent khác OS permission.
- [ ] Copy sản phẩm tiếng Việt, số tiền/điểm/đơn vị rõ; technical IDs chỉ trong annotations. Không thêm tính năng ngoài scope.

## Review policy và handoff

- [ ] D-093–100 áp dụng đúng, OQ-048/049 đã đóng; không quay lại debt/clawback/mặc định hard-block dispatch thiếu tiền.
- [ ] OQ-050/OQ-042 và các phần P còn mở có branch/assumption riêng; không đánh đồng toàn bộ19topics đều pending hoặc approved.
- [ ] AG-001–016 có disposition/capability status hiện tại; prototype không tự đóng backend gaps.
- [ ] Actual exports/manifest/fix-list có version và Missing/Needs-fix; code tasks chỉ ready sau dependency/gate phù hợp.
