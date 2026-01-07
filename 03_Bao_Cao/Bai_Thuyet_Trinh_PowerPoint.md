# BÀI THUYẾT TRÌNH ĐỒ ÁN XỬ LÝ ẢNH

## SLIDE 1: TRANG BÌA
---
### ỨNG DỤNG XỬ LÝ ẢNH TỔNG HỢP
**Bài 1 - Bài 12**

**Sinh viên thực hiện:** [Họ và tên]  
**MSSV:** [Mã số sinh viên]  
**Lớp:** [Lớp học]  
**Giảng viên hướng dẫn:** [Tên giảng viên]

**Năm học:** 2024-2025

---

## SLIDE 2: MỤC LỤC
---
### NỘI DUNG TRÌNH BÀY

1. Giới thiệu đồ án
2. Mục tiêu và yêu cầu
3. Công nghệ sử dụng
4. Kiến trúc hệ thống
5. Các chức năng đã cài đặt (Bài 1-12)
6. Giao diện ứng dụng
7. Demo và kết quả
8. Kết luận và hướng phát triển

---

## SLIDE 3: GIỚI THIỆU ĐỒ ÁN
---
### TỔNG QUAN

**Tên đồ án:** Ứng dụng xử lý ảnh tổng hợp

**Mô tả:**
- Xây dựng ứng dụng tích hợp đầy đủ các kỹ thuật xử lý ảnh
- Từ cơ bản đến nâng cao (12 bài tập)
- Giao diện đồ họa thân thiện, dễ sử dụng

**Ý nghĩa:**
- Củng cố kiến thức lý thuyết
- Thực hành lập trình xử lý ảnh
- Tạo sản phẩm ứng dụng hoàn chỉnh

---

## SLIDE 4: MỤC TIÊU VÀ YÊU CẦU
---
### MỤC TIÊU

✅ **Mục tiêu chính:**
- Cài đặt đầy đủ 12 bài tập xử lý ảnh
- Tích hợp vào một ứng dụng duy nhất
- Giao diện trực quan, dễ sử dụng

✅ **Yêu cầu kỹ thuật:**
- Sử dụng Python và các thư viện chuyên dụng
- Cài đặt thuật toán chính xác
- Tối ưu hiệu suất
- Có thể đóng gói thành file .exe

---

## SLIDE 5: CÔNG NGHỆ SỬ DỤNG
---
### TECHNOLOGY STACK

**Ngôn ngữ lập trình:**
- Python 3.8+

**Thư viện xử lý ảnh:**
- OpenCV (cv2) - Xử lý ảnh
- NumPy - Tính toán ma trận
- Pillow (PIL) - Định dạng ảnh

**Thư viện giao diện:**
- Tkinter - GUI framework (built-in)
- Matplotlib - Vẽ biểu đồ

**Công cụ đóng gói:**
- PyInstaller - Tạo file .exe

---

## SLIDE 6: KIẾN TRÚC HỆ THỐNG
---
### CẤU TRÚC DỰ ÁN

```
📁 01_Source_Code/
   ├── image_processing.py      (Core Library)
   ├── comprehensive_app.py     (GUI Application)
   ├── create_samples.py        (Sample Generator)
   └── requirements.txt         (Dependencies)

📁 02_Ung_Dung_San_Pham/
   ├── XuLyAnh_Final.exe       (Executable)
   └── sample_images/           (Demo Images)

📁 03_Bao_Cao/
   └── Bao_Cao_Ket_Thuc_Mon.docx
```

**Mô hình:** Separation of Concerns
- Logic xử lý tách biệt khỏi giao diện
- Dễ bảo trì và mở rộng

---

## SLIDE 7: KIẾN TRÚC CODE
---
### THIẾT KẾ MÃ NGUỒN

**File `image_processing.py`:**
- Class `ImageProcessor` với static methods
- 25+ hàm xử lý ảnh độc lập
- Input/Output: NumPy arrays
- Không phụ thuộc vào GUI

**File `comprehensive_app.py`:**
- Class `ImageProcessingApp` (Tkinter)
- Quản lý giao diện người dùng
- Gọi hàm từ `ImageProcessor`
- Hiển thị kết quả trực quan

**Ưu điểm:**
- Code gọn gàng, dễ đọc
- Tái sử dụng cao
- Dễ kiểm thử

---

## SLIDE 8: BÀI 1-3 - CHỨC NĂNG Cơ BẢN
---
### XỬ LÝ CƠ BẢN

**1. Chuyển đổi ảnh xám (Grayscale)**
- Công thức: `L = 0.299×R + 0.587×G + 0.114×B`
- Giảm 3 kênh màu thành 1 kênh
- Mục đích: Đơn giản hóa xử lý

**2. Phân ngưỡng (Binary Threshold)**
- Tách đối tượng khỏi nền
- Ngưỡng điều chỉnh được (0-255)
- Kết quả: Ảnh nhị phân (đen/trắng)

**3. Tách kênh màu (Channel Splitting)**
- Hiển thị riêng kênh R, G, B
- Hỗ trợ cả kênh Alpha (độ trong suốt)
- Phân tích thành phần màu

---

## SLIDE 9: BÀI 4 - KÉO GIÃN TƯƠNG PHẢN
---
### CONTRAST STRETCHING

**Nguyên lý:**
- Mở rộng dải giá trị pixel về [0, 255]
- Công thức: `Out = (In - Min) × 255 / (Max - Min)`

**Ứng dụng:**
- Ảnh có độ tương phản thấp
- Ảnh quá tối hoặc quá sáng
- Cải thiện chất lượng hiển thị

**Kết quả:**
- Tăng độ tương phản tuyến tính
- Dễ phân biệt vùng tối/sáng
- Không làm mất thông tin

---

## SLIDE 10: BÀI 5-6 - HISTOGRAM
---
### XỬ LÝ BIỂU ĐỒ

**Cân bằng Histogram (Equalization)**
- Phân bố đều độ sáng
- Tăng độ tương phản toàn cục
- Dùng `cv2.equalizeHist()`

**Khớp Histogram (Matching)**
- Biến đổi theo phân bố mẫu (Gaussian)
- Điều chỉnh phân bố độ sáng
- Sử dụng CDF (Cumulative Distribution Function)

**CLAHE (Adaptive Equalization)**
- Cân bằng cục bộ từng vùng
- Clip limit để tránh nhiễu
- Tile size: 8×8 pixels

---

## SLIDE 11: BÀI 7 - LỌC NHIỄU
---
### NOISE FILTERING

**Lọc trung bình (Average Filter)**
- Kernel: 3×3, 5×5
- Lấy giá trị trung bình cộng
- Làm mờ ảnh, giảm nhiễu
- Nhược điểm: Làm mờ cả biên

**Lọc trung vị (Median Filter)**
- Kernel: 3×3, 5×5
- Lấy giá trị trung vị
- Hiệu quả với nhiễu muối tiêu
- Ưu điểm: Giữ được độ sắc nét biên

**So sánh:**
- Average: Nhanh nhưng mờ biên
- Median: Chậm hơn nhưng giữ biên tốt

---

## SLIDE 12: BÀI 8 - TÁCH BIÊN BậC 1 (Phần 1)
---
### SOBEL & PREWITT

**Sobel Edge Detection**
- Đạo hàm bậc 1 theo x và y
- Kernel 3×3
- Tính magnitude: `√(Gx² + Gy²)`
- Phổ biến, chính xác

**Prewitt Edge Detection**
- Tương tự Sobel
- Kernel khác một chút
- Độ nhạy thấp hơn Sobel
- Đơn giản hơn

**Ứng dụng:**
- Phát hiện đường viền
- Nhận dạng đối tượng
- Phân đoạn ảnh

---

## SLIDE 13: BÀI 8 - TÁCH BIÊN BậC 1 (Phần 2)
---
### ROBERTS & KIRSCH

**Roberts Edge Detection**
- Đạo hàm bậc 1 đơn giản
- Kernel 2×2
- Nhanh nhưng nhạy nhiễu
- Dùng cho ảnh chất lượng tốt

**Kirsch Edge Detection**
- Phát hiện theo 8 hướng
- 8 kernel khác nhau
- Lấy giá trị max
- Phát hiện biên toàn diện

**So sánh:**
- Sobel/Prewitt: Cân bằng tốc độ & chất lượng
- Roberts: Nhanh nhưng yếu với nhiễu
- Kirsch: Chậm nhưng toàn diện

---

## SLIDE 14: BÀI 9 - TÁCH BIÊN BậC 2
---
### LAPLACIAN & LoG

**Laplacian**
- Đạo hàm bậc 2
- Phát hiện điểm thay đổi đột ngột
- Nhạy với nhiễu

**LoG (Laplacian of Gaussian)**
- Làm mịn trước (Gaussian)
- Sau đó áp dụng Laplacian
- Giảm nhiễu, tăng độ chính xác
- Kernel size: 5×5

**Image Sharpening**
- Công thức: `Sharp = Original - Laplacian`
- Làm nổi bật chi tiết
- Tăng độ sắc nét ảnh

---

## SLIDE 15: BÀI 10 - BIẾN ĐỔI FOURIER
---
### FFT TRANSFORM

**Nguyên lý:**
- Chuyển ảnh từ miền không gian → miền tần số
- Sử dụng `np.fft.fft2()`
- Dịch DC component về giữa: `fftshift()`

**Magnitude Spectrum:**
- Hiển thị phổ biên độ
- Điểm sáng ở giữa = tần số 0 (độ sáng TB)
- Xa tâm = tần số cao (chi tiết, biên)

**Ứng dụng:**
- Phân tích tần số ảnh
- Lọc trong miền tần số
- Nén ảnh

---

## SLIDE 16: BÀI 11 - LỌC THÔNG THẤP
---
### LOW-PASS FILTERS

**Ideal Low-pass Filter**
- Cắt bỏ hoàn toàn tần số cao
- Mask hình tròn với bán kính cutoff
- Làm mờ ảnh
- Nhược điểm: Hiện tượng ringing

**Gaussian Low-pass Filter**
- Giảm dần tần số cao (không cắt đột ngột)
- Mask Gaussian: `exp(-D²/2σ²)`
- Làm mờ mịn hơn
- Giảm ringing

**Tham số:**
- Cutoff: 10-100 (điều chỉnh được)
- Cutoff nhỏ → mờ nhiều
- Cutoff lớn → giữ nhiều chi tiết

---

## SLIDE 17: BÀI 12 - LỌC THÔNG CAO
---
### HIGH-PASS FILTERS

**Ideal High-pass Filter**
- Loại bỏ tần số thấp
- Giữ lại tần số cao (biên, chi tiết)
- Mask: `1 - Low-pass mask`
- Làm nổi bật biên

**Butterworth High-pass Filter**
- Giảm dần tần số thấp
- Công thức: `1 / (1 + (D₀/D)^2n)`
- Tham số n (order): Độ dốc
- Tách biên mềm mại hơn

**Ứng dụng:**
- Tách biên
- Làm nét ảnh
- Nén ảnh

---

## SLIDE 18: GIAO DIỆN ỨNG DỤNG
---
### USER INTERFACE

**Layout:**
- **Panel trái:** Điều khiển (Control Panel)
  - Nhóm chức năng theo bài tập
  - Nút bấm và thanh trượt
  - Scrollable để chứa nhiều chức năng

- **Panel phải:** Hiển thị (Display Panel)
  - Ảnh gốc và ảnh xử lý song song
  - Thông tin chi tiết
  - Ma trận pixel (nếu cần)

**Tính năng:**
- Tải ảnh (Load Image)
- Lưu ảnh (Save Image)
- Reset về ảnh gốc
- Áp dụng các chức năng xử lý

---

## SLIDE 19: DEMO - WORKFLOW SỬ DỤNG
---
### QUY TRÌNH SỬ DỤNG

**Bước 1:** Tải ảnh
- Click "Tải ảnh" → Chọn file

**Bước 2:** Chọn chức năng
- Click vào nút chức năng mong muốn
- Điều chỉnh tham số (nếu có)

**Bước 3:** Xem kết quả
- So sánh ảnh gốc và ảnh xử lý
- Đọc thông tin chi tiết

**Bước 4:** Lưu hoặc thử lại
- Lưu ảnh kết quả
- Hoặc Reset và thử chức năng khác

---

## SLIDE 20: KẾT QUẢ DEMO (Phần 1)
---
### MỘT SỐ KẾT QUẢ

**Ảnh xám:**
- Input: Ảnh màu
- Output: Ảnh đen trắng
- Thời gian: < 0.1s

**Cân bằng Histogram:**
- Input: Ảnh tối
- Output: Ảnh sáng rõ, tương phản tốt
- Hiệu quả: Rõ ràng

**Lọc Median:**
- Input: Ảnh nhiễu muối tiêu
- Output: Ảnh sạch, giữ biên tốt
- Kernel 5×5: Tốt nhất

---

## SLIDE 21: KẾT QUẢ DEMO (Phần 2)
---
### TÁCH BIÊN & FOURIER

**Sobel Edge:**
- Input: Ảnh gốc
- Output: Đường viền rõ ràng
- Ứng dụng: Nhận dạng vật thể

**FFT Spectrum:**
- Hiển thị phổ tần số
- Phân tích cấu trúc ảnh
- Hỗ trợ lọc trong miền tần số

**Butterworth High-pass:**
- Tách biên mềm mại
- Tham số order điều chỉnh được
- Kết quả tự nhiên hơn Ideal

---

## SLIDE 22: ƯU ĐIỂM & HẠN CHẾ
---
### ĐÁNH GIÁ

**Ưu điểm:**
✅ Tích hợp đầy đủ 22+ chức năng
✅ Giao diện thân thiện, trực quan
✅ Code sạch sẽ, có cấu trúc
✅ Tài liệu đầy đủ (Tiếng Việt)
✅ Có ảnh mẫu để demo
✅ Có thể đóng gói thành .exe

**Hạn chế:**
⚠️ Chưa hỗ trợ xử lý video
⚠️ Chưa có undo/redo
⚠️ Chưa tối ưu cho ảnh cực lớn
⚠️ Chưa có batch processing

---

## SLIDE 23: HƯỚNG PHÁT TRIỂN
---
### TƯƠNG LAI

**Ngắn hạn:**
- Thêm undo/redo
- Batch processing (xử lý nhiều ảnh)
- Lưu/load preset tham số
- Thêm shortcuts (Ctrl+O, Ctrl+S)

**Dài hạn:**
- Xử lý video
- Tích hợp Machine Learning
  - Face detection
  - Object recognition
  - Style transfer
- Cloud integration
- Mobile app version

---

## SLIDE 24: KINH NGHIỆM RÚT RA
---
### BÀI HỌC

**Về kỹ thuật:**
- Hiểu sâu về xử lý ảnh
- Thành thạo OpenCV, NumPy
- Kỹ năng tối ưu thuật toán

**Về lập trình:**
- Tổ chức code theo mô hình MVC
- Separation of Concerns
- Viết code dễ bảo trì

**Về soft skills:**
- Quản lý dự án
- Viết tài liệu kỹ thuật
- Trình bày demo

---

## SLIDE 25: KẾT LUẬN
---
### TÓM TẮT

**Đã hoàn thành:**
✅ Cài đặt đầy đủ 12 bài tập (22+ chức năng)
✅ Xây dựng ứng dụng GUI hoàn chỉnh
✅ Tài liệu đầy đủ bằng Tiếng Việt
✅ Sẵn sàng demo và nộp bài

**Đóng góp:**
- Sản phẩm ứng dụng thực tế
- Tài liệu tham khảo cho sinh viên khóa sau
- Nền tảng để phát triển thêm

**Cảm ơn sự theo dõi của quý thầy cô!**

---

## SLIDE 26: PHẦN HỎI ĐÁP
---
### Q&A

**Sẵn sàng trả lời các câu hỏi về:**

1. Thuật toán và cài đặt
2. Lựa chọn công nghệ
3. Kiến trúc hệ thống
4. Kết quả và demo
5. Hướng phát triển

**Demo trực tiếp:** Có thể demo bất kỳ chức năng nào

---

## SLIDE 27: TÀI LIỆU THAM KHẢO
---
### REFERENCES

**Sách:**
1. Rafael C. Gonzalez, Richard E. Woods
   "Digital Image Processing", 4th Edition

**Documentation:**
2. OpenCV Documentation
   https://docs.opencv.org/

3. NumPy Documentation
   https://numpy.org/doc/

4. Python Tkinter
   https://docs.python.org/3/library/tkinter.html

**Source code:**
5. GitHub Repository
   https://github.com/minhhieucnttai/testhfd

---

## PHỤ LỤC: THÔNG TIN THỐNG KÊ
---
### PROJECT METRICS

**Code:**
- Python files: 3
- Total lines: ~1,000
- Functions: 25+
- Classes: 2

**Features:**
- GUI features: 22+
- Sample images: 5

**Documentation:**
- Markdown files: 7
- README: 3
- Guides: 2
- Report: 1

**Testing:**
- Security scan: 0 vulnerabilities
- Code review: Passed
- All functions: Tested ✅
