import os
import random
from shutil import copyfile

# Path to the master folder containing subfolders A, B, etc.
master_folder = "/media/gratus/HDD/TRS/paddleocr/CNN letter Dataset"
# Ratio for train/test split
train_ratio = 0.98

# Create train and test folders
train_folder = os.path.join(master_folder, "train")
test_folder = os.path.join(master_folder, "test")
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Iterate through each subfolder (A, B, etc.)
for subdir in os.listdir(master_folder):
    subdir_path = os.path.join(master_folder, subdir)
    if os.path.isdir(subdir_path):
        # Get list of image files in the current subfolder
        images = [f for f in os.listdir(subdir_path) if f.endswith(".jpg") or f.endswith(".png")]
        # Shuffle the images
        random.shuffle(images)
        # Calculate the number of images for training and testing based on the ratio
        train_count = int(len(images) * train_ratio)
        test_count = len(images) - train_count
        
        # Copy images to train folder
        for img in images[:train_count]:
            src_path = os.path.join(subdir_path, img)
            dest_path = os.path.join(train_folder, img)
            copyfile(src_path, dest_path)
        
        # Copy images to test folder
        for img in images[train_count:]:
            src_path = os.path.join(subdir_path, img)
            dest_path = os.path.join(test_folder, img)
            copyfile(src_path, dest_path)

# Create rec_gt_train.txt and rec_gt_test.txt files
def create_label_file(folder, label_file):
    with open(label_file, 'w') as f:
        for subdir in os.listdir(folder):
            subdir_path = os.path.join(folder, subdir)
            if os.path.isdir(subdir_path):
                for img in os.listdir(subdir_path):
                    img_path = os.path.join(subdir_path, img)
                    f.write(f"{img_path}\t{subdir}\n")

create_label_file(train_folder, os.path.join(master_folder, "rec_gt_train.txt"))
create_label_file(test_folder, os.path.join(master_folder, "rec_gt_test.txt"))

print("Dataset organization completed.")
