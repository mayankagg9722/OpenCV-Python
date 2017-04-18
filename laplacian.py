import  numpy as np
import cv2

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    cv2.imshow('frame',frame)
    cv2.imshow('laplacian',laplacian)
    
    if cv2.waitKey(5) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()