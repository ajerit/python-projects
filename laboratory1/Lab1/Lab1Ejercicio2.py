#
# DESCRIPCION: Dados tres valores enteros a,b,c que cumplen a>=b>=c, intercambie los
# valores de manera que cumplan a<=b<=c
#
#
# Autor: 
#	Adolfo Jeritson. 12-
#   Laboratorio de Algoritmos y Estructuras 1. Seccion 2
#
# Ultima modificacion: 14/04/2015
#

# VARIABLES:
#	a: int // Valor entero cualquiera
#   b: int // Valor entero cualquiera
#	c: int // Valor entero cualquiera

#Valores iniciales
a = 100
b = 50
c = 25

#Precondicion
assert(a >= b and b >= c)

#Instrucciones
a, b, c = c, b, a

#Poscondicion
assert(a <= b and b <= c)

#Salida
print("Los nuevos valores intercambiados son: ")
print("a = " + str(a))
print("b = " + str(b))
print("c = " + str(c)) 