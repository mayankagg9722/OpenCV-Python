import numpy as np
from PIL import Image
import cv2
from numpy import array

image=Image.open('./captcha.bmp').convert('P')
emptyImage = Image.new('P',image.size,255)
newemptyimage = Image.new('P',image.size,255)

# myim=cv2.imread('./captcha.bmp')
# myim=cv2.cvtColor(myim,cv2.COLOR_BGR2GRAY)
# cv2.imshow('mayank',myim)
# k=np.ones((20,20),np.uint8)
# # mynewim=cv2.blur(myim,(2,2))
# kernel = np.ones((2,3), np.uint8)
# mynewim = cv2.dilate(myim, kernel, iterations=1)
# cv2.imshow('mynewim',mynewim)
# cv2.waitKey(0)
# cv2.destroyAllWindows() 

# print(image.histogram())

for i in range(image.size[0]):
    for j in range(image.size[1]):

        pix = image.getpixel((i,j))

        if(pix == 1):
            emptyImage.putpixel((i,j),0)

emptyImage.show()

for i in range(image.size[0]):
    for j in range(1,image.size[1]-1):

        upperPixel = image.getpixel((i,j-1))
        pix = image.getpixel((i,j))
        lowerPixel = image.getpixel((i,j+1))

        if ( pix==1 and (pix == upperPixel or pix == lowerPixel)):
            newemptyimage.putpixel((i,j),0)

newemptyimage.show()

# newcropimage=Image.new('P',image.size,255)
startpix=(0,0)
endpix=(0,0)
# print(newemptyimage.histogram())
flag=0
for j in range(newemptyimage.size[1]):
    for i in range(newemptyimage.size[0]):
        pix=newemptyimage.getpixel((i,j))
        # print(pix)
        if(pix==255):
            if flag==0 :
                continue
            elif flag==1:
                endpix=(i-1,j)
                flag=2 
                break 
        elif(pix==0):
            if(flag==0):
                startpix=(i,j)
                flag=1      
heightPIX=-1
for i in range(newemptyimage.size[0]):
    for j in range(newemptyimage.size[1]):
        pix=newemptyimage.getpixel((i,j))
        if(pix==0):
            if heightPIX<j:
                heightPIX=j                       
print(startpix) 
print(endpix) 
print(heightPIX) 
img2 = newemptyimage.crop((startpix[0], startpix[1], endpix[0], 18))
img2.show()

# newImage=[]
# width=image.size[0]
# height=image.size[1]
# pixels=image.load()


# for color in image.getdata():
    
#     if color==86:
#         newImage.append(86)
#     else:
#         newImage.append(0)

# newim = Image.new(image.mode,image.size)
# newim.putdata(newImage)
       
        
# for y in range(0,height):
#     for x in range(0,width):
#         rgb=image.getpixel((x,y))
#         # if(rgb==86):
#             # pixels[y,x]=255
#             # image.getpixel((x,y))=250
#             # print rgb

# # npArray=np.asarray(image)
# # l=[]
# # for c,k in enumerate(npArray):
# #     for p,q in enumerate(k):
# #         x,y=q
# #         # print x
# #         # print y
# #         if(x==255):
#               q=250,255
# #             l.append((250,255))
            
# #         else:
# #             l.append((x,y))
# #     m.append(l)
# #         # print q
# #         # print q[0]
# #         # print q[1]
# #         # l.append(x)
# #         # m.append(y)


# # # print m
# # # a = array(m)
# # # img = Image.fromarray(a, 'L')
# # # img.show()


