# Hướng dẫn tạo file .EXE

## Bước 1: Cài đặt PyInstaller

Mở Terminal/CMD tại thư mục `01_Source_Code` và chạy:

```bash
pip install pyinstaller
```

## Bước 2: Tạo file .EXE

Chạy lệnh sau:

```bash
pyinstaller --noconfirm --onefile --windowed --name "XuLyAnh_Final" --clean comprehensive_app.py
```

**Giải thích các tham số:**
- `--noconfirm`: Không hỏi xác nhận ghi đè
- `--onefile`: Đóng gói thành 1 file .exe duy nhất
- `--windowed`: Không hiển thị console (cho ứng dụng GUI)
- `--name "XuLyAnh_Final"`: Đặt tên cho file .exe
- `--clean`: Xóa cache trước khi build

## Bước 3: Lấy file .EXE

1. Sau khi chạy xong, vào thư mục `dist/` vừa được tạo ra
2. Copy file `XuLyAnh_Final.exe` vào thư mục `02_Ung_Dung_San_Pham/`
3. Copy cả thư mục `sample_images/` vào `02_Ung_Dung_San_Pham/` để có sẵn ảnh demo

## Bước 4: Kiểm tra

1. Vào thư mục `02_Ung_Dung_San_Pham/`
2. Double-click vào `XuLyAnh_Final.exe` để chạy
3. Thử tải ảnh từ `sample_images/` và test các chức năng

## Lưu ý

- File .exe có thể chạy trên máy Windows mà không cần cài Python
- Lần đầu chạy có thể bị Windows Defender cảnh báo, chọn "Run anyway"
- Kích thước file .exe khoảng 100-200MB do chứa toàn bộ thư viện

## Cấu trúc thư mục cuối cùng

```
02_Ung_Dung_San_Pham/
├── XuLyAnh_Final.exe    # File ứng dụng
├── sample_images/        # Ảnh mẫu
│   ├── gradient.png
│   ├── checkerboard.png
│   ├── noisy.png
│   ├── color_blocks.png
│   └── low_contrast.png
└── HUONG_DAN.md         # File này
```

## Troubleshooting

### Lỗi: "Failed to execute script"
- Đảm bảo file `image_processing.py` cùng thư mục với `comprehensive_app.py`
- Thử thêm option `--onedir` thay vì `--onefile`

### Lỗi: Import Error
- Cài đầy đủ thư viện: `pip install -r requirements.txt`
- Chạy lại PyInstaller

### File .exe quá lớn
- Đây là bình thường vì chứa Python runtime và thư viện
- Có thể dùng UPX để nén: `pip install pyinstaller[encryption]`
