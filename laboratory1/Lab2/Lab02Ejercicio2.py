#
# 
#
# DESCRIPCION: Determina una persona puede votar o no

# Autor: 
#	Adolfo Jeritson. 12-10523
#
#

# Variables
# esDescendienteExtranjero: boolean
# edad: int
# puedeVotar: boolean
# extranjero: str

# Valores iniciales
edad = int(input("Introduzca edad: "))
extranjero = input("Es descendiente extranjero? (Responda True o False): ")

if extranjero.lower() == "true":
	esDescendienteExtranjero = True
elif extranjero.lower() == "false":
	esDescendienteExtranjero = False
else:
	print("No respondio True o False. Vuelva a intentar")
	esDescendienteExtranjero = ""

# Precondicion
assert(0 < edad < 120 and (esDescendienteExtranjero == True or esDescendienteExtranjero == False))

# Calculos
puedeVotar = True

if esDescendienteExtranjero:
	if edad >= 25:
		pass
	elif edad < 25:
		puedeVotar = False
elif not esDescendienteExtranjero:
	if edad >= 18:
		pass
	elif edad < 18:
		puedeVotar = False
		
# Poscondicion
assert(puedeVotar == False or puedeVotar == True)

# Salida
print("El ciudadano puede votar? " + str(puedeVotar))
