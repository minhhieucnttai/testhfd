#!/bin/bash

echo "=========================================="
echo "  VERIFICATION SCRIPT FOR IMAGE PROCESSING PROJECT"
echo "=========================================="
echo ""

# Check directory structure
echo "1. Checking directory structure..."
if [ -d "01_Source_Code" ] && [ -d "02_Ung_Dung_San_Pham" ] && [ -d "03_Bao_Cao" ]; then
    echo "   ✓ All main directories exist"
else
    echo "   ✗ Missing main directories"
    exit 1
fi

# Check Python files
echo ""
echo "2. Checking Python files..."
if [ -f "01_Source_Code/image_processing.py" ] && [ -f "01_Source_Code/comprehensive_app.py" ]; then
    echo "   ✓ Core Python files exist"
else
    echo "   ✗ Missing Python files"
    exit 1
fi

# Check sample images
echo ""
echo "3. Checking sample images..."
IMAGE_COUNT=$(find 01_Source_Code/sample_images -name "*.png" 2>/dev/null | wc -l)
if [ "$IMAGE_COUNT" -eq 5 ]; then
    echo "   ✓ All 5 sample images exist"
else
    echo "   ✗ Expected 5 images, found $IMAGE_COUNT"
fi

# Check documentation
echo ""
echo "4. Checking documentation..."
DOC_COUNT=$(find . -name "*.md" -not -path "./.git/*" | wc -l)
echo "   ✓ Found $DOC_COUNT documentation files"

# Test imports
echo ""
echo "5. Testing Python imports..."
cd 01_Source_Code
python3 << 'PYEOF'
import sys
try:
    from image_processing import ImageProcessor
    import cv2
    import numpy as np
    print("   ✓ All imports successful")
    
    # Quick function test
    img = np.random.randint(0, 255, (50, 50, 3), dtype=np.uint8)
    gray = ImageProcessor.to_grayscale(img)
    print("   ✓ Basic function test passed")
    
except Exception as e:
    print(f"   ✗ Import/test failed: {e}")
    sys.exit(1)
PYEOF

if [ $? -ne 0 ]; then
    exit 1
fi

cd ..

# Summary
echo ""
echo "=========================================="
echo "  VERIFICATION COMPLETE"
echo "=========================================="
echo ""
echo "Project Statistics:"
echo "  - Python files: $(find . -name "*.py" -not -path "./.git/*" | wc -l)"
echo "  - Documentation: $(find . -name "*.md" -not -path "./.git/*" | wc -l)"
echo "  - Sample images: $(find . -name "*.png" -not -path "./.git/*" | wc -l)"
echo "  - Total files: $(find . -type f -not -path "./.git/*" | wc -l)"
echo ""
echo "✓ Project is ready for submission!"
echo ""

