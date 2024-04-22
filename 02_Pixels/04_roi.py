import cv2
import numpy as np
import matplotlib.pyplot as plt


# ROI : Region of interest ------>ilgi alanı


img_path="../img/basketboll.jpg"

img= cv2.imread(img_path)
cv2.namedWindow("Basket",cv2.WINDOW_NORMAL)
print("Shape img : {}".format(img.shape))

roi=img[100:200, 0:50]

img[200:300,300:350]=roi


cv2.imshow("Basket",img)
cv2.imshow("Basletbol Roi", roi)
cv2.waitKey(0)
cv2.destroyAllWindows()