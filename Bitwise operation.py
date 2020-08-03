import cv2
import numpy as np

img1=np.zeros([500,500,3],np.uint8)

#lets make a rectangle in it of white color
img1=cv2.rectangle(img1, (100,200), (350,300),(255,255,255),-1) #here -1 is the thickness which will cover whole area in the rectangle

#now read a black and white image
img2=cv2.imread('blackwhite.png')
img2=cv2.resize(img2,(500,500)) # both image must have same height and width

#now lets try bitwise-and operation
bitwise_and=cv2.bitwise_and(img1, img2)

#now lets try bitwise-or operation
bitwise_or=cv2.bitwise_or(img1,img2)

#now lets try bitwise-xor operation
bitwise_xor=cv2.bitwise_xor(img1,img2)

#now lets try bitwise-not operation
bitwise_not=cv2.bitwise_not(img1)

#cv2.imshow("img1",img1)
cv2.imshow("img1",img1)
cv2.imshow("bitwise_not",bitwise_not) #so bitwise-not is just opposite of original image

cv2.waitKey(0)
cv2.destroyAllWindows()
