import cv2
import numpy
import matplotlib.pyplot as plt

img=cv2.imread('../baby.png',cv2.IMREAD_GRAYSCALE)
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.imshow(img,cmap='gray',interpolation='bicubic')
plt.plot([100,100],[500,500],'black',linewidth=20)
plt.show()