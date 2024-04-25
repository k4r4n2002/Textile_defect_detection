import os
import shutil

# Function to create a folder if it doesn't exist
def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# Source directory containing both JPEG and XML files
source_dir = "datset2/valid"

# Destination directories for JPEG and XML files
jpg_dir = "datset2/images"
xml_dir = "datset2/labels"

# Create destination folders if they don't exist
create_folder(jpg_dir)
create_folder(xml_dir)

# Iterate over files in the source directory
for file in os.listdir(source_dir):
    # Check if it's a JPEG file
    if file.endswith(".jpg"):
        shutil.move(os.path.join(source_dir, file), os.path.join(jpg_dir, file))
    # Check if it's an XML file
    elif file.endswith(".xml"):
        shutil.move(os.path.join(source_dir, file), os.path.join(xml_dir, file))
