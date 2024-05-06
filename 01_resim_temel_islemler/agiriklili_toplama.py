# f(x,y)=x*a+y*b+c fonksiyonunu tanımlayın
# Bu fonksiyon, iki görüntü arasında ağırlıklı bir toplam oluşturmak için kullanılacaktır
# Bu toplam, birinci görüntünün %70'ini ve ikinci görüntünün %30'unu kullanacaktır

# OpenCV ve NumPy kütüphanelerini içeri aktarın
import cv2
import numpy as np

# Beyaz bir arka plan üzerinde mavi bir daire çizin
crile = np.zeros((512,512,3), np.uint8) + 255
cv2.circle(crile, (256,256), 60, (255,0,0), -1)

# Beyaz bir arka plan üzerinde kırmızı bir dikdörtgen çizin
rectangle = np.zeros((512,512,3), np.uint8) + 255
cv2.rectangle(rectangle, (150,150), (350,350), (0,0,255), -1)

# Ağırlıklı toplamı hesaplayın
dist = cv2.addWeighted(crile, 0.7, rectangle, 0.3, 0)

# Ekranda göster
cv2.imshow("Daire", crile)
cv2.imshow("Dikdörtgen", rectangle)
cv2.imshow("Ağırlıklı Gösterim", dist)

# Kullanıcı kapatana kadar bekleyin
cv2.waitKey(0)
cv2.destroyAllWindows()
