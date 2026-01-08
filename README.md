# Ứng Dụng Xử Lý Ảnh - Đồ Án Kết Thúc Môn

## 🎉 Version 2.0 - Enhanced Edition

**ỨNG DỤNG ĐÃ ĐƯỢC NÂNG CẤP TOÀN DIỆN!**

Phiên bản nâng cao với giao diện hiện đại, tích hợp đầy đủ 22+ chức năng từ Bài 1-12 cùng 10 tính năng nâng cao mới.

## ⚡ Quick Start

```bash
cd 01_Source_Code
pip install opencv-python numpy pillow matplotlib
python comprehensive_app.py
```

📖 **Xem thêm:** [QUICKSTART.md](QUICKSTART.md) | [ENHANCEMENTS.md](ENHANCEMENTS.md)

## 🆕 Tính năng mới (Version 2.0)

### Interface & UX
- ✅ **Tabbed Interface:** 6 tabs có tổ chức (Cơ bản, Histogram, Lọc, Tách biên, Fourier, Nâng cao)
- ✅ **Menu Bar:** File, Edit, View, Processing, Help với keyboard shortcuts
- ✅ **Undo/Redo:** 10 levels history (Ctrl+Z/Ctrl+Y)
- ✅ **Real-time Histogram:** Tích hợp panel so sánh histogram
- ✅ **Zoom Support:** 10%-500% zoom với phím tắt (+/-/0)
- ✅ **Auto Preview:** Real-time updates khi kéo slider
- ✅ **Resizable Panels:** Tùy chỉnh kích thước panels

### Advanced Features
- ✅ **3 Presets:** Black&White, Enhance Brightness, Edge Detection
- ✅ **3 Pipelines:** Noise Reduction, Edge Enhancement, Contrast Enhancement
- ✅ **Batch Processing:** Xử lý nhiều ảnh (coming soon)
- ✅ **Compare Mode:** So sánh 2 ảnh (coming soon)

## Giới thiệu

Dự án này là một ứng dụng xử lý ảnh tổng hợp hoàn chỉnh, được xây dựng để đáp ứng yêu cầu đồ án môn Xử lý ảnh. 

**Version 2.0** nâng cấp từ giao diện cơ bản lên giao diện chuyên nghiệp với nhiều tính năng tiên tiến.

## Cấu trúc dự án (CD Nộp Bài)

```
MSSV_HoTen_DoAnXuLyAnh/
├── 01_Source_Code/           # Mã nguồn Python
│   ├── comprehensive_app.py  # File chạy chính (GUI)
│   ├── image_processing.py   # Thư viện xử lý ảnh
│   ├── requirements.txt      # Danh sách thư viện
│   ├── create_samples.py     # Tạo ảnh mẫu
│   ├── sample_images/        # Ảnh mẫu demo
│   └── README.md             # Hướng dẫn chi tiết
│
├── 02_Ung_Dung_San_Pham/     # Ứng dụng đóng gói (.EXE)
│   ├── XuLyAnh_Final.exe     # File chạy trực tiếp
│   ├── sample_images/        # Ảnh mẫu
│   └── HUONG_DAN.md          # Hướng dẫn tạo .exe
│
└── 03_Bao_Cao/               # Báo cáo
    ├── Bai_Thuyet_Trinh.pptx         # PowerPoint (27 slides) ✨ NEW
    ├── Bai_Thuyet_Trinh_PowerPoint.md # Source markdown cho slides
    ├── Bao_Cao_Ket_Thuc_Mon.docx     # Báo cáo Word (5 chương) ✨ NEW
    ├── Bao_Cao_Ket_Thuc_Mon.md       # Source markdown cho báo cáo
    └── README.md                      # Hướng dẫn sử dụng files ✨ NEW
```

## Tính năng chính

### 🆕 Version 2.0 Enhanced Features

#### Interface Improvements
- **Tabbed Organization:** 6 tabs chuyên biệt cho từng nhóm chức năng
- **Menu Bar:** Complete menu system với keyboard shortcuts
- **History System:** Undo/Redo 10 levels
- **Integrated Histogram:** Real-time comparison panel
- **Zoom & Pan:** Flexible image viewing (10%-500%)

#### Advanced Processing
- **Presets:** 3 quick presets cho các tác vụ thường gặp
- **Pipelines:** 3 multi-step processing pipelines
- **Auto Preview:** Real-time parameter adjustment
- **Canvas Display:** Better image rendering

### Core Functions (All Versions)

### Bài 1-3: Xử lý cơ bản
- ✅ Chuyển đổi ảnh xám (Grayscale)
- ✅ Phân ngưỡng (Binary Threshold)
- ✅ Tách kênh màu (R, G, B, Alpha)

### Bài 4-6: Xử lý Histogram
- ✅ Kéo giãn tương phản
- ✅ Cân bằng Histogram
- ✅ Khớp Histogram
- ✅ CLAHE (Adaptive)

### Bài 7: Lọc nhiễu
- ✅ Lọc trung bình (Average)
- ✅ Lọc trung vị (Median)

### Bài 8: Tách biên bậc 1
- ✅ Sobel
- ✅ Prewitt
- ✅ Roberts
- ✅ Kirsch

### Bài 9: Tách biên bậc 2
- ✅ Laplacian
- ✅ LoG (Laplacian of Gaussian)
- ✅ Image Sharpening

### Bài 10-12: Xử lý Fourier
- ✅ FFT Transform
- ✅ Ideal Low-pass Filter
- ✅ Gaussian Low-pass Filter
- ✅ Ideal High-pass Filter
- ✅ Butterworth High-pass Filter

## Công nghệ sử dụng

- **Python 3.8+**
- **OpenCV** - Xử lý ảnh
- **NumPy** - Tính toán ma trận
- **Pillow** - Xử lý định dạng ảnh
- **Matplotlib** - Vẽ biểu đồ
- **Tkinter** - Giao diện đồ họa

## Hướng dẫn nhanh

### Cài đặt và chạy

```bash
# Di chuyển vào thư mục source code
cd 01_Source_Code

# Cài đặt thư viện
pip install -r requirements.txt

# Tạo ảnh mẫu
python create_samples.py

# Chạy ứng dụng
python comprehensive_app.py
```

### Tạo file .EXE

```bash
# Cài PyInstaller
pip install pyinstaller

# Đóng gói ứng dụng
pyinstaller --noconfirm --onefile --windowed --name "XuLyAnh_Final" --clean comprehensive_app.py

# File .exe sẽ nằm trong thư mục dist/
```

## Hướng dẫn sử dụng ứng dụng

1. **Tải ảnh**: Click "Tải ảnh" để chọn ảnh từ máy
2. **Chọn chức năng**: Click vào các nút bên trái để xử lý
3. **Xem kết quả**: Ảnh gốc và ảnh xử lý hiển thị song song
4. **Lưu kết quả**: Click "Lưu ảnh" để lưu ảnh đã xử lý
5. **Reset**: Click "Reset" để quay về ảnh gốc

## Cấu trúc code

### `image_processing.py`
Thư viện xử lý ảnh với class `ImageProcessor` chứa các static methods:
- Tất cả hàm nhận input là numpy array
- Tự động chuyển sang grayscale khi cần
- Return kết quả dưới dạng numpy array

### `comprehensive_app.py`
Giao diện ứng dụng với class `ImageProcessingApp`:
- Sử dụng Tkinter để tạo GUI
- Gọi các hàm từ `image_processing.py`
- Hiển thị ảnh và thông tin xử lý

## Câu hỏi vấn đáp

**Q: Tại sao chuyển sang ảnh xám trước khi xử lý?**

A: Xử lý trên ảnh xám giảm khối lượng tính toán gấp 3 lần so với ảnh màu. Thông tin về cấu trúc và biên chủ yếu nằm ở cường độ sáng chứ không phải màu sắc.

**Q: Khác biệt giữa Average và Median filter?**

A: Average lấy trung bình cộng, làm mờ cả biên. Median lấy giá trị trung vị, giữ được độ sắc nét, hiệu quả với nhiễu muối tiêu.

**Q: Tại sao FFT spectrum có điểm sáng ở giữa?**

A: Điểm sáng ở giữa là DC component (tần số 0), đại diện cho độ sáng trung bình. Dùng `fftshift` để đưa tần số 0 vào giữa cho dễ quan sát.

## Tài liệu tham khảo

- [OpenCV Documentation](https://docs.opencv.org/)
- [NumPy Documentation](https://numpy.org/doc/)
- Digital Image Processing - Gonzalez & Woods

## Tác giả

- **Sinh viên**: [Tên của bạn]
- **MSSV**: [Mã số sinh viên]
- **Môn học**: Xử lý ảnh
- **Năm học**: 2024-2025

## License

Dự án này được tạo cho mục đích học tập.