#first step was to install the img2pdf package/library which was done through pip
import os
import img2pdf

image_dir = "/Users/dorianjackson/Library/CloudStorage/OneDrive-Personal/Career/Projects/Images to PDF/images_to_PDF/images_to_PDF"

#os.path.join
jpg_files = [os.path.join(image_dir, i) for i in os.listdir(image_dir) if i.endswith(".jpg")]

if jpg_files:  # Check if the list is not empty
    with open("ImageContainerFile.pdf", "wb") as file:  
        file.write(img2pdf.convert(jpg_files))
    print("PDF created successfully.")
else:
    print("No JPEG files found.")
