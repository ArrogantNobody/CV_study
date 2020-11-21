import cv2
import numpy as np

# cv2.IMREAD_COLOR 加载一个彩色图片，图片的透明度会被忽律，也是缺省参数。
# cv2.IMREAD_GRAYSCALE 加载黑白图片
# cv2.IMREAD_UNCHANGED 加载包含alpha通道的图片

img = cv2.imread('./images/banfu.jpg')#,0)#gray level
GrayImage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('image',img)
cv2.imshow("gray", GrayImage)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',GrayImage)
    cv2.destroyAllWindows()