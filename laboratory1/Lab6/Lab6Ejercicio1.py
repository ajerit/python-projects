#
# Adolfo Jeritson. 12-10523
# 19/05/2015
#
# Descripcion: Chequear si una secuencia esta ordenada.
#

# Analisis descendente
def entradaSec(n: int) -> [int]:
	# PRECONDICION: N > 1
	# POSCONDICION: True
	# var a:array[0,n) of int
	# cota n - x
	a = []
	for x in range(n):
 		a.append(int(input("Ingrese elemento #"+str(x+1)+": ")))
	return a
	
def chequearSec(A: [int]) -> str:
	# PRECONDICION: len(a) > 1
	# POSCONDICION: 
	# var k: int
	# var orden: str
  if all(A[i] >= A[i+1] for i in range(len(A)-1)):
  	orden = "Descendiente"
  elif all(A[i] <= A[i+1] for i in range(len(A)-1)):
  	orden = "Ascendiente"
  else:
  	orden = "Desordenada"
  return orden
  	
def salida(o: str) -> str:
	print("La lista tiene el siguiente orden: ")
	print(o)

# Variables
# N: int
# sec: [int]
# resultado: str

# Valores iniciales:
N = int(input("Inserte cuantos elementos quiere ingresar: "))

# Precondicion:
assert(N>1)

# Programa
sec = entradaSec(N)
resultado = chequearSec(sec)

# Poscondicion
assert(not(resultado == "Descendiente") or all(sec[i] >= sec[i+1] for i in range(len(sec)-1)))
assert(not(resultado == "Ascendiente") or all(sec[i] <= sec[i+1] for i in range(len(sec)-1)))
assert(not(resultado == "Desordenada") or not(all(sec[i] >= sec[i+1] for i in range(len(sec)-1))))

# Salida
salida(resultado)

