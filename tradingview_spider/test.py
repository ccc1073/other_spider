from PIL import Image
import pytesseract

images = Image.open('1539259359.png')
region = (0, 320, 170, 350)
cropImg = images.crop(region)
text=pytesseract.image_to_string(cropImg,lang='chi_sim')
print(text)