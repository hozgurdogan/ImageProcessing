import cv2

img_path="../img/openCv_Logo.png"
img =cv2.imread(img_path,3)

print(img.shape) #height ,width  , chanels num

# channel -----> 3 ise color
# channel ------> 1 ise grayscale

print("height  pixels {}, width  : {} ,  channels : {}".format(img.shape[0], img.shape[1], img.shape[2]))
print("height  pixels {}, width  : {} ".format(img.shape[0], img.shape[1]))
# 3 farklı kanaldan sadece 1 tane olursa boyut 1/3 e düşer
# size

print(" img size {} ".format(img.size))

# datatype
print("Data Type {} ".format(img.dtype))

cv2.imshow("Logo", img)

cv2.waitKey(0)
cv2.namedWindow("Logo",cv2.WINDOW_NORMAL)
