# Import required libraries
import nibabel as nib  # For reading and processing NIfTI files
import matplotlib.pyplot as plt  # For visualizing images

# Define the path to the input NIfTI file
nifti_path = "/Nifti/hippocampus_013.nii.gz"

# Load the NIfTI file
nifti_file = nib.load(nifti_path)
print(nifti_file)

# Access and display the 'srow_x' field from the NIfTI header
nifti_file.header["srow_x"]
nifti_file.shape

# Extract the image data as a NumPy array
image_data = nifti_file.get_fdata()

# Create a 3x3 grid of subplots for displaying slices
fig, axis = plt.subplots(3, 3, figsize=(15, 15))

# Initialize a counter for selecting slices to display
slice_counter = 0

# Loop through the 3x3 grid and display the first 9 axial slices
for i in range(3):
    for j in range(3):
        axis[i][j].imshow(image_data[:, :, slice_counter], cmap="gray")  # Display slice in grayscale
        slice_counter += 1

# Apply a threshold to the image data, setting values below 250 to 0
image_data_processed = image_data * (image_data > 250)

# Create a new 3x3 grid of subplots for displaying processed slices
fig, axis = plt.subplots(3, 3, figsize=(15, 15))

# Reset the slice counter
slice_counter = 0

# Loop through the 3x3 grid and display the first 9 processed axial slices
for i in range(3):
    for j in range(3):
        axis[i][j].imshow(image_data_processed[:, :, slice_counter], cmap="gray")  # Display processed slice in grayscale
        slice_counter += 1

# Create a new NIfTI image from the processed data, preserving the original affine transformation
processed_nifti = nib.Nifti1Image(image_data_processed, nifti_file.affine)

# Save the processed NIfTI image to a new file
nib.save(processed_nifti, "/Nifti/test.nii.gz")