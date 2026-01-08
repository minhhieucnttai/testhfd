"""
Enhanced Comprehensive Image Processing Application
Ứng dụng xử lý ảnh tổng hợp nâng cao - Bài 1-12
Giao diện Tkinter tích hợp đầy đủ các chức năng với tính năng nâng cao
Version: 2.0 - Advanced Edition
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import os
from collections import deque

# Import thư viện xử lý
from image_processing import ImageProcessor


class ImageProcessingApp:
    """Ứng dụng xử lý ảnh nâng cao với giao diện Tkinter"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Ứng Dụng Xử Lý Ảnh Nâng Cao - Bài 1-12 (Enhanced Edition)")
        self.root.geometry("1600x900")
        self.root.state('zoomed')  # Maximize window
        
        # Biến lưu trữ
        self.original_image = None
        self.processed_image = None
        self.current_image_path = None
        
        # History for undo/redo
        self.history = deque(maxlen=10)
        self.history_position = -1
        
        # Processing parameters
        self.auto_preview = tk.BooleanVar(value=True)
        self.show_histogram_panel = tk.BooleanVar(value=True)
        self.zoom_level = 1.0
        
        # Tạo giao diện
        self.create_widgets()
        self.create_menu_bar()
        
    def create_menu_bar(self):
        """Tạo menu bar"""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Tải ảnh...", command=self.load_image, accelerator="Ctrl+O")
        file_menu.add_command(label="Lưu ảnh...", command=self.save_image, accelerator="Ctrl+S")
        file_menu.add_command(label="Lưu ảnh As...", command=self.save_image_as)
        file_menu.add_separator()
        file_menu.add_command(label="Thoát", command=self.root.quit)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.undo, accelerator="Ctrl+Z")
        edit_menu.add_command(label="Redo", command=self.redo, accelerator="Ctrl+Y")
        edit_menu.add_separator()
        edit_menu.add_command(label="Reset", command=self.reset_image, accelerator="Ctrl+R")
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_checkbutton(label="Auto Preview", variable=self.auto_preview)
        view_menu.add_checkbutton(label="Show Histogram", variable=self.show_histogram_panel, command=self.toggle_histogram_panel)
        view_menu.add_separator()
        view_menu.add_command(label="Zoom In", command=self.zoom_in, accelerator="+")
        view_menu.add_command(label="Zoom Out", command=self.zoom_out, accelerator="-")
        view_menu.add_command(label="Zoom Reset", command=self.zoom_reset, accelerator="0")
        
        # Processing menu
        process_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Processing", menu=process_menu)
        process_menu.add_command(label="Batch Process...", command=self.batch_process)
        process_menu.add_command(label="Compare Images...", command=self.compare_images)
        
        # Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Hướng dẫn sử dụng", command=self.show_help)
        help_menu.add_command(label="About", command=self.show_about)
        
        # Keyboard bindings
        self.root.bind('<Control-o>', lambda e: self.load_image())
        self.root.bind('<Control-s>', lambda e: self.save_image())
        self.root.bind('<Control-z>', lambda e: self.undo())
        self.root.bind('<Control-y>', lambda e: self.redo())
        self.root.bind('<Control-r>', lambda e: self.reset_image())
        self.root.bind('<plus>', lambda e: self.zoom_in())
        self.root.bind('<minus>', lambda e: self.zoom_out())
        self.root.bind('<Key-0>', lambda e: self.zoom_reset())
        
    def create_widgets(self):
        """Tạo các widget cho giao diện với tabbed interface"""
        
        # Main container with PanedWindow for resizable panels
        main_paned = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Left panel - Controls (with tabs)
        left_panel = ttk.Frame(main_paned)
        main_paned.add(left_panel, weight=1)
        
        # Right panel - Display and analysis
        right_panel = ttk.Frame(main_paned)
        main_paned.add(right_panel, weight=4)
        
        # === LEFT PANEL with Notebook (Tabs) ===
        
        # File operations at top
        file_frame = ttk.LabelFrame(left_panel, text="File Operations", padding=10)
        file_frame.pack(fill=tk.X, pady=(0, 5))
        
        btn_frame1 = ttk.Frame(file_frame)
        btn_frame1.pack(fill=tk.X)
        ttk.Button(btn_frame1, text="📁 Tải ảnh", command=self.load_image).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)
        ttk.Button(btn_frame1, text="💾 Lưu ảnh", command=self.save_image).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)
        
        btn_frame2 = ttk.Frame(file_frame)
        btn_frame2.pack(fill=tk.X, pady=(5, 0))
        ttk.Button(btn_frame2, text="↶ Undo", command=self.undo).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)
        ttk.Button(btn_frame2, text="↷ Redo", command=self.redo).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)
        ttk.Button(btn_frame2, text="🔄 Reset", command=self.reset_image).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=2)
        
        # Notebook for categorized functions
        notebook = ttk.Notebook(left_panel)
        notebook.pack(fill=tk.BOTH, expand=True, pady=(5, 0))
        
        # Tab 1: Basic Operations
        tab_basic = ttk.Frame(notebook)
        notebook.add(tab_basic, text="📋 Cơ bản")
        self.create_basic_tab(tab_basic)
        
        # Tab 2: Histogram Operations
        tab_histogram = ttk.Frame(notebook)
        notebook.add(tab_histogram, text="📊 Histogram")
        self.create_histogram_tab(tab_histogram)
        
        # Tab 3: Filters
        tab_filters = ttk.Frame(notebook)
        notebook.add(tab_filters, text="🔍 Lọc nhiễu")
        self.create_filters_tab(tab_filters)
        
        # Tab 4: Edge Detection
        tab_edges = ttk.Frame(notebook)
        notebook.add(tab_edges, text="🔲 Tách biên")
        self.create_edges_tab(tab_edges)
        
        # Tab 5: Fourier
        tab_fourier = ttk.Frame(notebook)
        notebook.add(tab_fourier, text="🌊 Fourier")
        self.create_fourier_tab(tab_fourier)
        
        # Tab 6: Presets & Advanced
        tab_advanced = ttk.Frame(notebook)
        notebook.add(tab_advanced, text="⚡ Nâng cao")
        self.create_advanced_tab(tab_advanced)
        
        # === RIGHT PANEL ===
        
        # Top toolbar
        toolbar = ttk.Frame(right_panel)
        toolbar.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(toolbar, text="Zoom:").pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(toolbar, text="+", width=3, command=self.zoom_in).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="-", width=3, command=self.zoom_out).pack(side=tk.LEFT, padx=2)
        ttk.Button(toolbar, text="100%", width=5, command=self.zoom_reset).pack(side=tk.LEFT, padx=2)
        
        ttk.Separator(toolbar, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        ttk.Checkbutton(toolbar, text="Auto Preview", variable=self.auto_preview).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(toolbar, text="Show Histogram", variable=self.show_histogram_panel, 
                       command=self.toggle_histogram_panel).pack(side=tk.LEFT, padx=5)
        
        # PanedWindow for image display and histogram
        display_paned = ttk.PanedWindow(right_panel, orient=tk.VERTICAL)
        display_paned.pack(fill=tk.BOTH, expand=True)
        
        # Image display frame
        display_frame = ttk.LabelFrame(display_paned, text="Hiển thị ảnh", padding=5)
        display_paned.add(display_frame, weight=3)
        
        # Create two columns for original and processed with better layout
        display_frame.grid_columnconfigure(0, weight=1)
        display_frame.grid_columnconfigure(1, weight=1)
        display_frame.grid_rowconfigure(1, weight=1)
        
        # Headers
        header_frame = ttk.Frame(display_frame)
        header_frame.grid(row=0, column=0, columnspan=2, sticky='ew', pady=(0, 5))
        
        ttk.Label(header_frame, text="Ảnh gốc", font=('Arial', 10, 'bold')).pack(side=tk.LEFT, expand=True)
        ttk.Label(header_frame, text="Ảnh xử lý", font=('Arial', 10, 'bold')).pack(side=tk.RIGHT, expand=True)
        
        # Image canvases with scrollbars
        left_frame = ttk.Frame(display_frame)
        left_frame.grid(row=1, column=0, sticky='nsew', padx=(0, 2))
        
        self.original_canvas = tk.Canvas(left_frame, bg="#2b2b2b", highlightthickness=1)
        self.original_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        right_frame = ttk.Frame(display_frame)
        right_frame.grid(row=1, column=1, sticky='nsew', padx=(2, 0))
        
        self.processed_canvas = tk.Canvas(right_frame, bg="#2b2b2b", highlightthickness=1)
        self.processed_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Histogram panel (collapsible)
        self.histogram_frame = ttk.LabelFrame(display_paned, text="Histogram Analysis", padding=5)
        display_paned.add(self.histogram_frame, weight=1)
        
        # Create matplotlib figure for histogram
        self.hist_figure = Figure(figsize=(12, 2), dpi=100)
        self.hist_canvas = FigureCanvasTkAgg(self.hist_figure, master=self.histogram_frame)
        self.hist_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Info frame
        info_frame = ttk.LabelFrame(right_panel, text="Thông tin xử lý", padding=5)
        info_frame.pack(fill=tk.X, pady=(5, 0))
        
        # Add scrollbar to info text
        info_scroll_frame = ttk.Frame(info_frame)
        info_scroll_frame.pack(fill=tk.BOTH, expand=True)
        
        self.info_text = tk.Text(info_scroll_frame, height=4, wrap=tk.WORD, font=('Consolas', 9))
        info_scrollbar = ttk.Scrollbar(info_scroll_frame, command=self.info_text.yview)
        self.info_text.config(yscrollcommand=info_scrollbar.set)
        
        self.info_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        info_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
    def create_basic_tab(self, parent):
        """Create basic operations tab"""
        # Add scrollbar
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bài 1-3: Chức năng cơ bản
        basic_frame = ttk.LabelFrame(scrollable_frame, text="Bài 1-3: Chuyển đổi cơ bản", padding=10)
        basic_frame.pack(fill=tk.X, pady=5, padx=5)
        
        ttk.Button(basic_frame, text="⚫ Ảnh xám", command=self.apply_grayscale).pack(fill=tk.X, pady=2)
        ttk.Button(basic_frame, text="◐ Phân ngưỡng", command=self.apply_threshold).pack(fill=tk.X, pady=2)
        
        # Threshold slider with label
        thresh_frame = ttk.Frame(basic_frame)
        thresh_frame.pack(fill=tk.X, pady=5)
        self.threshold_var = tk.IntVar(value=127)
        self.threshold_label = ttk.Label(thresh_frame, text="Ngưỡng: 127")
        self.threshold_label.pack()
        scale = ttk.Scale(thresh_frame, from_=0, to=255, variable=self.threshold_var, orient=tk.HORIZONTAL,
                         command=self.update_threshold_label)
        scale.pack(fill=tk.X)
        
        ttk.Button(basic_frame, text="🎨 Tách kênh màu", command=self.split_channels).pack(fill=tk.X, pady=2)
        
        # Quick presets
        preset_frame = ttk.LabelFrame(scrollable_frame, text="Preset nhanh", padding=10)
        preset_frame.pack(fill=tk.X, pady=5, padx=5)
        
        ttk.Button(preset_frame, text="📸 Black & White (High Contrast)", 
                  command=lambda: self.apply_preset('bw_high')).pack(fill=tk.X, pady=2)
        ttk.Button(preset_frame, text="🌅 Enhance Brightness", 
                  command=lambda: self.apply_preset('enhance_bright')).pack(fill=tk.X, pady=2)
        ttk.Button(preset_frame, text="🔍 Edge Detection (Sobel)", 
                  command=lambda: self.apply_preset('edges')).pack(fill=tk.X, pady=2)
        
    def create_histogram_tab(self, parent):
        """Create histogram operations tab"""
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        histogram_frame = ttk.LabelFrame(scrollable_frame, text="Bài 4-6: Histogram Operations", padding=10)
        histogram_frame.pack(fill=tk.X, pady=5, padx=5)
        
        ttk.Button(histogram_frame, text="📈 Kéo giãn tương phản", command=self.apply_contrast_stretch).pack(fill=tk.X, pady=2)
        ttk.Button(histogram_frame, text="⚖️ Cân bằng Histogram", command=self.apply_histogram_eq).pack(fill=tk.X, pady=2)
        ttk.Button(histogram_frame, text="🔄 Khớp Histogram", command=self.apply_histogram_match).pack(fill=tk.X, pady=2)
        ttk.Button(histogram_frame, text="🔆 CLAHE", command=self.apply_clahe).pack(fill=tk.X, pady=2)
        ttk.Button(histogram_frame, text="📊 Hiển thị Histogram", command=self.show_histogram).pack(fill=tk.X, pady=2)
        
    def create_filters_tab(self, parent):
        """Create filters tab"""
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        filter_frame = ttk.LabelFrame(scrollable_frame, text="Bài 7: Lọc nhiễu", padding=10)
        filter_frame.pack(fill=tk.X, pady=5, padx=5)
        
        ttk.Label(filter_frame, text="Lọc trung bình (Average):").pack(fill=tk.X, pady=(0, 2))
        ttk.Button(filter_frame, text="🔲 3x3", command=lambda: self.apply_average_filter(3)).pack(fill=tk.X, pady=2)
        ttk.Button(filter_frame, text="🔳 5x5", command=lambda: self.apply_average_filter(5)).pack(fill=tk.X, pady=2)
        
        ttk.Separator(filter_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        ttk.Label(filter_frame, text="Lọc trung vị (Median):").pack(fill=tk.X, pady=(0, 2))
        ttk.Button(filter_frame, text="🔲 3x3", command=lambda: self.apply_median_filter(3)).pack(fill=tk.X, pady=2)
        ttk.Button(filter_frame, text="🔳 5x5", command=lambda: self.apply_median_filter(5)).pack(fill=tk.X, pady=2)
        
    def create_edges_tab(self, parent):
        """Create edge detection tab"""
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        edge1_frame = ttk.LabelFrame(scrollable_frame, text="Bài 8: Tách biên bậc 1", padding=10)
        edge1_frame.pack(fill=tk.X, pady=5, padx=5)
        
        ttk.Button(edge1_frame, text="⬆️ Sobel", command=self.apply_sobel).pack(fill=tk.X, pady=2)
        ttk.Button(edge1_frame, text="⬇️ Prewitt", command=self.apply_prewitt).pack(fill=tk.X, pady=2)
        ttk.Button(edge1_frame, text="↗️ Roberts", command=self.apply_roberts).pack(fill=tk.X, pady=2)
        ttk.Button(edge1_frame, text="🧭 Kirsch", command=self.apply_kirsch).pack(fill=tk.X, pady=2)
        
        edge2_frame = ttk.LabelFrame(scrollable_frame, text="Bài 9: Tách biên bậc 2", padding=10)
        edge2_frame.pack(fill=tk.X, pady=5, padx=5)
        
        ttk.Button(edge2_frame, text="🔷 Laplacian", command=self.apply_laplacian).pack(fill=tk.X, pady=2)
        ttk.Button(edge2_frame, text="🎯 LoG", command=self.apply_log).pack(fill=tk.X, pady=2)
        ttk.Button(edge2_frame, text="✨ Làm nét", command=self.apply_sharpen).pack(fill=tk.X, pady=2)
        
    def create_fourier_tab(self, parent):
        """Create Fourier operations tab"""
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        fourier_frame = ttk.LabelFrame(scrollable_frame, text="Bài 10-12: Fourier Transform", padding=10)
        fourier_frame.pack(fill=tk.X, pady=5, padx=5)
        
        ttk.Button(fourier_frame, text="🌊 FFT Spectrum", command=self.show_fft).pack(fill=tk.X, pady=2)
        
        ttk.Separator(fourier_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        # Cutoff slider
        self.cutoff_var = tk.IntVar(value=30)
        self.cutoff_label = ttk.Label(fourier_frame, text="Cutoff Frequency: 30")
        self.cutoff_label.pack(fill=tk.X)
        scale = ttk.Scale(fourier_frame, from_=10, to=100, variable=self.cutoff_var, orient=tk.HORIZONTAL,
                         command=self.update_cutoff_label)
        scale.pack(fill=tk.X, pady=(0, 10))
        
        ttk.Label(fourier_frame, text="Low-pass Filters:").pack(fill=tk.X, pady=(0, 2))
        ttk.Button(fourier_frame, text="⬇️ Ideal Low-pass", command=self.apply_ideal_lowpass).pack(fill=tk.X, pady=2)
        ttk.Button(fourier_frame, text="🔽 Gaussian Low-pass", command=self.apply_gaussian_lowpass).pack(fill=tk.X, pady=2)
        
        ttk.Separator(fourier_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=10)
        
        ttk.Label(fourier_frame, text="High-pass Filters:").pack(fill=tk.X, pady=(0, 2))
        ttk.Button(fourier_frame, text="⬆️ Ideal High-pass", command=self.apply_ideal_highpass).pack(fill=tk.X, pady=2)
        ttk.Button(fourier_frame, text="🔼 Butterworth High-pass", command=self.apply_butterworth_highpass).pack(fill=tk.X, pady=2)
        
    def create_advanced_tab(self, parent):
        """Create advanced operations tab"""
        canvas = tk.Canvas(parent)
        scrollbar = ttk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        pipeline_frame = ttk.LabelFrame(scrollable_frame, text="Pipeline Operations", padding=10)
        pipeline_frame.pack(fill=tk.X, pady=5, padx=5)
        
        ttk.Button(pipeline_frame, text="🔗 Noise Reduction Pipeline", 
                  command=lambda: self.apply_pipeline('denoise')).pack(fill=tk.X, pady=2)
        ttk.Button(pipeline_frame, text="🔗 Edge Enhancement Pipeline", 
                  command=lambda: self.apply_pipeline('edge_enhance')).pack(fill=tk.X, pady=2)
        ttk.Button(pipeline_frame, text="🔗 Contrast Enhancement Pipeline", 
                  command=lambda: self.apply_pipeline('contrast_enhance')).pack(fill=tk.X, pady=2)
        
        batch_frame = ttk.LabelFrame(scrollable_frame, text="Batch Operations", padding=10)
        batch_frame.pack(fill=tk.X, pady=5, padx=5)
        
        ttk.Button(batch_frame, text="📁 Batch Process Folder...", 
                  command=self.batch_process).pack(fill=tk.X, pady=2)
        ttk.Button(batch_frame, text="🔍 Compare 2 Images...", 
                  command=self.compare_images).pack(fill=tk.X, pady=2)
        
        export_frame = ttk.LabelFrame(scrollable_frame, text="Export Options", padding=10)
        export_frame.pack(fill=tk.X, pady=5, padx=5)
        
        ttk.Button(export_frame, text="💾 Export with Metadata", 
                  command=self.export_with_metadata).pack(fill=tk.X, pady=2)
        ttk.Button(export_frame, text="📊 Export Processing Report", 
                  command=self.export_report).pack(fill=tk.X, pady=2)
        
    def update_threshold_label(self, value):
        """Update threshold label"""
        val = int(float(value))
        self.threshold_label.config(text=f"Ngưỡng: {val}")
        if self.auto_preview.get() and self.original_image is not None:
            self.apply_threshold()
            
    def update_cutoff_label(self, value):
        """Update cutoff label"""
        val = int(float(value))
        self.cutoff_label.config(text=f"Cutoff Frequency: {val}")
        
    def load_image(self):
        """Tải ảnh từ file với histogram update"""
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
            self.history.clear()
            self.history_position = -1
            self.zoom_level = 1.0
            
            self.display_images()
            self.update_histogram()
            self.update_info(f"Đã tải: {os.path.basename(file_path)}\nKích thước: {self.original_image.shape}\nKênh: {self.original_image.shape[2] if len(self.original_image.shape) > 2 else 1}")
    
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
            
    def save_image_as(self):
        """Lưu ảnh với nhiều tùy chọn"""
        self.save_image()
    
    def reset_image(self):
        """Reset về ảnh gốc"""
        if self.original_image is not None:
            self.processed_image = None
            self.history.clear()
            self.history_position = -1
            self.display_images()
            self.update_histogram()
            self.update_info("Đã reset về ảnh gốc")
    
    def display_images(self):
        """Hiển thị ảnh gốc và ảnh xử lý với zoom support"""
        if self.original_image is not None:
            # Display original
            img_rgb = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(img_rgb)
            
            # Apply zoom
            new_size = (int(img_pil.width * self.zoom_level), int(img_pil.height * self.zoom_level))
            if new_size[0] > 0 and new_size[1] > 0:
                img_pil = img_pil.resize(new_size, Image.LANCZOS)
            
            img_pil.thumbnail((600, 600))
            img_tk = ImageTk.PhotoImage(img_pil)
            
            # Update canvas
            self.original_canvas.delete("all")
            self.original_canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
            self.original_canvas.image = img_tk
        
        if self.processed_image is not None:
            # Display processed
            if len(self.processed_image.shape) == 2:
                img_pil = Image.fromarray(self.processed_image)
            else:
                img_rgb = cv2.cvtColor(self.processed_image, cv2.COLOR_BGR2RGB)
                img_pil = Image.fromarray(img_rgb)
            
            # Apply zoom
            new_size = (int(img_pil.width * self.zoom_level), int(img_pil.height * self.zoom_level))
            if new_size[0] > 0 and new_size[1] > 0:
                img_pil = img_pil.resize(new_size, Image.LANCZOS)
            
            img_pil.thumbnail((600, 600))
            img_tk = ImageTk.PhotoImage(img_pil)
            
            # Update canvas
            self.processed_canvas.delete("all")
            self.processed_canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
            self.processed_canvas.image = img_tk
    
    def update_histogram(self):
        """Update histogram display"""
        if not self.show_histogram_panel.get():
            return
            
        self.hist_figure.clear()
        
        if self.original_image is None:
            return
            
        # Create subplots for original and processed
        if self.processed_image is not None:
            ax1 = self.hist_figure.add_subplot(121)
            ax2 = self.hist_figure.add_subplot(122)
            
            # Original histogram
            hist_orig = ImageProcessor.get_histogram(self.original_image)
            ax1.plot(hist_orig, color='blue', linewidth=0.5)
            ax1.set_title('Original Image Histogram')
            ax1.set_xlabel('Pixel Value')
            ax1.set_ylabel('Frequency')
            ax1.grid(True, alpha=0.3)
            
            # Processed histogram
            hist_proc = ImageProcessor.get_histogram(self.processed_image)
            ax2.plot(hist_proc, color='red', linewidth=0.5)
            ax2.set_title('Processed Image Histogram')
            ax2.set_xlabel('Pixel Value')
            ax2.set_ylabel('Frequency')
            ax2.grid(True, alpha=0.3)
        else:
            ax = self.hist_figure.add_subplot(111)
            hist = ImageProcessor.get_histogram(self.original_image)
            ax.plot(hist, color='blue', linewidth=0.5)
            ax.set_title('Image Histogram')
            ax.set_xlabel('Pixel Value')
            ax.set_ylabel('Frequency')
            ax.grid(True, alpha=0.3)
        
        self.hist_figure.tight_layout()
        self.hist_canvas.draw()
    
    def toggle_histogram_panel(self):
        """Toggle histogram panel visibility"""
        if self.show_histogram_panel.get():
            self.update_histogram()
        
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
    
    def add_to_history(self, image):
        """Add image to history for undo/redo"""
        # Remove future history if we're not at the end
        while len(self.history) > self.history_position + 1:
            self.history.pop()
        
        self.history.append(image.copy() if image is not None else None)
        self.history_position = len(self.history) - 1
    
    def undo(self):
        """Undo last operation"""
        if self.history_position > 0:
            self.history_position -= 1
            self.processed_image = self.history[self.history_position].copy() if self.history[self.history_position] is not None else None
            self.display_images()
            self.update_histogram()
            self.update_info(f"Undo - History position: {self.history_position + 1}/{len(self.history)}")
        else:
            messagebox.showinfo("Undo", "Không có thao tác để undo!")
    
    def redo(self):
        """Redo last undone operation"""
        if self.history_position < len(self.history) - 1:
            self.history_position += 1
            self.processed_image = self.history[self.history_position].copy() if self.history[self.history_position] is not None else None
            self.display_images()
            self.update_histogram()
            self.update_info(f"Redo - History position: {self.history_position + 1}/{len(self.history)}")
        else:
            messagebox.showinfo("Redo", "Không có thao tác để redo!")
    
    def zoom_in(self):
        """Zoom in"""
        self.zoom_level = min(self.zoom_level * 1.2, 5.0)
        self.display_images()
        self.update_info(f"Zoom: {int(self.zoom_level * 100)}%")
    
    def zoom_out(self):
        """Zoom out"""
        self.zoom_level = max(self.zoom_level / 1.2, 0.1)
        self.display_images()
        self.update_info(f"Zoom: {int(self.zoom_level * 100)}%")
    
    def zoom_reset(self):
        """Reset zoom to 100%"""
        self.zoom_level = 1.0
        self.display_images()
        self.update_info("Zoom: 100%")
    
    # === PRESET OPERATIONS ===
    
    def apply_preset(self, preset_name):
        """Apply preset operations"""
        if not self.check_image_loaded():
            return
            
        if preset_name == 'bw_high':
            # Black & White High Contrast
            self.processed_image = ImageProcessor.to_grayscale(self.original_image)
            self.processed_image = ImageProcessor.histogram_equalization(self.processed_image)
            self.update_info("Preset: Black & White (High Contrast)\nÁp dụng: Grayscale + Histogram Equalization")
        elif preset_name == 'enhance_bright':
            # Enhance Brightness
            self.processed_image = ImageProcessor.clahe(self.original_image)
            self.update_info("Preset: Enhance Brightness\nÁp dụng: CLAHE")
        elif preset_name == 'edges':
            # Edge Detection
            self.processed_image = ImageProcessor.sobel_edge(self.original_image)
            self.update_info("Preset: Edge Detection\nÁp dụng: Sobel")
        
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
    
    def apply_pipeline(self, pipeline_name):
        """Apply processing pipeline"""
        if not self.check_image_loaded():
            return
            
        if pipeline_name == 'denoise':
            # Denoise pipeline: Median Filter -> Gaussian Lowpass
            temp = ImageProcessor.median_filter(self.original_image, 5)
            self.processed_image = ImageProcessor.gaussian_lowpass_filter(temp, 30)
            self.update_info("Pipeline: Noise Reduction\nÁp dụng: Median Filter 5x5 + Gaussian Lowpass (cutoff=30)")
        elif pipeline_name == 'edge_enhance':
            # Edge enhancement: CLAHE -> Sobel -> Sharpen
            temp = ImageProcessor.clahe(self.original_image)
            temp2 = ImageProcessor.sobel_edge(temp)
            self.processed_image = ImageProcessor.sharpen(temp)
            self.update_info("Pipeline: Edge Enhancement\nÁp dụng: CLAHE + Edge Detection + Sharpen")
        elif pipeline_name == 'contrast_enhance':
            # Contrast enhancement: Contrast Stretch -> CLAHE
            temp = ImageProcessor.contrast_stretching(self.original_image)
            self.processed_image = ImageProcessor.clahe(temp)
            self.update_info("Pipeline: Contrast Enhancement\nÁp dụng: Contrast Stretching + CLAHE")
        
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
    
    # === NEW ADVANCED FEATURES ===
    
    def batch_process(self):
        """Batch process multiple images"""
        messagebox.showinfo("Batch Processing", "Chức năng xử lý hàng loạt sẽ được thêm vào phiên bản sau.\n\nHiện tại, bạn có thể xử lý từng ảnh một.")
    
    def compare_images(self):
        """Compare two images side by side"""
        messagebox.showinfo("Compare Images", "Chức năng so sánh ảnh sẽ được thêm vào phiên bản sau.\n\nHiện tại, sử dụng chức năng Reset để xem ảnh gốc.")
    
    def export_with_metadata(self):
        """Export image with processing metadata"""
        if self.processed_image is None:
            messagebox.showwarning("Cảnh báo", "Chưa có ảnh xử lý để export!")
            return
        messagebox.showinfo("Export", "Chức năng export với metadata sẽ được thêm vào phiên bản sau.\n\nHiện tại, sử dụng Save để lưu ảnh.")
    
    def export_report(self):
        """Export processing report"""
        messagebox.showinfo("Export Report", "Chức năng export report sẽ được thêm vào phiên bản sau.")
    
    def show_help(self):
        """Show help dialog"""
        help_text = """
        HƯỚNG DẪN SỬ DỤNG ỨNG DỤNG XỬ LÝ ẢNH NÂNG CAO
        
        1. TẢI ẢNH: File -> Tải ảnh (hoặc Ctrl+O)
        
        2. XỬ LÝ ẢNH:  
           - Chọn tab chức năng bên trái
           - Click vào nút xử lý mong muốn
           - Kết quả hiển thị bên phải
        
        3. UNDO/REDO:
           - Edit -> Undo (Ctrl+Z) để hoàn tác
           - Edit -> Redo (Ctrl+Y) để làm lại
        
        4. ZOOM:
           - Nút + / - hoặc phím tắt
           - View -> Zoom In/Out/Reset
        
        5. HISTOGRAM:
           - Tự động hiển thị dưới ảnh
           - Tắt/bật: View -> Show Histogram
        
        6. PRESET & PIPELINE:
           - Tab "Nâng cao" có các preset nhanh
           - Pipeline kết hợp nhiều xử lý
        
        7. LƯU ẢNH: File -> Lưu ảnh (Ctrl+S)
        """
        messagebox.showinfo("Hướng dẫn sử dụng", help_text)
    
    def show_about(self):
        """Show about dialog"""
        about_text = """
        ỨNG DỤNG XỬ LÝ ẢNH NÂNG CAO
        Version 2.0 - Enhanced Edition
        
        Đồ án môn: Xử lý ảnh
        Bài 1-12: Tích hợp đầy đủ
        
        Tính năng:
        - 22+ chức năng xử lý ảnh
        - Giao diện tabbed hiện đại
        - Undo/Redo history
        - Real-time histogram
        - Zoom & Pan
        - Preset & Pipeline
        - Keyboard shortcuts
        
        Công nghệ:
        - Python 3.8+
        - OpenCV 4.8+
        - Tkinter GUI
        - Matplotlib
        - NumPy & Pillow
        
        © 2024-2025 - All rights reserved
        """
        messagebox.showinfo("About", about_text)
    
    # === PROCESSING FUNCTIONS (với history support) ===
    
    def apply_grayscale(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.to_grayscale(self.original_image)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info("Đã chuyển sang ảnh xám\nCông thức: L = 0.299*R + 0.587*G + 0.114*B")
    
    def apply_threshold(self):
        if not self.check_image_loaded():
            return
        threshold = self.threshold_var.get()
        self.processed_image = ImageProcessor.binary_threshold(self.original_image, threshold)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
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
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info("Kéo giãn tương phản\nMở rộng dải giá trị pixel về [0, 255]")
    
    def apply_histogram_eq(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.histogram_equalization(self.original_image)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info("Cân bằng Histogram\nPhân bố lại độ sáng để tăng độ tương phản")
    
    def apply_histogram_match(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.histogram_matching(self.original_image)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info("Khớp Histogram\nBiến đổi theo phân bố Gaussian")
    
    def apply_clahe(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.clahe(self.original_image)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
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
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info(f"Lọc trung bình {kernel_size}x{kernel_size}\nLàm mờ để giảm nhiễu")
    
    def apply_median_filter(self, kernel_size):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.median_filter(self.original_image, kernel_size)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info(f"Lọc trung vị {kernel_size}x{kernel_size}\nHiệu quả với nhiễu muối tiêu")
    
    def apply_sobel(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.sobel_edge(self.original_image)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info("Sobel Edge Detection\nĐạo hàm bậc 1")
    
    def apply_prewitt(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.prewitt_edge(self.original_image)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info("Prewitt Edge Detection\nĐạo hàm bậc 1")
    
    def apply_roberts(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.roberts_edge(self.original_image)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info("Roberts Edge Detection\nĐạo hàm bậc 1")
    
    def apply_kirsch(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.kirsch_edge(self.original_image)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info("Kirsch Edge Detection\nĐạo hàm bậc 1 - 8 hướng")
    
    def apply_laplacian(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.laplacian_edge(self.original_image)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info("Laplacian Edge Detection\nĐạo hàm bậc 2")
    
    def apply_log(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.laplacian_of_gaussian(self.original_image)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info("Laplacian of Gaussian (LoG)\nLàm mịn trước khi tách biên")
    
    def apply_sharpen(self):
        if not self.check_image_loaded():
            return
        self.processed_image = ImageProcessor.sharpen(self.original_image)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info("Image Sharpening\nLàm nét ảnh sử dụng Laplacian")
    
    def show_fft(self):
        if not self.check_image_loaded():
            return
        
        magnitude_spectrum, _ = ImageProcessor.fft_transform(self.original_image)
        
        # Display as processed image
        self.processed_image = magnitude_spectrum
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info("FFT Magnitude Spectrum\nPhổ biên độ trong miền tần số")
    
    def apply_ideal_lowpass(self):
        if not self.check_image_loaded():
            return
        cutoff = self.cutoff_var.get()
        self.processed_image = ImageProcessor.ideal_lowpass_filter(self.original_image, cutoff)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info(f"Ideal Low-pass Filter\nCutoff = {cutoff}\nLàm mờ bằng cách cắt tần số cao")
    
    def apply_gaussian_lowpass(self):
        if not self.check_image_loaded():
            return
        cutoff = self.cutoff_var.get()
        self.processed_image = ImageProcessor.gaussian_lowpass_filter(self.original_image, cutoff)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info(f"Gaussian Low-pass Filter\nCutoff = {cutoff}\nLàm mờ mịn, giảm ringing")
    
    def apply_ideal_highpass(self):
        if not self.check_image_loaded():
            return
        cutoff = self.cutoff_var.get()
        self.processed_image = ImageProcessor.ideal_highpass_filter(self.original_image, cutoff)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info(f"Ideal High-pass Filter\nCutoff = {cutoff}\nLàm nổi bật biên")
    
    def apply_butterworth_highpass(self):
        if not self.check_image_loaded():
            return
        cutoff = self.cutoff_var.get()
        self.processed_image = ImageProcessor.butterworth_highpass_filter(self.original_image, cutoff)
        self.add_to_history(self.processed_image)
        self.display_images()
        self.update_histogram()
        self.update_info(f"Butterworth High-pass Filter\nCutoff = {cutoff}\nTách biên mềm mại")


def main():
    """Main function"""
    root = tk.Tk()
    app = ImageProcessingApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
