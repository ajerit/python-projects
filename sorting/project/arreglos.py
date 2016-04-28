#! /usr/bin/python
# -*- coding: utf-8 -*-
# Autores:
# Mathias San Miguel 	13-11310
# Adolfo Jeritson 		12-10523
import random

# Descripcion: Chequea si el arreglo dado esta ordenado
# Parametros: A: Un arreglo de elementos numericos
#             dataset: Tipo de arreglo a crear
# Retorna: True si esta ordenado, detiene el programa en caso contrario
def estaOrdenado(A):
    for i in range(0, len(A)-1):
        if A[i] > A[i+1]:
        	return False
    return True
    
# Descripcion: Crea el arreglo segun el dataset deseado
# Parametros: n: Numero de elementos del arreglo
#             dataset: Tipo de arreglo a crear
# Retorna: Un objeto lista con n valores, cuya composicion depende del
#           dataset elegido
def obtenerArreglo(n, dataset):
    if dataset == 1:
        # Punto flotante
        array = [random.random() for x in range(n)]
        
    elif dataset == 2:
        # Ordenado ascendentemente
        array = [random.randint(0, 1000000) for x in range(n)]
        array.sort()
        
    elif dataset == 3:
        # Ordenado descendentemente
        array = [random.randint(0, 1000000) for x in range(n)]
        array.sort(None, None, True)
        
    elif dataset == 4:
        # Cero-uno
        array = [random.randint(0, 1) for x in range(n)]
        
    elif dataset == 5:
        # Arreglo de tipo [1..n/2,n/2..1]
        half1 = [x for x in range(1, n/2 + 1)]
        half2 = [x for x in range(n/2,0, -1)]
        array = half1 + half2
        
    elif dataset == 6:
        # Casi ordenado 1: Número constante de swaps
        array = [random.randint(0, 1000000) for x in range(n)]
        array.sort()
        for x in range(16):
            i = random.randint(0, n-9)
            array[i], array[i+8] = array[i+8], array[i]
        
    elif dataset == 7:
        # Casi ordenado 2: O(n) swaps
        array = [random.randint(0, 1000000) for x in range(n)]
        array.sort()
        
        for x in range(n/4):
            i = random.randint(0, n-5)
            array[i], array[i+4] = array[i+4], array[i]
        
    else:
        print("Las opciones validas para el dataset son entre 1 y 7.")
        sys.exit()
        
    return array