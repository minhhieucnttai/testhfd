# QUICK START GUIDE - Enhanced Image Processing Application v2.0

## 🚀 Cách chạy ứng dụng

### Bước 1: Cài đặt dependencies

```bash
cd 01_Source_Code
pip install opencv-python numpy pillow matplotlib
```

### Bước 2: Chạy ứng dụng

```bash
python comprehensive_app.py
```

## 📋 Tính năng chính

### 1. Interface với 6 Tabs
- **📋 Cơ bản:** Grayscale, Threshold, Channel Splitting + 3 Presets
- **📊 Histogram:** Contrast Stretching, Histogram Equalization, CLAHE
- **🔍 Lọc nhiễu:** Average Filter, Median Filter (3x3, 5x5)
- **🔲 Tách biên:** Sobel, Prewitt, Roberts, Kirsch, Laplacian, LoG, Sharpen
- **🌊 Fourier:** FFT, Low-pass, High-pass Filters
- **⚡ Nâng cao:** Pipelines, Batch Processing, Advanced Tools

### 2. Menu Bar
- **File:** Load (Ctrl+O), Save (Ctrl+S), Exit
- **Edit:** Undo (Ctrl+Z), Redo (Ctrl+Y), Reset (Ctrl+R)
- **View:** Zoom (+/-/0), Toggle Histogram, Auto Preview
- **Help:** User Guide, About

### 3. Tính năng nâng cao
- ✅ **Undo/Redo:** 10 levels history
- ✅ **Real-time Histogram:** Side-by-side comparison
- ✅ **Zoom:** 10% - 500%
- ✅ **Presets:** Quick processing (3 presets)
- ✅ **Pipelines:** Multi-step processing (3 pipelines)
- ✅ **Auto Preview:** Real-time parameter updates

## 🎯 Workflow ví dụ

### Workflow 1: Xử lý ảnh tối
```
1. Load image (Ctrl+O)
2. Tab "Histogram" -> Click "Cân bằng Histogram"
3. Xem histogram comparison
4. If needed, Undo (Ctrl+Z) and try CLAHE
5. Save (Ctrl+S)
```

### Workflow 2: Phát hiện biên
```
1. Load image
2. Tab "Nâng cao" -> Click "Edge Enhancement Pipeline"
3. Zoom in (+) to check details
4. Tab "Tách biên" -> Try different methods (Sobel, Prewitt)
5. Use Undo/Redo to compare
6. Save best result
```

### Workflow 3: Giảm nhiễu
```
1. Load noisy image
2. Tab "Lọc nhiễu" -> Try "Lọc trung vị 5x5"
3. Check histogram
4. Tab "Nâng cao" -> Try "Noise Reduction Pipeline"
5. Compare results with Undo/Redo
6. Save
```

## 📊 So sánh Version 1.0 vs 2.0

| Feature | v1.0 | v2.0 Enhanced |
|---------|------|---------------|
| Interface | Single panel | 6 Tabs + Menu |
| Functions | 22 | 32+ |
| Undo/Redo | ❌ | ✅ (10 levels) |
| Histogram | External window only | Integrated panel |
| Zoom | ❌ | ✅ (10%-500%) |
| Presets | ❌ | ✅ (3 presets) |
| Pipelines | ❌ | ✅ (3 pipelines) |
| Shortcuts | ❌ | ✅ (Full keyboard support) |
| Auto Preview | ❌ | ✅ |
| Code lines | 467 | 1040 (+122%) |

## 🔧 Troubleshooting

### Lỗi: ModuleNotFoundError: No module named 'cv2'
**Giải pháp:**
```bash
pip install opencv-python
```

### Lỗi: Application chậm với ảnh lớn
**Giải pháp:**
- Tắt histogram panel (View -> Show Histogram)
- Sử dụng ảnh có kích thước < 2000x2000 pixels

### Lỗi: Không thể load ảnh
**Giải pháp:**
- Kiểm tra định dạng ảnh (phải là .jpg, .png, .bmp, .tiff)
- Thử ảnh mẫu trong thư mục sample_images/

## 📖 Tài liệu chi tiết

- **ENHANCEMENTS.md:** Tài liệu đầy đủ về các tính năng mới
- **HUONG_DAN_SU_DUNG.md:** Hướng dẫn sử dụng chi tiết
- **README.md:** Tổng quan dự án

## 💡 Tips hay

1. **Phím tắt thường dùng:**
   - Ctrl+O: Load image
   - Ctrl+S: Save image
   - Ctrl+Z: Undo
   - Ctrl+Y: Redo
   - +/-: Zoom in/out
   - 0: Reset zoom

2. **Sử dụng Auto Preview:**
   - Bật checkbox "Auto Preview"
   - Kéo slider "Ngưỡng" hoặc "Cutoff" để xem kết quả real-time

3. **Workflow hiệu quả:**
   - Dùng Presets cho xử lý nhanh
   - Dùng Pipelines cho kết quả chuyên nghiệp
   - Dùng Undo/Redo để so sánh các phương pháp

## 🎓 Dành cho sinh viên

### Các bài tập được tích hợp:
- **Bài 1-3:** Tab "Cơ bản"
- **Bài 4-6:** Tab "Histogram"
- **Bài 7:** Tab "Lọc nhiễu"
- **Bài 8:** Tab "Tách biên" (Edge 1st order)
- **Bài 9:** Tab "Tách biên" (Edge 2nd order + Sharpen)
- **Bài 10-12:** Tab "Fourier"

### Demo cho giảng viên:
1. Mở app -> tự động maximize
2. Load ảnh mẫu từ sample_images/
3. Demo các tab lần lượt
4. Showcase Undo/Redo
5. Showcase Zoom
6. Showcase Histogram comparison
7. Demo Presets & Pipelines

## 🏆 Điểm nổi bật

✨ **Giao diện chuyên nghiệp** - Tabbed layout với 6 tabs có tổ chức
✨ **Chức năng đầy đủ** - 22+ functions + 10 advanced features
✨ **Dễ sử dụng** - Intuitive UI, keyboard shortcuts, auto-preview
✨ **Mạnh mẽ** - Undo/redo, zoom, histogram, pipelines
✨ **Hiện đại** - Modern styling, responsive panels, rich info

---

**Version 2.0 - Enhanced Edition**
**Developed for Image Processing Course**
**© 2024-2025**
