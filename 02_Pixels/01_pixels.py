import cv2
import numpy as np



file_path="../img/openCv_Logo.png"

img = cv2.imread(file_path)

cv2.namedWindow("CV logo", cv2.WINDOW_NORMAL)
cv2.imshow("CV logo",img)


#print(img)

#px=img [0,0]
#print(px)

(b,g,r )= img [222,30]

print("(222,30) - Red: {} , Green : {} , Blue:  {} ".format(r,g,b))

cv2.waitKey(0)

"""
BGR/RGB ise 0-255 arası bir sıkalada değer alırlrar
0  ------------>Black
255---------->WHİTE


"""

#accsesing pixel value 1
blue = img[100,100,0]
print(blue)

green = img[100,100,1]
print(green)

red = img[100,100,2]
print(red)
print("Before ", img[100,100])
img[100,100]=[100,100,100]

print("After " , img[100,100])


