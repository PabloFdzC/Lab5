import cv2
import numpy as np

# Función para hacer la interpolación en
# colindacia N, solo se hacen los calculos
# si la N = 4 o N = 8 
def interpolacion(image, N, pinta_primero):
  (h, w) = image.shape[:2]
  wResult = np.zeros((h, w, 3), dtype = "uint8")
  # Se crean las matrices para calcular el
  # promedio solo con los valores deseados
  if(N == 4):
    vals = np.array([[0,1,0],[1,0,1],[0,1,0]]) / 4
  elif(N == 8):
    vals = np.array([[1,1,1],[1,0,1],[1,1,1]]) / 8
  for x in range(h):
    if pinta_primero:
      inicio = 0
    else:
      inicio = 1
    for y in range(inicio, w, 2):
      mean = 0
      for xVals in range(vals.shape[0]):
        for yVals in range(vals.shape[1]):
          if vals[xVals][yVals] != 0:
            imgX = x+xVals-1
            imgY = y+yVals-1
            # Se ajusta el X y Y de la imagen
            # original para obtener los valores
            # correctos, en este caso los bordes
            # toman el valor que tenga el punto
            # que se revisa actualmente
            if imgX < 0 or imgX >= h-1:
              imgX = x
            if imgY < 0 or imgY >= w-1:
              imgY = y
            mean += vals[xVals][yVals] * image[imgX][imgY]
      wResult[x][y] = mean
    pinta_primero = not pinta_primero
  return wResult

lab1_imagen1 = cv2.imread("lab1_imagen1.jpg")

# Punto 1 mapeo inverso e interpolación en
# colindancia N=4
lab5_imagen1 = interpolacion(lab1_imagen1, 4, True)
cv2.imwrite("lab5_imagen1.jpg", lab5_imagen1)

lab1_imagen2 = cv2.imread("lab1_imagen2.jpg")

# Punto 1 mapeo inverso e interpolación en
# colindancia N=4
lab5_imagen2 = interpolacion(lab1_imagen2, 4, True)
cv2.imwrite("lab5_imagen2.jpg", lab5_imagen2)