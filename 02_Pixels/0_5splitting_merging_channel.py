import cv2
import numpy as np
import matplotlib.pyplot as plt

# ROI : Region of interest ------>ilgi alanı

# Resmin dosya yolunu belirt
img_path = "../img/openCv_Logo.png"

# Resmi oku
img = cv2.imread(img_path)

# Görüntü penceresinin boyutunu ayarla
cv2.namedWindow("OpenCv", cv2.WINDOW_NORMAL)

# Görüntünün şeklini yazdır
print("Shape img : {}".format(img.shape))

# BGR renk kanallarına ayır
(B, G, R) = cv2.split(img)

# BGR kanallarını birleştir
merged = cv2.merge(([B, G, R]))

# Siyah bir ekran oluştur
blackScreen = np.zeros(img.shape[:2], "uint8")
cv2.imshow("Black", blackScreen)

# Sadece kırmızı rengi göster
cv2.imshow("RED", cv2.merge([blackScreen, blackScreen, R]))

# Sadece yeşil rengi göster
cv2.imshow("Green", cv2.merge([blackScreen, G, blackScreen]))

# Sadece mavi rengi göster
cv2.imshow("Blue", cv2.merge([B, blackScreen, blackScreen]))

# Orijinal görüntüyü göster
cv2.imshow("OpenCv", img)

# BGR kanallarını göster
cv2.imshow("B", B)
# cv2.imshow("G", G)  # Yeşil kanalı göstermek için yorum satırı
cv2.imshow("R", R)

# Bir tuşa basılmasını bekle
cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()
