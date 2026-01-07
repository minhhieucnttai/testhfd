# Ứng Dụng Xử Lý Ảnh - Bài 1-12

## Giới thiệu

Dự án này là một ứng dụng xử lý ảnh tổng hợp được phát triển bằng Python, tích hợp đầy đủ các kỹ thuật xử lý ảnh từ cơ bản đến nâng cao cho môn học Xử lý ảnh.

## Cấu trúc thư mục

```
MSSV_HoTen_DoAnXuLyAnh/
├── 01_Source_Code/           # Mã nguồn Python
│   ├── sample_images/        # Ảnh mẫu để demo
│   ├── comprehensive_app.py  # File chạy chính (Giao diện)
│   ├── image_processing.py   # Thư viện xử lý ảnh
│   ├── requirements.txt      # Các thư viện cần cài
│   ├── create_samples.py     # Script tạo ảnh mẫu
│   └── README.md             # File này
│
├── 02_Ung_Dung_San_Pham/     # File .EXE (tạo bằng PyInstaller)
│   ├── XuLyAnh_Final.exe     # Ứng dụng đã đóng gói
│   └── sample_images/        # Copy thư mục ảnh vào đây
│
└── 03_Bao_Cao/               # Báo cáo
    └── Bao_Cao_Ket_Thuc_Mon.docx
```

## Các chức năng đã cài đặt

### Bài 1-3: Chức năng cơ bản
- **Chuyển đổi ảnh xám (Grayscale)**: Công thức L = 0.299×R + 0.587×G + 0.114×B
- **Phân ngưỡng (Binary)**: Tùy chỉnh ngưỡng qua thanh trượt
- **Tách kênh màu**: Hiển thị riêng kênh R, G, B, Alpha

### Bài 4-6: Xử lý Histogram
- **Kéo giãn tương phản**: Mở rộng dải giá trị pixel
- **Cân bằng Histogram**: Phân bố lại độ sáng
- **Khớp Histogram**: Biến đổi theo phân bố Gaussian
- **CLAHE**: Cân bằng thích ứng cục bộ

### Bài 7: Lọc nhiễu
- **Lọc trung bình (Average)**: Kernel 3×3, 5×5
- **Lọc trung vị (Median)**: Kernel 3×3, 5×5 - Hiệu quả với nhiễu muối tiêu

### Bài 8: Tách biên bậc 1
- **Sobel**: Đạo hàm bậc 1
- **Prewitt**: Đạo hàm bậc 1
- **Roberts**: Đạo hàm bậc 1
- **Kirsch**: Đạo hàm bậc 1 - 8 hướng

### Bài 9: Tách biên bậc 2 & Làm nét
- **Laplacian**: Đạo hàm bậc 2
- **LoG (Laplacian of Gaussian)**: Làm mịn trước khi tách biên
- **Image Sharpening**: Làm nét ảnh

### Bài 10-12: Xử lý trong miền tần số (Fourier)
- **FFT Transform**: Biến đổi Fourier, hiển thị phổ biên độ
- **Ideal Low-pass Filter**: Cắt tần số cao, làm mờ
- **Gaussian Low-pass Filter**: Làm mờ mịn, giảm ringing
- **Ideal High-pass Filter**: Giữ tần số cao, nổi bật biên
- **Butterworth High-pass Filter**: Tách biên mềm mại

## Hướng dẫn cài đặt

### Yêu cầu hệ thống
- Python 3.8 trở lên
- Hệ điều hành: Windows, macOS, Linux

### Bước 1: Cài đặt Python
Tải và cài đặt Python từ: https://www.python.org/downloads/

### Bước 2: Cài đặt thư viện
Mở Terminal/CMD tại thư mục `01_Source_Code` và chạy:

```bash
pip install -r requirements.txt
```

### Bước 3: Tạo ảnh mẫu
```bash
python create_samples.py
```

### Bước 4: Chạy ứng dụng
```bash
python comprehensive_app.py
```

## Hướng dẫn tạo file .EXE

### Cài đặt PyInstaller
```bash
pip install pyinstaller
```

### Tạo file .EXE
Chạy lệnh sau tại thư mục `01_Source_Code`:

```bash
pyinstaller --noconfirm --onefile --windowed --name "XuLyAnh_Final" --clean comprehensive_app.py
```

### Kết quả
- File `.exe` sẽ được tạo trong thư mục `dist/`
- Copy file `XuLyAnh_Final.exe` vào thư mục `02_Ung_Dung_San_Pham/`
- Copy thư mục `sample_images/` vào `02_Ung_Dung_San_Pham/` để có ảnh mẫu demo

## Hướng dẫn sử dụng

1. **Tải ảnh**: Click nút "Tải ảnh" để mở ảnh từ máy tính
2. **Chọn chức năng**: Click vào các nút chức năng bên trái để xử lý
3. **Xem kết quả**: Ảnh gốc và ảnh xử lý hiển thị bên phải
4. **Lưu ảnh**: Click "Lưu ảnh" để lưu kết quả
5. **Reset**: Click "Reset" để quay về ảnh gốc

## Cấu trúc mã nguồn

### `image_processing.py`
Class `ImageProcessor` chứa các phương thức static để xử lý ảnh:
- Tất cả các hàm đều nhận input là numpy array
- Tự động chuyển sang ảnh xám khi cần thiết
- Return kết quả dưới dạng numpy array

### `comprehensive_app.py`
Class `ImageProcessingApp` tạo giao diện Tkinter:
- Panel điều khiển bên trái
- Hiển thị ảnh bên phải
- Thông tin xử lý ở dưới

## Thư viện sử dụng

- **OpenCV (cv2)**: Xử lý ảnh cơ bản
- **NumPy**: Tính toán ma trận
- **Pillow (PIL)**: Xử lý định dạng ảnh, hiển thị
- **Matplotlib**: Vẽ biểu đồ Histogram
- **Tkinter**: Giao diện đồ họa (built-in)

## Câu hỏi vấn đáp thường gặp

### 1. Tại sao chuyển sang ảnh xám trước khi xử lý?
Xử lý trên ảnh xám (ma trận 2D) giảm khối lượng tính toán gấp 3 lần so với ảnh màu (3 kênh). Các thông tin về cấu trúc, biên dạng và độ sáng chủ yếu nằm ở cường độ sáng (intensity) chứ không phụ thuộc vào màu sắc.

### 2. Khác biệt giữa Average và Median filter?
- **Average**: Lấy trung bình cộng, làm mờ cả biên
- **Median**: Lấy giá trị trung vị, giữ được độ sắc nét của biên, hiệu quả với nhiễu muối tiêu

### 3. Tại sao FFT spectrum có điểm sáng ở giữa?
Điểm sáng ở giữa đại diện cho thành phần tần số bằng 0 (DC component), tức độ sáng trung bình của toàn bộ ảnh. Các điểm càng xa tâm thì đại diện cho tần số cao (chi tiết, biên). Sử dụng `np.fft.fftshift` để đưa tần số 0 vào giữa.

### 4. Cấu trúc code được tổ chức như thế nào?
- `image_processing.py`: Class chứa các phương thức xử lý tĩnh (Static methods)
- `comprehensive_app.py`: Giao diện Tkinter, gọi hàm từ thư viện xử lý
- Cách này giúp code gọn gàng, dễ bảo trì và tái sử dụng

## Tác giả

- Sinh viên: [Tên của bạn]
- MSSV: [Mã số sinh viên]
- Môn học: Xử lý ảnh
- Năm học: 2024-2025

## License

Dự án này được tạo cho mục đích học tập.
