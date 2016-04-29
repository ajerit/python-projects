#
# Adolfo Jeritson. 12-10523
#
# Descripcion: Dados los coeficientes de un polinomio, lo construye y 
# muestra el grado del mismo
#
# 5/05/2015
#

# Variables
# coef : array(0,M] of int
# c: int
# M: int
# polinom: array[0, len(coef)+1) of str
# grado: int
# i: int

# Valores Iniciales
M = int(input("Introduza el valor de M (Limite del grado): "))
coef, polinom = [], []

for i in range(M+1):
	c = int(input("Introduzca el coeficiente C" + str(i) + ": "))
	if c == 0:
		break
	else:
		coef.append(c)

# Precondicion
assert(M >= 0 and len(coef) <= M + 1)

# Calculos
for i in range(len(coef)):
	if i == 0:
		polinom.append(str(coef[i]))  # El primer coeficiente no tiene variable
	elif i == 1:
		polinom.append(str(coef[i])+"X")  # El segundo coeficiente es de grado 1
	else:
		polinom.append(str(coef[i])+"X^"+str(i))

if M == 0:  # Consideramos el caso del polinomio cero
	grado = 0
	if coef == []:
		polinom = [0]
else:		
	grado = len(coef) - 1

# Poscondicion
assert(grado <= M)

# Salida
print("El grado del polinomio es: " + str(grado))
print("La forma polinomial es: ")

for i in range(len(polinom)):
	if i == len(polinom) - 1:
		print(polinom[i])
	else:
		print(polinom[i]+"+", end="")
	
