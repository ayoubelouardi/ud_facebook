# JPG Analysis
   - Collect sample JPG images
   - Extract original EXIF metadata using exiftool
   - Upload images to Facebook
   - Download processed images
   - Compare pre/post upload metadata to identify changes

---


## Methodology
1. Use @art.jpg as the original image
2. Extract original EXIF metadata using exiftool
3. Upload @art.jpg to Facebook via Chrome browser on desktop
4. Download processed image as @facebook-1.jpg from Facebook
5. Extract EXIF metadata from @facebook-1.jpg
6. Compare pre/post upload metadata using compare-json.py
