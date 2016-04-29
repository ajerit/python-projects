#
# Adolfo Jeritson. 12-10523
#
# Descripcion: Sumar elementos de una matriz NxM
#
# Fecha: 5/05/2015
#

# Variables
# suma: int
# matriz: array[0,N)[0,M)
# i: int
# j: int
# N: int
# M: int

# Valores Iniciales
suma, i, j = 0, 0, 0

# Precondicion
assert(N>0 and M>0)

# Calculos
for i in range(N):
	for j in range(M):
		suma = suma + matriz[j][i]

# Poscondicion
assert(suma == sum(matriz[y][x] for x in range(N) for y in range(M)))

# Salida
print("La suma de los elementos de la matriz es: " + str(suma))
