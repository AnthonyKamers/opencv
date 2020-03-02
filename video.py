import cv2
import numpy as np

#como não especifica, será da webcam
cap = cv2.VideoCapture(0)

contadorBalada = 0
while(True):
    existeFrame, frame = cap.read()

    altura, largura, _ = frame.shape

    imagemVazia = np.zeros((altura, largura), dtype="uint8")

    (b, g, r) = cv2.split(frame)
    r = cv2.merge([imagemVazia, imagemVazia, r])
    g = cv2.merge([imagemVazia, g, imagemVazia])
    b = cv2.merge([b, imagemVazia, imagemVazia])

    imagemBalada = np.zeros((altura, largura, 3), dtype="uint8")

    contadorBalada = contadorBalada % 4
    contadorBalada += 1

    if(contadorBalada == 0):
        imagemBalada = frame
    elif (contadorBalada == 1):
        imagemBalada = r
    elif (contadorBalada == 2):
        imagemBalada = g
    elif (contadorBalada == 3):
        imagemBalada = b

    cv2.imshow('webcam - balada', imagemBalada)

    if(cv2.waitKey(50) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()