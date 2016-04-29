# -*- coding: utf-8 -*-
#
# Adolfo Jeritson. 12-10523
# 23/05/2015
#
# Descripcion: Lee un archivo input.txt donde interpreta una secuencia
# factorizada y devuelve la secuencia completa.
#
import sys

# Analisis Descendente
def leer_archivo(path: str) -> [str]:
	# PRECONDICION  isinstance(path, str)
	# POSCONDICION adnlist == [line.rstrip('\n') for line in open(path)]
	# var adnlist: array of str
	# var lines: array of str
	with open(path, 'r') as f:
		lines = f.readlines()
	f.closed
	adnlist = [line.rstrip('\n') for line in lines]
	return adnlist

def es_erronea(linea: str) -> bool:
	# PRECONDICION isinstance(linea, str)
	# POSCONDICION es_erronea == ((int(linea.split(maxsplit=1)[0]) <= 0) or
	# 		(any(ch!='A' and ch!='T' and ch!='G' and ch!='C' for ch in 
	#		linea.split(maxsplit=1)[1])) or (
	#		len(int(linea.split(maxsplit=1)[0])*
	#		(linea.split(maxsplit=1)[1])) > 50))
			
	return ((int(linea.split(maxsplit=1)[0]) <= 0) or (any(ch!='A' and 
				ch!='T' and ch!='G' and ch!='C' for ch in 
				linea.split(maxsplit=1)[1])) or (
				len(int(linea.split(maxsplit=1)[0])*
				(linea.split(maxsplit=1)[1])) > 50))

def desfactorizar(linea: str) -> str:
	# PRECONDICION isinstance(linea, str)
	# POSCONDICION desfactorizar == int(linea.split(maxsplit=1)[0])*
	#													(linea.split(maxsplit=1)[1])
	return int(linea.split(maxsplit=1)[0])*(linea.split(maxsplit=1)[1])
			
def procesar_adn(adn: [str]) -> [str]:
	# PRECONDICION isinstance(adn, list):
	# POSCONDICION procesar_adn = ["Línea errónea." if es_erronea(x) else 
	#														desfactorizar(x) for x in adn]
	# var final: array of str
	# var cota: int
	# var k: int
	final = []
	k = 0
	cota = len(adn) - k
	
	# Invariante antes del ciclo
	assert(final == ["Línea errónea." if es_erronea(x) else desfactorizar(x) 
				for x in adn[:k]])
	# Cota antes del ciclo
	assert(cota >= 0)
				
	for item in adn:
		if es_erronea(item):
			final.append("Línea errónea.")
		else:
			final.append(desfactorizar(item))
		k = k + 1	
		
		# Invariante durante el ciclo
		assert(final == ["Línea errónea." if es_erronea(x) else desfactorizar(x) 
					for x in adn[:k]])
		# Cota decreciente despues del ciclo
		assert(cota > len(adn) - k)
		cota = len(adn) - k
		# Cota positiva despues del ciclo
		assert(cota >= 0)
		
	return final		

def guardar_salida(lista: [str], path: str) -> 'void':
	# PRECONDICION isinstance(path, str) and isinstance(lista, list)
	# POSCONDICION f.closed
	with open(path, 'w') as f:
		f.write("\n".join(lista))
	f.closed

def imprimir_salida(path: str) -> 'void':
	# PRECONDICION isinstance(path, str)
	# POSCONDICION f.closed
	with open(path, 'r') as f:
		for line in f:
			print(line, end="")
	f.closed

# Variables
# adn: array of str
# adnpro: array of str
# entrada: str
# salida: str

# Valores iniciales:
entrada = 'input.txt'
salida = 'output.txt'

# Precondicion
try:
	assert(all(int(item.split(maxsplit=1)[0]) > 0 for item in 
				[line.rstrip('\n') for line in open(entrada)]))
	assert(all(len(int(item.split(maxsplit=1)[0])*(item.split(maxsplit=1)[1])) <= 
				50 for item in [line.rstrip('\n') for line in open(entrada)]))
except:
	print("*****")
	print("Se encontraron errores en los datos de entrada del ADN.")
	print("Se va a procesar el ADN y las líneas donde se encontraron errores")
	print("serán identificadas como 'Línea errónea.'")
	print("*****")
	
# Calculos
adnfact = leer_archivo(entrada)
adnpro = procesar_adn(adnfact)
guardar_salida(adnpro, salida)

# Poscondicion:
try: 
	assert(adnpro == ["Línea errónea." if es_erronea(x) else desfactorizar(x) 
				for x in leer_archivo(entrada)])
except:
	print("Error al procesar el ADN.")
	print("La lista del input es: ")
	print(adn)
	print("La lista del ADN procesado es: ")
	print(adnpro)
	sys.exit()
	
# Salida
imprimir_salida(salida)
print("")

