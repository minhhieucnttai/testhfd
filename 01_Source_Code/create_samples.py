"""
Script để tạo ảnh mẫu cho demo
Run this script to create sample_images folder with test images
"""

import cv2
import numpy as np
import os


def create_sample_images():
    """Tạo các ảnh mẫu để demo"""
    
    # Tạo thư mục
    os.makedirs('sample_images', exist_ok=True)
    
    # 1. Ảnh gradient
    gradient = np.zeros((300, 300), dtype=np.uint8)
    for i in range(300):
        gradient[i, :] = int(i * 255 / 300)
    cv2.imwrite('sample_images/gradient.png', gradient)
    
    # 2. Ảnh checkerboard
    checkerboard = np.zeros((300, 300), dtype=np.uint8)
    square_size = 30
    for i in range(0, 300, square_size):
        for j in range(0, 300, square_size):
            if ((i // square_size) + (j // square_size)) % 2 == 0:
                checkerboard[i:i+square_size, j:j+square_size] = 255
    cv2.imwrite('sample_images/checkerboard.png', checkerboard)
    
    # 3. Ảnh với nhiễu muối tiêu
    clean = np.ones((300, 300), dtype=np.uint8) * 128
    cv2.circle(clean, (150, 150), 80, 255, -1)
    
    # Thêm nhiễu
    noisy = clean.copy()
    noise_mask = np.random.random((300, 300))
    noisy[noise_mask < 0.02] = 0  # Pepper
    noisy[noise_mask > 0.98] = 255  # Salt
    cv2.imwrite('sample_images/noisy.png', noisy)
    
    # 4. Ảnh màu đơn giản
    color_image = np.zeros((300, 300, 3), dtype=np.uint8)
    cv2.rectangle(color_image, (50, 50), (150, 150), (255, 0, 0), -1)  # Blue
    cv2.rectangle(color_image, (150, 50), (250, 150), (0, 255, 0), -1)  # Green
    cv2.rectangle(color_image, (50, 150), (150, 250), (0, 0, 255), -1)  # Red
    cv2.rectangle(color_image, (150, 150), (250, 250), (255, 255, 0), -1)  # Cyan
    cv2.imwrite('sample_images/color_blocks.png', color_image)
    
    # 5. Ảnh có độ tương phản thấp
    low_contrast = np.random.randint(100, 150, (300, 300), dtype=np.uint8)
    cv2.circle(low_contrast, (150, 150), 80, 130, -1)
    cv2.imwrite('sample_images/low_contrast.png', low_contrast)
    
    print("✓ Đã tạo xong các ảnh mẫu trong thư mục 'sample_images'")
    print("  - gradient.png")
    print("  - checkerboard.png")
    print("  - noisy.png")
    print("  - color_blocks.png")
    print("  - low_contrast.png")


if __name__ == "__main__":
    create_sample_images()
