import os
import xml.etree.ElementTree as ET

# Path to the directory containing XML files
xml_dir = "xml_annotations/"

# Path to the output directory for YOLO format text files
output_dir = "yolo_annotations/"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Iterate over XML files in the directory
for xml_file in os.listdir(xml_dir):
    if xml_file.endswith(".xml"):
        xml_path = os.path.join(xml_dir, xml_file)
        
        # Parse XML file
        tree = ET.parse(xml_path)
        root = tree.getroot()

        # Get image width and height
        size = root.find('size')
        width = int(size.find('width').text)
        height = int(size.find('height').text)

        # Create YOLO format text file
        txt_filename = os.path.splitext(xml_file)[0] + ".txt"
        txt_path = os.path.join(output_dir, txt_filename)
        with open(txt_path, 'w') as f:
            # Iterate over objects in the XML file
            for obj in root.iter('object'):
                cls = obj.find('name').text
                bbox = obj.find('bndbox')
                xmin = int(bbox.find('xmin').text)
                ymin = int(bbox.find('ymin').text)
                xmax = int(bbox.find('xmax').text)
                ymax = int(bbox.find('ymax').text)

                # Convert bounding box coordinates to YOLO format
                x_center = (xmin + xmax) / (2.0 * width)
                y_center = (ymin + ymax) / (2.0 * height)
                w = (xmax - xmin) / width
                h = (ymax - ymin) / height

                # Write the YOLO formatted line to the file
                f.write(f"{cls} {x_center} {y_center} {w} {h}\n")
