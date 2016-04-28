#! /usr/bin/python
# -*- coding: utf-8 -*-
# Autores:
# Mathias San Miguel 	13-11310
# Adolfo Jeritson 		12-10523

limite = 15 #tamano (dado) minimo de subarreglo para ordenar con otro algoritmo diferente a insertionsort

############
#
# HeapSort 
#
############

# Parametros: seq: Arreglo que representa un cuasi-heap
#             i: elemento a arreglar (para volver seq[i..hasta] un heap)
#             hasta: limite derecho del heap
# Retorna: 		Nada
# Pre: Hijo derecho de i es un heap ADN Hijo izquierdo de i es un heap AND seq tiene posición i y pos hasta
# Post: árbol binario con raíz en i es un heap
def heapfy(seq, i, hasta):
	while(i*2 <= hasta):
		if(i*2+1<=hasta):
			if  (seq[i] < seq[i*2+1] and seq[i*2] <= seq[i*2+1]):
				seq[i],seq[i*2 + 1] = seq[i*2+1],seq[i]
				i=i*2+1
			elif(seq[i] < seq[i*2] and seq[i*2 +1] <= seq[i*2]):
				seq[i],seq[i*2] = seq[i*2],seq[i]
				i=i*2
			else :
				break
		else:
			if  (seq[i] < seq[i*2]):
				seq[i],seq[i*2] = seq[i*2],seq[i]
				i=i*2
			else :
				break

# Parametros: seq: Arreglo a ordenar de manera que represente un heap, usando heapify
#             [a..b] subarreglo a ordenar
# Retorna: 		Nada
# Pre: a y b son indices de seq.
# Post: seq es un heap
def buildHeap(seq, a, b):
	for i in range(b,a-1,-1):
		heapfy(seq, i, b)

# Parametros: seq: Arreglo a ordenar con HeapSort, usando buildHeap y heapify
#             [a..b] subarreglo a ordenar
# Retorna: 		Nada
# Pre: a y b son indices de seq
# Post: seq esta ordenado
def heapsort(seq, a, b):
	buildHeap(seq, a, b)
	tam = b-a
	for i in range(a,b+1):
		seq[a],seq[a+tam] = seq[a+tam],seq[a]
		tam-=1
		heapfy(seq, a, a+tam)

############
#
# InsertionSort
#
############

# Parametros: seq: Arreglo a ordenar con insertion-sort
#             [a..b] subarreglo a ordenar
# Retorna: 		Nada
# Pre: a y b son indices de seq
# Post: seq esta ordenado
def insertionsort(seq, a, b):
    for i in range(a+1, b+1):
        x = seq[i]
        j = i-1
        while(j>=a and seq[j]>x):
            seq[j+1] = seq[j]
            j-=1
        seq[j+1] = x


############
#
# QuickSort : Median-of-3
#
############

# Parametros: a, b, c enteros
# Retorna: 		la mediana de a, b y c
# Pre: True
# Post: retorna x tal que x==a OR x==b OR x==c
#				y x es la mediana de esos tres
def med3(a,b,c):
	if(a>=b):
		if(c>=a):
			return a
		elif(c>=b):
			return c
		else:
			return b
	else:
		if(c>=b):
			return b
		elif(c>=a):
			return c
		else:
			return a

# Parametros: A: Arreglo a particionar
#             [f..b] subarreglo a considerar
# Retorna: 		indice de la posicion final del pivote
# Pre: l y r son indices de seq
# Post: Si i<=j entonces A[i]<=A[j+1] AND Si i>=j entonces A[i]>=A[j+1]
def partition(A, l, r):
	x=A[l]
	i = l
	j = r
	while(i<=j):
		while(A[i]<x and i<=j): i+=1
		while(A[j]>=x and i<=j): j-=1
		A[i],A[j]=A[j],A[i]
	A[i],A[j]=A[j],A[i]
	A[l],A[j]=A[j],A[l]
	#print(A)
	return j+1

# Parametros: A: Arreglo a ordenar con Quicksort, usando el partition de arriba
#             [f..b] subarreglo a ordenar
# Retorna: 		Nada
# Pre: f y b son indices de A
# Post: Para todo A[i] con f<=i<=f, A[i] esta a como mucho limite posiciones de 
#					su posicion correcta si A[f..b] estuviese ordenado
def quicksort_loop(A,f,b):
	while(b - f + 1 > limite):
		if(A[f]>=A[(b+f)//2]):
			if(A[b]>=A[f]):
				pass
			elif(A[b]>=A[(b+f)//2]):
				A[f],A[b]=A[b],A[f]
			else:
				A[f],A[(b+f)//2]=A[(b+f)//2],A[f]
		else:
			if(A[b]>=A[(b+f)//2]):
				A[f],A[(b+f)//2]=A[(b+f)//2],A[f]
			elif(A[b]>=A[0]):
				A[f],A[b]=A[b],A[f]
			else:
				pass
		p = partition(A,f,b)
		if(p-f>=b-p):
			quicksort_loop(A,p+1,b)
			b=p
		else:
			quicksort_loop(A,f,p)
			f=p+1
	

# Parametros: A: Arreglo a ordenar con Quicksort, usando el quicksort_loop de arriba, insertionsort cuando el subarreglo sea pequeno
#             [f..b] subarreglo a ordenar
# Retorna: 		Nada
# Pre: f y b son indices de A
# Post: A esta ordenado
def quicksort(A,f,b):
	quicksort_loop(A,f,b)
	insertionsort(A,f,b)

############
#
# QuickSort : IntroSort
#
############

# Parametros: A: Arreglo a ordenar con IntroSort, 
#							heapsort al alcanzar cota de recursion
#             [f..b] subarreglo a ordenar
#			  depth_lim: limite de profundidad de la recursion
# Retorna: 		Nada
# Pre: f y b son indices de A AND depth_lim>=1
# Post: Para todo A[i] con f<=i<=f, A[i] esta a como mucho limite posiciones de 
#					su posicion correcta si A[f..b] estuviese ordenado
def introsort_loop(A,f,b,depth_lim):
	while(b - f + 1 > limite):
		if(depth_lim<=0):
			heapsort(A,f,b)
			return

		if(A[f]>=A[(b+f)//2]):
			if(A[b]>=A[f]):
				pass
			elif(A[b]>=A[(b+f)//2]):
				A[f],A[b]=A[b],A[f]
			else:
				A[f],A[(b+f)//2]=A[(b+f)//2],A[f]
		else:
			if(A[b]>=A[(b+f)//2]):
				A[f],A[(b+f)//2]=A[(b+f)//2],A[f]
			elif(A[b]>=A[0]):
				A[f],A[b]=A[b],A[f]

		depth_lim-=1
		p = partition(A,f,b)
		introsort_loop(A,f,p,depth_lim)
		f=p+1

from math import log
# Parametros: A: Arreglo a ordenar con IntroSort, usando el loop de arriba, 
#							insertionsort cuando subarreglos sean pequenos
# 							y 2*log(b-f+1) como cota de recursion
#             [f..b] subarreglo a ordenar
# Retorna: 		Nada
# Pre: f y b son indices de A
# Post: A esta ordenado
def introsort(A,f,b):
	introsort_loop(A,f,b, 2*int(log(b-f+1)))
	insertionsort(A,f,b)

############
#
# QuickSort : 3-Way
#
############

# Parametros: A: Arreglo a ordenar con 3-Way Partitioning QuickSort
#             [l..r] subarreglo a ordenar
# Retorna: 		Nada
# Pre: l y r son indices de A
# Post: A esta ordenado
def threesort_loop(A,l,r):
	if r<=l: return
	if r-l+1<=15:
		insertionsort(A,l,r)
		pass
	else:
		i, j, p, q, v  =  l-1, r, l-1, r, A[r]
		if(r>l):
			while(True):

				while(True):
					i+=1
					if A[i]>=v: 	break
				while(True):
					j-=1
					if v>=A[j] or j==l: 	break

				if(i>=j):	break

				A[i],A[j]=A[j],A[i]

				if(A[i]==v):
					p+=1
					A[p],A[i]=A[i],A[p]

				if(v==A[j]):
					q-=1
					A[j],A[q]=A[q],A[j]

			A[i],A[r]=A[r],A[i]
			j=i-1
			i=i+1
			for k in range(l,p):
				A[k],A[j]=A[j],A[k]
				j-=1
			for k in range(r-1,q,-1):
				A[k],A[i]=A[i],A[k]
				i+=1
			threesort_loop(A,l,j)
			threesort_loop(A,i,r)

# Parametros: A: Arreglo a ordenar con 3-Way Partitioning QuickSort,
# 				usando threesort_loop, insertion sort para subarreglos pequenos
#             [l..r] subarreglo a ordenar
# Retorna: 		Nada
# Pre: f y b son indices de A
# Post: A esta ordenado
def threesort(A,f,b):
	threesort_loop(A,f,b)
	insertionsort(A,f,b)


############
#
# QuickSort : Yaroslavsky
#
############

# Parametros: A: Arreglo a ordenar con Yaroslavskiy's QuickSort
#             [left..right] subarreglo a ordenar
# Retorna: 		Nada
# Pre: left y right son indices de A
# Post: A esta ordenado
def quicksort_dual(A,left,right):
	if(right-left+1 <= limite):
		insertionsort(A,left,right)
	else:
		if(A[left]>A[right]):
			p,q=A[right],A[left]
		else:
			p,q=A[left],A[right]

		l=left+1
		g=right-1
		k=l
		while(k<=g):
			if(A[k]<p):
				A[k],A[l]=A[l],A[k]
				l+=1
			else:
				if(A[k]>=q):
					while(A[g]>q and k<g):
						g-=1
					if(A[g]>=p):
						A[k],A[g]=A[g],A[k]
					else:
						A[k],A[g]=A[g],A[k]
						A[k],A[l]=A[l],A[k]
						l+=1
					g-=1
			k+=1
		l-=1
		g+=1
		A[left]=A[l]
		A[l]=p
		A[right]=A[g]
		A[g]=q
		quicksort_dual(A,left,l-1)
		quicksort_dual(A,l+1,g-1)
		quicksort_dual(A,g+1,right)
