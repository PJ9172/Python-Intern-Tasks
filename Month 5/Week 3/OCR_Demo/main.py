import cv2

import easyocr

from preprocess import preprocess

reader = easyocr.Reader(['hi', 'en'])

# image = preprocess("Pancard.jpeg")

result = reader.readtext("Pancard.jpeg")

for _, text, confidence in result:
    print(text)