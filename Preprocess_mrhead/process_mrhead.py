# Install or upgrade the nibabel library
!pip install nibabel --upgrade

# Import required libraries
import nibabel as nib  
import nibabel.processing  # For advanced NIfTI processing (e.g., resampling)
import matplotlib.pyplot as plt  
import numpy as np  

# Load the NIfTI file containing MR head data
Head_MR = nib.load("/learning/MRHead.nii.gz")

# Extract the image data as a NumPy array
Head_MR_data = Head_MR.get_fdata()

# Get the affine transformation matrix and shape of the image data
affine = Head_MR.affine
shape = Head_MR.shape

print("affine:", affine)
print("shape:", shape)

# Print the voxel sizes (zooms) and axis orientations from the NIfTI header
print("Head_MR.header.get_zooms():", Head_MR.header.get_zooms())
print("nib.aff2axcodes(affine):", nib.aff2axcodes(affine))

# Create a 1x3 subplot to display three coronal slices
fig, axis = plt.subplots(1, 3, figsize=(13, 13))
axis[0].imshow(Head_MR_data[50, :, :], cmap="gray")  # Display coronal slice at index 50
axis[1].imshow(Head_MR_data[120, :, :], cmap="gray")  # Display coronal slice at index 120
axis[2].imshow(Head_MR_data[220, :, :], cmap="gray")  # Display coronal slice at index 220

# Create a 1x3 subplot to display three sagittal slices
fig, axis = plt.subplots(1, 3, figsize=(13, 13))
axis[0].imshow(Head_MR_data[:, 50, :], cmap="gray")  # Display sagittal slice at index 50
axis[1].imshow(Head_MR_data[:, 120, :], cmap="gray")  # Display sagittal slice at index 120
axis[2].imshow(Head_MR_data[:, 220, :], cmap="gray")  # Display sagittal slice at index 220

# Create a 1x3 subplot to display three axial slices
fig, axis = plt.subplots(1, 3, figsize=(13, 13))
axis[0].imshow(Head_MR_data[:, :, 6], cmap="gray")  # Display axial slice at index 6
axis[1].imshow(Head_MR_data[:, :, 75], cmap="gray")  # Display axial slice at index 75
axis[2].imshow(Head_MR_data[:, :, 125], cmap="gray")  # Display axial slice at index 125

# Convert voxel coordinates (0, 0, 0, 1) to physical coordinates using the affine matrix
voxel_coords = np.array((0, 0, 0, 1))
physical_coords = affine @ voxel_coords

# Print the physical coordinates and the translation component of the affine matrix
print("physical_coords:", physical_coords)
print("affine [: , 3:]:", affine[:, 3:])

# Manually compute physical coordinates for voxel (0, 0, 0) without homogeneous coordinate
voxel_coords_manual = np.array((0, 0, 0))
physical_coords_manual = affine[:3, :3] @ voxel_coords_manual
physical_coords_manual += affine[:3, 3]
physical_coords_manual

# Convert physical coordinates back to voxel coordinates using the inverse affine matrix
physical_coords = [-86.64489746, 133.92860413, 116.78569794, 1.0]
(np.linalg.inv(affine) @ physical_coords).round()

# Resample the NIfTI image to a new shape (128x128x65) with voxel size (2, 2, 2) and PIR orientation
voxel_size = (2, 2, 2)
Head_MR_resized = nibabel.processing.conform(Head_MR, (128, 128, 65), voxel_size, orientation="PIR")
Head_MR_resized_data = Head_MR_resized.get_fdata()

# Print the shape and voxel sizes of the resized image
print(Head_MR_resized.shape)
print(Head_MR_resized.header.get_zooms())

# Create a 1x2 subplot to compare original and resized axial slices
fig, axis = plt.subplots(1, 2, figsize=(13, 13))
axis[0].imshow(Head_MR_data[:, :, 10], cmap='gray')  # Display original axial slice at index 10
axis[1].imshow(Head_MR_resized_data[:, :, 10], cmap='gray')  # Display resized axial slice at index 10

# Normalize the image data by dividing by the maximum value (3071)
Head_MR_data_standard = Head_MR_data / 3071
plt.figure(figsize=(10, 10))
plt.imshow(np.rot90(Head_MR_data_standard[:, :, 20]), cmap='gray')  # Display rotated normalized axial slice

# Apply windowing to the image data with a window level of [0, 100]
Head_MR_window = np.clip(Head_MR_data, 0, 100)
plt.figure()
plt.imshow(np.rot90(Head_MR_window[:, :, 100]), cmap="bone")  # Display rotated windowed axial slice

# Apply windowing to the image data with a window level of [0, 300]
Head_MR_window = np.clip(Head_MR_data, 0, 300)
plt.figure()
plt.imshow(np.rot90(Head_MR_window[:, :, 100]), cmap="bone")  # Display rotated windowed axial slice

# Standardize the image data using z-score normalization
mean, std = np.mean(Head_MR_data), np.std(Head_MR_data)
Head_MR_data_norm = (Head_MR_data - mean) / std
Head_MR_data_standardized = (Head_MR_data_norm - np.min(Head_MR_data_norm)) / (
    np.max(Head_MR_data_norm) - np.min(Head_MR_data_norm)
)

# Print statistics for original and standardized data
np.mean(Head_MR_data), np.max(Head_MR_data), np.min(Head_MR_data)
np.mean(Head_MR_data_standardized), np.max(Head_MR_data_standardized), np.min(Head_MR_data_standardized)