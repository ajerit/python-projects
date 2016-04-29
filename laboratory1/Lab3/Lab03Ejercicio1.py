#
#
#
# DESCRIPCION: (1: Superficie de una habitación; 
# 2: Área de una circunferencia; 3: Suma de cuadrados
#
#  Autor: Adolfo Jeritson. 12-105231
#
#

# Constantes
# PI: real

# Variables
# S: int
# suma: int
# largo: real
# ancho: real
# radio: real
# area: real
# N: int
# k: int
# elegir: int

from decimal import *

# Valores Iniciales
PI = 3.1416
suma = 0
N = 0
ancho = 0
largo = 0
area = 0
s = 0
radio = 0
k = 1

print("Opciones: ")
print("1 - Calcular superficie.")
print("2 - Calcular area circunferencia.")
print("3 - Calcular sumatoria de cuadrados.")

elegir = int(input("Inserte solo el numero de la opcion a elegir (1, 2 o 3): "))
if elegir == 1:
	ancho = float(input("Inserte el ancho: "))
	largo = float(input("Inserte largo: "))
elif elegir == 2:
	radio = float(input("Inserte el area de la circunferencia: "))
elif elegir == 3: 
	N = int(input("Inserte numero N natural para calculas sumatoria: "))
else:
	print("No eligio una opcion valida, intente de nuevo.")

# Precondicion
assert(N >= 1 or (ancho >= 0 and largo >= 0) or area >= 0)

# Calculos
if elegir == 1:
	s = ancho*largo
	print("La superficie es:","%.4f" % s)
elif elegir == 2:
	area = PI * (radio ** 2)
	print("El area es:", area)
elif elegir == 3:
	#suma = sum(x**2 for x in range(1,N+1))
	# Verificar invariante antes del ciclo
	assert(1 <= k <= N + 1 and suma == sum(x**2 for x in range(1,k)))
	cota = N - k
	
	while k <= N:
		print("k es:", k)
		suma = suma + k**2
		print("La suma va:",suma)
		k = k + 1
		# Verificar cota e invariante en cada ciclo
		assert(1 <= k <= N + 1 and suma == sum(x**2 for x in range(1,k)))
		assert(cota > N - k)
		print("cota es:", cota)
		print("---")
		cota = N - k
	print("La sumatoria de cuadrados es: ",suma)
	
# Poscondicion
assert(s == ancho * largo or area == PI * (radio**2) or suma == sum(x**2 for x in range(1,N+1)))




