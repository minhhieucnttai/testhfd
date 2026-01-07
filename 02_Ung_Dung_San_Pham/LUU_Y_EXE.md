# Lưu ý về file .EXE

## Trạng thái hiện tại

File `XuLyAnh_Final.exe` **CHƯA ĐƯỢC TẠO** trong repository này.

## Lý do

File `.exe` được tạo bằng PyInstaller có kích thước rất lớn (100-200MB) do chứa:
- Python runtime
- Tất cả thư viện (OpenCV, NumPy, Pillow, Matplotlib)
- Dependencies

Do đó, file .exe **KHÔNG NÊN** commit vào Git repository.

## Cách tạo file .EXE

Làm theo hướng dẫn trong file `HUONG_DAN.md` hoặc thực hiện các bước sau:

### Bước 1: Cài đặt PyInstaller
```bash
pip install pyinstaller
```

### Bước 2: Di chuyển vào thư mục source code
```bash
cd 01_Source_Code
```

### Bước 3: Chạy lệnh đóng gói
```bash
pyinstaller --noconfirm --onefile --windowed --name "XuLyAnh_Final" --clean comprehensive_app.py
```

### Bước 4: Lấy file .exe
- File `XuLyAnh_Final.exe` sẽ nằm trong thư mục `dist/`
- Copy file này vào thư mục `02_Ung_Dung_San_Pham/`

### Bước 5: Kiểm tra
- Double-click vào `XuLyAnh_Final.exe` để chạy
- Thử tải ảnh từ thư mục `sample_images/`
- Test các chức năng

## Lưu ý khi nộp bài

Khi chuẩn bị CD nộp bài:
1. Tạo file .exe như hướng dẫn trên
2. Copy vào thư mục `02_Ung_Dung_San_Pham/`
3. Đảm bảo thư mục `sample_images/` đã được copy
4. Nén toàn bộ thư mục `MSSV_HoTen_DoAnXuLyAnh/` để nộp

## Cấu trúc thư mục khi hoàn thành

```
02_Ung_Dung_San_Pham/
├── XuLyAnh_Final.exe     ← File này bạn cần tạo
├── sample_images/         ← Đã có sẵn
├── HUONG_DAN.md          ← Đã có sẵn
└── LUU_Y_EXE.md          ← File này
```
