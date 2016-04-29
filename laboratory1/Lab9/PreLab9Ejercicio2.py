#
# Adolfo Jeritson. 12-10523
#
# Descripcion: Determinar si una palabra es palindromo
#

# Analisis Descendente
def esPalindromo(word: str) -> bool:
	# PRE: len(word) >= 0
	# POS: esPalindromo == (word == word[::-1])
	# var palin: bool
	if len(word) < 2:
		palin = True
	elif word[0] == word[-1]:
		palin = esPalindromo(word[1:-1])
	else: 
		palin = False
	return palin	

# Variables
# strAChequear: str
# esPal: bool

# Valores Iniciales
print("DETERMINAR SI UNA PALABRA ES PALINDROMO.")
palabra = input("Inserte palabra para determinar si es palindromo: ")

# Precondicion
assert(len(palabra) >= 0)

# Calculos
strAChequear = palabra.lower()
esPal = esPalindromo(strAChequear)

# Poscondicion
assert(esPal == (strAChequear == strAChequear[::-1]))

#Salida
if esPal:
	print("La palabra "+palabra+" es un palindromo.")
else:
	print("La palabra "+palabra+" NO es un palindromo.")
