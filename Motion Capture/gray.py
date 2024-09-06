import cv2 as cv

img=cv.imread("Photos/image2.jpeg")
cv.imshow("Colour",img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
graycolor=cv.cvtColor(gray,cv.COLOR_GRAY2RGB)*255
cv.imshow("gray",gray)
cv.imshow("Gray Colour",graycolor)
cv.waitKey(0)