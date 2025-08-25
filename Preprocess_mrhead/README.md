# MR Head NIfTI Image Processing

## Overview
This project processes a NIfTI file containing MRI head data (`MRHead.nii.gz`). It loads the NIfTI file, extracts and visualizes slices in coronal, sagittal, and axial orientations, performs coordinate transformations, resamples the image to a new resolution, and applies normalization and windowing techniques. The project is implemented in Python using the `nibabel` library for NIfTI file handling, `matplotlib` for visualization, and `numpy` for numerical operations.

## Prerequisites
To run this project, you need the following dependencies:
- Python 3.x
- `nibabel` (for reading and processing NIfTI files)
- `matplotlib` (for visualizing images)
- `numpy` (for numerical operations)

You can install the required libraries using:
```bash
pip install nibabel matplotlib numpy
```

## Dataset
The project uses a single NIfTI file, `MRHead.nii.gz`, which contains MRI head data. Ensure this file is available and update the `nifti_path` variable in the script to point to its location.

## Usage
1. Clone this repository to your local machine:
   ```bash
   git clone <https://github.com/ErfanShakouri/AI_Medicine_learn.git>
   ```
2. Place the `MRHead.nii.gz` file in an accessible directory and update the `nifti_path` variable in the script (e.g., `/learning/MRHead.nii.gz`).
3. Run the Python script:
   ```bash
   python process_mrhead.py
   ```
4. The script will:
   - Load the `MRHead.nii.gz` file and print its affine matrix, shape, voxel sizes, and axis orientations.
   - Display three coronal, sagittal, and axial slices in separate 1x3 subplots.
   - Perform voxel-to-physical coordinate transformations and print the results.
   - Resample the image to a new shape (128x128x65) with 2mm isotropic voxels and PIR orientation.
   - Display a comparison of original and resampled axial slices.
   - Normalize the image data by dividing by the maximum value (3071) and display a rotated axial slice.
   - Apply windowing with two different levels ([0, 100] and [0, 300]) and display rotated axial slices.
   - Standardize the image data using z-score normalization and min-max scaling, then print statistics.

## Output
- The script prints the affine matrix, shape, voxel sizes, and axis orientations of the NIfTI file.
- It displays three sets of 1x3 subplots for coronal, sagittal, and axial slices of the original data.
- It prints physical coordinates for a given voxel and the translation component of the affine matrix.
- It prints the shape and voxel sizes of the resampled image.
- It displays a 1x2 subplot comparing original and resampled axial slices.
- It displays rotated axial slices for normalized and windowed data.
- It prints statistics (mean, max, min) for the original and standardized image data.

## Notes
- Ensure the `MRHead.nii.gz` file path is correctly specified in the script.
- The normalization value (3071) and windowing levels ([0, 100], [0, 300]) are hardcoded; adjust these as needed for your data.
- The resampling parameters (shape, voxel size, orientation) can be modified in the `nibabel.processing.conform` call.
- Adjust the `figsize` parameter in the `plt.subplots` calls to change the size of the output plots if needed.

