from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\programs\\tesseract\\tesseract.exe'

# Load the images using Pillow (PIL)
image_ids = sorted(os.listdir("./img"), key=lambda x: int((x.split("_")[1]).split('.')[0]))

# We will store the texts from each image in this list
extracted_texts = []

# Loop through the image IDs, open each image, and use Tesseract to extract text
for image_id in image_ids:
    image_path = "./img/"+image_id
    print(image_path)
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='eng') # lang='eng'
    extracted_texts.append(text)

# Print the extracted texts to the file
with open("extracted_texts.txt", "w", encoding='utf-8') as f:
    for text in extracted_texts:
        f.write(text)
        f.write("\n")
