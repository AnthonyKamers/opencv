import cv2

img = cv2.imread('images/lena.jpg', 0)

limiar, imgLimiar = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

cv2.imshow('imagem limiar', imgLimiar)

cv2.waitKey(0)
cv2.destroyAllWindows()