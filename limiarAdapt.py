import cv2
import numpy as np

img = cv2.imread('images/lena.jpg', 0) #carregar preto e branco

adp1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

adp2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('original', img)
cv2.imshow('limiarizada', adp1)
cv2.imshow('limiar - gaussian', adp2)

cv2.waitKey(0)
cv2.destroyAllWindows()