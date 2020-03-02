from PIL import Image
import pytesseract as pyt
import cv2
import numpy as np
import os

if __name__ == "__main__":
    
    #carrega imagem
    imagem = cv2.imread('images/capa-livro1.jpg')

    #salva imagem em arquivo temporário
    filenameImagem = "{}.jpg".format(os.getpid())
    cv2.imwrite(filenameImagem, imagem)

    #carrega imagem usando PIL/pillow e aplica OCR
    texto = pyt.image_to_string(Image.open(filenameImagem))

    #deleta arquivo temporario
    os.remove(filenameImagem)

    print("Texto: \n" + texto)

    #exibe imagem
    cv2.imshow('imagem conteudo', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()