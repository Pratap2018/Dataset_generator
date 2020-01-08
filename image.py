import numpy as np 
import cv2 
x=cv2.imread('iron-mask-avengers-end-game-wallpaper.jpg',1)
cv2.namedWindow("s",cv2.WINDOW_NORMAL)
cv2.imshow("s",x)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()