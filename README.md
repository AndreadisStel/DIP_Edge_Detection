# Image Edge and Circle (Hough) Detection

This project demonstrates basic edge-detection techniques and circle detection using the Hough Transform. It provides:
- Image loading and preprocessing
- Sobel edge detection
- Laplacian of Gaussian (LoG) edge detection
- Circle detection using a custom Hough Transform implementation
- Visualization of all intermediate and final results

---

## Table of Contents
- [Requirements](#requirements)
- [Usage](#usage)
- [Prosessing Pipeline](#prosessing-pipeline)
- [Output](#output)
- [Results](#results)
- [Notes](#notes)
- [License](#license)

---

## Requirements
Ensure the following Python packages are installed:
- numpy
- matplotlib
- Pillow (PIL)

Install dependencies using:
```bash
pip install numpy matplotlib pillow
```

---

## Usage
Place your input image or use the existing one in the project directory, be certain that your image name and name in demo.py match.\
Run the script:
```python
python demo.py
```

---

## Processing Pipeline
1. Preprocessing
  - The input image is converted to grayscale, cast to float, and normalized to [0, 1].

2. Edge Detection
  - Sobel: applied with a configurable threshold (default: 0.5)
  - LoG: applied using the custom LoG operator
Both results are visualized side-by-side with the original image.

3. Circle Detection (Hough Transform)
  - The grayscale image is resized to a maximum dimension of 300 px
  - Sobel edges are computed
  - The custom Hough Transform searches for circular shapes using:
    - ```R_max = 300.0```
    - ```dim = [100, 100, 50]```
    - ```V_min = 55```
Detected circles are drawn on the image and displayed.

---

## Output
The script displays:
  - Grayscale input image
  - Sobel edge map
  - LoG edge map
  - Final image with detected circles\
Image saving functionality is present but commented out. Uncomment to export results.

---

## Report
A full project report with results and analysis is available here (in Greek, but you can see different outputs for different parameters):\
[Open Project Report (PDF)](report.pdf)

---

## Notes
- This implementation assumes working custom modules for Sobel, LoG, and Hough circle detection.
- Image resizing accelerates the computation without significantly affecting detection quality.

---

## License

---
