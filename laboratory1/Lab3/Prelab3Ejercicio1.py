#
# DESCRIPCION: Calcular la suma de los factoriales desde 0 hasta un numero entero definido por el usuario.
#
#
# Autor: 
#	Adolfo Jeritson. 12-10523
#   Laboratorio de Algoritmos y Estructuras 1. Seccion 2
#
# Ultima modificacion: 23/04/2015
#

# Variables:
#	suma: int
#	fact: int
#	k: int
#	cota: int
#	N: int

# Valores iniciales:
N = int(input("Introduzca el numero para calcular sumatoria de factoriales: "))
k, suma, fact = 0, 0, 1
cota = N + 1 - k

def prod(iterable):
	p = 1
	for n in iterable:
		p *= n
	return p	

# Precondicion:
assert(N >= 0)

# Verificar cota e invariantes al iniciar:
assert(0 <= k <= N + 1 and suma == sum(prod(j for j in range(1,x+1)) for x in range(0, k)))

while k <= N:
	print("k vale:", k)
	if k > 0:
		fact = fact * k
	suma = suma + fact	
	k = k + 1
	
	# Verificar invariante y cota en cada iteracion:
	assert(0 <= k <= N + 1 and suma == sum(prod(j for j in range(1,x+1)) for x in range(0, k)))
	assert(cota > N + 1 - k)
	print("cota:",cota)
	cota = N + 1 - k 
	print("----")  
	
# Poscondicion
assert(suma == sum(prod(j for j in range(1,x+1)) for x in range(0, k)))

# Salida
print("La sumatoria de factoriales desde cero a", str(N) ,"es:", str(suma))
	