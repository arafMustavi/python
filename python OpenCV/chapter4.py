# KEY TAKEAWAYS
# SHAPES AND TEXTS

import cv2
import numpy as np


def animateBlueBox():
    img = np.zeros((512, 512, 3), np.uint8)
    x1, x2 = 0, 100
    y1, y2 = 300, 400
    while True:
        img[x1:x2, y1:y2] = 0, 0, 0
        x1 += 1
        x2 += 1
        img[x1:x2, y1:y2] = 255, 0, 0
        cv2.imshow("", img)
        # cv2.waitKey(100)
        if cv2.waitKey(50) & 0xFF == ord('q'):
            break

def imageCross():
    img = np.zeros((512, 512, 3), np.uint8)
    line1 = cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 3)
    line2 = cv2.line(img, (0, img.shape[0]), (img.shape[1], 0), (0, 0, 255), 3)
    cv2.imshow("The Line Demo", line1)
    cv2.imshow("The Line Demo", line2)
    cv2.waitKey(0)


# Animate_BlueBox_Down()

# imgPlainZeros = np.zeros((512, 512))
# imgPlainOnes = np.ones((512, 512))
# 0 produces Black but 1 produces White
# REMEMBER : 1 to turn On Pixel, 0 to turn Off

# print(imgPlainZeros.shape)
# print(imgPlainOnes.shape)

# img[100:200, 300:400] = 255, 0, 0
# cv2.imshow("The Zeros", imgPlainZeros)
# cv2.imshow("The Ones", imgPlainOnes)

# Lines in the image
# img = np.zeros((512, 512, 3), np.uint8)
# line = cv2.line(img, (0, 0), (300, 300), (0, 255, 255), 3)
# # Line Parameter Format (image, start, end, color, Thickness)
# line1 = cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 3)
# line2 = cv2.line(img, (0, img.shape[0]), (img.shape[1], 0), (0, 0, 255), 3)
#
# cv2.imshow("The Line Demo", line1)
# cv2.imshow("The Line Demo", line2)
# cv2.waitKey(0)


# Rectangles in the image
# Rectangle Parameter Format (image, start, end, color, Thickness)

img = np.zeros((512, 512, 3), np.uint8)
rectangle = cv2.rectangle(img, (20, 30), (250, 350), (0, 0, 255), 2)
circle = cv2.circle(img, (20, 30), 30, (0, 0, 255), 5)

# cv2.imshow("The Rectangle Demo", rectangle)
cv2.imshow("The Circle Demo", circle)
cv2.waitKey(0)
