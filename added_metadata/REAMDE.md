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

### actual output 

```c
this key-value 'ExifToolVersion':'12.57' is the same as 'ExifToolVersion':'12.57'
this key-value 'Directory':'./added_metadata' is the same as 'Directory':'./added_metadata'
this key-value 'FilePermissions':'-rw-r--r--' is the same as 'FilePermissions':'-rw-r--r--'
this key-value 'ImageWidth':'512' is the same as 'ImageWidth':'512'
this key-value 'ImageWidth':'512' is the same as 'ImageHeight':'512'
this key-value 'ImageHeight':'512' is the same as 'ImageWidth':'512'
this key-value 'ImageHeight':'512' is the same as 'ImageHeight':'512'
this key-value 'BitDepth':'8' is the same as 'BitsPerSample':'8'
this key-value 'Copyright':'3cb632af8f7f9e80a06b206addc8c2c6' is the same as 'CopyrightNotice':'3cb632af8f7f9e80a06b206addc8c2c6'
this key-value 'ImageSize':'512x512' is the same as 'ImageSize':'512x512'
this key-value 'Megapixels':'0.262' is the same as 'Megapixels':'0.262'
```


## Key Findings
- The hash value persisted through Facebook's processing despite key name changes
- 'Copyright' field was renamed to 'CopyrightNotice' but maintained the same hash value
`this key-value 'Copyright':'3cb632af8f7f9e80a06b206addc8c2c6' is the same as 'CopyrightNotice':'3cb632af8f7f9e80a06b206addc8c2c6'`
- Core image metadata (dimensions, size) remained unchanged
- This confirms Facebook preserves certain metadata fields while renaming them
