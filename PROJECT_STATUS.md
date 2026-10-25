# Project Status — TPX

## Snapshot

| Mục | Giá trị |
| --- | --- |
| Dự án | Thực phẩm xanh (TPX) |
| Gate hiện tại | BRD/PRD/Technical đang review; chưa freeze G2/G3/G4 |
| Phase hiện tại | Design brief v0.4 đã kiểm tra DS/UI flows và source; chờ actual design, complete-unpaid/update settlement còn review |
| Trạng thái | Design Brief v0.4 Ready — OQ-050/042 Branches Annotated |
| Người quyết định | User |
| Cập nhật | 2026-10-25 |

## Hồ sơ và tiến độ sản phẩm

| Nhóm | Hồ sơ hiện tại | Gate/sản phẩm |
| --- | --- | --- |
| Business/BRD | Quy tắc và scope theo D-001–101 | Chưa freeze |
| PRD | 21 specs, 63 screens/routes, 119 API, 116 feature AC, 42 QA, 18 NFR | Draft sẵn review, 19 chủ đề review có phần đã chốt D-093–100, OQ-048/049 đã đóng; còn OQ-050/042 |
| Technical | Stack duyệt; 68 bảng logic/API/state/security/cache/integrations | TD-001–026, schema/contracts chưa freeze |
| Design handoff | Prompt/context v0.4, 21 stories/63 screens/56 CMP/190 cells + 25 J/100 FC/16 AG | Inputs ready; actual DS/UI output Pending |
| Delivery graph | Traceability/test plan đã soạn | Chưa phân rã tasks implementation |
| Implementation | Chưa bắt đầu | Không tạo skeleton/migration/account |
| QA/Release | AC/scenarios là đặc tả kiểm thử | Chưa có product test/release results |

## Task Summary

| Status | Count |
| --- | --- |
| Todo | 0 |
| Ready | 0 |
| Running | 1 |
| Review | 1 |
| Done | 27 |
| Blocked | 0 |

Các task Done hiện là công việc hồ sơ; không đại diện phần trăm hoàn thành sản phẩm.

## Next Actions

1. Review [PRD overview](doc/2-PRD/00-prd-overview.md), theo [P-001–019](doc/2-PRD/11-review-decisions.md) cho các chi tiết tiền/state/UX chưa chốt. Firebase Auth và SĐT checkout đã chốt, không hỏi lại.
2. Chốt schema/API/session/targets và các policy còn review trước Technical freeze; tiếp tục dùng server user có sẵn, không khảo sát mua máy/ngân sách.
3. OQ-048/049 đã đóng: joint hold và refund giữ ORDER_EARN; tiếp tục OQ-050/OQ-042 và các review còn lại. Dùng prompt/context v0.4 khi design; không dùng lại đề xuất debt hoặc mandatory-funded-dispatch cũ.
4. Credentials và dữ liệu vận hành cấu hình trước release; không yêu cầu cung cấp secret trong PRD hoặc tạo account lúc này.

## Unblocked

Đã unblock đặc tả hold/capture/release points, admin cancel, admin quyết giao thiếu tiền, update đơn và tách giao hàng khỏi refund pending. OQ-048/049 đã đóng; OQ-050/042 còn mở; actual design/implementation chưa có, Technical gate chưa freeze.

## Git publication

T-029 đang chuẩn bị initial commit và push tới origin main (hwgapp/tpx). Chỉ publish hồ sơ/tooling hiện có, implementation vẫn chưa bắt đầu.
