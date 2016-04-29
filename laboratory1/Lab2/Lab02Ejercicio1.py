#
# 
#
# DESCRIPCION: Determina si un anyo es bisiesto

# Autor: 
#	Adolfo Jeritson. 12-10523
#
#

# Variables
#  anyo: int
#  esBisiesto: boolean

# Valores iniciales:
anyo = int(input("Inserte anyo a revisar: "))

# Precondicion: 
assert(anyo > 0)

# Calculos:
esBisiesto = True
if anyo%4 != 0:
	esBisiesto = False
elif anyo%100 != 0 or anyo%400 == 0:
	pass
elif anyo%4 == 0 and anyo%100 == 0 and anyo%400 != 0:
	esBisiesto = False

# Postcondicion: 
assert(esBisiesto == False or esBisiesto == True)

# Salida:
print("El anyo " + str(anyo) + " es bisiesto? " + str(esBisiesto))
