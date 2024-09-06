import numpy as np
import cv2 as cv
img=cv.imread("Photos/download.jpeg")
#cv.imshow("Name",img)
#cv.waitKey(0)
blankimg=np.zeros((500,500,3),dtype="uint8")
#img2=cv.imread(blankimg)
#cv.imshow("blank image",blankimg)
blankimg[:]=0,255,0
#cv.imshow("green",blankimg)
blankimg[200:250,100:200]=255,0,0
#cv.rectangle(name of the image,start co-ordinates,end coordiantes, colour,thickness)
cv.rectangle(blankimg,(200,0),(250,250),(0,255,255),thickness=10)
cv.circle(blankimg,(blankimg.shape[1]//2,blankimg.shape[0]//2),40,(230,100,255),thickness=-1)
cv.line(blankimg,(100,100),(20,20),(100,200,255),thickness=10)
#cv.putText(name of the image,"what text",where text,what font,size of text,colour,thickness)
cv.putText(blankimg,"hello",(255,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(100,200,20),2)
cv.imshow("random red",blankimg)
cv.waitKey(0)