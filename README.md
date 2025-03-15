# ud_facebook

**Private Project - Do Not Share**

This project aims to encode a hash into the EXIF metadata of an image in a way that is resistant to Facebook's encoding processes.  Facebook often modifies or removes EXIF data, so this project focuses on robust encoding techniques.

## Methodology

1. **JPG Analysis**
   - Collect sample JPG images
   - Extract original EXIF metadata using exiftool
   - Upload images to Facebook
   - Download processed images
   - Compare pre/post upload metadata to identify changes

2. **PNG Analysis**
   - Collect sample PNG images
   - Extract original metadata (PNG uses different format than EXIF)
   - Upload images to Facebook
   - Download processed images
   - Compare pre/post upload metadata to identify changes

3. **Metadata Persistence Test**
   - Create test images (both JPG and PNG)
   - Add hash value to "Copyright" EXIF field using exiftool
   - Upload images to Facebook
   - Download processed images
   - Check if "Copyright" field remains intact
   - Record success/failure rate for each image type


## Scripts

### extract_metadata
- Bash script to process images in a directory
- Extracts metadata using exiftool
- Generates both HTML and JSON output files
- Usage: Run script and provide directory path when prompted

### compare-json.py
- Python script to compare two JSON files
- Identifies differences and similarities in metadata
- Usage: `python compare-json.py <file1.json> <file2.json>`

## Project Goals

*   Develop encoding methods that are robust against Facebook's image processing.
*   Identify which EXIF fields are most likely to survive Facebook's processing.
*   Create tools for easily encoding and decoding hashes in images.
*   Evaluate the success rate of encoding/decoding on various image types and sizes.

## Potential Challenges

*   Facebook's encoding process is private - we don't know which metadata parts are changed, destroyed, or preserved.
*   Facebook's processing may differ between app and web versions.
*   Instagram and other social media platforms may have different metadata handling than Facebook.
*   EXIF data has size limitations, restricting the size of the hash that can be encoded.
*   Image compression can corrupt the encoded data.

## Technologies Used

*   **exiftool:** For reading and writing EXIF metadata.
*   **Python:** For scripting and potentially more complex encoding/decoding logic.
*   **Bash:** For shell scripting and automation.


## Installation

1.  **Install exiftool:**  Follow the instructions for your operating system on the [exiftool website](https://exiftool.org/).  This is crucial for the project to function.  (e.g., `sudo apt-get install libimage-exiftool-perl` on Debian/Ubuntu).

## Usage

Explain the purpose of each script and any required arguments.

