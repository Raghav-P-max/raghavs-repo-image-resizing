import os
from PIL import Image

def image_resize(folder_input, folder_output, height, width):
    extensions = ('.jpg', '.jpeg', '.png', '.gif')

    for file in os.listdir(folder_input):
        if file.lower().endswith(extensions):
            image_path = os.path.join(folder_input, file)

            image = Image.open(image_path)

            final_image = image.resize((width, height))
            final_path = os.path.join(folder_output, file)

            final_image.save(final_path)

            print("The files that have been resized are :", file)


folder_input = r"C:\Users\ragha\OneDrive\Documents\python elevate labs tasks\images"
folder_output = r"C:\Users\ragha\OneDrive\Documents\python elevate labs tasks\resized images"
width = int(input("Enter the width you want to resize the images to: "))                     
height = int(input("Enter the height you want to resize the images to: "))

image_resize(folder_input, folder_output, height, width)
print("\n All the images have been resized and outputted above. You can check them in the respective folder!")