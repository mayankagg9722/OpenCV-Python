import numpy as np
import cv2
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)




    light_blue=np.array([100,100,0])
    dark_blue=np.array([150,255,255])

    mask=cv2.inRange(hsv,light_blue,dark_blue)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    if cv2.waitKey(5) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()