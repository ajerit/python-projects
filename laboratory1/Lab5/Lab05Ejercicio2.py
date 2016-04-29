#
# Adolfo Jeritson. 12-10523
#
# Descripcion: Conjetura de numeros naturales
#
# Fecha: 12/05/2015
#

# Variables
# N: int
# k: int 
# cota: int 
# sec: array of int

import sys
# Valores Iniciales
sec = []
N = int(input("Inserte un numero natural: "))
sec.append(N)
k = 0
cota = 10000 - k

# Verificacion de la precondicion
try:
	assert(N > 0)
except:
	print("No introdujo un numero natural.")
	print("Intente de nuevo.")
	sys.exit()
	
# Calculos
# Verificar invariante antes del ciclo
try:
	assert(0<=k<=10000)
except:
	print("Error del invariante antes del ciclo.")	
	sys.exit()
# Verificar cota positiva
try:
	assert(cota >= 0)
except:
 print("Error. Cota negativa antes del ciclo.")
 sys.exit()
 
while sec[k] != 4:
	print("Elementos en la secuencia: "+str(len(sec)))
	print("El X es: "+str(sec[k]))
	if sec[k] % 2 == 0:
		sec.append(int(sec[k] / 2))
	else:
		sec.append(3*sec[k] + 1)
	k = k + 1
	print("-----")

	# Verificacion invariante durante ciclo
	try:
		assert(0<=k<=10000)
	except:
		print("Error del invariante durante el ciclo")	
		sys.exit()
	# Verificacion cota decreciente
	try:
		assert(cota > 10000 - k)
	except:
		print("Error, cota no decreciente.")
		print("Cota = "+str(cota))
		sys.exit()
	cota = 10000 - k
	# Verificacion cota positiva 
	try:
		assert(cota >= 0)
	except:
		print("Error, cota es negativa.")
		print("Cota = "+str(cota))
		sys.exit()
		
print("Elementos en la secuencia: "+str(len(sec)))
print("El X es: "+str(sec[k]))	
print("-----")

# Verificacion de la poscondicion
try:
	assert(sec[k] == 4)
except:
	print("Error de la poscondicion.")
	print("No se ha llegado a 4")
	sys.exit()
	
# Salida
print("La secuencia completa es: ")
print(sec)
