import cv2
import numpy as np

img = cv2.imread("../img/helicopter.jpg",0)

row,col= img.shape

print(row)
print(col)

M = np.float32([[1,0,200],[0,1,100]])

dst = cv2.warpAffine(img,M,(row,col))

cv2.imshow("dst",dst)

cv2.waitKey(0)