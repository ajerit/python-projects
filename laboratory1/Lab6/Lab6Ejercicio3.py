#
# Adolfo Jeritson. 12-10523
#	19/05/2015
#
# Descripcion: Generar la lista de los factores primos de M menores o iguales
# que N.
#

def EsPrimo(x: int) -> bool:
	# PRECONDICION: x >= 0
	# POSCONDICION primo == all(x % i for i in range(2, x))
	# var primo: bool
	if x < 2:
		primo = False
	elif x >= 2:
		primo = all(x % i for i in range(2, x))
	return primo
	
def DivideA(x: int, y: int) -> bool:
	# PRECONDICION: x >= 0 and y > 0
	# POSCONDICION: divide == (x % y == 0)
	# var divide: bool
	divide = False
	if x % y == 0:
		divide = True
	return divide

def ObtenerDivsHasta(m: int, n: int) -> [int]:
	# PRECONDICION: M > 0
	# POSCONDICION: divs == [x in range(1, n+1) if DivideA(m, x)]
	# var divs: array of int
	divs = [1]
	k = 1
	assert(divs == [x for x in range(1, k+1) if DivideA(M, x)]) # Invariante
	for k in range(2, n+1):
		if DivideA(m, k):
			divs.append(k)
		assert(divs == [x for x in range(1, k+1) if DivideA(M, x)]) # Invariante	
	return divs
	
def ObtenerFactPrimos(l: [int]) -> [int]:
	# PRECONDICION: len(l) > 0
	# POSCONDICION: facts == [x in l if EsPrimo(x)]
	# var facts: array of int
	facts = []
	for k in l:
		if EsPrimo(k):
			facts.append(k)
	return facts

def salida(a: [int]) -> 'void':
	print("Los factores primos de "+str(M)+" menores o iguales a "+str(N)+" son:")
	print(a)

# Variables:
# M: int
# N: int
# divisores: array of int
# factores: array of int
# Valores iniciales:
print("DADOS M y N, BUSCAR LOS FACTORES PRIMOS DE M MENORES O IGUALES QUE N")
M = int(input("Ingrese el numero natural para buscar factores primos (M): "))
N = int(input("Ingrese restriccion hasta donde buscar (N): "))

# Precondicion
assert(M >= N and N >= 0)

# Calculos
divisores = ObtenerDivsHasta(M, N)
factores = ObtenerFactPrimos(divisores)

# Poscondicion
assert(factores == [y for y in [x for x in range(1, N+1) if DivideA(M, x)] if EsPrimo(y)])
# Salida
salida(factores)

