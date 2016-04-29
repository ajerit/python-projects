#
# Adolfo Jeritson. 12-10523
#
# Descripcion: Determinar A**B recursivamente
#

# Analisis Descendente
def fastPow(a: int, b: int) -> int:
	# PRE b > 0
	# POS fastPow == a ** b
	# var pot: int
	
	if b == 0: 
		pot = 1
	elif b != 0:
		pot = fastPow(a, b // 2)
		pot = pot * pot
		if b%2 != 0:
			pot = pot * a
	
	return pot

# Variables
# potencia, x, y: int

# Valores Iniciales
print("CALCULO DE A ** B RECURSIVO.")
x = int(input("Introduzca valor de A: "))
y = int(input("Introduzca valor de B: "))

# Precondicion
assert(y > 0)

# Calculos
potencia = fastPow(x, y)

# Poscondicion
assert(potencia == x ** y)

#Salida
print("La potencia es "+str(potencia))