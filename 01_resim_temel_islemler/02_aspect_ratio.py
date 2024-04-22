import cv2

def resizewithAspectRatio(img, width=None, height=None, inter=cv2.INTER_AREA):
    """
    Belirli bir genişlik veya yükseklik verilerek görüntüyü yeniden boyutlandırır.
    Görüntünün oranlarını korur.

    :param img: Görüntü
    :param width: Yeniden boyutlandırılacak genişlik (piksel cinsinden)
    :param height: Yeniden boyutlandırılacak yükseklik (piksel cinsinden)
    :param inter: Yeniden boyutlandırma için kullanılacak interpolasyon yöntemi
    :return: Yeniden boyutlandırılmış görüntü
    """
    dimension = None
    (h, w) = img.shape[:2]
    if width is None and height is None:
        return img
    if width is None:
        r = height / float(h)
        dimension = (int(w * r), height)
    return cv2.resize(img, dimension, interpolation=inter)

# Görüntüyü oku
img = cv2.imread("../img/cloneSlodier.png")

# Görüntüyü yeniden boyutlandır
img1 = resizewithAspectRatio(img, width=None, height=None, inter=cv2.INTER_AREA)

# Orijinal ve yeniden boyutlandırılmış görüntüleri göster
cv2.imshow("original", img)
cv2.imshow("Resized", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()