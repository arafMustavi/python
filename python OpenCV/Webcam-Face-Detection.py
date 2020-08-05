# Invoking the Web-Cam to show video
import cv2

cap = cv2.VideoCapture(0)
# cap.set method is used to set some variable from the Web-Cam
# 3 is for Width
# 4 is for Height
# 10 is for Brightness

cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 10)

while True:
    success, vidImg = cap.read()
    # success is a bool variable that shows whether the rendering is successful or not
    # print(success, type(success))

    faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(vidImg, 1.1, 4)
    faces = faceCascade.detectMultiScale(vidImg, 1.1, 4)

    for (x, y, width, height) in faces:
        cv2.rectangle(vidImg, (x, y), (x + width, y + height), (0, 255, 0), 2)

#    cv2.imshow("The Contour", img)
#    cv2.waitKey(0)

    # cv2.imshow("Web-Cam Captures with Contour", vidImg)
    cv2.imshow("Face Detection", vidImg)

    # title for the web-cam pan's video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q is pressed to stop the video")
        break
    # As long as q is not pressed,the video gets rendered


# img = cv2.imread('Resources/araf.jpg')
# imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

