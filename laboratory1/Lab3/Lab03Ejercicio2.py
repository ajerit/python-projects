#
#
#
# DESCRIPCION: Dado un entero positivo N, ver si es primo
#
#  Autor: Adolfo Jeritson. 12-105231
#
#

# Variables
# k: int
# N: int
# cota: int 
# EsPrimo: bool

# Valores iniciales
N = int(input("Inserte numero para verificar si es primo: "))
k = 2
cota = N + 2 - k
EsPrimo = True

# Precondicion
assert(N > 0)

# Verificar cota e invariante al inicio
assert(2 <= k <= N and (EsPrimo == True or EsPrimo == False))

# Calculos
if N < 2:
	EsPrimo = False
elif N >= 2:
	while k < N:
		print("Probando divisor:", k)
		if N % k == 0:
			EsPrimo = False
		if N % k != 0:
			pass
		k = k + 1
		
		# Verificar cota e invariante en cada ciclo
		assert(2 <= k <= N and (EsPrimo == True or EsPrimo == False))
		assert(cota > N + 2 - k)
		cota = N + 2 - k
		print("---")

# Poscondicion
assert(EsPrimo == True or EsPrimo == False)

# Salida
print("El numero",N,"es primo?:",EsPrimo)

