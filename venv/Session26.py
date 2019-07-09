import cv2
import pytesseract

image = cv2.imread("data.png", 1)
print(image) # numpy array

print("***********")

text = pytesseract.image_to_string(image)
print(text)