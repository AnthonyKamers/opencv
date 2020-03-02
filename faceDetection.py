import cv2
import numpy as np

def main():
    #carrega classificador de arquivo
    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')

    #carrega vídeo
    cap = cv2.VideoCapture('videos/megamind.avi')

    while True:
        #carrega o frame do video
        frameExiste, frame = cap.read()

        if(frameExiste == False):
            cap.release()
            return
        
        #só funciona com tons de cinza
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        #1: frame em preto e branco
        #2: especifica o quanto a imagem redimensiona
        #3: quantidade de vizinhos (para não fazer vários quadrados)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        #para cada face detectada
        for(x, y, w, h) in faces:
            #desenhar retangulo
            frame = cv2.rectangle(frame, (x, y), (x+w, y+w), (255, 0, 0), 4)

        cv2.imshow("detecção", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    main()