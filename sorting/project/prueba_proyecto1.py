#! /usr/bin/python
# -*- coding: utf-8 -*-

# Descripcion: Proyecto 1 para el Laboratorio de Algoritmos y Estructuras 2
#     	       Genera el tiempo promedio para diferentes algoritmos de
#              ordenamiento, dados el tamaño y el tipo de elementos que
#              conformaran el arreglo a ordenar.
# 
# Febrero 2016
#
# Autores:
# Mathias San Miguel 	13-11310
# Adolfo Jeritson 		12-10523


# La sipnosis de la linea de comandos es:
#
# python prueba_proyecto1.py <numero de elementos> <dataset> <numero de pruebas>
#
# <numero de elementos> indica el numero de elementos que va a tener el arreglo
# <dataset> indica el tipo de elementos que va a tener el arreglo
# <numero de pruebas> indica cuantas veces se repetiran las pruebas

from arreglos import *
import sys, traceback, random, time, threading
from sorts import *


# Descripcion: Corre los diferentes algoritmos de ordenamiento, tomando
#               el tiempo a cada prueba para sacar su promedio
# Parametros: array: Arreglo a ordenar
#             repetir: Numero de veces a repetir la prueba de ordenamiento >= 3
#             f: Nombre de la funcion del algoritmo a utilizar
# Retorna: Tiempo promedio del algoritmo, sin tomar en cuenta ni el mejor
#           ni el peor tiempo. Es decir (tiempoTotal-minT-maxT) / (repetir-2)
# Variables: 	tiempoTotal: la sumatoria de todos los tiempos encontrados
#			 	minT: el minimo tiempo encontrado
#			 	maxT: el maximo tiempo encontrado
#			
# Pre: repetir>=1 AND f es alguno de los algoritmos a utilizar
# Post: devuelve el tiempo promedio de los obtenidos menos el mejor y peor caso
def pruebaTiempos(array, repetir, f):
    tiempoTotal = 0
    minT = 999999999
    maxT = 0

    for i in range(repetir):
        start_time = time.time()
        f(array, 0, len(array)-1)
        t_usado = time.time() - start_time
        tiempoTotal += t_usado
        maxT=max(t_usado,maxT)
        minT=min(t_usado,minT)
        print(i+1),
    
    tiempoTotal=tiempoTotal - minT - maxT
    
    return tiempoTotal / (repetir-2)


# Descripcion: Prueba los algoritmos de ordenamientos con una lista de elementos.
#
# Parametros: datos: arreglo con elementos de tipo numerico
#             pruebas: numero de veces a repetir las pruebas
# Pre: pruebas>=3
# Post: tiempos[] tiene 5 floats que son cada uno el promedio de 
#                   los tiempos obtenidos (sin el peor y mejor caso) de cada algoritmo
def probarAlgoritmos(datos, pruebas):

    tiempos = []	# Arreglo de tiempos promedio para print conjunto

    print("Comenzando pruebas con Heapsort...")
    arrayResult = list(datos)								#Copia el arreglo antes generado
    tiempo = pruebaTiempos(arrayResult, pruebas, heapsort)	#Se prueba el algoritmo y mide el tiempo
    assert(estaOrdenado(arrayResult))						#Se asegura que está ordenado
    print("...LISTO")
    tiempos.append(tiempo)									#Se anade el tiempo a tiempos
    														###Esto se repite para cada algoritmo propuesto
    
    print("Comenzando pruebas con Median-Of-3 QuickSort...")
    arrayResult = list(datos)
    tiempo = pruebaTiempos(arrayResult, pruebas, quicksort)
    assert(estaOrdenado(arrayResult))
    print("...LISTO")
    tiempos.append(tiempo)
    

    print("Comenzando pruebas con IntroSort...")
    arrayResult = list(datos)
    tiempo = pruebaTiempos(arrayResult, pruebas, introsort)
    assert(estaOrdenado(arrayResult))
    print("...LISTO")
    tiempos.append(tiempo)
    

    print("Comenzando pruebas con 3-Way Partition QuickSort...")
    arrayResult = list(datos)
    tiempo = pruebaTiempos(arrayResult, pruebas, threesort)
    assert(estaOrdenado(arrayResult))
    print("...LISTO")
    tiempos.append(tiempo)
    

    print("Comenzando pruebas con Dual Pivot QuickSort (Yaroslavskiy)...")
    arrayResult = list(datos)
    tiempo = pruebaTiempos(arrayResult, pruebas, quicksort_dual)
    assert(estaOrdenado(arrayResult))
    print("...LISTO")
    tiempos.append(tiempo)

    #Se imprimen los tiempos calculados
    print("HeapSort: \t"+str(tiempos[0]))
    print("MedianOf3: \t"+str(tiempos[1]))
    print("IntroSort: \t"+str(tiempos[2]))
    print("3WayParti: \t"+str(tiempos[3]))
    print("DualPivot: \t"+str(tiempos[4]))
    

# Descripcion: Funcion driver para usar en thread con mayor limite de stack
#
# Parametros: N: tamaño de arreglo a generar >=1
#             T: tipo de arreglo a generar <=7 y >=1
#			  M: número de pruebas a realizar >=3
# Pre: N>=1 AND 1<=T<=7 AND 3<=M
# Post: True
def driver(N,T,M):
	datos = obtenerArreglo(N, T)
	probarAlgoritmos(datos, M)


# Descripcion: Checkea input correcto del usuario
#
# Parametros: N: tamaño de arreglo a generar >=1
#             T: tipo de arreglo a generar <=7 y >=1
#			  M: número de pruebas a realizar >=3
# Pre: N>=1 AND 1<=T<=7 AND 3<=M
# Post: inp = [N, T, M] AND (N,T,M no cambian)
def parseArgs(args):
	msg = "Error en la linea de comando:\ndriver <numero de elementos> <tipo de arreglo> <numero de pruebas>"
	if len(args) != 4:
		print(msg)
		sys.exit(1)
	inp = []
	inp.append(int(args[1]))
	inp.append(int(args[2]))
	inp.append(int(args[3]))
	if(inp[0]<1):
		print("Error, se necesita un tamano positivo de arreglo")
		sys.exit()
	if(inp[1]<1 or inp[1]>7):
		print("Error, se necesita tipo de arreglo en [1..7]")
		sys.exit()
	if(inp[2]<3):
		print("Error, se necesita un minimo de 3 repeticiones")
		sys.exit()
	return inp

# Descripcion: Función main
#
# Parametros: Ninguno
if __name__ == "__main__":	
	args = parseArgs(sys.argv)
	N = int(args[0])
	T = int(args[1])
	M = int(args[2])
	sys.setrecursionlimit(N+1000)	#Aumentamos el limite de recursion
	threading.stack_size(67108864)	
	driver = threading.Thread(target=driver,args=(N,T,M)) #Creamos un thread con un stack de 64MB
	driver.start()