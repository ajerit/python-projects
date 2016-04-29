# 
# Adolfo Jeritson 12-10523
# PreLaboratorio 4
# Laboratorio de Algoritmos y Estrusturas 1
#
# Descripcion: Dada una lista de N enteros dados por el usuario, calcular la suma
#

# Variables
# N: int
# A: array[0, N) of int
# suma: int
# i: int

# Valores iniciales
N = int(input("Indique el valor de N (Cantidad de elementos de la lista A) = "))

A = [ int(input("A[" + str(i) + "] = ")) for i in range(N) ]  

suma, i = 0, 0

# Precondicion
assert(N>0)

# Calculos

# Cota N - i
# Invariante
assert(0 <= i < N and suma == sum(A[x] for x in range(i)))

for i in range(N):
	print("iteracion #%s" % i)
	print("sumando el elemento: %s" % A[i])
	suma = suma + A[i]
	print("suma va: %s" % suma)
	print("-----")
	
	# Invariante
	assert(0 <= i < N and suma == sum(A[x] for x in range(i+1)))
	
# Poscondicion
assert(suma == sum(A[x] for x in range(N)))

# Salida
print("La suma de los elementos de la lista es: %s" % suma)