"""
Image Processing Library
Thư viện xử lý ảnh cho đồ án Xử lý ảnh - Bài 1-12
Chứa các phương thức static để xử lý ảnh từ cơ bản đến nâng cao
"""

import cv2
import numpy as np
from typing import Tuple, Optional


class ImageProcessor:
    """Class chứa các phương thức xử lý ảnh tĩnh"""
    
    @staticmethod
    def to_grayscale(image: np.ndarray) -> np.ndarray:
        """
        Chuyển đổi ảnh màu sang ảnh xám
        Công thức: L = 0.299*R + 0.587*G + 0.114*B
        """
        if len(image.shape) == 2:
            return image
        if image.shape[2] == 4:
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    @staticmethod
    def binary_threshold(image: np.ndarray, threshold: int = 127) -> np.ndarray:
        """
        Phân ngưỡng ảnh (Binary)
        threshold: Ngưỡng phân ngưỡng (0-255)
        """
        gray = ImageProcessor.to_grayscale(image)
        _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
        return binary
    
    @staticmethod
    def split_channels(image: np.ndarray) -> dict:
        """
        Tách kênh màu
        Trả về dictionary chứa các kênh R, G, B, Alpha
        """
        if len(image.shape) == 2:
            return {
                'R': image.copy(),
                'G': image.copy(),
                'B': image.copy(),
                'Alpha': None
            }
        
        channels = {}
        if image.shape[2] == 3:
            b, g, r = cv2.split(image)
            channels['R'] = r
            channels['G'] = g
            channels['B'] = b
            channels['Alpha'] = None
        elif image.shape[2] == 4:
            b, g, r, a = cv2.split(image)
            channels['R'] = r
            channels['G'] = g
            channels['B'] = b
            channels['Alpha'] = a
        
        return channels
    
    @staticmethod
    def contrast_stretching(image: np.ndarray) -> np.ndarray:
        """
        Kéo giãn tương phản (Contrast Stretching)
        Mở rộng dải giá trị pixel về [0, 255]
        """
        gray = ImageProcessor.to_grayscale(image)
        min_val = np.min(gray)
        max_val = np.max(gray)
        
        if max_val == min_val:
            return gray
        
        stretched = ((gray - min_val) / (max_val - min_val) * 255).astype(np.uint8)
        return stretched
    
    @staticmethod
    def histogram_equalization(image: np.ndarray) -> np.ndarray:
        """
        Cân bằng biểu đồ (Histogram Equalization)
        Phân bố lại độ sáng để tăng độ tương phản
        """
        gray = ImageProcessor.to_grayscale(image)
        equalized = cv2.equalizeHist(gray)
        return equalized
    
    @staticmethod
    def histogram_matching(image: np.ndarray, reference_hist: Optional[np.ndarray] = None) -> np.ndarray:
        """
        Khớp biểu đồ (Histogram Matching)
        Biến đổi histogram của ảnh theo phân bố Gaussian
        """
        gray = ImageProcessor.to_grayscale(image)
        
        # Tạo histogram tham chiếu (Gaussian)
        if reference_hist is None:
            reference_hist = np.zeros(256)
            mu, sigma = 128, 50
            for i in range(256):
                reference_hist[i] = np.exp(-((i - mu) ** 2) / (2 * sigma ** 2))
            reference_hist = reference_hist / reference_hist.sum() * gray.size
        
        # Tính histogram tích lũy
        hist_src = cv2.calcHist([gray], [0], None, [256], [0, 256]).flatten()
        cdf_src = hist_src.cumsum()
        cdf_src = cdf_src / cdf_src[-1] * 255
        
        cdf_ref = reference_hist.cumsum()
        cdf_ref = cdf_ref / cdf_ref[-1] * 255
        
        # Ánh xạ
        lookup = np.zeros(256, dtype=np.uint8)
        for i in range(256):
            j = np.argmin(np.abs(cdf_ref - cdf_src[i]))
            lookup[i] = j
        
        matched = lookup[gray]
        return matched
    
    @staticmethod
    def clahe(image: np.ndarray, clip_limit: float = 2.0, tile_size: int = 8) -> np.ndarray:
        """
        CLAHE - Contrast Limited Adaptive Histogram Equalization
        Cân bằng histogram thích ứng cục bộ
        """
        gray = ImageProcessor.to_grayscale(image)
        clahe_obj = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(tile_size, tile_size))
        result = clahe_obj.apply(gray)
        return result
    
    @staticmethod
    def average_filter(image: np.ndarray, kernel_size: int = 3) -> np.ndarray:
        """
        Lọc trung bình (Average Filter)
        Làm mờ ảnh để giảm nhiễu
        """
        gray = ImageProcessor.to_grayscale(image)
        filtered = cv2.blur(gray, (kernel_size, kernel_size))
        return filtered
    
    @staticmethod
    def median_filter(image: np.ndarray, kernel_size: int = 3) -> np.ndarray:
        """
        Lọc trung vị (Median Filter)
        Hiệu quả với nhiễu muối tiêu (Salt & Pepper)
        """
        gray = ImageProcessor.to_grayscale(image)
        filtered = cv2.medianBlur(gray, kernel_size)
        return filtered
    
    @staticmethod
    def sobel_edge(image: np.ndarray) -> np.ndarray:
        """
        Tách biên Sobel
        Đạo hàm bậc 1 - phát hiện biên
        """
        gray = ImageProcessor.to_grayscale(image)
        
        # Sobel X và Y
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        
        # Magnitude
        magnitude = np.sqrt(sobelx**2 + sobely**2)
        magnitude = np.uint8(np.clip(magnitude, 0, 255))
        
        return magnitude
    
    @staticmethod
    def prewitt_edge(image: np.ndarray) -> np.ndarray:
        """
        Tách biên Prewitt
        Đạo hàm bậc 1 - phát hiện biên
        """
        gray = ImageProcessor.to_grayscale(image)
        
        # Prewitt kernels
        kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
        kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
        
        prewitt_x = cv2.filter2D(gray, cv2.CV_64F, kernel_x)
        prewitt_y = cv2.filter2D(gray, cv2.CV_64F, kernel_y)
        
        magnitude = np.sqrt(prewitt_x**2 + prewitt_y**2)
        magnitude = np.uint8(np.clip(magnitude, 0, 255))
        
        return magnitude
    
    @staticmethod
    def roberts_edge(image: np.ndarray) -> np.ndarray:
        """
        Tách biên Roberts
        Đạo hàm bậc 1 - phát hiện biên
        """
        gray = ImageProcessor.to_grayscale(image)
        
        # Roberts kernels
        kernel_x = np.array([[1, 0], [0, -1]])
        kernel_y = np.array([[0, 1], [-1, 0]])
        
        roberts_x = cv2.filter2D(gray, cv2.CV_64F, kernel_x)
        roberts_y = cv2.filter2D(gray, cv2.CV_64F, kernel_y)
        
        magnitude = np.sqrt(roberts_x**2 + roberts_y**2)
        magnitude = np.uint8(np.clip(magnitude, 0, 255))
        
        return magnitude
    
    @staticmethod
    def kirsch_edge(image: np.ndarray) -> np.ndarray:
        """
        Tách biên Kirsch
        Đạo hàm bậc 1 - 8 hướng
        """
        gray = ImageProcessor.to_grayscale(image)
        
        # 8 Kirsch kernels
        kernels = [
            np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]]),
            np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]]),
            np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]]),
            np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]]),
            np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]]),
            np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]]),
            np.array([[5, -3, -3], [5, 0, -3], [5, -3, -3]]),
            np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]])
        ]
        
        # Tính magnitude từ tất cả các hướng
        max_magnitude = np.zeros_like(gray, dtype=np.float64)
        for kernel in kernels:
            filtered = cv2.filter2D(gray, cv2.CV_64F, kernel)
            max_magnitude = np.maximum(max_magnitude, np.abs(filtered))
        
        result = np.uint8(np.clip(max_magnitude, 0, 255))
        return result
    
    @staticmethod
    def laplacian_edge(image: np.ndarray) -> np.ndarray:
        """
        Tách biên Laplacian
        Đạo hàm bậc 2 - phát hiện biên
        """
        gray = ImageProcessor.to_grayscale(image)
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        result = np.uint8(np.abs(laplacian))
        return result
    
    @staticmethod
    def laplacian_of_gaussian(image: np.ndarray, kernel_size: int = 5) -> np.ndarray:
        """
        LoG - Laplacian of Gaussian
        Làm mịn trước khi tách biên
        """
        gray = ImageProcessor.to_grayscale(image)
        
        # Gaussian blur trước
        blurred = cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)
        
        # Laplacian
        log = cv2.Laplacian(blurred, cv2.CV_64F)
        result = np.uint8(np.abs(log))
        
        return result
    
    @staticmethod
    def sharpen(image: np.ndarray) -> np.ndarray:
        """
        Làm nét ảnh (Image Sharpening)
        Sử dụng Laplacian
        """
        gray = ImageProcessor.to_grayscale(image)
        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        
        # Sharpened = Original - Laplacian
        sharpened = gray.astype(np.float64) - laplacian
        result = np.uint8(np.clip(sharpened, 0, 255))
        
        return result
    
    @staticmethod
    def fft_transform(image: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Biến đổi Fourier (FFT)
        Trả về: (magnitude_spectrum, fft_shift)
        """
        gray = ImageProcessor.to_grayscale(image)
        
        # FFT
        f = np.fft.fft2(gray)
        fshift = np.fft.fftshift(f)
        
        # Magnitude spectrum
        magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)
        
        # Normalize để hiển thị
        magnitude_display = np.uint8(255 * magnitude_spectrum / np.max(magnitude_spectrum))
        
        return magnitude_display, fshift
    
    @staticmethod
    def ideal_lowpass_filter(image: np.ndarray, cutoff: int = 30) -> np.ndarray:
        """
        Lọc thông thấp lý tưởng (Ideal Low-pass Filter)
        Làm mờ ảnh bằng cách cắt bỏ tần số cao
        """
        gray = ImageProcessor.to_grayscale(image)
        
        # FFT
        f = np.fft.fft2(gray)
        fshift = np.fft.fftshift(f)
        
        # Tạo mask
        rows, cols = gray.shape
        crow, ccol = rows // 2, cols // 2
        
        mask = np.zeros((rows, cols), np.uint8)
        cv2.circle(mask, (ccol, crow), cutoff, 1, -1)
        
        # Áp dụng mask
        fshift_filtered = fshift * mask
        
        # IFFT
        f_ishift = np.fft.ifftshift(fshift_filtered)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        
        result = np.uint8(np.clip(img_back, 0, 255))
        return result
    
    @staticmethod
    def gaussian_lowpass_filter(image: np.ndarray, cutoff: int = 30) -> np.ndarray:
        """
        Lọc thông thấp Gaussian (Gaussian Low-pass Filter)
        Làm mờ mịn hơn, giảm ringing
        """
        gray = ImageProcessor.to_grayscale(image)
        
        # FFT
        f = np.fft.fft2(gray)
        fshift = np.fft.fftshift(f)
        
        # Tạo Gaussian mask
        rows, cols = gray.shape
        crow, ccol = rows // 2, cols // 2
        
        x = np.arange(cols) - ccol
        y = np.arange(rows) - crow
        X, Y = np.meshgrid(x, y)
        D = np.sqrt(X**2 + Y**2)
        
        mask = np.exp(-(D**2) / (2 * (cutoff**2)))
        
        # Áp dụng mask
        fshift_filtered = fshift * mask
        
        # IFFT
        f_ishift = np.fft.ifftshift(fshift_filtered)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        
        result = np.uint8(np.clip(img_back, 0, 255))
        return result
    
    @staticmethod
    def ideal_highpass_filter(image: np.ndarray, cutoff: int = 30) -> np.ndarray:
        """
        Lọc thông cao lý tưởng (Ideal High-pass Filter)
        Làm nổi bật biên bằng cách giữ lại tần số cao
        """
        gray = ImageProcessor.to_grayscale(image)
        
        # FFT
        f = np.fft.fft2(gray)
        fshift = np.fft.fftshift(f)
        
        # Tạo mask (inverse của lowpass)
        rows, cols = gray.shape
        crow, ccol = rows // 2, cols // 2
        
        mask = np.ones((rows, cols), np.uint8)
        cv2.circle(mask, (ccol, crow), cutoff, 0, -1)
        
        # Áp dụng mask
        fshift_filtered = fshift * mask
        
        # IFFT
        f_ishift = np.fft.ifftshift(fshift_filtered)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        
        result = np.uint8(np.clip(img_back, 0, 255))
        return result
    
    @staticmethod
    def butterworth_highpass_filter(image: np.ndarray, cutoff: int = 30, order: int = 2) -> np.ndarray:
        """
        Lọc thông cao Butterworth (Butterworth High-pass Filter)
        Tách biên mềm mại hơn, kiểm soát độ dốc qua tham số bậc n
        """
        gray = ImageProcessor.to_grayscale(image)
        
        # FFT
        f = np.fft.fft2(gray)
        fshift = np.fft.fftshift(f)
        
        # Tạo Butterworth mask
        rows, cols = gray.shape
        crow, ccol = rows // 2, cols // 2
        
        x = np.arange(cols) - ccol
        y = np.arange(rows) - crow
        X, Y = np.meshgrid(x, y)
        D = np.sqrt(X**2 + Y**2)
        
        # Tránh chia cho 0
        D[D == 0] = 0.01
        
        mask = 1 / (1 + (cutoff / D) ** (2 * order))
        
        # Áp dụng mask
        fshift_filtered = fshift * mask
        
        # IFFT
        f_ishift = np.fft.ifftshift(fshift_filtered)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        
        result = np.uint8(np.clip(img_back, 0, 255))
        return result
    
    @staticmethod
    def get_histogram(image: np.ndarray) -> np.ndarray:
        """
        Tính histogram của ảnh xám
        """
        gray = ImageProcessor.to_grayscale(image)
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
        return hist.flatten()
