import cv2
import numpy as np
import pytesseract
from PIL import Image

# Path of working folder on Disk
src_path = r"C:\Users\VISHAL\Desktop"

def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path, 0)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(r"C:\Users\VISHAL\Desktop" + "\removed_noise.png", img)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(r"C:\Users\VISHAL\Desktop" + "\thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(r"C:\Users\VISHAL\Desktop" + "\thres.png"))

    # Remove template file
    #os.remove(temp)

    return result

print ('--- Start recognize text from image ---')
text = get_string(open(r"C:\Users\VISHAL\Desktop\med1.jpg","r"))
print("Recognized Text", text)
print ("------ Done Recognizing -------")


