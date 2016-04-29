#
# 
#
# DESCRIPCION: Dados dos números enteros m y n,
# devuelva m/n si m=10, m*n si m=5,
# m+n si m=3, m-n si m=2 y en cualquier otro devuelva m

# Autor: 
#	Adolfo Jeritson. 12-10523
#
#

# Variables
# m: int
# n: int
# resultado: int

# Valores iniciales
m = int(input("Introduzca el valor de m: "))
n = int(input("Introduzca el valor de n: "))

# Precondicion
assert(n != 0)

# Calculos
resultado = m

if m == 10:
	resultado = m / n
elif m == 5:
	resultado = m * n
elif m == 3:
	resultado = m + n
elif m == 2:
	resultado = m - n
else:
	pass

# Poscondicion
assert(resultado == m or resultado == m / n or resultado == m * n or resultado == m + n or resultado == m - n)

# Salida
print(str(resultado))



