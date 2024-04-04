import os
import random
from shutil import copyfile

# Path to the master folder containing subfolders A, B, etc.
master_folder = "/media/gratus/HDD/TRS/paddleocr/CNN letter Dataset"
# Ratio for train/test split
train_ratio = 0.98

# Create train and test folders in the root of the project
train_root_folder = "train_data"
test_root_folder = "test_data"
os.makedirs(train_root_folder, exist_ok=True)
os.makedirs(test_root_folder, exist_ok=True)

# Function to copy images and generate label files
def copy_images_and_generate_labels(source_folder, destination_root_folder, label_file):
    with open(label_file, 'w') as f:
        for subdir in os.listdir(source_folder):
            subdir_path = os.path.join(source_folder, subdir)
            if os.path.isdir(subdir_path):
                images = [f for f in os.listdir(subdir_path) if f.endswith(".jpg") or f.endswith(".png")]
                # Create train and test folders within destination root folder
                train_folder = os.path.join(destination_root_folder, "train")
                test_folder = os.path.join(destination_root_folder, "test")
                os.makedirs(train_folder, exist_ok=True)
                os.makedirs(test_folder, exist_ok=True)
                # Calculate train and test counts
                train_count = int(len(images) * train_ratio)
                test_count = len(images) - train_count
                # Copy images to train folder and generate train label file
                for img in images[:train_count]:
                    src_path = os.path.join(subdir_path, img)
                    dest_path = os.path.join(train_folder, img)
                    copyfile(src_path, dest_path)
                    f.write(f"{dest_path}\t{subdir}\n")
                # Copy images to test folder and generate test label file
                for img in images[train_count:]:
                    src_path = os.path.join(subdir_path, img)
                    dest_path = os.path.join(test_folder, img)
                    copyfile(src_path, dest_path)
                    f.write(f"{dest_path}\t{subdir}\n")

# Call the function to copy images and generate label files for train set
copy_images_and_generate_labels(master_folder, train_root_folder, "train_labels.txt")

# Call the function to copy images and generate label files for test set
copy_images_and_generate_labels(master_folder, test_root_folder, "test_labels.txt")

print("Dataset organization completed.")
