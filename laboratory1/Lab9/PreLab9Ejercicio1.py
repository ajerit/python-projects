#
# Adolfo Jeritson. 12-10523
#
# Descripcion: Determinar mcd recursivamente
#

# Analisis descendente
def MCD(a: int, b: int) -> int:
	# PRECONDICION: a>=0 and b>=0
	# POSCONDICION MCD ==  max(i for i in range(1,min(a,b)) if (a%i == 0 and b%i == 0))
	# var m: int
	if b == 0:
		m = a
	elif b != 0:
		m = MCD(b, a%b)
	return m	
	
# Variables
# max, x, y: int

# Valores iniciales
print("CALCULO DEL MCD DE A Y B RECURSIVAMENTE.")
x = int(input("Introduzca el valor de A: "))
y = int(input("Introduzca el valor de B: "))

# Precondicion
assert(x >= 0 and y >= 0)
# Calculos
mcd = MCD(x, y)

# Poscondicion
assert(x%MCD(x, y) == 0 and y%MCD(x, y) == 0 and mcd == max(i for i in range(1,min(x,y)) if (x%i == 0 and y%i == 0)))

# Salida
print("El MCD es "+str(mcd))