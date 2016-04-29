#
# DESCRIPCION: Calcular la suma de los factoriales desde 0 hasta un numero entero definido por el usuario.
#                         con verificacion de aserciones usando try/except
#
# Autor: 
#	Adolfo Jeritson. 12-10523
#   Laboratorio de Algoritmos y Estructuras 1. Seccion 2
#
# Ultima modificacion: 16/05/2015
#

# Variables:
#	N: int
# resultado: int

# Valores iniciales:
import sys

def prod(iterable):
	p = 1
	for n in iterable:
		p *= n
	return p	

# Verificacion de la Precondicion:
while True:
	try:
		N = int(input("Introduzca el numero para calcular sumatoria de factoriales: "))
		assert(N >= 0)
		break
	except:
		print("Hubo un error con el valor de N. No fue aceptado.")
		print("Intente nuevamente.")
		
def SumaFactoriales(n: int) -> int:
	# PRECONDICION: n>=0
	# POSCONDICION: SumaFactoriales == sum(prod(j for j in range(1,x+1)) for x in range(0, k)))
	# var k, suma, fact, cota : int // Variables locales de la funcion
	
	k, suma, fact = 0, 0, 1
	cota = n + 1 - k

	# Verificar cota e invariantes al iniciar:
	try:
		assert(0 <= k <= n + 1 and suma == sum(prod(j for j in range(1,x+1)) for x in range(0, k)))
	except:
		print("Hubo un error en el invariante antes de iniciar el ciclo.")
		print("Los valores del error son: k = "+str(k)+" y suma = "+str(suma))
		sys.exit()
	try:
		assert(cota >= 0)
	except:
		print("Error de cota antes de entrar al ciclo.")
		print("Cota = "+str(cota))
		sys.exit()
	
	# Ciclo
	while k <= n:
		print("k vale:", k)
		if k > 0:
			fact = fact * k
		suma = suma + fact	
		k = k + 1
	
		# Verificar invariante
		try:
			assert(0 <= k <= N + 1 and suma == sum(prod(j for j in range(1,x+1)) for x in range(0, k)))
		except:
			print("Hubo un error en el invariante durante la ejecucion del ciclo: ")
			print("k = "+str(k)+" y suma = "+str(suma))
			sys.exit()
	
		# Verificar cota decreciente	
		try:
			assert(cota > N + 1 - k)
			print("cota:",cota)
			print("----")  
		except:
			print("Error, cota no decreciente.")
			print("Cota = "+str(cota))
			sys.exit()
		
		cota = N + 1 - k 	
		
		# Verificar cota positiva
		try:
			assert(cota >= 0)
		except:
			print("Error, cota negativa.")
			print("Cota = "+str(cota))
			sys.exit()
		
	return suma	
	
# Llamada a la funcion
resultado = SumaFactoriales(N)	

# Verificar Poscondicion
try:
	assert(resultado == sum(prod(j for j in range(1,x+1)) for x in range(0, N+1)))
except:
	print("Error en la poscondicion.") 
	print("La expresion resultado == sum(prod(j for j in range(1,x+1)) for x in range(0, k))")
	print("Los valores del error son: suma = "+str(resultado)+" y el cuantificador da :"+str( sum(prod(j for j in range(1,x+1)) for x in range(0, N+1)) ))
	sys.exit()

# Salida
print("La sumatoria de factoriales desde cero a", str(N) ,"es:", str(resultado))
	
