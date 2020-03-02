import cv2

img = cv2.imread('images/lena.jpg', 1)
cv2.imshow('image', img)

#cv2.imwrite('lena.png', img) #criar nova imagem em .png

cv2.waitKey(0)
cv2.destroyAllWindows()
