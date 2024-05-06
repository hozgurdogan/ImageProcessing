import cv2
import numpy as np

# Kameradan video akışını başlat
cap = cv2.VideoCapture(0)


# Bir trackbar için boş bir fonksiyon tanımla
def nothing(x):
    pass


# Trackbar penceresini oluştur ve boyutunu ayarla
cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar", 500, 500)

# Alt renk sınırları için trackbar'ları oluştur
cv2.createTrackbar("Lover -H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Lover -S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Lover -V", "Trackbar", 0, 255, nothing)

# Üst renk sınırları için trackbar'ları oluştur
cv2.createTrackbar("Upper -H", "Trackbar", 0, 180, nothing)
cv2.createTrackbar("Upper -S", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("Upper -V", "Trackbar", 0, 255, nothing)

# Üst renk sınırları için varsayılan değerleri ayarla
cv2.setTrackbarPos("Upper -H", "Trackbar", 180)
cv2.setTrackbarPos("Upper -S", "Trackbar", 255)
cv2.setTrackbarPos("Upper -V", "Trackbar", 255)

while True:
    # Kameradan bir kareyi oku
    ret, frame = cap.read()

    # Kareyi yatay olarak çevir
    frame = cv2.flip(frame, 1)

    # Kareyi HSV formatına dönüştür
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Alt renk sınırlarını trackbar'lardan al
    lower_h = cv2.getTrackbarPos("Lover -H", "Trackbar")
    lower_s = cv2.getTrackbarPos("Lover -S", "Trackbar")
    lower_v = cv2.getTrackbarPos("Lover -V", "Trackbar")

    # Üst renk sınırlarını trackbar'lardan al
    upper_h = cv2.getTrackbarPos("Upper -H", "Trackbar")
    upper_s = cv2.getTrackbarPos("Upper -S", "Trackbar")
    upper_v = cv2.getTrackbarPos("Upper -V", "Trackbar")

    # Alt ve üst renk sınırlarını belirle
    lower_color = np.array([lower_h, lower_s, lower_v])
    upper_color = np.array([upper_h, upper_s, upper_v])

    # Renk sınırlarına göre maske oluştur
    mask = cv2.inRange(frame_hsv, lower_color, upper_color)

    # Orijinal kareyi göster
    cv2.imshow("Orijinal Kare", frame)

    # Maskeyi göster
    cv2.imshow("Maske", mask)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

# Kullanılan kaynakları serbest bırak ve tüm pencereleri kapat
cap.release()
cv2.destroyAllWindows()
