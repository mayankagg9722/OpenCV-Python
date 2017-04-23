import numpy as np
import cv2

# Add two images in weighted manner
'''
img=cv2.imread('./Black.jpg')
img2=cv2.imread('./captcha.bmp')

img3=cv2.addWeighted(img2,0.3,img2,0.1,0)
cv2.imshow('weighted',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
# DRAWING Write N using cv2

img=np.zeros((512,512,4),np.uint8)
cv2.line(img, (50, 50), (50, 100), (255,0,0), 5)
cv2.line(img, (50, 50), (100, 100), (255,0,0), 5)
cv2.line(img, (100, 100), (100, 50), (255,0,0), 5)

cv2.rectangle(img, (0,0), (200,200), (0,255,0), 5)

font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img,'N using OpenCV',(10,500), font, 1,(255,255,255),2)

cv2.imshow("myimage",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# img = cv2.imread('./captcha.bmp')
# # cv2.imshow('sift_keypoints',img)
# gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# sift = cv2.FastFeatureDetector()
# kp = sift.detect(gray,None)
# img=cv2.drawKeypoints(gray,kp)

# cv2.imshow('sift_keypoints',img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

