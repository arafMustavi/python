import cv2
import numpy as np

img = cv2.imread("Resources/araf.jpg")
print(img.shape)
# Shape outputs (height, width, RGB color Channel Value)

imgResize = cv2.resize(img,(300,300))
print(imgResize.shape)

# Image Show
cv2.imshow("Original Image", img)
cv2.imshow("Resized 300x300", imgResize)

cv2.waitKey(0)
