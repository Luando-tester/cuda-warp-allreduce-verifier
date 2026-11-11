<!-- Ban thao do Gemini lam qua Pepper Hunter Doer - CHUA NOP, can duyet truoc khi gui. -->

Chào bạn, với vai trò là kỹ sư phần mềm, tôi đã phân tích yêu cầu từ issue được cung cấp và lập tài liệu `SOLUTION.md` theo đúng các tiêu chí của bạn, đảm bảo không bịa đặt thêm chi tiết ngoài nội dung issue.

Dưới đây là nội dung chi tiết của tệp `SOLUTION.md`:

```markdown
# SOLUTION.md - Align SM90 warp butterfly accumulator rounding across subnormal lane boundaries

## 1. Tóm tắt yêu cầu + Tiêu chí nghiệm thu (trích từ issue)

### Tóm tắt yêu cầu (Problem Summary)
1. Sửa lỗi hàm `reduce_warp_fp8_lanes` trong `nv_warp/butterfly_reduce.py` hiện đang từ chối các frame có độ dài byte bằng với `frame_ceiling` (gắn mã lỗi `VEC-14-EXACT-CEILING-BOUNDARY`).
2. Căn chỉnh lại `SM90_FMA_MANTISSA_BIAS` và `BUTTERFLY_LANE_STRIDE` trong `nv_warp/butterfly_reduce.py` (lưu ý: **không được sửa đổi** file `tests/check_sm90_ulp.py`).

### Tiêu chí nghiệm thu (Acceptance Criteria)
- Chạy lệnh `python3 tests/check_sm90_ulp.py` vượt qua tất cả 24 vectors (được định nghĩa qua các specification shards hoặc tập kiểm thử đi kèm).
- CI quorum chuyển sang trạng thái "green" (để giải phóng tiền thưởng escrow tự động).

---

## 2. Cách tiếp cận kỹ thuật từng bước

1. **Khắc phục lỗi biên (Boundary Check Fix):**
   - Kiểm tra logic điều kiện kiểm tra độ dài byte của frame trong hàm `reduce_warp_fp8_lanes` tại `nv_warp/butterfly_reduce.py`.
   - Sửa đổi toán tử so sánh (ví dụ: từ `<=` hoặc `<` thành điều kiện chính xác cho phép `frame_ceiling`) để tránh việc từ chối các frame có độ dài byte bằng `frame_ceiling`.

2. **Căn chỉnh thông số toán học và stride:**
   - Điều chỉnh giá trị của `SM90_FMA_MANTISSA_BIAS`.
   - Điều chỉnh giá trị của `BUTTERFLY_LANE_STRIDE`.
   - Mục tiêu căn chỉnh là đảm bảo tích lũy làm tròn (accumulator rounding) qua các ranh giới lane subnormal khớp hoàn toàn với tiêu chuẩn IEEE-754-2019 §5.4.1 / CUDA Math ABI v12.6 mà không làm thay đổi hay can thiệp vào test suite gốc (`tests/check_sm90_ulp.py`).

---

## 3. File / Đường dẫn dự kiến sửa
*(Dựa trên cấu trúc repo thể hiện trong issue)*

- `nv_warp/butterfly_reduce.py` (File duy nhất được phép và cần thiết chỉnh sửa để cập nhật `reduce_warp_fp8_lanes`, `SM90_FMA_MANTISSA_BIAS`, và `BUTTERFLY_LANE_STRIDE`).

---

## 4. Kế hoạch tự test (Self-Test Plan)

1. **Kiểm tra môi trường:** Đảm bảo môi trường Python và các công cụ CUDA/Math tương thích với CUDA Math ABI v12.6.
2. **Chạy tập kiểm thử ULP:**
   ```bash
   python3 tests/check_sm90_ulp.py
   ```
3. **Xác nhận kết quả:** 
   - Đảm bảo script trả về kết quả thành công (pass) cho toàn bộ 24 vectors.
   - Xác nhận không có bất kỳ thay đổi nào được thực hiện lên thư mục hoặc file `tests/check_sm90_ulp.py`.
```
