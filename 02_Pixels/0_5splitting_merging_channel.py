import cv2
import numpy as np
import matplotlib.pyplot as plt


# ROI : Region of interest ------>ilgi alanı


img_path="../img/openCv_Logo.png"

img= cv2.imread(img_path)
cv2.namedWindow("OpenCv",cv2.WINDOW_NORMAL)
print("Shape img : {}".format(img.shape))


#BGR


(B,G,R)=cv2.split(img)

merged=cv2.merge(([B,G,R]))


blackScreen=np.zeros(img.shape[:2], "uint8")
cv2.imshow("Black",blackScreen)


cv2.imshow("RED",cv2.merge([blackScreen,blackScreen,R]))
cv2.imshow("Green",cv2.merge([blackScreen,G,blackScreen]))

cv2.imshow("Blue",cv2.merge([B,blackScreen,blackScreen]))
cv2.imshow("OpenCv",img)

#cv2.imshow("OpenCv MERGED",merged)


#cv2.imshow("B",B)
#cv2.imshow("G",G)
#cv2.imshow("R",R)

cv2.waitKey(0)
cv2.destroyAllWindows()