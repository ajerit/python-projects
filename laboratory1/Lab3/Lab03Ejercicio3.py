#
#
#
# DESCRIPCION: Verificar si un numero es perfecto
#
#  Autor: Adolfo Jeritson. 12-105231
#
#

# Variables
# N: int
# EsPerfecto: bool
# suma: int
# i: int
# cota: int

# Valores iniciales
N = int(input("Inserte un entero positivo para verificar si es perfecto: "))
suma = 0
i = 1
cota = N - i

# Precondicion
assert(N > 0)

# Verificar invariante
assert(1<=i<=N and suma == sum(x for x in range(1,i) if (N%x == 0)))

# Calculos
while i < N:
	if N % i == 0:
		suma = suma + i
	i = i + 1
	# Verificar cota e invariante
	assert(1<=i<=N  and suma == sum(x for x in range(1,i) if (N%x == 0)))
	assert(cota > N - i)

	cota = N - i
	
EsPerfecto = suma == N

# Poscondicion 
assert(EsPerfecto == True or EsPerfecto == False)

# Salida
print("El numero",N,"es perfecto?:",EsPerfecto)
