#
# Adolfo Jeritson. 12-10523
#
# Descripcion: Chequear si un numero es perfecto
#
# Fecha: 12/05/2015
#

# Variables
# N: int
# EsPerfecto: bool
# suma: int
# i: int
# cota: int

import sys
# Valores iniciales
N = int(input("Inserte un entero positivo para verificar si es perfecto: "))
suma = 0
i = 1
cota = N - i
 
# Precondicion
try:
	assert(N > 0)
except:
	print("Error, introduzca un entero positivo.")
	sys.exit()
	
# Verificar invariante
try: 
	assert(1<=i<=N and suma == sum(x for x in range(1,i) if (N%x == 0)))
except:
	print("Error del invariante antes del ciclo.")
	sys.exit()
# Verificar cota positiva
try:
	assert(cota >= 0)
except:
	print("Error, cota negativa antes del ciclo.")
	sys.exit()
	
# Calculos
while i < N:
    if N % i == 0:
        suma = suma + i
    i = i + 1
    
    # Verificar invariante
    try:
    	assert(1<=i<=N  and suma == sum(x for x in range(1,i) if (N%x == 0)))
    except: 
    	print("Error del invariante durante el ciclo.")
    	sys.exit()
    
    try: #Verifico cota negativa
    	assert(cota >= 0)
    except:
    	print("Error, cota negativa durante el ciclo")
    	sys.exit()
    	
    try: #Verifica cota decreciente
    	assert(cota > N - i)
    except:
    	print("Error, cota no decreciente")
 
    cota = N - i
     
EsPerfecto = suma == N
 
# Poscondicion 
try:
	assert(EsPerfecto == (N == sum(x for x in range(1,N) if (N%x == 0))))
except:
	print("Error de la poscondicion.")
	print("EsPerfecto = "+str(EsPerfecto)+" suma = "+str(suma))
	
# Salida
if EsPerfecto:
	print("El numero "+str(N)+" es perfecto.")
else:
	print("El numero "+str(N)+" NO es perfecto.")
