# QUIZ 1
# Adolfo Jeritson. 12-10523
#

# Variables
# a: int
# b: int
# c: int
# d: int
# per: int
# area: float
# lados: int
# raiz: float
# h: float

# Valores iniciales

import math

print("CALCULO DE PROPIEDADES DE UN POLIGONO")
lados = int(input("Introduzca el numero de lados: "))
a = int(input("Introduzca el lado a: "))
b = int(input("Introduzca el lado b: "))
c = int(input("Introduzca el lado a: "))
if lados == 4:
	d = int(input("Introduzca el lado d: "))

# Precondicion
if lados == 3:
	assert(a > 0 and b > 0 and c > 0)
elif lados == 4:
	assert(a > 0 and b > 0 and c > 0 and d > 0)

# Calculos
if lados == 3:  # Triangulos
	per = a + b + c
	if a == b and b == c:  # equilatero, area
		assert(a > c / 2)
		raiz = math.sqrt(3)
		h = a * raiz / 2
		area = c * h / 2
	if a != b and b != c and a != c:  # escaleno, perimetro
		area = False
		h = False
	if (a == b and c != a) or (a == c and b != a):  # isoceles, per y area
		assert(a > c / 2)
		raiz = math.sqrt(4 * a ** 2 - c ** 2)
		h = raiz / 2
		area = c * h / 2
elif lados == 4:  # Cuadrilateros
	h = b
	per = a + b + c + d
	if a == b and b == c and c == d:  # cuadrado, area
		area = a ** 2
	else:  # rectangulo, per
		area = False

# Poscondicion
assert(area == c * h / 2 or per == a + b + c or area == a ** 2 or per == a + b + c + d or area == c * h)

# Salida
if lados == 3:
	if a == b and b == c:
		print("El area del triangulo equilatero es:",area)
	if a != b and b != c and a != c:
		print("El perimetro del triangulo escaleno es:",per)
	if (a == b and c != a) or (a == c and b != a):
		print("El perimetro del triangulo isosceles es:",per)
		print("El area del triangulo isosceles es:", area)
elif lados == 4:
	if a == b and b == c and c == d:
		print("El area del cuadrado es:",area)
	else:
		print("El perimetro del rectangulo es:",per)
