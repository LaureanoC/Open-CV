import cv2
import numpy as np

parametros = cv2.aruco.DetectorParameters()

diccionario = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)

cap = cv2.VideoCapture(1)


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    esquinas, ids, candidatos_malos = cv2.aruco.detectMarkers(gray, diccionario, parameters=parametros)

    if np.all(ids != None):
        aruco = cv2.aruco.drawDetectedMarkers(frame, esquinas)

        c1 = (esquinas[0][0][0][0], esquinas[0][0][0][1])
        c2 = (esquinas[0][0][1][0], esquinas[0][0][1][1])
        c3 = (esquinas[0][0][2][0], esquinas[0][0][2][1])
        c4 = (esquinas[0][0][3][0], esquinas[0][0][3][1])

        copy = frame

        imagen = cv2.imread('hpollocompleta.png')

        tamanio = imagen.shape

        puntos_aruco = np.array([c1,c2,c3,c4])

        puntos_imagen = np.array([
            [0,0],
            [tamanio[1] - 1, 0],
            [tamanio[1] -1, tamanio[0] - 1],
            [0, tamanio[0] - 1]


        ], dtype = float)

        h, estado = cv2.findHomography(puntos_imagen, puntos_aruco)

        perspectiva = cv2.warpPerspective(imagen, h, (copy.shape[1], copy.shape[0]))
        cv2.fillConvexPoly(copy, puntos_aruco.astype(int), 0, 16)
        copy = copy + perspectiva
        cv2.imshow('Realidad aumentada', copy)

    else:
        cv2.imshow('Realidad aumentada', frame)
    
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()