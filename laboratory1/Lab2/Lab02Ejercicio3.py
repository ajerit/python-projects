#
# 
#
# DESCRIPCION: Dados tres valores enteros A, B y C con valores
# diferentes, determinar el valor máximo de ellos”

# Autor: 
#	Adolfo Jeritson. 12-10523
#
#

# Variables
# A: int
# B: int
# C: int
# mayor: int

# Valores iniciales
A = int(input("Inserte primer valor: "))
B = int(input("Inserte segundo valor: "))
C = int(input("Inserte tercer valor valor: "))

# Precondicion
assert(A != B and B != C and A != C)

# Calculos

if A > B:
	if A > C:
		mayor = A
	elif C > A:
		mayor = C
elif B > A:
	if B > C:
		mayor = B
	elif C > B:
		mayor = C
elif C > A:
	if C > B:
		mayor = C
	elif B > C:
		mayor = B
elif A > C:
	if A > B:
		mayor = A
	elif B > A:
		mayor = B

# Poscondicion
assert(mayor == max(A, B, C))

# Salida
print("El valor maximo es: " + str(mayor)) 
