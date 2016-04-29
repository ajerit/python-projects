#
# Adolfo Jeritson. 12-10523
#
# Descripcion: Chequear si una secuencia de enteros esta ordenada
#
# Fecha: 12/05/2015
#
  
# Variables
# ordenada: bool
# sec: array[0,len(sec)) of int
# N: int
# k: int
# cota: int

import sys
# Valores Iniciales
sec = []
k = 1
ordenada = True

# Cota 500 - k
for i in range(500):
	N = int(input("Inserte el entero #"+str(i+1)+" de la secuencia: "))
	if N == 0:
		break
	else:	
		sec.append(N)

cota = len(sec) - k

# Verificacion de la precondicion
try:
	assert(len(sec) > 1 and not(any(sec[x] for x in range(len(sec)) if sec[x] < 0)))
except:
	print("Error, la secuencia debe tener a lo sumo 2 elementos, todos positivos.")
	print("Vuelva a intentarlo.")
	sys.exit()
# Calculos

# Verificacion de cota al inicio
try:
	assert(cota >= 0)
except:
	print("Error. Cota no positiva antes del ciclo.")
	print("Cota : "+str(cota))
	sys.exit()
# Verificacion del invariante antes del ciclo
try:
	assert(1<=k<=len(sec) and ordenada == all(sec[x] for x in range(1,k) if sec[x-1] <= sec[x]))
except:
	print("Error del invariante antes del ciclo.")
	sys.exit()
	
print(sec)	
while k < len(sec):
	print("Comparando "+str(sec[k-1])+" y "+str(sec[k]))
	
	if sec[k-1] > sec[k]:
		ordenada = False
		
	k = k + 1	
		
	# Verificacion de invariante durante el ciclo
	try:
		assert(1<=k<=len(sec) and not ordenada == any(sec[x] for x in range(1,k) if sec[x-1] > sec[x]))
	except:
		print("Error del invariante durante el ciclo.")
		print("ordenada = "+str(ordenada))
		print("inv: "+str(any(sec[x] for x in range(1,k) if sec[x-1] > sec[x])))
		sys.exit()
		
	# Verificacion de cota decreciente
	try:
		assert(cota > len(sec)- k)
	except:
		print("Error. Cota no dereciente durante el ciclo.")
		print("Cota : "+str(cota))
		sys.exit()
	cota = len(sec) - k	
	# Verificacion de cota no negativa
	try:
		assert(cota >= 0)
	except:
		print("Error. Cota no positiva durante el ciclo.")
		print("Cota : "+str(cota))
		sys.exit()
		
	
# Verificacion de la poscondicion
try:
	assert(not ordenada == any(sec[x] for x in range(1,k) if sec[x-1] > sec[x]))
except:
	print("Error de la poscondicion.")
	print("ordenada = "+str(ordenada))
	sys.exit()
	
# Salida
print("---")
if ordenada:
	print("La secuencia esta ordenada.")
else:
	print("La secuencia no esta ordenada.")
