import cv2
import numpy as np

img = cv2.imread("Resources/araf.jpg")
kernel = np.ones((5, 5), np.uint8)

# Greyscale Image
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# openCV uses BGR Format

# Image Blur
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)
imgBlur2 = cv2.GaussianBlur(img, (13, 13), 0)
# The second parameter in GaussianBlur defines the intensity
# Must be odd number
# The higher the numbers are,the grater the blur

# Image Edge Detection
imgCanny = cv2.Canny(img, 100, 100)
imgCanny2 = cv2.Canny(img, 200, 200)
imgCanny3 = cv2.Canny(img, 150, 150)
# The Higher the canny values,the lesser the edges


imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgDilation2 = cv2.dilate(imgCanny, kernel, iterations=5)
# The Higher the iterations,the thicker the images

imgEroded = cv2.erode(img, kernel, iterations=1)
# The Higher the iterations,the thinner the images


# Showing all the images
# cv2.imshow("Grey Image" , imgGrey)
# cv2.imshow("Blur Image" , imgBlur)
# cv2.imshow("Blur2 Image" , imgBlur2)
# cv2.imshow("Canny image", imgCanny)
# cv2.imshow("Canny image2", imgCanny2)
# cv2.imshow("Canny image3", imgCanny3)
# cv2.imshow("Dilation Image", imgDilation)
# cv2.imshow("Dilation2 Image", imgDilation2)
# cv2.imshow("Eroded Image", imgEroded)


cv2.waitKey(0)
