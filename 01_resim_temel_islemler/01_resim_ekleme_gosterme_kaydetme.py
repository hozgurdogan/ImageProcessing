import cv2

# Resmi oku
img = cv2.imread("../img/cloneSlodier.png")

# Resmi yazdır (Matris olarak)
print(img)

# Yeni bir pencere oluştur ve resmi göster
cv2.namedWindow("Gorsel", cv2.WINDOW_NORMAL)
cv2.imshow("Gorsel", img)

# Resmi "klone1.jpg" olarak kaydet
cv2.imwrite("klone1.jpg", img)

# Bir tuşa basılmasını bekle
cv2.waitKey(0)

# Tüm pencereleri kapat
cv2.destroyAllWindows()
