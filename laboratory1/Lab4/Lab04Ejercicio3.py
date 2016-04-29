# 
# Adolfo Jeritson 12-10523
#
# Descripcion: Dado un grupo de 10 estudiantes, y las notas de dos parciales
# calcular promedio de ambos parciales y nota de cada estudiante desde 1 a 5
#
# 6/06/2015

# Variables
# grupo: array[0, 10) of Estudiante()
# nota: int
# p1: int
# p2: int
# i: int
# j: int
# k: int
# suma1: int
# suma2: int
# prom1: real
# prom2: real

# Valores iniciales
class Estudiante:
	nota = 0
	p1 = 0
	p2 = 0 
	
grupo = [Estudiante() for x in range(10)]	

grupo[0].p1 = 37
grupo[0].p2 = 50
grupo[1].p1 = 29
grupo[1].p2 = 12 
grupo[2].p1 = 44
grupo[2].p2 = 5
grupo[3].p1 = 14
grupo[3].p2 = 50
grupo[4].p1 = 24
grupo[4].p2 = 49
grupo[5].p1 = 43
grupo[5].p2 = 45
grupo[6].p1 = 33
grupo[6].p2 = 18
grupo[7].p1 = 16
grupo[7].p2 = 24
grupo[8].p1 = 37
grupo[8].p2 = 22
grupo[9].p1 = 43
grupo[9].p2 = 36

suma1, suma2, prom1, prom2 = 0, 0, 0.0, 0.0

# Precondicion
assert(0 <= grupo[i].p1 <= 50 for i in range(10))
assert(0 <= grupo[j].p2 <= 50 for j in range(10))
assert(grupo[k].p1 + grupo[k].p2 <= 100 for k in range(10))

# Calculos
for i in range(10):
	final = grupo[i].p1 + grupo[i].p2
	if 85 <= final <= 100:
		grupo[i].nota = 5
	elif 70 <= final < 85:
		grupo[i].nota = 4
	elif 50 <= final < 70:
		grupo[i].nota = 3
	elif 30 <= final < 50:
		grupo[i].nota = 2
	else:
		grupo[i].nota = 1
		
for j in range(10):
		suma1 = suma1 + grupo[j].p1
		suma2 = suma2 + grupo[j].p2
		
prom1 = suma1 / 10
prom2 = suma2 / 10
	
# Poscondicion
# Traduccion de la implicacion: P => Q == (not P) or Q
assert(not (85 <= grupo[x].p1 + grupo[x].p2 <= 100) or grupo[x].nota == 5 for x in range(10)) 
assert(not (70 <= grupo[x].p1 + grupo[x].p2 < 85) or grupo[x].nota == 4 for x in range(10))
assert(not (50 <= grupo[x].p1 + grupo[x].p2 < 70) or grupo[x].nota == 3 for x in range(10))
assert(not (30 <= grupo[x].p1 + grupo[x].p2 < 50) or grupo[x].nota == 2 for x in range(10))
assert(not (grupo[x].p1 + grupo[x].p2 < 30) or grupo[x].nota == 1 for x in range(10))
assert(prom1 == sum(grupo[x].p1 for x in range(10)) / 10 and prom2 == sum(grupo[x].p2 for x in range(10)) / 10)

# Salida
print("-----")
for i in range(10):
	print("La nota del estudiante #" + str(i+1) + " es " + str(grupo[i].nota))
print("-----")
print("El promedio del primer parcial es " + str(prom1))
print("El promedio del segundo parcial es " + str(prom2))