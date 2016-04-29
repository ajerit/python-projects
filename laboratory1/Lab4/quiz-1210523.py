# Adolfo Jeritson. 12-10523
#
# Descripcion: Calcular la aproximacion del logaritmo natural de un numero real
#
# 5/05/2015
#

# Variables
# N: real
# it: int
# suma: real
# aprox: real
# produc: real

# Valores Iniciales
print("CALCULO DEL VALOR APROXIMADO DE ln x")
N = float(input("Diga el numero x al que desea calcular el logaritmo natural: "))
it = int(input("Introduzca el numero de iteraciones deseadas: "))
aprox, suma = 0, 0

# Precondicion
assert(0 < it <= 50)

# Calculos

for i in range(it):
	if i == 0:
		produc = 1
	else:	
		produc = produc * ((-1) * (N - 1))
		
	suma = (1 / (i + 1)) * ((N - 1) * produc)            
	aprox = aprox + suma
	
# Poscondicion
assert(aprox == sum((((-1)**x)*(N-1)**(x+1)/(x+1)) for x in range(it)))

# Salida
print("El valor aproximado es: ",aprox)
