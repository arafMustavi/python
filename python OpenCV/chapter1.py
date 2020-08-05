import cv2

# Loading the Image
img = cv2.imread("Resources/araf.jpg")

# Showing the Image
cv2.imshow("Man", img)
cv2.waitKey(0)
# The waitkey parameter takes in milisecond
# 0 in waitkey means eternity

# Loading a video
cap = cv2.VideoCapture("Resources/test.mp4")

while True:
    success, vidImg = cap.read()
    # success : a bool variable that shows whether the rendering is successful
    # print(type(success))

    cv2.imshow("video from HDD", vidImg)
    # Pan title Video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # Pressing q will terminate the process

