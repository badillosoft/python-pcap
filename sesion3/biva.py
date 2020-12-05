# Un módulo es un archivo de python, que puede ejecutarse incluso como un programa tradicional,
# sin embargo, está pensado, para declarar funciones, clases y demás elementos que sean declaraciones
# útiles que sean usadas en otros programas.
# Es decir, un módulo es un archivo dónde declaramos funciones y demás, para ser utilizadas en otro archivo/programa.
# Esto hace que nuestro código sea portable y lo podamos reutilizar.

# En este archivo vamos a declarar algunas funciones útiles, para consumirlas en otro programa

def min_max(lista):
    # return a, b -> return (a, b)
    return min(lista), max(lista) # Cuidado: Observa que esta es una tupla (*, *) debido a la coma que separa los valores, los parentésis fueron omitidos

# Una matriz es una lista de listas y se puede una matriz de 2x2 como:
# matriz = [ [1, 2], [3, 4] ]
# Una matriz de 3x5 se podría ver como:
# matriz = [ [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15] ]
# 3 filas por 5 columnas o 3 vectores de 5 valores cada vector

# Para resolver un sistema de ecuaciones lineales, podemos asociar una matriz a los coefiecientes de las ecuaciones y tener un vector (una lista) de soluciones,
# por ejemplo, si tenemos 2 ecuaciones lineales 2x + 5y = 9, 3x - 2y = 4, entonces la matriz asociada de coeficientes se puede ver como:
# matriz = [ [2, 5], [3, -2] ]
# El vector asociado se puede ver como
# vector = [9, 4]
# Entonces para resolver el problema, podemos usar la matriz inversa transpuesta y multiplicarla por el vector de coeficientes
# A (x, y) = b
# (x, y) = A^-1 b
def solveMatriz(A, s):
    # A[0] -> [2, 5]
    # A[0][0] -> 2
    # A[0][1] -> 5
    # A[1] -> [3, -2]
    # A[1][0] -> 3
    # A[1][1] -> -2
    a = A[0][0]
    b = A[0][1]
    c = A[1][0]
    d = A[1][1]
    
    det = a * d - b * c
    
    Ainv = [
        [d / det, -b / det],
        [-c / det, a / det]
    ]
    
    x = Ainv[0][0] * s[0] + Ainv[0][1] * s[1]
    y = Ainv[1][0] * s[0] + Ainv[1][1] * s[1]
    
    return (x, y)

# Requests es un módulo de python que nos permite solicitar peticiones web a servidores y sitios web
# Podemos lanzar peticiones de tipo GET, POST, PUT, etc. y descargar imágenes, html plano, etc.
import requests
from PIL import Image
from io import BytesIO

# Vamos a crear una función que tome una url de una imagen y el nombre del archivo cómo queremos guardar la imagen
# Entonces, nuestra función a través de requests, tomará la url, descargará la imagen y la guardará
def downloadImage(url, filename):
    response = requests.get(url)
    
    if response.status_code != 200:
        return False
    
    image = Image.open(BytesIO(response.content))
    
    image.save(filename)
    
    return True