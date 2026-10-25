# Feature Inventory

> PRD v0.1 — Draft sẵn review. Tất cả21 feature thuộc R1; P0/P1 là thứ tự làm, **không phải hoãn P1 khỏi bản đầy đủ**. Dependencies là foundation để đặc tả; test tích hợp complete/refund liên module vẫn cần thực hiện. Chưa là delivery task graph.

| Feature ID | Feature/spec | Priority | Release | Foundation dependencies | Source | Policy còn review |
| --- | --- | --- | --- | --- | --- | --- |
| F-001 | [Định danh, social login và hồ sơ khách](04-detailed-feature-specs/F-001.md) | P0 | R1 | — | BR-014; D-087–089; TD-025 | P-011/P-012 |
| F-002 | [Catalog nguyên liệu thô](04-detailed-feature-specs/F-002.md) | P0 | R1 | F-009 | BR-008/009/027 | P-007 |
| F-003 | [Món sơ chế, khẩu phần và công thức](04-detailed-feature-specs/F-003.md) | P0 | R1 | F-002, F-009 | BR-027/031–034 | P-007 |
| F-004 | [Giỏ chung, báo giá và đặt đơn](04-detailed-feature-specs/F-004.md) | P0 | R1 | F-001, F-002, F-003, F-008, F-010, F-012, F-014 | BR-005/020/025/027; D-081/082 | P-001/P-005/P-006 |
| F-005 | [Chuyển khoản và xác nhận thủ công](04-detailed-feature-specs/F-005.md) | P0 | R1 | F-004, F-009 | BR-005/012; D-048/068 | P-001/P-006 |
| F-006 | [Đợt thu mua và tổng hợp nhu cầu](04-detailed-feature-specs/F-006.md) | P0 | R1 | F-004, F-005, F-009 | BR-002/003/012; D-080 | P-006/P-008 |
| F-007 | [Tập kết, sơ chế và giao hàng](04-detailed-feature-specs/F-007.md) | P0 | R1 | F-006, F-009 | BR-003/007/026/031 | P-008 |
| F-008 | [Ngày giao, vùng giao và khung giờ](04-detailed-feature-specs/F-008.md) | P0 | R1 | F-014 | BR-002/006/007/011/034; D-079/080 | P-009 |
| F-009 | [Admin, RBAC, audit và dashboard](04-detailed-feature-specs/F-009.md) | P0 | R1 | — | BR-012/015; D-086; TD-020 | P-010/P-011 |
| F-010 | [Số dư tiền hoàn và lịch sử](04-detailed-feature-specs/F-010.md) | P0 | R1 | F-001, F-009 | BR-017–022/035 | P-001 |
| F-011 | [Yêu cầu rút và chuyển hoàn ngân hàng](04-detailed-feature-specs/F-011.md) | P0 | R1 | F-010, F-009 | BR-019/035; D-078 | P-002 |
| F-012 | [Tích, dùng, hoàn và thu hồi loyalty](04-detailed-feature-specs/F-012.md) | P0 | R1 | F-009, F-014 | BR-023–025/036/037; D-081–085 | P-003/P-004/P-005 |
| F-013 | [Thông báo giao dịch Zalo/push](04-detailed-feature-specs/F-013.md) | P0 | R1 | F-001, F-009 | BR-016; D-032 | P-010 |
| F-014 | [Settings và báo cáo cấu hình](04-detailed-feature-specs/F-014.md) | P0 | R1 | F-009 | BR-010/024/029 | P-009/P-010 |
| F-015 | [Nội dung minh bạch và ảnh](04-detailed-feature-specs/F-015.md) | P1 | R1 | F-002, F-003, F-009 | BR-028/032; D-013 | P-010 |
| F-016 | [Đánh giá verified purchase](04-detailed-feature-specs/F-016.md) | P1 | R1 | F-001, F-007, F-015 | BR-028 | P-010 |
| F-017 | [Referral và thưởng điểm](04-detailed-feature-specs/F-017.md) | P1 | R1 | F-001, F-007, F-012, F-014 | BR-029; D-054/073 | P-006 |
| F-018 | [Mua lại đơn](04-detailed-feature-specs/F-018.md) | P1 | R1 | F-001, F-004 | BR-030 | P-010 |
| F-019 | [Danh sách món thường mua](04-detailed-feature-specs/F-019.md) | P1 | R1 | F-001, F-004, F-007 | BR-030 | P-010 |
| F-020 | [Nhắc đặt trước giờ chốt](04-detailed-feature-specs/F-020.md) | P1 | R1 | F-001, F-013, F-014 | BR-030 | P-010 |
| F-021 | [Hủy, thiếu hàng, điều chỉnh và hoàn](04-detailed-feature-specs/F-021.md) | P0 | R1 | F-004, F-005, F-007, F-010, F-011, F-012 | BR-004/011/026/034/036/037 | P-001/P-003/P-004/P-008 |

Khách có một flow chung household/restaurant, không role B2B/giá sỉ riêng. Một backend phục vụ web và Flutter; admin riêng, không có app nhân viên/shipper độc lập. Những quyết định cần review nằm trong [review register](11-review-decisions.md).
