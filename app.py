import os
import random
from shutil import copyfile

# Path to the master folder containing subfolders A, B, etc.
master_folder = "/media/gratus/HDD/TRS/paddleocr/CNN letter Dataset"
# Ratio for train/test split
train_ratio = 0.98

# Path to the folder where train and test data will be stored
train_data_path = "/path/to/train/data"
test_data_path = "/path/to/test/data"

# Create train and test folders
train_folder = os.path.join(train_data_path, "train")
test_folder = os.path.join(test_data_path, "test")
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Function to copy images and generate label files
def copy_images_and_generate_labels(source_folder, destination_folder, label_file):
    with open(label_file, 'w') as f:
        for subdir in os.listdir(source_folder):
            subdir_path = os.path.join(source_folder, subdir)
            if os.path.isdir(subdir_path):
                images = [f for f in os.listdir(subdir_path) if f.endswith(".jpg") or f.endswith(".png")]
                for img in images:
                    src_path = os.path.join(subdir_path, img)
                    dest_path = os.path.join(destination_folder, img)
                    copyfile(src_path, dest_path)
                    f.write(f"{dest_path}\t{subdir}\n")

# Copy images to train folder and generate train label file
copy_images_and_generate_labels(master_folder, train_folder, os.path.join(train_data_path, "rec_gt_train.txt"))

# Copy images to test folder and generate test label file
copy_images_and_generate_labels(master_folder, test_folder, os.path.join(test_data_path, "rec_gt_test.txt"))

print("Dataset organization completed.")
