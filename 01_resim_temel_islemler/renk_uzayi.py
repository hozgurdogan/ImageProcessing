import cv2

# Resmi oku
img = cv2.imread("../img/cloneSlodier.png")

# Resmi RGB formatına dönüştür
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Resmi HSV formatına dönüştür
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Resmi gri tonlamaya dönüştür
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Orijinal, RGB, HSV ve gri tonlamalı resimleri göster
cv2.imshow("ORJ", img)
cv2.imshow("RGB Goruntu", img_rgb)
cv2.imshow("HSV Goruntu", img_hsv)
cv2.imshow("Gri Tonlamali Goruntu", img_gray)

# Kullanıcı kapatana kadar bekleyin
cv2.waitKey(0)
cv2.destroyAllWindows()
