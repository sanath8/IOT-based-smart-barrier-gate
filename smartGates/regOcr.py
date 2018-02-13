from PIL import Image
import pytesseract

def getRegistrationNumber(imagePath):

    im = Image.open(imagePath)
    text = pytesseract.image_to_string(im, lang = 'eng')
    print(text)
    return text
