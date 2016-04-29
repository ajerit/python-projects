"""
 DESCRIPCION: Algoritmo para calcular las raices del polinomio “AX2+BX+C”
						con verificacion de als aserciones usando try/except

 Autor: 
	Adolfo Jeritson. 12-10523
   Laboratorio de Algoritmos y Estructuras 1. Seccion 2

 Ultima modificacion: 10/05/2015
"""
import sys
from math import sqrt   # Del modulo de matematica traer la funcion raiz cuadrada


# Variables
#	A: int
#	B: int
#	C: int 
#	x1: float
#	x2: float

# Verificacion de la Precondicion
while True:
	try:
		A = int(input("Introduzca el valor de la primera constante: "))
		B = int(input("Introduzca el valor de la segunda constante: "))
		C = int(input("Introduzca el valor de la tercera constante: "))
		
		assert(A != 0 and 4 * A * C <= B * B)
		
		break
	except:
		print("Hubo un error en la entrada de los datos.")
		print("A no puede ser cero, y el discriminante debe ser positivo")
		print("para que existan raices reales.")
		print("Vuelva a intentarlo.")

# Algoritmo para calcular raices usando la formula resolvente
x1 = (-B + sqrt(B * B - 4 * A * C)) / 2 * A
x2 = (-B - sqrt(B * B - 4 * A * C)) / 2 * A

# Verificacion de la Poscondicion
try:
	assert(A * x1 * x1 + B * x1 + C == 0 and A * x2 * x2 + B * x2 + C == 0)
except:
	print("Hubo un error al calcular las raices del polinomio.")
	print("Las expresiones A*x1*x1 + B*x1 + C = 0 y A*x2*x2 + B*x2 + C = 0")
	print("no son correctas.")
	print("x1 = "+str(x1)+" , x2 = "+str(x2))
	sys.exit()

# Salida
print("Las raices son: " + str(x1) + " y " + str(x2))