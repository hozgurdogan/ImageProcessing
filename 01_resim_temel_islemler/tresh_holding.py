import cv2
from matplotlib import pyplot as plt

# Resmi yükle
img = cv2.imread("../img/helic1.jpg")

# Resmi griye dönüştür
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold uygula
ret, th1 = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)

# Orijinal ve işlenmiş resmi göster
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title('Orijinal Resim')

plt.subplot(1, 2, 2)
plt.imshow(th1, cmap='gray')
plt.axis('off')
plt.title('Threshold Uygulanmış Resim')

plt.show()

# Adaptive threshold uygula
th2 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Görselleri OpenCV ile göster
# Görüntüleri yeniden boyutlandır
height, width = img.shape[:2]
th1_resized = cv2.resize(th1, (512, 464))
th2_resized = cv2.resize(th2, (512, 464))
cv2.imshow("img-th1", th1_resized)
cv2.imshow("img-th2", th2_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
