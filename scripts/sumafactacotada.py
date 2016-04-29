# SUMA DE FACTORIALES
# ACOTADO DESDE UN I HASTA UN N DADOS
# USANDO ANALISIS DESCENDENTE
#

import math

N = int(input("Tope: "))
i = int(input("Inicio: "))
print("---")

def SumaFact(N, i):
	def fact(x):
		assert(x>=0)
		x1 = x
		num = 1
		while x >= 1:
			num = num*x
			x = x - 1
		assert(num == math.factorial(x1))
		return num
	
	assert(N >= i and i >= 0)
	k = i
	suma = 0
	while k <= N:
		suma = suma + fact(k)
		k = k+1
	assert(suma == sum(fact(x) for x in range(i,N+1)))
	return suma

resultado = SumaFact(N, i)
assert(resultado == sum(math.factorial(x) for x in range(i,N+1)))
print("Suma de factoriales desde "+str(i)+" hasta "+str(N))
print(resultado)