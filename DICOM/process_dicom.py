# Install the pydicom library if not already installed
!pip install pydicom

# Import required libraries
import pydicom  # For reading and processing DICOM files
import matplotlib.pyplot as plt  # For visualizing images
from pathlib import Path  # For handling file paths

# Read a single DICOM file from the specified path
pydicom_file = pydicom.dcmread('/dicom_dir/ID_0015_AGE_0061_CONTRAST_1_CT.dcm')

# Display the DICOM file object to inspect its metadata
pydicom_file

# Print specific metadata fields from the DICOM file
print("pydicom_file[0x0008,0x0032]:", pydicom_file[0x0008,0x0032])  # Acquisition Time tag
print("pydicom_file.AcquisitionTime :", pydicom_file.AcquisitionTime)  # Acquisition Time attribute

# Extract the pixel data from the DICOM file and store it as a CT image
ct = pydicom_file.pixel_array

# Create a new figure for plotting
plt.figure()

# Display the CT image in grayscale
plt.imshow(ct, cmap='gray')

# Define the path to the directory containing DICOM files
path_ct = Path('/dicom_dir')

# Get a list of all files in the DICOM directory
all_files = list(path_ct.glob("*"))

# Display the list of files
all_files

# Initialize an empty list to store DICOM data
ct_data = []

# Loop through all files in the directory and read each DICOM file
for path in all_files:
    data = pydicom.dcmread(path)
    ct_data.append(data)

# Sort the DICOM data by SliceLocation to ensure correct order
ct_data_sorted = sorted(ct_data, key=lambda slice: slice.SliceLocation)

# Print the SliceLocation of the first 10 slices
for slice in ct_data_sorted[:10]:
    print(slice.SliceLocation)

# Initialize an empty list to store pixel arrays of all slices
all_slice = []

# Extract pixel arrays from sorted DICOM data
for slice in ct_data_sorted:
    all_slice.append(slice.pixel_array)

# Print the number of slices
len(all_slice)

# Create a 3x4 grid of subplots for displaying slices
fig, axis = plt.subplots(3, 4, figsize=(15, 15))

# Initialize a counter for selecting slices to display
slice_counter = 0

# Loop through the 3x4 grid and display the first 12 slices
for i in range(3):
    for j in range(4):
        axis[i][j].imshow(all_slice[slice_counter], cmap='gray')  # Display slice in grayscale
        slice_counter += 1