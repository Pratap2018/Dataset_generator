import numpy as np
import cv2 as cv
cap = cv.VideoCapture('/home/pratap/Videos/Paladins 2020-01-01 20-41-36-892.mp4')
c=0;
x=[]
while cap.isOpened(): 
    ret,frame =cap.read()
    if ret is True:
        x.append(frame)
    if not ret:
       print("Can't receive frame (stream end?). Exiting ...")
       break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.rectangle(frame,(797,0),(1354,450),(0,0,255),3)
    cv.namedWindow('vid',cv.WINDOW_FREERATIO)
    cv.imshow('vid',frame);
    if cv.waitKey(1) == ord('q'):
        frame1=frame[0:450,797:1354]
        break
cap.release()
cv.imshow('vid1',frame1);
print(frame1.shape)
cv.waitKey(0)
cv.destroyAllWindows()