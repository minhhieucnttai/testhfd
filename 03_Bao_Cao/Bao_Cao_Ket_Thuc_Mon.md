# BÁO CÁO KẾT THÚC MÔN

## XỬ LÝ ẢNH

**Đề tài:** Xây dựng ứng dụng xử lý ảnh tổng hợp (Bài 1 - Bài 12)

---

**Sinh viên:** [Họ và tên của bạn]  
**MSSV:** [Mã số sinh viên của bạn]  
**Lớp:** [Lớp học của bạn]  
**Giảng viên hướng dẫn:** [Tên giảng viên]

---

## CHƯƠNG 1: GIỚI THIỆU ĐỀ TÀI

### 1.1. Mục tiêu

Xây dựng một phần mềm hoàn chỉnh tích hợp các kỹ thuật xử lý ảnh từ cơ bản đến nâng cao, bao gồm:
- Biến đổi mức xám
- Xử lý biểu đồ (Histogram)
- Lọc nhiễu
- Tách biên
- Xử lý trong miền tần số (Fourier)

### 1.2. Công cụ thực hiện

- **Ngôn ngữ:** Python 3.x
- **Thư viện giao diện:** Tkinter (Tích hợp sẵn, nhẹ, dễ sử dụng)
- **Thư viện xử lý ảnh:** 
  - OpenCV (cv2) - Xử lý ảnh
  - NumPy - Tính toán ma trận
  - Pillow - Xử lý định dạng ảnh
- **Thư viện biểu đồ:** Matplotlib

---

## CHƯƠNG 2: CÁC CHỨC NĂNG ĐÃ CÀI ĐẶT

Ứng dụng được chia thành các module chức năng theo trình tự logic:

### 2.1. Nhóm chức năng cơ bản (Bài 1-3)

**a) Chuyển đổi ảnh xám (Grayscale)**
- Công thức: L = 0.299×R + 0.587×G + 0.114×B
- Mục đích: Giảm khối lượng tính toán, tập trung vào cường độ sáng

**b) Phân ngưỡng (Binary)**
- Cho phép người dùng tùy chỉnh ngưỡng qua thanh trượt
- Mục đích: Tách đối tượng khỏi nền

**c) Tách kênh màu**
- Hiển thị riêng biệt các kênh Red, Green, Blue và Alpha
- Mục đích: Phân tích thành phần màu

### 2.2. Nhóm chức năng nâng cao độ tương phản (Bài 4-6)

**a) Kéo giãn tương phản (Contrast Stretching)**
- Mở rộng dải giá trị pixel về [0, 255]
- Tăng độ tương phản tuyến tính

**b) Cân bằng biểu đồ (Histogram Equalization)**
- Phân bố lại độ sáng giúp ảnh rõ nét hơn
- Cải thiện độ tương phản toàn cục

**c) Khớp biểu đồ (Histogram Matching)**
- Biến đổi histogram theo phân bố Gaussian
- Điều chỉnh phân bố độ sáng theo mẫu

**d) CLAHE (Contrast Limited Adaptive Histogram Equalization)**
- Cân bằng histogram cục bộ
- Tăng chi tiết ở vùng tối/sáng quá mức mà không gây nhiễu

### 2.3. Lọc nhiễu và Tách biên (Bài 7-9)

**a) Lọc nhiễu**
- **Lọc trung bình (Average Filter):** Kernel 3×3, 5×5 - Làm mờ để giảm nhiễu
- **Lọc trung vị (Median Filter):** Kernel 3×3, 5×5 - Hiệu quả với nhiễu muối tiêu

**b) Tách biên bậc 1 (Edge Detection)**
- **Sobel:** Đạo hàm bậc 1 theo x và y
- **Prewitt:** Đạo hàm bậc 1 với kernel khác
- **Roberts:** Đạo hàm bậc 1 đơn giản
- **Kirsch:** Đạo hàm bậc 1 theo 8 hướng

**c) Tách biên bậc 2 & Làm nét**
- **Laplacian:** Đạo hàm bậc 2 - phát hiện biên
- **LoG (Laplacian of Gaussian):** Làm mịn trước khi tách biên
- **Image Sharpening:** Làm nét ảnh sử dụng Laplacian

### 2.4. Xử lý trong miền tần số - Fourier (Bài 10-12)

**a) Biến đổi Fourier (FFT)**
- Chuyển ảnh sang miền tần số
- Hiển thị phổ biên độ (Magnitude Spectrum)

**b) Lọc thông thấp (Low-pass Filters)**
- **Ideal Low-pass:** Cắt bỏ tần số cao, làm mờ ảnh
- **Gaussian Low-pass:** Làm mờ mịn hơn, giảm hiện tượng gợn sóng (ringing)

**c) Lọc thông cao (High-pass Filters)**
- **Ideal High-pass:** Giữ lại tần số cao, làm nổi bật biên
- **Butterworth High-pass:** Tách biên mềm mại hơn, kiểm soát độ dốc qua tham số bậc n

---

## CHƯƠNG 3: KẾT QUẢ VÀ HƯỚNG DẪN SỬ DỤNG

### 3.1. Giao diện chương trình

*[Chèn hình ảnh giao diện chính của ứng dụng]*

**Mô tả:**
- Giao diện chia làm 2 phần chính:
  - **Panel điều khiển bên trái:** Các nút chức năng được nhóm theo bài tập
  - **Màn hình hiển thị bên phải:** Hiển thị ảnh gốc và ảnh xử lý song song

### 3.2. Hướng dẫn sử dụng

**Bước 1:** Click "Tải ảnh" để mở ảnh từ máy tính

**Bước 2:** Chọn chức năng xử lý từ panel bên trái

**Bước 3:** Xem kết quả trên màn hình bên phải

**Bước 4:** Click "Lưu ảnh" để lưu kết quả hoặc "Reset" để quay về ảnh gốc

### 3.3. Kết quả minh họa

*[Chèn các hình ảnh minh họa cho từng chức năng]*

**Ví dụ:**
- Ảnh gốc → Ảnh xám
- Ảnh nhiễu → Lọc median → Kết quả sạch
- Ảnh tối → Cân bằng histogram → Ảnh sáng rõ
- Ảnh gốc → Sobel edge → Biên được phát hiện
- Ảnh gốc → FFT spectrum → Phổ tần số

---

## CHƯƠNG 4: CẤU TRÚC MÃ NGUỒN

### 4.1. Tổ chức code

**File `image_processing.py`:**
- Class `ImageProcessor` chứa toàn bộ các phương thức xử lý tĩnh (Static methods)
- Dễ tái sử dụng và kiểm thử
- Tách biệt logic xử lý khỏi giao diện

**File `comprehensive_app.py`:**
- Class `ImageProcessingApp` tạo giao diện Tkinter
- Gọi các hàm từ `image_processing.py`
- Xử lý tương tác người dùng

### 4.2. Ưu điểm của cấu trúc

- **Separation of Concerns:** Logic và giao diện tách biệt
- **Maintainability:** Dễ bảo trì và mở rộng
- **Reusability:** Các hàm có thể tái sử dụng
- **Testability:** Dễ kiểm thử từng module

---

## CHƯƠNG 5: KINH NGHIỆM VÀ KẾT LUẬN

### 5.1. Kiến thức đạt được

- Hiểu sâu về các kỹ thuật xử lý ảnh từ cơ bản đến nâng cao
- Thành thạo sử dụng OpenCV, NumPy, Matplotlib
- Kỹ năng xây dựng giao diện với Tkinter
- Tổ chức code theo mô hình MVC

### 5.2. Khó khăn gặp phải

- Tối ưu hiệu suất khi xử lý ảnh lớn
- Hiển thị ảnh với nhiều định dạng khác nhau
- Đóng gói ứng dụng thành file .exe

### 5.3. Hướng phát triển

- Thêm chức năng xử lý video
- Tích hợp Machine Learning cho phân loại ảnh
- Cải thiện giao diện người dùng
- Tối ưu hóa thuật toán

### 5.4. Kết luận

Ứng dụng đã hoàn thành đầy đủ các yêu cầu của môn học, bao gồm:
- ✅ Tất cả 12 bài tập đã được cài đặt
- ✅ Giao diện trực quan, dễ sử dụng
- ✅ Code được tổ chức khoa học
- ✅ Hoạt động ổn định và chính xác

Ứng dụng có thể chạy độc lập dưới dạng file .exe, thuận tiện cho việc demo và nộp bài.

---

## TÀI LIỆU THAM KHẢO

1. Rafael C. Gonzalez, Richard E. Woods, "Digital Image Processing", 4th Edition
2. OpenCV Documentation: https://docs.opencv.org/
3. NumPy Documentation: https://numpy.org/doc/
4. Tkinter Documentation: https://docs.python.org/3/library/tkinter.html

---

**Ngày hoàn thành:** [Ngày/Tháng/Năm]

**Chữ ký sinh viên**

---

## PHỤ LỤC

### A. Danh sách file code

- `comprehensive_app.py` - File chính (500+ dòng)
- `image_processing.py` - Thư viện xử lý (600+ dòng)
- `create_samples.py` - Tạo ảnh mẫu
- `requirements.txt` - Danh sách thư viện

### B. Hướng dẫn cài đặt

Xem file `README.md` trong thư mục `01_Source_Code`

### C. Hướng dẫn tạo file .exe

Xem file `HUONG_DAN.md` trong thư mục `02_Ung_Dung_San_Pham`
