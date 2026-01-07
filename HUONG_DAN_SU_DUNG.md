# HƯỚNG DẪN SỬ DỤNG ỨNG DỤNG XỬ LÝ ẢNH

## Tổng quan

Ứng dụng xử lý ảnh tổng hợp này cung cấp giao diện đồ họa thân thiện để thực hiện 12 bài tập xử lý ảnh từ cơ bản đến nâng cao.

## Giao diện chính

```
┌─────────────────────────────────────────────────────────────────────┐
│  Ứng Dụng Xử Lý Ảnh - Bài 1-12                                      │
├──────────────────┬──────────────────────────────────────────────────┤
│  PANEL ĐIỀU      │  HIỂN THỊ ẢNH                                    │
│  KHIỂN           │  ┌──────────────┬──────────────┐                │
│                  │  │  Ảnh gốc     │  Ảnh xử lý   │                │
│ [Tải ảnh]        │  │              │              │                │
│ [Lưu ảnh]        │  │              │              │                │
│ [Reset]          │  │              │              │                │
│                  │  │              │              │                │
│ Bài 1-3: Cơ bản │  └──────────────┴──────────────┘                │
│ ├─ Ảnh xám       │                                                  │
│ ├─ Phân ngưỡng   │  THÔNG TIN                                       │
│ └─ Tách kênh     │  ┌──────────────────────────────┐               │
│                  │  │ Thông tin về ảnh và          │               │
│ Bài 4-6: Hist   │  │ kỹ thuật xử lý hiện tại      │               │
│ ├─ Kéo giãn      │  └──────────────────────────────┘               │
│ ├─ Cân bằng      │                                                  │
│ ├─ Khớp          │                                                  │
│ └─ CLAHE         │                                                  │
│                  │                                                  │
│ ... (và nhiều    │                                                  │
│      chức năng   │                                                  │
│      khác)       │                                                  │
└──────────────────┴──────────────────────────────────────────────────┘
```

## Quy trình sử dụng cơ bản

### Bước 1: Khởi động ứng dụng

**Cách 1: Chạy từ source code**
```bash
cd 01_Source_Code
python comprehensive_app.py
```

**Cách 2: Chạy file .exe (nếu đã tạo)**
```
Double-click vào XuLyAnh_Final.exe trong thư mục 02_Ung_Dung_San_Pham
```

### Bước 2: Tải ảnh

1. Click nút **"Tải ảnh"**
2. Chọn file ảnh từ máy tính (hỗ trợ .jpg, .png, .bmp, .tiff)
3. Ảnh gốc sẽ hiển thị bên phải

**Tip:** Sử dụng các ảnh trong thư mục `sample_images/` để thử nghiệm

### Bước 3: Áp dụng chức năng xử lý

#### Bài 1-3: Chức năng cơ bản

**Chuyển ảnh xám:**
- Click **"Ảnh xám"**
- Kết quả: Ảnh màu → Ảnh đen trắng

**Phân ngưỡng:**
1. Kéo thanh trượt **"Ngưỡng"** (0-255)
2. Click **"Phân ngưỡng"**
3. Kết quả: Ảnh nhị phân (chỉ đen và trắng)

**Tách kênh màu:**
- Click **"Tách kênh màu"**
- Cửa sổ mới hiện ra với 3 kênh R, G, B riêng biệt

#### Bài 4-6: Xử lý Histogram

**Kéo giãn tương phản:**
- Dùng cho ảnh có độ tương phản thấp
- Click **"Kéo giãn tương phản"**
- Kết quả: Ảnh sáng và tối rõ hơn

**Cân bằng Histogram:**
- Dùng cho ảnh tối hoặc sáng quá
- Click **"Cân bằng Histogram"**
- Kết quả: Độ sáng được phân bố đều

**Hiển thị Histogram:**
- Click **"Hiển thị Histogram"**
- Xem biểu đồ phân bố độ sáng

**CLAHE:**
- Cân bằng thích ứng cục bộ
- Click **"CLAHE"**
- Kết quả: Chi tiết rõ hơn ở từng vùng

#### Bài 7: Lọc nhiễu

**Khi nào dùng:**
- Ảnh có nhiễu muối tiêu (chấm đen/trắng rải rác)
- Ảnh bị nhiễu gaussian

**Lọc trung bình:**
- Click **"Lọc trung bình 3x3"** hoặc **"5x5"**
- Kết quả: Ảnh mịn hơn, nhiễu giảm

**Lọc trung vị:**
- Click **"Lọc trung vị 3x3"** hoặc **"5x5"**
- Kết quả: Loại bỏ nhiễu muối tiêu tốt hơn

**Gợi ý:** Thử với ảnh `noisy.png` trong sample_images

#### Bài 8: Tách biên bậc 1

**Mục đích:** Phát hiện đường viền, biên của đối tượng

**Các phương pháp:**
- **Sobel:** Click **"Sobel"** - Phổ biến nhất
- **Prewitt:** Click **"Prewitt"** - Tương tự Sobel
- **Roberts:** Click **"Roberts"** - Đơn giản, nhanh
- **Kirsch:** Click **"Kirsch"** - Phát hiện 8 hướng

**Kết quả:** Ảnh chỉ còn đường viền trắng trên nền đen

**Gợi ý:** Thử với ảnh `checkerboard.png`

#### Bài 9: Tách biên bậc 2 & Làm nét

**Laplacian:**
- Click **"Laplacian"**
- Phát hiện biên bằng đạo hàm bậc 2

**LoG (Laplacian of Gaussian):**
- Click **"LoG"**
- Làm mịn trước rồi mới tách biên
- Kết quả sạch hơn Laplacian thông thường

**Làm nét:**
- Click **"Làm nét"**
- Kết quả: Ảnh sắc nét hơn, chi tiết rõ hơn

#### Bài 10-12: Xử lý Fourier

**FFT Spectrum:**
- Click **"FFT Spectrum"**
- Xem phổ tần số của ảnh
- Điểm sáng ở giữa = tần số 0 (độ sáng TB)

**Lọc thông thấp (Low-pass):**
1. Kéo thanh **"Cutoff"** (10-100)
2. Click **"Ideal Low-pass"** hoặc **"Gaussian Low-pass"**
3. Kết quả: Ảnh bị làm mờ (loại bỏ chi tiết)

**Lọc thông cao (High-pass):**
1. Kéo thanh **"Cutoff"** (10-100)
2. Click **"Ideal High-pass"** hoặc **"Butterworth High-pass"**
3. Kết quả: Chỉ giữ lại biên, chi tiết

### Bước 4: Lưu kết quả

1. Click **"Lưu ảnh"**
2. Chọn vị trí và tên file
3. Chọn định dạng (.png hoặc .jpg)
4. Click "Save"

### Bước 5: Thử chức năng khác

- Click **"Reset"** để quay về ảnh gốc
- Thử chức năng khác
- Hoặc tải ảnh mới

## Mẹo và thủ thuật

### Mẹo 1: So sánh các phương pháp
1. Tải ảnh
2. Áp dụng Sobel → Lưu ảnh
3. Reset
4. Áp dụng Prewitt → Lưu ảnh
5. So sánh hai ảnh đã lưu

### Mẹo 2: Kết hợp các kỹ thuật
Ví dụ: Xử lý ảnh nhiễu
1. Tải ảnh nhiễu
2. Áp dụng Lọc trung vị 5x5
3. Áp dụng Sobel để tách biên
4. Lưu kết quả

### Mẹo 3: Điều chỉnh tham số
- Thử các giá trị ngưỡng khác nhau (0-255)
- Thử các cutoff khác nhau cho Fourier (10-100)
- Thử kernel size khác nhau (3x3 vs 5x5)

### Mẹo 4: Ảnh mẫu phù hợp

| Ảnh mẫu | Thử với chức năng |
|---------|-------------------|
| gradient.png | Histogram, FFT |
| checkerboard.png | Edge detection, FFT |
| noisy.png | Median filter |
| color_blocks.png | Channel splitting |
| low_contrast.png | Contrast stretching, CLAHE |

## Xử lý sự cố

### Vấn đề: Không tải được ảnh
- **Giải pháp:** Kiểm tra định dạng ảnh (phải là .jpg, .png, .bmp, .tiff)

### Vấn đề: Ứng dụng chậm
- **Giải pháp:** Sử dụng ảnh có kích thước nhỏ hơn (< 2000x2000 pixels)

### Vấn đề: Kết quả không như mong đợi
- **Giải pháp:** 
  - Reset và thử lại
  - Điều chỉnh tham số (ngưỡng, cutoff)
  - Thử chức năng khác phù hợp hơn

### Vấn đề: Không lưu được ảnh
- **Giải pháp:** 
  - Đảm bảo đã áp dụng ít nhất 1 chức năng xử lý
  - Kiểm tra quyền ghi vào thư mục đích

## Câu hỏi thường gặp

**Q: Tại sao một số chức năng kết quả giống nhau?**

A: Một số kỹ thuật (Sobel, Prewitt) có kết quả tương tự nhưng khác nhau về chi tiết. Thử với nhiều ảnh khác nhau để thấy sự khác biệt.

**Q: Có thể xử lý nhiều ảnh cùng lúc không?**

A: Không. Ứng dụng chỉ xử lý từng ảnh một. Muốn xử lý ảnh khác thì tải ảnh mới.

**Q: Làm sao để xem ảnh gốc sau khi đã xử lý?**

A: Click nút "Reset" để quay về ảnh gốc.

**Q: Có thể áp dụng nhiều chức năng liên tiếp không?**

A: Có! Ví dụ: Tải ảnh → Lọc trung vị → Sobel → Lưu ảnh

## Kết luận

Ứng dụng này cung cấp đầy đủ các công cụ xử lý ảnh cần thiết cho môn học. Hãy thử nghiệm với nhiều ảnh và chức năng khác nhau để hiểu rõ hơn về xử lý ảnh!

---

**Lưu ý:** Hướng dẫn này dành cho người dùng cuối. Nếu bạn là developer và muốn hiểu về code, xem file `README.md` trong thư mục `01_Source_Code/`.
