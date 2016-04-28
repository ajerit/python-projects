# Adolfo Jeritson. 2015
# Returns the area of a circle

r = (int(input("Diga el radio de la circunferencia: ")))

def area(n):
	pi = 3.14159
	return pi * (n **2)
	
if r>0:
	print("El area de la circunferencia es: " + str(area(r))

else:
	print("El radio debe ser un valor positivo.")

	