#
# Lab3Ejemplo1.py
#
# DESCRIPCION: Programa que dado un número N,
# calcula la sumatoria de los números pares entre 0 y N-1. 
# Dicho sumatoria 
# es almacenada en suma.
#
# Versión de: 
#	Prof. Josué Ramírez
#
# Ultima modificacion: 20/04/2015
#
#
# CONSTANTES:
#	N: int // Límite superior del rango de enteros pares a sumar
N=10
# VARIABLES:
#	k: int // Valor que permite recorrer los enteros entre 0 y N-1
#	cota: int // Valor de la cota decreciente que permitirá que el ciclo termine
#	suma: int // Valor de la sumatoria de los enteros pares entre 0 y N-1

# Valores iniciales:
k,suma=0,0
cota = N-k

# Precondicion: 
assert(N >= 0)

# Verificacion de invariante y cota al inicio
assert( 0<=k<=N and suma == sum ( x for x in range(0,k) if (x % 2 ==0) ) )

while ( k <= N ):
   print("k vale:",k)
   if (k % 2 == 0):
      suma=suma+k 
   k=k+1

   # Verificacion de invariante y cota en cada iteracion
   assert( 0<=k<=N+1 and suma == sum ( x for x in range(0,k) if (x % 2 ==0) ) )
   assert( cota > N-k )
   print("cota:",cota)
   cota = N-k
   print("----")   

# Postcondicion: 
assert( 0<=k<=N+1 and suma == sum ( x for x in range(0,k) if (x % 2 ==0) ) )

 # Salida:
print("La sumatoria de enteros pares de cero a",N,"es:")
print(suma)