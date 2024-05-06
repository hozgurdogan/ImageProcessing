import cv2
import numpy as np

# Görüntü dosyasını yükle
img_filter = cv2.imread("../img/Noisy_img.jpg")

# Görüntüyü Gauss filtresiyle bulanıklaştır
blur_b = cv2.GaussianBlur(img_filter, (5, 5), cv2.BORDER_DEFAULT)

# Görüntüyü median filtresiyle bulanıklaştır
blur_b = cv2.medianBlur(img_filter, 11)

# Bulanıklaştırılmış görüntüyü göster
cv2.imshow("Blurry Image", blur_b)
cv2.waitKey(0)
