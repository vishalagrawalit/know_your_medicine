# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
src_path = "C:\git\know_your_medicine\Image"

# load the example image and convert it to grayscale
image = cv2.imread(src_path + med2.jpg)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", gray)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
print(filename)
cv2.imwrite(src_path + filename, gray)

# show the saved gray image
#img = cv2.imread("C:/Users/VISHAL/images/" + filename)
#cv2.imshow(filename, img)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(src_path + filename))
os.remove(src_path + filename)
print(text)

# show the output images
# cv2.imshow("Image", image)
#cv2.imshow("Output", gray)
cv2.waitKey(0)
