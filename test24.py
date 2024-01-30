import numpy as np
import cv2
from PIL import Image
import pytesseract

filename = 'number.png'
img = np.array(Image.open(filename))
text = pytesseract.image_to_string(img,lang='Hangul')
print(text)