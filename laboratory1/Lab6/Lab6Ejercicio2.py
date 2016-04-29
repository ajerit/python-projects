#
# Adolfo Jeritson. 12-10523
#	19/05/2015
#
# Descripcion: Producir el numero de fibonacci para cada elemento de un
# arreglo dado por el usuario.
#

def entradaSec(n: int) -> [int]:
	# PRECONDICION: N > 0
	# POSCONDICION: True
	# var a:array[0,n) of int
	# cota n - x
	a = []
	for x in range(n):
 		a.append(int(input("Ingrese elemento #"+str(x+1)+": ")))
	return a

def fib(n: int) -> [int]:
	# PRECONDICION: True
	# POSCONDICION: t == t + j
	# var k, i, j, , cota: int
	# var nums: [int]
	nums = []
	i = 1
	j = 0
	k = 0
	t = 0
	cota = n - k
	assert(n - k >= 0) # Verificar cota positiva
	assert(0<=k<=n) # Verificar invariante
	while k < n:
		t = i + j
		i = j
		j = t
		k = k+1
		assert(0<=k<=n) # Verificar invariante
		assert(n - k >= 0) # Verificar cota positiva
		assert(cota > n - k) # Verificar cota decreciente
		cota = n - k
		nums.append(j)
	return nums

def sacarFib(a: [int]) -> [int]:
	# PRECONDICION: len(a) > 0
	# POSCONDICION: l = [fib(x) for x in a]
	# var l: array[0, len(a)) of int
	l = []
	for x in a:
		l.append(fib(x))
	return l

def salida(a: [int], b: [int]) -> 'void':
	# PRECONDICION: len(a) > 0
	# POSCONDICION: True
	print("Los numeros de fibonacci de los elementos ingresados son: ")
	for x in range(len(a)):
	  print("De "+str(a[x])+" son: "+str(b[x]))
	  print("----")

# Variables
# N: int
# sec: array[0,N) of int
# secfib: array[0,N) of int

# Valores iniciales
N = int(input("Ingrese cuantos elementos quiere calcularles su secuencia: "))

# PRECONDICION
assert(N > 0)

# Programa
sec = entradaSec(N)
secfib = sacarFib(sec)

# POSCONDICION:
assert(secfib == sacarFib(sec))

# Salida:
salida(sec, secfib)
		

