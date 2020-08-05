import cv2
import numpy as np
from stackImage import stackImages

path = "Resources/shapes.png"


def getContour(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(imgContour, cnt, -1,(255, 0, 0), 3)


img = cv2.imread(path)
imgContour = img.copy()
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
imgBlank = np.zeros_like(img)

getContour(imgContour)

imgStack = stackImages(0.5, ([img, imgGrey, imgBlur],
                             [imgCanny, imgContour, imgBlank]))
cv2.imshow("Stacked", imgStack)
cv2.waitKey(0)
