# Added Metadata Analysis
   - Use same PNG image as previous analysis
   - Add hash value to "Copyright" field using exiftool
   - Upload modified image to Facebook via Chrome browser on desktop
   - Download processed image from Facebook
   - Compare pre/post upload metadata to check if "Copyright" field persists

---

## Methodology
1. Use @art.png as the original image
2. Add hash to "Copyright" field using exiftool
3. Extract modified metadata using exiftool
4. Upload modified @art.png to Facebook via Chrome browser on desktop
5. Download processed image as @facebook-2-hash.jpg from Facebook
6. Extract metadata from @facebook-2-hash.jpg
7. Compare pre/post upload metadata using compare-json.py
