import cv2
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread('Resources/araf.jpg')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGrey, 1.1, 4)

for (x, y, width, height) in faces:
    cv2.rectangle(img, (x, y), (x + width, y+height), (255, 0, 0), 2)

cv2.imshow("The Contour", img)
cv2.waitKey(0)
