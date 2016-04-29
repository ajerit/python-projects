# Suma de las potencias impares desde 0 hasta N

N = int(input("Inserte N mayor que cero: "))
print("Calculando la suma de las potencias de 2 impares")
print("---")

# Precondicion
assert(N >= 0)

# Valores iniciales
pot2 = 1
suma = 0
k = 0
cota = N - k

# Verificar invariantes antes del ciclo
assert(suma == sum(2**x for x in range(0, k) if (x % 2 == 1) and 0 <= k <= N))

# Calculos
while k <= N:
	print("k es: ", k)
	if k == 0:	
		pass
	elif k != 0 and k % 2 == 1:
		pot2 = pot2 * 2
		suma = suma + pot2
	elif k != 0 and k % 2 != 1:
		pot2 = pot2 * 2
	print("La suma va:", suma)	
	k = k + 1	
	
	# Verifico cota e invariante cada ciclo
	assert(suma == sum(2**x for x in range(0, k) if (x % 2 == 1) and 0 <= k <= N+1))
	assert(cota > N - k)
	print("cota:", cota)
	cota = N - k
	print("---")

# Poscondicion
assert(suma == sum(2**x for x in range(0, N+1) if (x % 2 == 1)))
print("La suma de las potencias impares de 2 es: ", suma)		