#
# Adolfo Jeritson
# Return Greatest Common Divisor and Least Common Multiple using either iterative
# or recursive methods.
# 2015
#
	a = int(raw_input("Numero 1: "))
	b = int(raw_input("Numero 2: "))

	# MCD metodo iterativo
	def iMCD(a, b):
		while (a != b):
			if a > b:
				a = a - b
			else:
				b = b - a
		return a	


	# MCD metodo recursivo de euclides
	def rMCD(a, b):
		while (b > 0):
			a, b = b, a%b
	
		return a	
		
	# MCM
	mcm = (a * b) / iMCD(a, b)
		
	metodo = raw_input("Elige el metodo: recursivo o iterativo: ")
	if metodo.lower() == "iterativo":
		print "El MCD es: " + str(iMCD(a, b)) + " y el MCM es: " + str(mcm)
	elif metodo.lower() == "recursivo":
		print "El MCD es: " + str(rMCD(a, b)) + " y el MCM es: " + str(mcm)
	else:
		print "No elegiste un metodo disponible"
		calc()
		
calc()		