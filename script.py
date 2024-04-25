import os
import cv2
import numpy as np
import xml.etree.ElementTree as ET

augmentation_names = ['contrast', 'sharpen', 'blur']

class SimpleAugmentation:
    def __init__(self, image, xml_path):
        self.image = image
        self.xml_path = xml_path

    def readImage(self):
        # Read original image
        self.image = cv2.imread(self.image)

    def readXML(self):
        # Read XML data
        tree = ET.parse(self.xml_path)
        self.xml_src = ET.tostring(tree.getroot()).decode("utf-8")

    def contrastImage(self):
        """
        To imporve the contrast effect of the images.
        1. Convert image to gray scale
        2. Perform Equlization Hist, to improve the contrast of the image
        """
        gray = cv2.cvtColor(self.image,cv2.COLOR_BGR2GRAY)
        self.image = cv2.equalizeHist(gray)
        
    def sharpenImage(self):
        """
        To sharpen the effects of the object in the image
        1. Define Kernel to sharpen (https://setosa.io/ev/image-kernels/)
        2. Using filter2D() for sharpening
        """
        kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
        self.image = cv2.filter2D(self.image, -1, kernel)
    
    def blurImage(self):
        """
        To remove noise from image. 
        As most of the Image data have low light intensity, Gaussain Blur is used, to remove noise without affecting
        the image
        
        kernel size = 15,15 is used as the image is large. This value can be increased or decreased based on the 
        desired output. 
        """
        self.image = cv2.GaussianBlur(self.image,(15,15),0)    

    def simpleBB(self):
        # Read image and XML
        self.readImage()
        self.readXML()

        # Perform augmentation techniques
        augmented_images = []
        

        for technique in augmentation_names:
            # Make a copy of the original image
            augmented_image = self.image.copy()

            # Apply augmentation technique
            if technique == 'contrast':
                self.contrastImage()
            elif technique == 'sharpen':
                self.sharpenImage()
            elif technique == 'blur':
                self.blurImage()

            augmented_images.append(augmented_image)

        return augmented_images
# Path to directory containing image and XML files
input_dir = "aug/"
output_dir = "augmented_data/"

# Create output directory if not exists
os.makedirs(output_dir, exist_ok=True)

# Iterate over image files in the directory
# Iterate over image files in the directory
for image_file in os.listdir(input_dir):
    if image_file.endswith(".jpg"):
        image_path = os.path.join(input_dir, image_file)
        xml_path = os.path.join(input_dir, image_file.replace(".jpg", ".xml"))

        if os.path.exists(xml_path):
            # Create SimpleAugmentation instance
            augmentation = SimpleAugmentation(image_path, xml_path)

            # Perform augmentation
            augmented_images = augmentation.simpleBB()

            # Save augmented images
            filename, ext = os.path.splitext(image_file)
            for i, image in enumerate(augmented_images):
                augmented_filename = f"aug_{filename}_{augmentation_names[i]}{ext}"
                output_image_path = os.path.join(output_dir, augmented_filename)
                cv2.imwrite(output_image_path, image)

                # Save corresponding XML
                xml_output_path = os.path.join(output_dir, f"aug_{filename}_{augmentation_names[i]}.xml")
                with open(xml_output_path, "w") as f:
                    f.write(augmentation.xml_src)