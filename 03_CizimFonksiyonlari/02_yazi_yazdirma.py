from builtins import print

import cv2
import numpy as np


canvas = np .zeros((512,512,3),dtype=np.uint8)+255
font1=cv2.FONT_ITALIC
cv2.putText(canvas,"Selin ", (30,100),font1,4,(0,0,0),cv2.LINE_AA )
# Bir tuşa basılmasını bekle
cv2.imshow("canvas",canvas)
cv2.namedWindow("canvas", cv2.WINDOW_NORMAL)
cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()
