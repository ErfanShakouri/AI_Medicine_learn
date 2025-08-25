# NIfTI Image Processing

## Overview
This project processes NIfTI files containing medical imaging data (e.g., MRI scans). It loads a NIfTI file, extracts and visualizes axial slices, applies a thresholding operation to the image data, and saves the processed data as a new NIfTI file. The project is implemented in Python using the `nibabel` library for NIfTI file handling and `matplotlib` for visualization.

## Prerequisites
To run this project, you need the following dependencies:
- Python 3.x
- `nibabel` (for reading and processing NIfTI files)
- `matplotlib` (for visualizing images)

You can install the required libraries using:
```bash
pip install nibabel matplotlib
```

## Usage
1. Clone this repository to your local machine:
   ```bash
   git clone <https://github.com/ErfanShakouri/AI_Medicine_learn.git>
   ```
2. Ensure you have a NIfTI file (e.g., `hippocampus_013.nii.gz`) available. Update the `nifti_path` variable in the script to point to your NIfTI file.
3. Run the Python script:
   ```bash
   python process_nifti.py
   ```
4. The script will:
   - Load the specified NIfTI file and print its metadata.
   - Display the `srow_x` field from the NIfTI header.
   - Extract and display the first 9 axial slices in a 3x3 grid using Matplotlib.
   - Apply a thresholding operation to the image data (values > 250 are retained, others set to 0).
   - Display the first 9 processed axial slices in a new 3x3 grid.
   - Save the processed image data as a new NIfTI file (`test.nii.gz`) in the same directory as the input file.

## Output
- The script prints the NIfTI file object and the `srow_x` header field.
- It displays the shape of the image data.
- It generates two 3x3 grids of axial slices: one for the original data and one for the processed (thresholded) data.
- A new NIfTI file (`test.nii.gz`) is created with the processed image data.

## Notes
- Ensure the input NIfTI file path is correctly specified in the script.
- The thresholding operation (`image_data > 250`) is hardcoded; modify the threshold value as needed for your data.
- Adjust the `figsize` parameter in the `plt.subplots` calls to change the size of the output plots if needed.
- The output NIfTI file is saved in the same directory as the input file. Update the output path in the script if desired.

