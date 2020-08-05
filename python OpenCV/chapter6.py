import cv2
import numpy as np
from stackImage import stackImages

img = cv2.imread("Resources/araf.jpg")

# Stacking images Horizontally and Vertically
imgHor = np.hstack((img, img))
# Places images in the manner  | XX |

imgVer = np.vstack((img, img))
# Places images in the manner  |  X  |
#                              |  X  |
print(img.shape)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgStack = stackImages(0.5, ([img, imgGray, img], [img, img, img]))
cv2.imshow("ImageStack", imgStack)

cv2.waitKey(0)

imgResized = cv2.resize(img, (int(img.shape[1] / 3), int(img.shape[0] / 3)))
imgHor = np.hstack((imgResized, imgResized))
imgVer = np.vstack((imgHor, imgHor))

# cv2.imshow("Horizontal", imgHor)
cv2.imshow("Stacked", imgVer)
cv2.waitKey(0)


# imgHor = np.hstack((img,img))
# imgVer = np.vstack((img,img))
#
# cv2.imshow("Horizontal",imgHor)
# cv2.imshow("Vertical",imgVer)
