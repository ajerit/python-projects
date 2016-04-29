"""
 DESCRIPCION: Algoritmo para calcular las raices del polinomio AX2+BX+C
						con verificacion de las aserciones usando try/except y usando
						subprogramas.
 Autor: 
	Adolfo Jeritson. 12-10523
   Laboratorio de Algoritmos y Estructuras 1. Seccion 2

 Ultima modificacion: 16/05/2015
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

# Funcion para calcular raices usando la formula resolvente
def CalcularRaices(a: int, b: int, c: int) -> (float, float):
	# PRECONDICION: a != 0 and 4*a*c <= b*b
	# POSCONDICION: CalcularRaices == ((-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a))
	# var d: int // Variable auxiliar del discriminante
	# var raiz1: float
	# var raiz2: float
	d = b*b - 4 * a * c
	raiz1 = (-b + sqrt(d)) / (2 * a)
	raiz2 = (-b - sqrt(d)) / (2 * a)
	return raiz1, raiz2
	
# Llamada a la funcion
x1, x2 = CalcularRaices(A, B, C)

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
