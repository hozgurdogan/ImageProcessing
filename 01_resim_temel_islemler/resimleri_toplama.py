# OpenCV ve NumPy kütüphanelerini içeri aktarın
import cv2
import numpy as np

# Beyaz bir arka plan üzerinde mavi bir daire çizin
crile = np.zeros((512,512,3), np.uint8) + 255
cv2.circle(crile, (256,256), 60, (255,0,0), -1)

# Beyaz bir arka plan üzerinde kırmızı bir dikdörtgen çizin
rectangle = np.zeros((512,512,3), np.uint8) + 255
cv2.rectangle(rectangle, (150,150), (350,350), (0,0,255), -1)

# Daire ve dikdörtgeni toplayın
add = cv2.add(crile, rectangle)

# Ekranda göster
cv2.imshow("Daire", crile)
cv2.imshow("Dikdörtgen", rectangle)
cv2.imshow("Toplam", add)

# (256, 256) koordinatındaki piksel değerini yazdırın
print(add[256, 256])

# Kullanıcı kapatana kadar bekleyin
cv2.waitKey(0)
cv2.destroyAllWindows()
