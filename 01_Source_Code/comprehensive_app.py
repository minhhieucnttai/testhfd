"""
Comprehensive Image Processing Application
Ứng dụng xử lý ảnh tổng hợp - Bài 1-12
Giao diện Tkinter tích hợp đầy đủ các chức năng
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import sys

# Import thư viện xử lý
from image_processing import ImageProcessor


class ImageProcessingApp:
    """Ứng dụng xử lý ảnh với giao diện Tkinter"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng Dụng Xử Lý Ảnh - Bài 1-12")
        self.root.geometry("1400x800")
        
        # Biến lưu trữ
        self.original_image = None
        self.processed_image = None
        self.current_image_path = None
        
        # Tạo giao diện
        self.create_widgets()
        
    def create_widgets(self):
        """Tạo các widget cho giao diện"""
        
        # Main container
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Controls
        left_panel = ttk.Frame(main_frame, width=300)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=(0, 10))
        
        # Right panel - Display
        right_panel = ttk.Frame(main_frame)
        right_panel.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # === LEFT PANEL ===
        
        # File operations
        file_frame = ttk.LabelFrame(left_panel, text="File Operations", padding=10)
        file_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(file_frame, text="Tải ảnh", command=self.load_image).pack(fill=tk.X, pady=2)
        ttk.Button(file_frame, text="Lưu ảnh", command=self.save_image).pack(fill=tk.X, pady=2)
        ttk.Button(file_frame, text="Reset", command=self.reset_image).pack(fill=tk.X, pady=2)
        
        # Scrollable function frame
        canvas_frame = ttk.Frame(left_panel)
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        canvas = tk.Canvas(canvas_frame, width=280)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bài 1-3: Chức năng cơ bản
        basic_frame = ttk.LabelFrame(scrollable_frame, text="Bài 1-3: Cơ bản", padding=10)
        basic_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(basic_frame, text="Ảnh xám", command=self.apply_grayscale).pack(fill=tk.X, pady=2)
        ttk.Button(basic_frame, text="Phân ngưỡng", command=self.apply_threshold).pack(fill=tk.X, pady=2)
        ttk.Button(basic_frame, text="Tách kênh màu", command=self.split_channels).pack(fill=tk.X, pady=2)
        
        # Threshold slider
        self.threshold_var = tk.IntVar(value=127)
        ttk.Label(basic_frame, text="Ngưỡng:").pack(fill=tk.X)
        ttk.Scale(basic_frame, from_=0, to=255, variable=self.threshold_var, orient=tk.HORIZONTAL).pack(fill=tk.X)
        
        # Bài 4-6: Histogram
        histogram_frame = ttk.LabelFrame(scrollable_frame, text="Bài 4-6: Histogram", padding=10)
        histogram_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(histogram_frame, text="Kéo giãn tương phản", command=self.apply_contrast_stretch).pack(fill=tk.X, pady=2)
        ttk.Button(histogram_frame, text="Cân bằng Histogram", command=self.apply_histogram_eq).pack(fill=tk.X, pady=2)
        ttk.Button(histogram_frame, text="Khớp Histogram", command=self.apply_histogram_match).pack(fill=tk.X, pady=2)
        ttk.Button(histogram_frame, text="CLAHE", command=self.apply_clahe).pack(fill=tk.X, pady=2)
        ttk.Button(histogram_frame, text="Hiển thị Histogram", command=self.show_histogram).pack(fill=tk.X, pady=2)
        
        # Bài 7: Lọc nhiễu
        filter_frame = ttk.LabelFrame(scrollable_frame, text="Bài 7: Lọc nhiễu", padding=10)
        filter_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(filter_frame, text="Lọc trung bình 3x3", command=lambda: self.apply_average_filter(3)).pack(fill=tk.X, pady=2)
        ttk.Button(filter_frame, text="Lọc trung bình 5x5", command=lambda: self.apply_average_filter(5)).pack(fill=tk.X, pady=2)
        ttk.Button(filter_frame, text="Lọc trung vị 3x3", command=lambda: self.apply_median_filter(3)).pack(fill=tk.X, pady=2)
        ttk.Button(filter_frame, text="Lọc trung vị 5x5", command=lambda: self.apply_median_filter(5)).pack(fill=tk.X, pady=2)
        
        # Bài 8: Tách biên bậc 1
        edge1_frame = ttk.LabelFrame(scrollable_frame, text="Bài 8: Tách biên bậc 1", padding=10)
        edge1_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(edge1_frame, text="Sobel", command=self.apply_sobel).pack(fill=tk.X, pady=2)
        ttk.Button(edge1_frame, text="Prewitt", command=self.apply_prewitt).pack(fill=tk.X, pady=2)
        ttk.Button(edge1_frame, text="Roberts", command=self.apply_roberts).pack(fill=tk.X, pady=2)
        ttk.Button(edge1_frame, text="Kirsch", command=self.apply_kirsch).pack(fill=tk.X, pady=2)
        
        # Bài 9: Tách biên bậc 2
        edge2_frame = ttk.LabelFrame(scrollable_frame, text="Bài 9: Tách biên bậc 2", padding=10)
        edge2_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(edge2_frame, text="Laplacian", command=self.apply_laplacian).pack(fill=tk.X, pady=2)
        ttk.Button(edge2_frame, text="LoG", command=self.apply_log).pack(fill=tk.X, pady=2)
        ttk.Button(edge2_frame, text="Làm nét", command=self.apply_sharpen).pack(fill=tk.X, pady=2)
        
        # Bài 10-12: Fourier
        fourier_frame = ttk.LabelFrame(scrollable_frame, text="Bài 10-12: Fourier", padding=10)
        fourier_frame.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Button(fourier_frame, text="FFT Spectrum", command=self.show_fft).pack(fill=tk.X, pady=2)
        ttk.Button(fourier_frame, text="Ideal Low-pass", command=self.apply_ideal_lowpass).pack(fill=tk.X, pady=2)
        ttk.Button(fourier_frame, text="Gaussian Low-pass", command=self.apply_gaussian_lowpass).pack(fill=tk.X, pady=2)
        ttk.Button(fourier_frame, text="Ideal High-pass", command=self.apply_ideal_highpass).pack(fill=tk.X, pady=2)
        ttk.Button(fourier_frame, text="Butterworth High-pass", command=self.apply_butterworth_highpass).pack(fill=tk.X, pady=2)
        
        # Cutoff slider for Fourier
        self.cutoff_var = tk.IntVar(value=30)
        ttk.Label(fourier_frame, text="Cutoff:").pack(fill=tk.X)
        ttk.Scale(fourier_frame, from_=10, to=100, variable=self.cutoff_var, orient=tk.HORIZONTAL).pack(fill=tk.X)
        
        # === RIGHT PANEL ===
        
        # Image display frame
        display_frame = ttk.LabelFrame(right_panel, text="Hiển thị ảnh", padding=10)
        display_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Create two columns for original and processed
        self.original_label = ttk.Label(display_frame, text="Ảnh gốc", anchor="center")
        self.original_label.grid(row=0, column=0, padx=5)
        
        self.processed_label = ttk.Label(display_frame, text="Ảnh xử lý", anchor="center")
        self.processed_label.grid(row=0, column=1, padx=5)
        
        self.original_canvas = tk.Label(display_frame, bg="gray", width=50, height=30)
        self.original_canvas.grid(row=1, column=0, padx=5, pady=5)
        
        self.processed_canvas = tk.Label(display_frame, bg="gray", width=50, height=30)
        self.processed_canvas.grid(row=1, column=1, padx=5, pady=5)
        
        # Info frame
        info_frame = ttk.LabelFrame(right_panel, text="Thông tin", padding=10)
        info_frame.pack(fill=tk.X)
        
        self.info_text = tk.Text(info_frame, height=6, wrap=tk.WORD)
        self.info_text.pack(fill=tk.BOTH, expand=True)
        
    def load_image(self):
        """Tải ảnh từ file"""
        file_path = filedialog.askopenfilename(
            title="Chọn ảnh",
            filetypes=[
                ("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.current_image_path = file_path
            self.original_image = cv2.imread(file_path)
            
            if self.original_image is None:
                messagebox.showerror("Lỗi", "Không thể đọc ảnh!")
                return
            
            self.processed_image = None
            self.display_images()
            self.update_info(f"Đã tải: {os.path.basename(file_path)}\nKích thước: {self.original_image.shape}")
    
    def save_image(self):
        """Lưu ảnh đã xử lý"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh xử lý để lưu!")
            return
        
        file_path = filedialog.asksaveasfilename(
            title="Lưu ảnh",
            defaultextension=".png",
            filetypes=[
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            cv2.imwrite(file_path, self.processed_image)
            messagebox.showinfo("Thành công", f"Đã lưu ảnh: {os.path.basename(file_path)}")
    
    def reset_image(self):
        """Reset về ảnh gốc"""
        if self.original_image is not None:
            self.processed_image = None
            self.display_images()
            self.update_info("Đã reset về ảnh gốc")
    
    def display_images(self):
        """Hiển thị ảnh gốc và ảnh xử lý"""
        if self.original_image is not None:
            # Display original
            img_rgb = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img_rgb)
            img_pil.thumbnail((400, 400))
            img_tk = ImageTk.PhotoImage(img_pil)
            self.original_canvas.configure(image=img_tk)
            self.original_canvas.image = img_tk
        
        if self.processed_image is not None:
            # Display processed
            if len(self.processed_image.shape) == 2:
                img_pil = Image.fromarray(self.processed_image)
            else:
                img_rgb = cv2.cvtColor(self.processed_image, cv2.COLOR_BGR2RGB)
                img_pil = Image.fromarray(img_rgb)
            
            img_pil.thumbnail((400, 400))
            img_tk = ImageTk.PhotoImage(img_pil)
            self.processed_canvas.configure(image=img_tk)
            self.processed_canvas.image = img_tk
    
    def update_info(self, text):
        """Cập nhật thông tin"""
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(1.0, text)
    
    def check_image_loaded(self):
        """Kiểm tra đã tải ảnh chưa"""
        if self.original_image is None:
            messagebox.showwarning("Cảnh báo", "Vui lòng tải ảnh trước!")
            return False
        return True
    
    # === PROCESSING FUNCTIONS ===
    
    def apply_grayscale(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.to_grayscale(self.original_image)
        self.display_images()
        self.update_info("Đã chuyển sang ảnh xám\nCông thức: L = 0.299*R + 0.587*G + 0.114*B")
    
    def apply_threshold(self):
        if not self.check_image_loaded():
            return
        threshold = self.threshold_var.get()
        self.processed_image = ImageProcessor.binary_threshold(self.original_image, threshold)
        self.display_images()
        self.update_info(f"Phân ngưỡng với ngưỡng = {threshold}")
    
    def split_channels(self):
        if not self.check_image_loaded():
            return
        channels = ImageProcessor.split_channels(self.original_image)
        
        # Create new window to show channels
        window = tk.Toplevel(self.root)
        window.title("Tách kênh màu")
        window.geometry("900x500")
        
        channel_names = ['R', 'G', 'B']
        for idx, name in enumerate(channel_names):
            frame = ttk.Frame(window)
            frame.grid(row=0, column=idx, padx=10, pady=10)
            
            ttk.Label(frame, text=f"Kênh {name}").pack()
            
            channel_img = channels[name]
            img_pil = Image.fromarray(channel_img)
            img_pil.thumbnail((250, 250))
            img_tk = ImageTk.PhotoImage(img_pil)
            
            label = tk.Label(frame, image=img_tk)
            label.image = img_tk
            label.pack()
        
        self.update_info("Đã tách các kênh màu R, G, B")
    
    def apply_contrast_stretch(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.contrast_stretching(self.original_image)
        self.display_images()
        self.update_info("Kéo giãn tương phản\nMở rộng dải giá trị pixel về [0, 255]")
    
    def apply_histogram_eq(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.histogram_equalization(self.original_image)
        self.display_images()
        self.update_info("Cân bằng Histogram\nPhân bố lại độ sáng để tăng độ tương phản")
    
    def apply_histogram_match(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.histogram_matching(self.original_image)
        self.display_images()
        self.update_info("Khớp Histogram\nBiến đổi theo phân bố Gaussian")
    
    def apply_clahe(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.clahe(self.original_image)
        self.display_images()
        self.update_info("CLAHE\nCân bằng Histogram thích ứng cục bộ")
    
    def show_histogram(self):
        if not self.check_image_loaded():
            return
        
        hist = ImageProcessor.get_histogram(self.original_image)
        
        # Create new window
        window = tk.Toplevel(self.root)
        window.title("Histogram")
        window.geometry("600x400")
        
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(hist)
        ax.set_xlabel('Pixel Value')
        ax.set_ylabel('Frequency')
        ax.set_title('Histogram')
        ax.grid(True)
        
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.update_info("Đã hiển thị Histogram")
    
    def apply_average_filter(self, kernel_size):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.average_filter(self.original_image, kernel_size)
        self.display_images()
        self.update_info(f"Lọc trung bình {kernel_size}x{kernel_size}\nLàm mờ để giảm nhiễu")
    
    def apply_median_filter(self, kernel_size):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.median_filter(self.original_image, kernel_size)
        self.display_images()
        self.update_info(f"Lọc trung vị {kernel_size}x{kernel_size}\nHiệu quả với nhiễu muối tiêu")
    
    def apply_sobel(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.sobel_edge(self.original_image)
        self.display_images()
        self.update_info("Sobel Edge Detection\nĐạo hàm bậc 1")
    
    def apply_prewitt(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.prewitt_edge(self.original_image)
        self.display_images()
        self.update_info("Prewitt Edge Detection\nĐạo hàm bậc 1")
    
    def apply_roberts(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.roberts_edge(self.original_image)
        self.display_images()
        self.update_info("Roberts Edge Detection\nĐạo hàm bậc 1")
    
    def apply_kirsch(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.kirsch_edge(self.original_image)
        self.display_images()
        self.update_info("Kirsch Edge Detection\nĐạo hàm bậc 1 - 8 hướng")
    
    def apply_laplacian(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.laplacian_edge(self.original_image)
        self.display_images()
        self.update_info("Laplacian Edge Detection\nĐạo hàm bậc 2")
    
    def apply_log(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.laplacian_of_gaussian(self.original_image)
        self.display_images()
        self.update_info("Laplacian of Gaussian (LoG)\nLàm mịn trước khi tách biên")
    
    def apply_sharpen(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.sharpen(self.original_image)
        self.display_images()
        self.update_info("Image Sharpening\nLàm nét ảnh sử dụng Laplacian")
    
    def show_fft(self):
        if not self.check_image_loaded():
            return
        
        magnitude_spectrum, _ = ImageProcessor.fft_transform(self.original_image)
        
        # Display as processed image
        self.processed_image = magnitude_spectrum
        self.display_images()
        self.update_info("FFT Magnitude Spectrum\nPhổ biên độ trong miền tần số")
    
    def apply_ideal_lowpass(self):
        if not self.check_image_loaded():
            return
        cutoff = self.cutoff_var.get()
        self.processed_image = ImageProcessor.ideal_lowpass_filter(self.original_image, cutoff)
        self.display_images()
        self.update_info(f"Ideal Low-pass Filter\nCutoff = {cutoff}\nLàm mờ bằng cách cắt tần số cao")
    
    def apply_gaussian_lowpass(self):
        if not self.check_image_loaded():
            return
        cutoff = self.cutoff_var.get()
        self.processed_image = ImageProcessor.gaussian_lowpass_filter(self.original_image, cutoff)
        self.display_images()
        self.update_info(f"Gaussian Low-pass Filter\nCutoff = {cutoff}\nLàm mờ mịn, giảm ringing")
    
    def apply_ideal_highpass(self):
        if not self.check_image_loaded():
            return
        cutoff = self.cutoff_var.get()
        self.processed_image = ImageProcessor.ideal_highpass_filter(self.original_image, cutoff)
        self.display_images()
        self.update_info(f"Ideal High-pass Filter\nCutoff = {cutoff}\nLàm nổi bật biên")
    
    def apply_butterworth_highpass(self):
        if not self.check_image_loaded():
            return
        cutoff = self.cutoff_var.get()
        self.processed_image = ImageProcessor.butterworth_highpass_filter(self.original_image, cutoff)
        self.display_images()
        self.update_info(f"Butterworth High-pass Filter\nCutoff = {cutoff}\nTách biên mềm mại")


def main():
    """Main function"""
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
