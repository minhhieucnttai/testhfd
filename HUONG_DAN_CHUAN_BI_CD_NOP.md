# Hướng Dẫn Chuẩn Bị CD Nộp

## Mục lục
1. [Yêu cầu chung](#yêu-cầu-chung)
2. [Cấu trúc thư mục](#cấu-trúc-thư-mục)
3. [Nội dung cần có trong CD](#nội-dung-cần-có-trong-cd)
4. [Quy tắc đặt tên file](#quy-tắc-đặt-tên-file)
5. [Hướng dẫn ghi CD](#hướng-dẫn-ghi-cd)
6. [Dán nhãn CD](#dán-nhãn-cd)
7. [Checklist trước khi nộp](#checklist-trước-khi-nộp)

---

## Yêu cầu chung

### Loại đĩa
- Sử dụng CD-R hoặc DVD-R mới, chất lượng tốt
- Không sử dụng CD-RW hay DVD-RW (đĩa có thể ghi đè)
- Dung lượng đĩa phù hợp với dữ liệu cần lưu

### Định dạng ghi
- Ghi ở chế độ **finalize** (hoàn thiện đĩa)
- Tốc độ ghi: 8x hoặc thấp hơn để đảm bảo chất lượng
- Định dạng file system: ISO 9660 hoặc UDF

---

## Cấu trúc thư mục

```
CD_ROOT/
│
├── 01_BAO_CAO/
│   ├── BaoCao_ChinhThuc.pdf
│   ├── BaoCao_TomTat.pdf
│   └── TaiLieu_ThamKhao/
│
├── 02_SOURCE_CODE/
│   ├── src/
│   ├── README.md
│   └── requirements.txt (nếu có)
│
├── 03_TAI_LIEU_HUONG_DAN/
│   ├── HuongDan_CaiDat.pdf
│   ├── HuongDan_SuDung.pdf
│   └── Video_Demo/ (nếu có)
│
├── 04_DU_LIEU/
│   ├── Database/
│   └── Sample_Data/
│
├── 05_SLIDE_THUYET_TRINH/
│   └── Slide_BaoCao.pptx
│
└── THONG_TIN.txt
```

---

## Nội dung cần có trong CD

### 1. Báo cáo (01_BAO_CAO)
- **Báo cáo chính thức** (PDF):
  - Trang bìa đầy đủ thông tin
  - Lời cảm ơn
  - Mục lục
  - Nội dung các chương
  - Tài liệu tham khảo
  - Phụ lục (nếu có)

- **Báo cáo tóm tắt** (PDF):
  - 2-5 trang tóm tắt nội dung chính
  - Mục tiêu, phương pháp, kết quả

### 2. Mã nguồn (02_SOURCE_CODE)
- Toàn bộ source code của dự án
- File README.md hướng dẫn:
  - Môi trường phát triển
  - Cách cài đặt
  - Cách chạy chương trình
  - Cấu trúc dự án
- File cấu hình (requirements.txt, package.json, etc.)
- **Lưu ý**: Không nén source code

### 3. Tài liệu hướng dẫn (03_TAI_LIEU_HUONG_DAN)
- **Hướng dẫn cài đặt**:
  - Yêu cầu hệ thống
  - Các bước cài đặt chi tiết
  - Xử lý lỗi thường gặp

- **Hướng dẫn sử dụng**:
  - Các chức năng chính
  - Hướng dẫn sử dụng có ảnh minh họa
  - FAQ

- **Video demo** (nếu có):
  - Định dạng: MP4, AVI
  - Thời lượng: 5-10 phút
  - Chất lượng: HD 720p trở lên

### 4. Dữ liệu (04_DU_LIEU)
- File database (SQL script, .db, etc.)
- Dữ liệu mẫu để test
- File cấu hình database

### 5. Slide thuyết trình (05_SLIDE_THUYET_TRINH)
- File PowerPoint hoặc PDF
- Nội dung rõ ràng, súc tích
- Có hình ảnh minh họa

### 6. File THONG_TIN.txt
File văn bản chứa thông tin cơ bản:
```
TÊN ĐỀ TÀI: [Tên đề tài]
MÔN HỌC: [Tên môn học]
LỚP: [Mã lớp]
GIẢNG VIÊN: [Tên giảng viên]

THÀNH VIÊN NHÓM:
1. [Họ tên] - [MSSV] - [Email] - [SĐT]
2. [Họ tên] - [MSSV] - [Email] - [SĐT]
...

NGÀY NỘP: [dd/mm/yyyy]

MÔ TẢ NGẮN:
[Mô tả ngắn gọn về đề tài]

CÔNG NGHỆ SỬ DỤNG:
- [Công nghệ 1]
- [Công nghệ 2]
...

GHI CHÚ:
[Các ghi chú đặc biệt nếu có]
```

---

## Quy tắc đặt tên file

### Nguyên tắc chung
- Không dùng dấu tiếng Việt
- Không dùng khoảng trắng (dùng _ hoặc -)
- Chỉ dùng chữ cái, số, gạch dưới (_) và gạch ngang (-)
- Tên file ngắn gọn, có ý nghĩa

### Ví dụ
✅ **Đúng**:
- `BaoCao_ChinhThuc.pdf`
- `Slide_BaoCao_Final.pptx`
- `HuongDan_CaiDat_v1.0.pdf`

❌ **Sai**:
- `Báo cáo chính thức.pdf` (có dấu)
- `report final final2.pdf` (có khoảng trắng, không rõ ràng)
- `bc.pdf` (quá ngắn, không rõ nghĩa)

---

## Hướng dẫn ghi CD

### Trên Windows

#### Sử dụng Windows Explorer
1. Mở **File Explorer**
2. Chuột phải vào ổ CD/DVD → chọn **Burn files to disc**
3. Nhập tên đĩa
4. Chọn **Like a USB flash drive** nếu muốn thêm file sau, hoặc **With a CD/DVD player** để finalize ngay
5. Kéo thả file vào cửa sổ đĩa
6. Click **Burn to disc** hoặc **Close session**

#### Sử dụng phần mềm CDBurnerXP (Miễn phí)
1. Tải và cài đặt CDBurnerXP từ trang chủ
2. Mở phần mềm, chọn **Data disc**
3. Thêm file/folder bằng cách kéo thả hoặc click **Add**
4. Kiểm tra dung lượng thanh dưới cùng
5. Click **Burn**
6. Chọn tốc độ ghi: **8x** hoặc thấp hơn
7. Tích chọn **Finalize disc**
8. Click **Burn disc**

#### Sử dụng ImgBurn (Miễn phí)
1. Tải và cài đặt ImgBurn
2. Chọn **Write files/folders to disc**
3. Thêm thư mục nguồn
4. Chọn tab **Advanced** → **Restrictions** → Tích **Finalize Disc**
5. Click **Build** để bắt đầu ghi

### Trên macOS

#### Sử dụng Finder
1. Mở **Finder**
2. Chèn đĩa CD/DVD trống
3. Chọn **Open Finder** khi được hỏi
4. Kéo thả file vào cửa sổ đĩa
5. Click **Burn** ở góc trên bên phải
6. Chọn tốc độ ghi thấp (4x-8x)
7. Click **Burn**

#### Sử dụng Disk Utility
1. Mở **Disk Utility** (Applications → Utilities)
2. Chọn menu **File** → **New Image** → **Image from Folder**
3. Chọn thư mục chứa dữ liệu
4. Lưu file .dmg
5. Click vào file .dmg → chọn **Burn**
6. Chọn đĩa CD/DVD và click **Burn**

### Trên Linux (Ubuntu)

#### Sử dụng Brasero
1. Cài đặt: `sudo apt-get install brasero`
2. Mở Brasero
3. Chọn **Data project**
4. Kéo thả file vào
5. Click **Burn**
6. Chọn tốc độ thấp và tích **Finalize disc**
7. Click **Burn**

#### Sử dụng dòng lệnh
```bash
# Tạo file ISO
mkisofs -o disc.iso -R -J /path/to/folder

# Ghi CD/DVD
cdrecord -v -dao speed=8 dev=/dev/sr0 disc.iso
```

---

## Dán nhãn CD

### Thông tin cần ghi trên nhãn

**Mặt trước:**
```
[TÊN TRƯỜNG ĐẠI HỌC]
[TÊN KHOA]

ĐỀ TÀI: [Tên đề tài]
MÔN HỌC: [Tên môn học]

SINH VIÊN THỰC HIỆN:
- [Họ tên 1] - [MSSV]
- [Họ tên 2] - [MSSV]

LỚP: [Mã lớp]
GVHD: [Tên giảng viên]

NGÀY NỘP: [dd/mm/yyyy]
```

### Cách dán nhãn

1. **Dùng bút CD chuyên dụng** (khuyến nghị):
   - Sử dụng bút dầu CD marker
   - Viết nhẹ nhàng, tránh gây trầy xước
   - Để khô hoàn toàn trước khi bảo quản

2. **Dùng nhãn in** (label sticker):
   - Sử dụng nhãn CD chuyên dụng
   - In bằng máy in laser hoặc in phun (mực khô nhanh)
   - Dán thẳng, tránh bong bóng khí
   - Chỉ dán 1 lớp, không dán chồng lên nhau

3. **In trực tiếp** (nếu máy hỗ trợ):
   - Sử dụng máy in CD có chức năng in trực tiếp
   - Chất lượng tốt nhất, chuyên nghiệp

### Lưu ý
- ❌ **KHÔNG** dùng bút thường, bút bi
- ❌ **KHÔNG** viết trực tiếp lên mặt ghi dữ liệu
- ❌ **KHÔNG** dùng băng dính thường
- ✅ Viết rõ ràng, dễ đọc
- ✅ Thông tin chính xác, đầy đủ

---

## Checklist trước khi nộp

### Kiểm tra nội dung

- [ ] Đã copy đầy đủ tất cả file cần thiết
- [ ] Cấu trúc thư mục đúng như yêu cầu
- [ ] Tên file, tên thư mục không có dấu tiếng Việt
- [ ] File THONG_TIN.txt có đầy đủ thông tin
- [ ] Báo cáo PDF mở được, không bị lỗi font
- [ ] Source code đầy đủ, có file README.md
- [ ] Tài liệu hướng dẫn rõ ràng, đầy đủ
- [ ] Slide thuyết trình hoàn chỉnh

### Kiểm tra kỹ thuật

- [ ] Đĩa đã được **finalize** (hoàn thiện)
- [ ] Kiểm tra đĩa trên ít nhất 1 máy tính khác
- [ ] Tất cả file đều mở được
- [ ] Không có file bị lỗi hoặc corrupt
- [ ] Tổng dung lượng không vượt quá dung lượng đĩa
- [ ] Tốc độ ghi đĩa ≤ 8x

### Kiểm tra nhãn và bao bì

- [ ] Đã dán/viết nhãn đầy đủ thông tin
- [ ] Thông tin trên nhãn chính xác
- [ ] Nhãn dán thẳng, không bị méo
- [ ] Đĩa không bị trầy xước
- [ ] Cho đĩa vào bao đựng chuyên dụng

### Kiểm tra cuối cùng

- [ ] Đọc lại toàn bộ thông tin 1 lần nữa
- [ ] So sánh với yêu cầu nộp bài của giảng viên
- [ ] Chuẩn bị 2 bản (nếu cần backup)
- [ ] Ghi nhận ngày nộp

---

## Xử lý sự cố thường gặp

### Đĩa không đọc được
**Nguyên nhân:**
- Đĩa chất lượng kém
- Tốc độ ghi quá cao
- Đầu đọc đĩa của máy tính bị lỗi
- Chưa finalize đĩa

**Giải pháp:**
- Sử dụng đĩa chất lượng tốt (Sony, Verbatim, Samsung)
- Ghi với tốc độ thấp (4x-8x)
- Luôn finalize đĩa sau khi ghi
- Kiểm tra trên nhiều máy khác nhau

### File bị lỗi khi mở
**Nguyên nhân:**
- File nguồn đã bị lỗi trước khi ghi
- Quá trình ghi bị lỗi
- Đĩa bị trầy xước

**Giải pháp:**
- Kiểm tra file nguồn trước khi ghi
- Ghi lại với tốc độ thấp hơn
- Sử dụng đĩa mới, tránh bụi bẩn

### Đĩa không đủ dung lượng
**Nguyên nhân:**
- Quá nhiều file không cần thiết
- File video/hình ảnh dung lượng lớn

**Giải pháp:**
- Sử dụng DVD thay vì CD (4.7GB vs 700MB)
- Nén video ở chất lượng vừa phải
- Loại bỏ file không cần thiết
- Chia thành 2 đĩa nếu cần

---

## Lời khuyên bổ sung

1. **Chuẩn bị sớm**: Ghi đĩa ít nhất 2-3 ngày trước ngày nộp
2. **Backup**: Luôn có 2 bản đĩa phòng trường hợp 1 bản bị lỗi
3. **Kiểm tra nhiều lần**: Mở từng file để đảm bảo không bị lỗi
4. **Bảo quản cẩn thận**: Để đĩa trong bao đựng, tránh ánh sáng mặt trời
5. **Đọc kỹ yêu cầu**: Mỗi giảng viên/môn học có thể có yêu cầu riêng
6. **Hỏi khi chưa rõ**: Liên hệ giảng viên nếu không chắc chắn về yêu cầu

---

## Tài liệu tham khảo

- ISO 9660 Standard
- CD-R/DVD-R Best Practices
- Hướng dẫn nộp đồ án của trường

---

**Chúc bạn hoàn thành tốt đồ án!**

*Tài liệu được tạo: 2026*
*Phiên bản: 1.0*
