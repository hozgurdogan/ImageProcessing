from builtins import print

import cv2
import numpy as np


"""
canvas = np .zeros((512,512,3),dtype=np.uint8)+200
print(canvas)



cv2.imshow("BlackScreen",canvas)
"""


canvas = np.zeros((512,512,3),dtype=np.uint8)+255
print(canvas)



print(canvas)




cv2.line(canvas,(0,0),(512,512),(255,0,0),thickness=10)

cv2.rectangle(canvas,(20,20),(100,500),(0,255,0), thickness=-1)

cv2.circle(canvas,(100,500),12,(0,0,255),thickness=-1)

points=np.array([[[110,140],[330,200],[290,300],[220,250]]],np.int32)
cv2.polylines(canvas,[points],True,(0,123,211),5)


# Bir tuşa basılmasını bekle
cv2.imshow("BlackScreen",canvas)

cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()
