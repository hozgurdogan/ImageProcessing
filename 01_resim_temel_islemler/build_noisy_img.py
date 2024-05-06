import cv2
import numpy as np

# Resmi yükle
image = cv2.imread('../img/openCv_Logo.png')

# Gürültü seviyesi
noise_level = 0.005

# Resmin boyutları
height, width, _ = image.shape

# Rastgele gürültü ekle
noise = np.random.normal(0, noise_level, (height, width, 3))
noisy_image = np.clip((image + noise*255).astype(np.uint8), 0, 255)

# Sonucu göster
cv2.imshow('Noisy Image', noisy_image)
cv2.imwrite('../img/Noisy_img.jpg', noisy_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
