#
# DESCRIPCION: Dado un valor b, determinar si es par.
#
#
# Autor: 
#	Adolfo Jeritson. 12-10523
#   Laboratorio de Algoritmos y Estructuras 1. Seccion 2
#
# Ultima modificacion: 14/04/2015
#

#Variables
# b: int // Valor a determinar

# Valores iniciales
b = 27638

#Precondicion
assert(True) # b puede ser cuaquier entero positivo o negativo, no tiene restricciones

#Calculo
def EsPar(b): return b%2 == 0

#Poscondicion
assert(EsPar(b) == True or EsPar(b) == False) #Asegura que el resultado va a ser Verdadero o Falso sobre si el numero b es par

#Salida 
print("El numero " + str(b) + " es par? " + str(EsPar(b)))

