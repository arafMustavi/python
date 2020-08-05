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
    print(success, type(success))

    cv2.imshow("Web-Cam Captures", vidImg)
    # title for the web-cam pan's video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("q is pressed to stop the video")
        break
    # As long as q is not pressed,the video gets rendered
