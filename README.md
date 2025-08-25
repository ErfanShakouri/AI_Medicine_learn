# DICOM CT Image Processing

## Overview
This project processes DICOM files containing CT scan images. It reads DICOM files from a specified directory, extracts metadata and pixel data, sorts the slices by their `SliceLocation`, and visualizes a subset of the slices in a 3x4 grid using Matplotlib. The project is implemented in Python using the `pydicom` library.

## Prerequisites
To run this project, you need the following dependencies:
- Python 3.x
- `pydicom` (for reading and processing DICOM files)
- `matplotlib` (for visualizing images)
- `pathlib` (included in Python standard library)

You can install the required libraries using:
```bash
pip install pydicom matplotlib
```

## Directory Structure
The project assumes that the DICOM files are stored in a directory named `dicom_dir`. Place your DICOM files (e.g., `.dcm` files) in this directory before running the script.

```plaintext
project_root/
│
├── dicom_dir/
│   ├── ID_0015_AGE_0061_CONTRAST_1_CT.dcm
│   ├── (other DICOM files)
│
├── process_dicom.py
├── README.md
```

## Usage
1. Clone this repository to your local machine:
   ```bash
   git clone <https://github.com/ErfanShakouri/AI_Medicine_learn.git>
   ```
2. Place your DICOM files in the `dicom_dir` folder.
3. Run the Python script:
   ```bash
   python process_dicom.py
   ```
4. The script will:
   - Read a sample DICOM file and print specific metadata (Acquisition Time).
   - Display a single CT slice in grayscale.
   - Read all DICOM files from the `dicom_dir` directory.
   - Sort the slices by `SliceLocation`.
   - Display the first 10 slice locations.
   - Visualize the first 12 slices in a 3x4 grid.

## Output
- The script prints metadata such as the `AcquisitionTime` for a sample DICOM file.
- It displays a single CT slice using Matplotlib.
- It prints the `SliceLocation` for the first 10 sorted slices.
- It generates a 3x4 grid of the first 12 CT slices, displayed in grayscale.

## Notes
- Ensure that the DICOM files in `dicom_dir` are valid and contain the `SliceLocation` attribute for proper sorting.
- The script assumes that all files in `dicom_dir` are DICOM files. If non-DICOM files are present, you may need to filter them (e.g., by checking file extensions).
- Adjust the `figsize` parameter in the `plt.subplots` call to change the size of the output plot if needed.

