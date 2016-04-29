#
# DESCRIPCION: Programa que dado el radio de una circunferencia
# calcula su area correspondiente.
#
#
# Autor: 
#	Adolfo Jeritson. 12-10523
#   Laboratorio de Algoritmos y Estructuras 1. Seccion 2
#
# Ultima modificacion: 14/04/2015
#

# VARIABLES:
#	r: float // Radio de la circunferencia
#   a: float // Resultado del area
#   pi: float // Almacena el valor de PI

#Valores iniciales
r = 10
pi = 3.14159

#Precondicion
assert(r > 0) #El radio debe ser un valor positivo

#Calculos
a = pi * (r ** 2)

#Poscondicion
assert(a == pi * (r*r))

#Salida
print("El area de la circunferencia es: ")
print(a)
