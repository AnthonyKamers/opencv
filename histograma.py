import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/lena.jpg', 0); #ler em preto e branco (0)

cv2.imshow('imagem original', img) #mostrar imagem

plt.hist(img.ravel(), 256, [0, 256]) #fazer histograma #ravel: transformar matriz 2d e formar vetor de 1d

plt.show() #mostrar histograma

cv2.waitKey(0)
cv2.destroyAllWindows()