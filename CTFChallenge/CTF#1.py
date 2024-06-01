import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

image_path = "flag1.jpg"
image = Image.open(image_path)

image = image.convert('L')
image = ImageEnhance.Contrast(image).enhance(2)
image = image.filter(ImageFilter.SHARPEN)

custom_config = r'--oem 3 --psm 6'
extracted_text = pytesseract.image_to_string(image, config=custom_config)

print("Extracted Text:")
print(extracted_text)

flag_name = "incorrect"

flag = f"ctf{{{flag_name}}}"

print("Flag:")
print(flag)
