import cv2
import numpy

img=cv2.imread('./Black.jpg',cv2.IMREAD_COLOR)
  
img[100:150,400:450]=[255,255,255]

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
