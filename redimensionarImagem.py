import cv2
import numpy as np

img = cv2.imread('images/lena.jpg')

tamanho = 0.5 #redimensionar em 50% do original

if __name__ == "__main__":

    largura, altura, _ = img.shape

    largura *= tamanho
    altura *= tamanho

    largura = int(largura)
    altura = int(altura)

    img = cv2.resize(img, (altura, largura))

cv2.imshow('imagem_redimensionada', img)

cv2.waitKey(0)
cv2.destroyAllWindows()