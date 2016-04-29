""""
 DESCRIPCION: Algoritmo que calcula el valor absoluto de “a”.


 Autor: 
	Adolfo Jeritson. 12-10523
   Laboratorio de Algoritmos y Estructuras 1. Seccion 2

 Ultima modificacion: 18/04/2015
"""

# Variables
#	A: int // Valor del numero introducido por el usuario
#   b: int // Valor del calculo del valor absoluto

# Valor inicial
A = int(input("Introduzca valor del numero: "))

# Precondicion
assert(True)

# Algoritmo valor absoluto
if A >= 0:
	b = A
elif A < 0:
	b = -A

# Poscondicion
assert(b == abs(A))

# Salida
print("El valor absoluto es " + str(b))



