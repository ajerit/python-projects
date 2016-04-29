#
# DESCRIPCION: Contar los divisores de un numero N dado a traves de la linea de comandos.
#
#
# Autor: 
#	Adolfo Jeritson. 12-10523
#   Laboratorio de Algoritmos y Estructuras 1. Seccion 2
#
# Ultima modificacion: 23/04/2015
#

# Variables
#	N: int
#	i: int
#	cuenta: int
#	cota: int

from sys import argv

# Valores iniciales
N = int(argv[1])
i = 1
cuenta = 0
cota = N - i + 2

# Precondicion
assert(N > 0)

# Verificar invariantes y cota antes del ciclo
assert(0<i<=N+1 and cuenta == sum(1 for x in range(1,i) if (N % x == 0)))

while i <= N:
	print("i vale:", i)
	if N % i == 0:
		cuenta = cuenta + 1
	i = i + 1	
	
	# Verificar cota e invariantes durante cada ciclo
	assert(0<i<=N+1 and cuenta == sum(1 for x in range(1,i) if (N % x == 0)))
	assert(cota > N - i + 2)
	print("cota:",cota)
	cota = N - i + 2
	print("----")  
	
# Poscondicion
assert(cuenta == sum(1 for x in range(1,i) if (N % x == 0)))	

# Salida
print("La cantidad de divisores de", str(N), "es:", str(cuenta))