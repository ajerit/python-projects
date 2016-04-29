# 
# Adolfo Jeritson 12-10523
# PreLaboratorio 4
# Laboratorio de Algoritmos y Estrusturas 1
#
# Descripcion: Dada una matriz 3x3, ver si es diagonal
#

# Variables
# M: array[0, 3)[0, 3) of int
# esDiagonal: bool
# i: int
# j: int

# Valores iniciales
M = [ [int(input("M["+str(j)+","+str(i)+"] = ")) for i in range(3)] for j in range(3) ]
esDiagonal = True
i, j = 0, 0

# Precondicion
assert(True)

# Cota 3 - i
# Invariante
assert( esDiagonal == all(sum([[M[x][y] == 0 for x in range(i)  if x!=y] for y in range(j)], [])) )  
"""
El invariante funciona asi: se chequean los elementos cuyas coordenadas son diferentes
(fuera de la diagonal principal), luego  lo que devuelve es una lista de listas con valores booleanos,
por lo tanto se usa sum() con [] para hacer que sea una lista unidimensional.
Luego con la funcion all() que es cuantificador universal, si se encuentra con un False en la lista, 
determina que la matriz no es diagonal.
"""

# Calculos
for i in range(3):
	for j in range(3):
		print("revisando coordenada: M["+str(i)+","+str(j)+"]")
		print("revisando %s" % M[i][j])
		if i != j:  # Consideramos los elementos fuera de la diagonal principal
			if M[i][j] != 0:
				esDiagonal = False
				print("resultado: %s" % esDiagonal)
				print("-----")
				break  # Dado que si algun elemento no es 0, entonces
							# ya sabemos que no es diagonal, no es necesario
							# seguir chequeando los demas elementos.
		print("resultado: %s" % esDiagonal)
		print("-----")
		# Invariante
		assert( esDiagonal == all(sum([[M[x][y] == 0 for x in range(i) if x!=y] for y in range(j)], [])) )
		
	if not esDiagonal:
		break  # Salimos del ciclo al saber que ya no es diagonal.
		 
		 
# Poscondicion
assert( esDiagonal == all(sum([[M[x][y] == 0 for x in range(3)  if x!=y] for y in range(3)], [])) )

# Salida
if esDiagonal:
	print("La matriz es diagonal.")
else:
	print("La matriz NO es diagonal.")