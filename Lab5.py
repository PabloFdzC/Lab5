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
    for y in range(w):
      mean = 0
      if (inicio+y) % 2 == 0:
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
      else:
        wResult[x][y] = image[x][y]
    pinta_primero = not pinta_primero
  return wResult

def resaltar_bordes(imagen, nombre_resultado, c):
  (h, w) = imagen.shape[:2]
  result = np.zeros((h, w, 3), dtype = "uint8")
  # Se hace la imagen blur
  imagen_blur = cv2.GaussianBlur(imagen, (3,3), 0)
  # Se convierte la imagen a escala de grises
  escala_de_grises = cv2.cvtColor(imagen_blur, cv2.COLOR_BGR2GRAY)
  # Se calcula el laplaciano de la imagen con opencv.
  laplaciano = cv2.Laplacian(escala_de_grises, cv2.CV_16S, 3)
  # Se calcula el valor abosulto de los resultados
  laplaciano = cv2.convertScaleAbs(laplaciano)
  # Se realiza el proceso de resaltar los bordes de la imagen 
  # utilizando el laplaciano.
  for x in range(h):
    for y in range(w):
      result[x][y] = imagen[x][y] + c * laplaciano[x][y]
  cv2.imwrite(nombre_resultado, result)



lab1_imagen1 = cv2.imread("lab1_imagen1.jpg")

# Punto 1 mapeo inverso e interpolación en
# colindancia N=4
lab5_imagen1 = interpolacion(lab1_imagen1, 4, True)
cv2.imwrite("lab5_imagen1.jpg", lab5_imagen1)

lab1_imagen2 = cv2.imread("lab1_imagen2.jpg")

# Punto 2 mapeo inverso e interpolación en
# colindancia N=4
lab5_imagen2 = interpolacion(lab1_imagen2, 4, True)
cv2.imwrite("lab5_imagen2.jpg", lab5_imagen2)

# Prueba de resaltado de bordes con c = 2
resaltar_bordes(lab5_imagen1, "PruebaC2.jpg", 2)

# Prueba de resaltado de bordes con c = 1
resaltar_bordes(lab5_imagen1, "PruebaC1.jpg", 1)

# Prueba de resaltado de bordes con c = 0.5
resaltar_bordes(lab5_imagen1, "PruebaC05.jpg", 0.5)

# Punto 5, mejora de nitidez utilizando la
# amplificación de bordes por medio del
# operador Laplaciano.
resaltar_bordes(lab5_imagen1, "lab5_imagen3.jpg", 0.1)

# Punto 5, mejora de nitidez utilizando la
# amplificación de bordes por medio del
# operador Laplaciano.
resaltar_bordes(lab5_imagen2, "lab5_imagen4.jpg", 0.1)

