import cv2 as cv
capture=cv.VideoCapture(0)
while True:
    isTrue,frame=capture.read()
    cv.imshow("Video Capture",frame)
    if cv.waitKey(20) and 0xFF==ord("d"):
        break
capture.release()
cv.destroyAllWindows()
