import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path="../img/forrset.jpg"
img = cv2.imread(img_path)

print(img)


corner=img[0:100 , 0:100]

corner1=img[0:100 , 0:250] # [y,x]  ilk değer y start  2 . değer y end değeri , 3 . değer x in start 4. değer x end  [y_start : y end ,x_start: x_end]


#bgr
# belli alanın rengini değiştirme

img[0:100,0:250]=(0,0,0)

cv2.imshow("forest", img)

#cv2.imshow("corner", corner)


#cv2.imshow("corner1", corner1)


cv2.namedWindow("forest", cv2.WINDOW_NORMAL)

cv2.waitKey(0)

cv2.destroyAllWindows()