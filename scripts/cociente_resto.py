#
# Adolfo Jeritson
# Returns quotient and remainder form the divison of two given numbers, 
# checks the result with the euclidean ecuation
# 2015
#

def calc(a, b):
	r = a
	q = 0
	
	while r >= b:
		r = r - y
		q = q + 1
	
	# Verifico que los valores satisfacen la ecuacion de euclides
	if a == b*q + r:
		return "El cociente es " + str(q) + " y el resto es " + str(r)	
	else:
		return "Los numeros no tienen sentido logico"
		
		
x = int(input("Dame el primer numero: "))
y = int(input("Dame con quien lo quieres dividir: "))
print ("Calculando la division de " + str(x) + " entre " + str(y) + " con su cociente y resto: ")

if x >= 0 and y > 0:
	print (calc(x, y))
else:
	print ("No se puede calcular para valores dados, vuelve a intentar")
	
 

		