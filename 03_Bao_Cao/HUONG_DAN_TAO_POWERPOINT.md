# HƯỚNG DẪN TẠO POWERPOINT TỪ NỘI DUNG

## Cách sử dụng file Bai_Thuyet_Trinh_PowerPoint.md

### Phương án 1: Tạo thủ công bằng Microsoft PowerPoint

1. **Mở PowerPoint** → Tạo presentation mới
2. **Chọn theme:** Chọn theme chuyên nghiệp (ví dụ: Ion, Facet, Integral)
3. **Tạo 27 slides** theo nội dung trong file .md
4. **Copy nội dung** từng slide vào PowerPoint

#### Gợi ý bố cục từng loại slide:

**Slide tiêu đề (Slide 1):**
- Layout: Title Slide
- Font lớn cho tiêu đề
- Thêm hình ảnh background liên quan đến image processing

**Slide nội dung (Slide 2-26):**
- Layout: Title and Content
- Bullet points rõ ràng
- Font size: Title 32pt, Content 20-24pt

**Slide kết thúc (Slide 27):**
- Layout: Title and Content
- Danh sách tài liệu tham khảo

### Phương án 2: Sử dụng công cụ chuyển đổi

#### A. Pandoc (Markdown → PowerPoint)
```bash
# Cài đặt pandoc
sudo apt-get install pandoc

# Chuyển đổi
pandoc Bai_Thuyet_Trinh_PowerPoint.md -o Bai_Thuyet_Trinh.pptx
```

#### B. Marp (Markdown Presentation)
```bash
# Cài đặt Marp CLI
npm install -g @marp-team/marp-cli

# Chuyển đổi sang PowerPoint
marp Bai_Thuyet_Trinh_PowerPoint.md --pptx -o Bai_Thuyet_Trinh.pptx
```

#### C. Google Slides
1. Tạo Google Slides mới
2. File → Import slides
3. Upload file hoặc paste nội dung

### Phương án 3: Sử dụng template có sẵn

Có thể tải template PowerPoint về và điền nội dung:
- Microsoft Office Templates
- SlidesCarnival
- SlidesGo

---

## GỢI Ý HÌNH ẢNH CHO TỪNG SLIDE

### SLIDE 1: Trang bìa
- Background: Gradient màu xanh dương/tím
- Icon: Camera, image processing symbols
- Logo trường đại học (nếu có)

### SLIDE 3: Giới thiệu
- Icon: Magnifying glass over image
- Diagram: Input → Process → Output

### SLIDE 4: Mục tiêu
- Checkmark icons
- Flowchart đơn giản

### SLIDE 5: Công nghệ
- Logo: Python, OpenCV, NumPy, Tkinter
- Stack diagram

### SLIDE 6: Kiến trúc
- Tree diagram của folder structure
- Icon folders

### SLIDE 7: Kiến trúc code
- UML class diagram (đơn giản)
- Code snippet (highlight syntax)

### SLIDE 8: Bài 1-3
- **Before/After images:**
  - Ảnh màu → Ảnh xám
  - Ảnh gốc → Ảnh binary
  - RGB channels separated

### SLIDE 9: Kéo giãn tương phản
- Histogram before/after
- Ảnh tối → Ảnh sáng

### SLIDE 10: Histogram
- Histogram charts
- CLAHE example

### SLIDE 11: Lọc nhiễu
- Noisy image → Clean image
- Comparison: Average vs Median

### SLIDE 12-13: Tách biên bậc 1
- Original → Sobel edge
- Original → Prewitt edge
- Original → Roberts edge
- Original → Kirsch edge
- Comparison table

### SLIDE 14: Tách biên bậc 2
- Laplacian result
- LoG result
- Sharpening example

### SLIDE 15: FFT
- Original image
- FFT spectrum (magnitude)
- Diagram: Spatial → Frequency domain

### SLIDE 16-17: Low-pass & High-pass
- Filter mask visualization
- Before/After images
- Frequency spectrum with filter overlay

### SLIDE 18: Giao diện
- **Screenshot của ứng dụng**
- Arrows pointing to features
- Labels cho các phần

### SLIDE 19: Demo workflow
- Flowchart: Load → Process → Save
- Screenshot từng bước

### SLIDE 20-21: Kết quả demo
- **Before/After comparisons**
- Metrics table (processing time, quality)

### SLIDE 22: Ưu điểm & Hạn chế
- Green checkmarks for pros
- Yellow warning icons for cons

### SLIDE 23: Hướng phát triển
- Roadmap timeline
- Future features icons

### SLIDE 24: Kinh nghiệm
- Lightbulb icon
- Quote box

### SLIDE 25: Kết luận
- Summary box
- Achievement badges
- Project metrics

### SLIDE 26: Q&A
- Question mark icon
- Contact information

### SLIDE 27: Tài liệu
- Book icons
- Links formatted nicely

---

## MÀU SẮC ĐỀ XUẤT

### Color Scheme 1: Professional Blue
- Primary: #2E86AB (Blue)
- Secondary: #A23B72 (Purple)
- Accent: #F18F01 (Orange)
- Background: #FFFFFF (White)
- Text: #1A1A1A (Dark Gray)

### Color Scheme 2: Tech Green
- Primary: #06A77D (Green)
- Secondary: #005F73 (Teal)
- Accent: #FF6B35 (Orange)
- Background: #FAFAFA (Light Gray)
- Text: #2C2C2C (Dark Gray)

### Color Scheme 3: Modern Purple
- Primary: #5E60CE (Purple)
- Secondary: #7209B7 (Dark Purple)
- Accent: #F72585 (Pink)
- Background: #FFFFFF (White)
- Text: #212529 (Black)

---

## FONT ĐỀ XUẤT

**Tiêu đề:**
- Montserrat Bold
- Roboto Bold
- Arial Bold

**Nội dung:**
- Open Sans Regular
- Roboto Regular
- Calibri Regular

**Code:**
- Consolas
- Courier New
- Monaco

---

## ANIMATION ĐỀ XUẤT

### Slide transitions:
- Fade (tinh tế)
- Push (chuyên nghiệp)
- Tránh: Quá nhiều hiệu ứng rườm rà

### Object animations:
- Appear (cho bullet points)
- Fade In (cho hình ảnh)
- Grow & Turn (cho tiêu đề quan trọng)

**Lưu ý:** Sử dụng animation vừa phải, không làm rối mắt người xem

---

## CHECKLIST HOÀN THIỆN POWERPOINT

### Nội dung:
- [ ] Tất cả 27 slides đã được tạo
- [ ] Thông tin cá nhân đã điền đầy đủ
- [ ] Không có lỗi chính tả
- [ ] Số liệu chính xác

### Hình ảnh:
- [ ] Có ít nhất 1 hình ảnh/biểu đồ cho mỗi slide
- [ ] Screenshot giao diện ứng dụng
- [ ] Before/After images cho các chức năng
- [ ] Logo và icons phù hợp

### Thiết kế:
- [ ] Theme nhất quán
- [ ] Màu sắc hài hòa
- [ ] Font size dễ đọc (Title: 32pt+, Content: 20pt+)
- [ ] Không quá nhiều text trên 1 slide

### Kỹ thuật:
- [ ] Animation vừa phải
- [ ] Slide numbers
- [ ] File size < 50MB
- [ ] Đã test trình chiếu

---

## TIPS TRÌNH BÀY

1. **Thời gian:** 15-20 phút cho 27 slides (~40s/slide)
2. **Tập trung:** Slides 8-17 (các chức năng chính)
3. **Demo:** Chuẩn bị demo trực tiếp ứng dụng
4. **Backup:** Lưu file PDF phòng hỏng file
5. **Questions:** Chuẩn bị câu trả lời cho Q&A

### Trong quá trình trình bày:
- Nói chậm, rõ ràng
- Giải thích thuật toán bằng ngôn ngữ đơn giản
- Chỉ vào hình ảnh khi giải thích
- Tương tác với khán giả
- Time management: Theo dõi thời gian

---

## MẪU TEMPLATE SẴN (Tùy chọn)

Nếu muốn sử dụng template có sẵn, có thể tải từ:

1. **Microsoft Office Templates**
   - Mở PowerPoint → File → New
   - Search: "Technical Presentation"

2. **SlidesCarnival** (Free)
   - https://www.slidescarnival.com/
   - Category: Technology, Education

3. **SlidesGo** (Free)
   - https://slidesgo.com/
   - Search: "Technology Presentation"

4. **Canva** (Free/Premium)
   - https://www.canva.com/
   - Templates: Presentation → Technology

---

## LƯU Ý CUỐI CÙNG

- **File name:** MSSV_HoTen_BaiThuyetTrinh.pptx
- **Backup:** Lưu cả Google Drive và USB
- **PDF version:** Export sang PDF để phòng trường hợp
- **Video:** Có thể quay video trình bày để luyện tập
- **Feedback:** Nhờ bạn bè xem và góp ý trước khi nộp

**Chúc bạn trình bày thành công! 🎉**
