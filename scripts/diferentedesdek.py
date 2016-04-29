# DiferenteDesdeK

print("Inserte el arreglo a continuacion: (escriba stop para terminar)")

A = []

while True:	
	X = input("Inserte elemento: ")
	if X == 'stop':
		break
	elif int(X) in range(10000):
		A.append(int(X))
		
N = len(A)

def DiferenteDesdeK(n, a, k):
	assert(n > 0 and 0<=k<=n)
	
	dif = True
	i = k
	
	while i < n-1:
		if a[k] == a[i+1]:
			dif = False
		elif a[k] != a[i+1]:
			pass
		i = i + 1	
		
	return dif	
	
todosdif = DiferenteDesdeK(N, A, 0)		

print(todosdif)
		
