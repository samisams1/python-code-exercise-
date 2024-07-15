from PIL import Image
import pytesseract

def ocr_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

print(ocr_image("image.jpg"))