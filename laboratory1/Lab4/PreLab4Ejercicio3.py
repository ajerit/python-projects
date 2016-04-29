# 
# Adolfo Jeritson 12-10523
# PreLaboratorio 4
# Laboratorio de Algoritmos y Estrusturas 1
#
# Descripcion: Dado un grupo de N estudiantes, calcular promedio de edad e indice.
#

# Variables
# indice: real
# edad: int
# nombre: str
# grupo: array[0, N) of Estudiante()
# N: int
# i: int
# j: int
# k: int
# sum1: int
# sum2: float
# proedad: int
# proind: float


# Valores iniciales
N = int(input("Inserte numero de estudiantes > "))

class Estudiante:
	nombre = ""
	edad = 0
	indice = 0.0

grupo = [Estudiante() for x in range(N)]	

#Cota: N - i
for i in range(N):
	grupo[i].nombre = input("Ingrese nombre del estudiante # " + str(i+1) + ": ")
print("-----")

#Cota: N - j
for j in range(N):
	grupo[j].edad = int(input("Ingrese edad del estudiante # " + str(j+1) + ": "))
print("-----")

#Cota: N - k
for k in range(N):
	grupo[k].indice = float(input("Ingrese indice del estudiante # " + str(k+1) + ": "))
print("-----")
	
sum1, sum2, i, j, k = 0, 0, 0, 0, 0

# Precondicion
assert(len(grupo[i].nombre) > 0 for i in range(N))
assert(grupo[j].edad > 0 for j in range(N))
assert(grupo[k].indice > 0 for k in range(N))

# Calculos

# Cota N - j
# Invariante
assert(0<= j < N and sum1 == sum(grupo[x].edad for x in range(j)) )

for j in range(N):
	sum1 = sum1 + grupo[j].edad
	# Invariante
	assert(0 <= j < N and sum1 == sum(grupo[x].edad for x in range(j+1)) )
	
proedad = sum1 // N

# Cota N - k
# Invariante
assert(0<= k < N and sum2 == sum(grupo[y].indice for y in range(k)) )
for k in range(N):
		sum2 = sum2 + grupo[k].indice
		# Invariante
		assert(0<= k < N and sum2 == sum(grupo[y].indice for y in range(k+1)) )
		
proind = sum2 / N		
	
# Poscondicion
assert(proedad == (sum(grupo[j].edad for j in range(N))) // N and proind == (sum(grupo[k].indice for k in range(N)) / N))

# Salida
print("-----")
print("El promedio de edad del grupo es: ", proedad)
print("El promedio de indices del grupo es: ", proind)