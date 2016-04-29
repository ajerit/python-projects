""""
 DESCRIPCION: Algoritmo para calcular las raices del polinomio “AX2+BX+C”


 Autor: 
	Adolfo Jeritson. 12-10523
   Laboratorio de Algoritmos y Estructuras 1. Seccion 2

 Ultima modificacion: 18/04/2015
"""
from math import sqrt   # Del modulo de matematica traer la funcion raiz cuadrada

# Variables
#	A: int
#	B: int
#	C: int 
#	x1: float
#	x2: float

# Valores iniciales
A = int(input("Introduzca el valor de la primera constante: "))
B = int(input("Introduzca el valor de la segunda constante: "))
C = int(input("Introduzca el valor de la tercera constante: "))

# Precondicion
assert(A != 0 and 4 * A * C <= B * B)

# Algoritmo para calcular raices usando la formula resolvente
x1 = (-B + sqrt(B * B - 4 * A * C)) / 2 * A
x2 = (-B - sqrt(B * B - 4 * A * C)) / 2 * A

# Poscondicion
assert(A * x1 * x1 + B * x1 + C == 0 and A * x2 * x2 + B * x2 + C == 0)

# Salida
print("Las raices son: " + str(x1) + " y " + str(x2))