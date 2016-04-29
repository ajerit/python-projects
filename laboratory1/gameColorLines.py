# -*- coding: utf-8 -*-
# 
# Adolfo Jeritson 12-10523
# Luis Carlos Marval 12-10620
#
# Laboratorio de Algoritmos y Estructuras I
# Proyecto: Lineas de colores y Rectangulos
#

import pygame, random

# ANALISIS DESCENDENTE
def InicializarGraficos(panel:'Pantalla', fondo: (int), negro: (int), 
						ancho: int, alto: int) -> 'void':
	# Asignamos los valores iniciales para la parte grafica del juego y
	# muestra los graficos al usuario.
	
	# PRECONDICION 
	assert(not FinDeJuego)
	
	# var fontObj: object
	# var X, Y: int
	# var text1SurfaceObj,text1RectObj, text2SurfaceObj, text2RectObj,
	# coordsxSurfaceObj, coordsxRectObj, coordsy0SurfaceObj, coordsy1SurfaceObj,
	# coordsy2SurfaceObj, coordsy3SurfaceObj, coordsy4SurfaceObj, 
	# coordsy5SurfaceObj, coordsy6SurfaceObj, coordsy7SurfaceObj,
	# coordsy8SurfaceObj, coordsy0RectObj, coordsy1RectObj, coordsy2RectObj,
	# coordsy3RectObj, coordsy4RectObj, coordsy5RectObj, coordsy6RectObj,
	# coordsy7RectObj, coordsy8RectObj: object
	
	# Titulo y fondo de la ventana del juego
	pygame.display.set_caption('Líneas de Colores y Rectángulos')
	panel.fill(fondo)

	# Codigo para crear los diferentes textos
	fontObj = pygame.font.Font('freesansbold.ttf', 20)
	text1SurfaceObj = fontObj.render('Puntaje: ' + str(puntaje), True, 
										negro)
	text1RectObj = text1SurfaceObj.get_rect()
	text1RectObj.center = (375, 50)

	text2SurfaceObj = fontObj.render('Próximos: ', True, negro)
	text2RectObj = text2SurfaceObj.get_rect()
	text2RectObj.center = (85, 75)

	coordsxSurfaceObj = fontObj.render('0     1     2     3     4     5     6     7     8', 
										True, negro)
	coordsxRectObj = coordsxSurfaceObj.get_rect()
	coordsxRectObj.center = (245, 120)

	coordsy0SurfaceObj = fontObj.render('0', True, negro)
	coordsy0RectObj = coordsy0SurfaceObj.get_rect()
	coordsy0RectObj.center = (45, 155)

	coordsy1SurfaceObj = fontObj.render('1', True, negro)
	coordsy1RectObj = coordsy1SurfaceObj.get_rect()
	coordsy1RectObj.center = (45, 195)

	coordsy2SurfaceObj = fontObj.render('2', True, negro)
	coordsy2RectObj = coordsy2SurfaceObj.get_rect()
	coordsy2RectObj.center = (45, 235)

	coordsy3SurfaceObj = fontObj.render('3', True, negro)
	coordsy3RectObj = coordsy3SurfaceObj.get_rect()
	coordsy3RectObj.center = (45, 275)

	coordsy4SurfaceObj = fontObj.render('4', True, negro)
	coordsy4RectObj = coordsy4SurfaceObj.get_rect()
	coordsy4RectObj.center = (45, 315)

	coordsy5SurfaceObj = fontObj.render('5', True, negro)
	coordsy5RectObj = coordsy5SurfaceObj.get_rect()
	coordsy5RectObj.center = (45, 355)

	coordsy6SurfaceObj = fontObj.render('6', True, negro)
	coordsy6RectObj = coordsy6SurfaceObj.get_rect()
	coordsy6RectObj.center = (45, 395)

	coordsy7SurfaceObj = fontObj.render('7', True, negro)
	coordsy7RectObj = coordsy7SurfaceObj.get_rect()
	coordsy7RectObj.center = (45, 435)

	coordsy8SurfaceObj = fontObj.render('8', True, negro)
	coordsy8RectObj = coordsy8SurfaceObj.get_rect()
	coordsy8RectObj.center = (45, 475)
	
	# Codigo para mostrar los textos
	panel.blit(text1SurfaceObj, text1RectObj)
	panel.blit(text2SurfaceObj, text2RectObj)
	panel.blit(coordsxSurfaceObj, coordsxRectObj)
	panel.blit(coordsy0SurfaceObj, coordsy0RectObj)
	panel.blit(coordsy1SurfaceObj, coordsy1RectObj)
	panel.blit(coordsy2SurfaceObj, coordsy2RectObj)
	panel.blit(coordsy3SurfaceObj, coordsy3RectObj)
	panel.blit(coordsy4SurfaceObj, coordsy4RectObj)
	panel.blit(coordsy5SurfaceObj, coordsy5RectObj)
	panel.blit(coordsy6SurfaceObj, coordsy6RectObj)
	panel.blit(coordsy7SurfaceObj, coordsy7RectObj)
	panel.blit(coordsy8SurfaceObj, coordsy8RectObj)
	
	# Creamos el tablero grafico del juego	
	pygame.draw.rect(panel, negro, (65, 135, ancho, alto), 3)
	
	# Ubicacion de la esquina superior izquierda del tablero en pixeles
	X = 65
	Y = 135
	
	# Lineas verticales del tablero
	# Cota: 8 - i
	for i in range(8):
		X = X + 40
		pygame.draw.line(panel, negro, [X,135],[X,495],3)
		
	# Lineas horizontales del tablero
	# Cota 8 - i		
	for i in range(8):
		Y = Y + 40
		pygame.draw.line(panel, negro, [65,Y],[425,Y],3)
		
	print("BIENVENIDO AL JUEGO LÍNEAS DE COLORES Y RECTÁNGULOS")
	print("---------------------------------------------------")
	
	# POSCONDICION 
	assert(not FinDeJuego)

def InicializarTablero(panel:'Pantalla', board:[[int]], caja:int) -> 'void':
	# Elegir 3 objetos al azar y los añadimos al tablero antes del primer
	# turno.
	# PRECONDICION 
	assert(all(board[x][y] == 0 for x in range(9) for y in range(9)))
	
	# var nuevoObj, posx, posy: int
	for i in range(3):
		nuevoObj = random.randint(1,7)
		posx, posy = PosAleatorias(board)
		board[posx][posy] = nuevoObj
		DibujarObjeto(panel, nuevoObj, posx, posy, caja)
	
	# POSCONDICION 
	assert(any(board[x][y] != 0 for x in range(9) for y in range(9)))

def ObtenerProxObjetos(panel:'Pantalla', board: [int], caja: int) -> [int]:
	# Funcion para obtener los 3 elementos que seran añadidos al tablero
	# si el usuario no logro eliminar nada en su turno
	# PRECONDICION 
	assert(any(board[x][y] != 0 for x in range(9) for y in range(9)))
	
	# var prox: [int]
	# var px: int
	# var nuevo: int
	
	prox = [random.randint(1,7), random.randint(1,7)]
	
	# Hacemos el conteo de cada tipo de elemento para obtener el tercero
	cont1 = sum(1 for x in range(9) for y in range(9) if board[x][y] == 1)
	cont2 = sum(1 for x in range(9) for y in range(9) if board[x][y] == 2)
	cont3 = sum(1 for x in range(9) for y in range(9) if board[x][y] == 3)
	cont4 = sum(1 for x in range(9) for y in range(9) if board[x][y] == 4)
	cont5 = sum(1 for x in range(9) for y in range(9) if board[x][y] == 5)
	cont6 = sum(1 for x in range(9) for y in range(9) if board[x][y] == 6)
	cont7 = sum(1 for x in range(9) for y in range(9) if board[x][y] == 7)
		
	nuevo = min(cont1, cont2, cont3, cont4, cont5, cont6, cont7)
	
	# Dependiendo de cual es el que menos tiene, decidimos cual agregar
	if nuevo == cont1:
		prox.append(1)
	elif nuevo == cont2:
		prox.append(2)
	elif nuevo == cont3:
		prox.append(3)
	elif nuevo == cont4:
		prox.append(4)
	elif nuevo == cont5:
		prox.append(5)
	elif nuevo == cont6:
		prox.append(6)
	elif nuevo == cont7:
		prox.append(7)
		
	px = 1
	# Cota: len(prox) - x
	for x in range(len(prox)):
		# Invariante: px == sum(i for i in range(1, x)
		px = px + 1
		DibujarObjeto(panel, prox[x], px, -2, caja)
	return prox
	
	# POSCONDICION 
	assert(True)

def ObtenerJugada(board:[[int]]) -> [int]:
	# Se le pide al usuario ingresar una jugada y revisa si es valida.
	# PRECONDICION: 
	assert(not FinDeJuego)
	
	# var mov: array[0,4) of int
	while True:
		print("INTRODUZCA SU JUGADA: ")
		print("-----------------------------------")
		print("(Recuerde que las coordenadas X son las horizontales y ")
		print("que las coordenadas Y son las verticales)")
		print("-----------------------------------")
		mov = []
		
		# Pedimos la jugada al usuario usando try/except para controlar
		# que si comete algun error pueda volver a intentarlo
		try:
			mov.append(int(input("Posición X del objeto >> ")))
			mov.append(int(input("Posición Y del objeto >> ")))
			mov.append(int(input("Posición X nueva del objeto >> ")))
			mov.append(int(input("Posición Y nueva del objeto >> ")))
			print("-----------------------------------")
			if ValidarJugada(board, mov):
				print(" >> ¡Jugada válida!")
				print("-----------------------------------")
				break
			else: 
				print(" >> Jugada inválida.")
				print(" >> Por favor vuelva a intentar con una jugada válida.")
				print(" >> Debe elegir una casilla con un objeto,")
				print("    y la casilla de destino debe estar vacía.")
				print("-----------------------------------")
				print(" >> Recuerde también que debe tener al menos un")
				print("    cuadro a su alrededor vacío.")
				print("-----------------------------------")
		except ValueError:
			print("-----------------------------------")
			print(" >> Error con la entrada de valores.")
			print(" >> Las posiciones deben ser números válidos.")
			print(" >> Vuelva a intentarlo.")
			print("-----------------------------------")
	return mov
	
	# POSCONDICION: 
	assert(ValidarJugada(board, mov))
	
def ValidarJugada(board:[[int]], mov:[int]) -> bool:
	# Chequemos si una jugada hecha es correcta. Da false en caso contrario
	# PRECONDICION: 
	assert(not FinDeJuego)
	
	# var valida: bool
	# var x, y, x2, y2: int
	valida = True
	x, y, x2, y2 = mov[0], mov[1], mov[2], mov[3]
	
	# Chequeamos que las coordenadas sean correctas (dentro del tablero)
	if any(mov[i] > 8 for i in range(4)):
		valida = False
	# Luego vemos que no estemos moviendo algo vacio hacia algo ocupado
	elif (board[x][y] == 0) or (board[x2][y2] != 0):
			valida = False
	
	# Revisamos que se cumpla la condicion de que debe tener algun espacio
	# vacio alrededor, tomando en cuenta distintos casos: (esquinas, filas
	# y columnas limite y luego caso general)
	elif x == 0:
		if y == 0:
			if (board[x][y+1] != 0 and board[x+1][y] != 0 and 
				board[x+1][y+1] != 0):
				valida = False
		if y == 8:
			if (board[x][y-1] != 0 and board[x+1][y-1] != 0 and 
				board[x+1][y+1] != 0):
				valida = False
		if y != 0 and y != 8:
			if (board[x][y-1] != 0 and board[x+1][y-1] != 0 and 
				board[x+1][y] != 0 and board[x+1][y+1] != 0 and 
				board[x][y+1] != 0):
				valida = False
				
	elif x == 8:
		if y == 0:
			if (board[x-1][y] != 0 and board[x-1][y+1] != 0 and 
				board[x][y+1] != 0):
				valida = False
		if y == 8:
			if (board[x][y-1] != 0 and board[x-1][y] != 0 and 
				board[x-1][y-1] != 0):
				valida = False
		if y != 0 and y != 8:
			if (board[x][y-1] != 0 and board[x-1][y-1] != 0 and 
				board[x-1][y] != 0 and board[x-1][y+1] != 0 and 
				board[x][y+1] != 0):
				valida = False
	
	elif y == 0:
		if x != 0 and x != 8:
			if (board[x-1][y] != 0 and board[x-1][y+1] != 0 and 
				board[x][y+1] != 0 and board[x+1][y+1] != 0 and 
				board[x+1][y] != 0):
				valida = False
				
	elif y == 8:
		if x != 0 and x != 8:
			if (board[x-1][y] != 0 and board[x-1][y-1] != 0 and 
				board[x][y-1] != 0 and board[x+1][y-1] != 0 and
				board[x-1][y] != 0):
				valida = False
				
	# Caso general
	elif x != 0 and y != 0 and x != 8 and y != 0:
		if (board[x-1][y-1] != 0 and board[x][y-1] != 0 and 
		board[x+1][y-1] != 0 and board[x-1][y] != 0 and 
		board[x-1][y] != 0 and board[x+1][y] != 0 and 
		board[x-1][y+1] != 0 and board[x][y+1] != 0 and 
		board[x+1][y+1] != 0):
			valida = False
 				
	# POSCONDICION: Coordenadas mayores a 8 dan False, si la casilla
	#				elegida esta vacia o la de destino esta llena, 
	#				tambien retorna False.
	return valida
	
def MoverObjeto(panel:'Pantalla', board: [[int]], mov: [int], caja: int) -> 'void':
	# Dada una jugada valida por el usuario, se efectua dicha jugada
	# PRECONDICION: 
	assert(ValidarJugada(board, mov))
	
	# var ObjAMover, x, y, x2, y2: int
	
	x, y, x2, y2 = mov[0], mov[1], mov[2], mov[3]
	# Obtenemos el tipo del objeto a mover
	ObjAMover = board[x][y]
	# Le asignamos vacio a la posicion vieja
	board[x][y] = 0
	# Asignamos el objeto a la nueva posicion
	board[x2][y2] = ObjAMover
	# "Borramos" el grafico del objeto de la posicion vieja
	# y lo dibujamos en la nueva
	DibujarObjeto(panel, 0, x, y, caja)
	DibujarObjeto(panel, ObjAMover, x2, y2, caja)
	
	# POSCONDICION: 
	assert(board[mov[0]][mov[1]] == 0 and board[mov[2]][mov[3]] != 0)	
		
def PosAleatorias(board:[[int]]) -> int:
	# Obtener una posicion aleatoria libre del tablero
	# PRECONDICION 
	assert(True)
	
	x = random.randint(0,8)
	y = random.randint(0,8)
	
	# Chequeamos que la posicion generada esta libre,
	# si no, generamos otra posicion hasta sea una libre.
	while board[x][y] != 0:
		# Invariante: board[x][y] es una posicion valida del tablero
		# Si el tablero ya esta lleno salimos del ciclo ya que no
		# tiene sentido seguir buscando.
		
		if all(board[x][y] != 0 for x in range(9) for y in range(9)):
			break
		x = random.randint(0,8)
		y = random.randint(0,8)
		
	# POSCONDICION 
	assert(True)
		
	return x, y
	
def EsqIzqEnPix(x:int , y:int, caja: int) -> (int):
	# Recibe coordenadas cartesianas y regresa coord en pixeles de la caja.
	# Especificamente da la ubicacion de la esquina izquierda de la caja
	# en las coordenadas cartesianas dadas.
	# PRECONDICION 
	assert(True)

	# var izq, tope: int
	izq = x * (caja) + 65
	tope = y * (caja) + 135
	return (izq, tope)
    
    # POSCONDICION  
	assert((izq == x * (caja) + 65) and (tope == y * (caja) + 135))

def DibujarObjeto(panel:'Pantalla', numObj: int, x:int, y:int, caja: int) -> 'void':
	# Funcion para dibujar los diferentes objetos del juego segun se
	# requiera.
	# PRECONDICION 
	assert(0<=numObj<=7)
	
	# var izq, tope: int
	izq, tope = EsqIzqEnPix(x, y, caja) # Convertimos coordenadas a pixeles
	
	# Dibujamos los objetos segun figura y color
	# 0 es un espacio en blanco, 1 es el cuadro, 2 a 7 son las bolas
	if numObj > 1:
		pygame.draw.circle(panel, figurasJuego[numObj][1], (izq+int(caja * 
							0.5), tope+int(caja * 0.5)), int(caja * 0.5)-5)
	elif numObj == 1:
		pygame.draw.rect(panel, figurasJuego[numObj][1], (izq+3, tope+3, 
							caja-5, caja-5))
	elif numObj == 0:
		pygame.draw.rect(panel, figurasJuego[numObj][1], (izq+3, tope+3, 
							caja-5, caja-5))
	
	# POSCONDICION 
	assert(True)

def AgregarProxObjetos(panel: 'Pantalla', board: [[int]], prox: [int], caja: int) -> 'void':
	# Funcion que añade los proximos objetos luego de que el usuario
	# no lograra eliminar nada en su turno
	# var x, y, px: int
	
	# PRECONDICION 
	assert(NoSeEliminoObjeto(tablero, objAntes))
	
	# Añadimos los objetos al tablero usando un ciclo for
	# Cota 3 - i
	for i in range(len(prox)):
		x, y = PosAleatorias(board)
		board[x][y] = prox[i]
		DibujarObjeto(panel, prox[i], x, y, caja)
	
	# "Borramos" los objetos ya agregados poniendo encima espacios vacios
	px = 1
	# Cota 3 - i
	for x in range(3):
		px = px + 1
		DibujarObjeto(panel, 0, px, -2, caja)
	
	# POSCONDICION 
	assert(True)

def DeterminarFinDeJuego(board: [[int]]) -> 'bool':
	# Determinar si todo el tablero esta lleno y terminar el juego.
	# var fin: bool
	
	# PRECONDICION 
	assert(True)
	
	fin = all(board[x][y] != 0 for x in range(9) for y in range(9))
	
	# POSCONDICION 
	assert(fin == all(board[x][y] != 0 for x in range(9) for y in range(9)))

	return fin

def ProcesarCirculos(panel: 'Pantalla', board: [[int]], caja: int) -> 'void':
	# Funcion que revisa si existen lineas horizontales, verticales o diagonales de
	# al menos 5 circulos del mismo color.
	# var x, y: int
	
	# PRECONDICION
	assert(not FinDeJuego)
	
	# Revisamos las coordenadas horizontales de una linea de 9
	for x in range(1):
		for y in range(9):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if (board[x][y] == k and board[x+1][y] == k and board[x+2][y] == k and board[x+3][y] == k and 
				board[x+4][y] == k and board[x+5][y] == k and board[x+6][y] == k and board[x+7][y] == k and
				board [x+8][y] == k):
					# Eliminamos las figuras del tablero
					for i in range(x, x+9):
						DibujarObjeto(panel, 0, i, y, caja)
						board[i][y] = 0
	
	# Revisamos las coordenadas horizontales de una linea de 8
	for x in range(2):
		for y in range(9):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if (board[x][y] == k and board[x+1][y] == k and board[x+2][y] == k and board[x+3][y] == k and 
				board[x+4][y] == k and board[x+5][y] == k and board[x+6][y] == k and board[x+7][y] == k):
					# Eliminamos las figuras del tablero
					for i in range(x, x+8):
						DibujarObjeto(panel, 0, i, y, caja)
						board[i][y] = 0
	
	# Revisamos las coordenadas horizontales de una linea de 7
	for x in range(3):
		for y in range(9):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if (board[x][y] == k and board[x+1][y] == k and board[x+2][y] == k and board[x+3][y] == k and 
				board[x+4][y] == k and board[x+5][y] == k and board[x+6][y] == k):
					# Eliminamos las figuras del tablero
					for i in range(x, x+7):
						DibujarObjeto(panel, 0, i, y, caja)
						board[i][y] = 0
	
	# Revisamos las coordenadas horizontales de una linea de 6
	for x in range(4):
		for y in range(9):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if (board[x][y] == k and board[x+1][y] == k and board[x+2][y] == k and board[x+3][y] == k and 
				board[x+4][y] == k and board[x+5][y] == k):
					# Eliminamos las figuras del tablero
					for i in range(x, x+6):
						DibujarObjeto(panel, 0, i, y, caja)
						board[i][y] = 0
	
	# Revisamos las coordenadas horizontales de una línea de 5
	for x in range(5):
		for y in range(9):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if board[x][y] == k and board[x+1][y] == k and board[x+2][y] == k and board[x+3][y] == k and board[x+4][y] == k:
					# Eliminamos las figuras del tablero
					for i in range(x, x+5):
						DibujarObjeto(panel, 0, i, y, caja)
						board[i][y] = 0
	
	# Revisamos las coordenadas verticales de una línea de 9
	for x in range(9):
		for y in range(1):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if (board[x][y] == k and board[x][y+1] == k and board[x][y+2] == k and board[x][y+3] == k and 
				board[x][y+4] == k and board[x][y+5] == k and board[x][y+6] == k and board[x][y+7] == k and
				board[x][y+8] == k):
					# Eliminamos las figuras del tablero
					for i in range(y, y+9):
						DibujarObjeto(panel, 0, x, i, caja)
						board[x][i] = 0
						
	# Revisamos las coordenadas verticales de una línea de 8
	for x in range(9):
		for y in range(2):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if (board[x][y] == k and board[x][y+1] == k and board[x][y+2] == k and board[x][y+3] == k and 
				board[x][y+4] == k and board[x][y+5] == k and board[x][y+6] == k and board[x][y+7] == k):
					# Eliminamos las figuras del tablero
					for i in range(y, y+8):
						DibujarObjeto(panel, 0, x, i, caja)
						board[x][i] = 0
						
	# Revisamos las coordenadas verticales de una línea de 7
	for x in range(9):
		for y in range(3):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if (board[x][y] == k and board[x][y+1] == k and board[x][y+2] == k and board[x][y+3] == k and 
				board[x][y+4] == k and board[x][y+5] == k and board[x][y+6] == k):
					# Eliminamos las figuras del tablero
					for i in range(y, y+7):
						DibujarObjeto(panel, 0, x, i, caja)
						board[x][i] = 0
						
	# Revisamos las coordenadas verticales de una línea de 6
	for x in range(9):
		for y in range(4):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if (board[x][y] == k and board[x][y+1] == k and board[x][y+2] == k and board[x][y+3] == k and 
				board[x][y+4] == k and board[x][y+5] == k):
					# Eliminamos las figuras del tablero
					for i in range(y, y+6):
						DibujarObjeto(panel, 0, x, i, caja)
						board[x][i] = 0
						
	# Revisamos las coordenadas verticales de una línea de 5
	for x in range(9):
		for y in range(5):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if board[x][y] == k and board[x][y+1] == k and board[x][y+2] == k and board[x][y+3] == k and board[x][y+4] == k:
					# Eliminamos las figuras del tablero
					for i in range(y, y+5):
						DibujarObjeto(panel, 0, x, i, caja)
						board[x][i] = 0
	
	# Revisamos las coordenadas diagonales / de línea de 9
	# Solo puede haber en un lugar
	xd = 0
	yd = 8
	# Revisamos las coordenadas para cada tipo de circulo
	for k in range(2, 8):
		if (board[xd][yd] == k and board[xd+1][yd-1] == k and board[xd+2][yd-2] == k and 
			board[xd+3][yd-3] == k and board[xd+4][yd-4] == k and board[xd+5][yd-5] == k and
			board[xd+6][yd-6] == k and board[xd+7][yd-7] == k and board[xd+8][yd-8] == k):
				for i in range(9):
					DibujarObjeto(panel, 0, xd+i, yd-i, caja)
					board[xd+i][yd-i] = 0
						
	# Revisamos las coordenadas diagonales / de línea de 8
	for x in range(2):
		for y in range(7, 9):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if (board[x][y] == k and board[x+1][y-1] == k and board[x+2][y-2] == k and 
				board[x+3][y-3] == k and board[x+4][y-4] == k and board[x+5][y-5] == k and
				board[x+6][y-6] == k and board[x+7][y-7] == k):
					for i in range(8):
						DibujarObjeto(panel, 0, x+i, y-i, caja)
						board[x+i][y-i] = 0
	
	# Revisamos las coordenadas diagonales / de línea de 7
	for x in range(3):
		for y in range(6, 9):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if (board[x][y] == k and board[x+1][y-1] == k and board[x+2][y-2] == k and 
				board[x+3][y-3] == k and board[x+4][y-4] == k and board[x+5][y-5] == k and
				board[x+6][y-6] == k):
					for i in range(7):
						DibujarObjeto(panel, 0, x+i, y-i, caja)
						board[x+i][y-i] = 0
						
	# Revisamos las coordenadas diagonales / de línea de 6
	for x in range(4):
		for y in range(5, 9):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if (board[x][y] == k and board[x+1][y-1] == k and board[x+2][y-2] == k and 
				board[x+3][y-3] == k and board[x+4][y-4] == k and board[x+5][y-5] == k):
					for i in range(6):
						DibujarObjeto(panel, 0, x+i, y-i, caja)
						board[x+i][y-i] = 0

	# Revisamos las coordenadas diagonales / de línea de 5
	for x in range(5):
		for y in range(4, 9):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if board[x][y] == k and board[x+1][y-1] == k and board[x+2][y-2] == k and board[x+3][y-3] == k and board[x+4][y-4] == k:
					for i in range(5):
						DibujarObjeto(panel, 0, x+i, y-i, caja)
						board[x+i][y-i] = 0					
	
	# Revisamos las coordenadas diagonales \ de 9
	# Solo ocurre en un lugar
	xdd = 0
	ydd = 0
	# Revisamos las coordenadas para cada tipo de circulo
	for k in range(2, 8):
		if (board[xdd][ydd] == k and board[xdd+1][ydd+1] == k and board[xdd+2][ydd+2] == k and 
		board[xdd+3][ydd+3] == k and board[xdd+4][ydd+4] == k and board[xdd+5][ydd+5] == k and 
		board[xdd+6][ydd+6] == k and board[xdd+7][ydd+7] == k and board[xdd+8][ydd+8] == k):
			for i in range(9):
				DibujarObjeto(panel, 0, xdd+i, ydd+i, caja)
				board[xdd+i][ydd+i] = 0
	
	# Revisamos las coordenadas diagonales \ de 8
	for x in range(2):
		for y in range(2):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if (board[x][y] == k and board[x+1][y+1] == k and board[x+2][y+2] == k and 
					board[x+3][y+3] == k and board[x+4][y+4] == k and board[x+5][y+5] == k and
					board[x+6][y+6] == k and board[x+7][y+7] == k):
					for i in range(8):
						DibujarObjeto(panel, 0, x+i, y+i, caja)
						board[x+i][y+i] = 0
	
	# Revisamos las coordenadas diagonales \ de 7
	for x in range(3):
		for y in range(3):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if (board[x][y] == k and board[x+1][y+1] == k and board[x+2][y+2] == k and 
					board[x+3][y+3] == k and board[x+4][y+4] == k and board[x+5][y+5] == k and
					board[x+6][y+6] == k):
					for i in range(7):
						DibujarObjeto(panel, 0, x+i, y+i, caja)
						board[x+i][y+i] = 0
				
	# Revisamos las coordenadas diagonales \ de 6
	for x in range(4):
		for y in range(4):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if (board[x][y] == k and board[x+1][y+1] == k and board[x+2][y+2] == k and 
					board[x+3][y+3] == k and board[x+4][y+4] == k and board[x+5][y+5] == k):
					for i in range(6):
						DibujarObjeto(panel, 0, x+i, y+i, caja)
						board[x+i][y+i] = 0
						
	# Revisamos las coordenadas diagonales \ de 5
	for x in range(5):
		for y in range(5):
			# Revisamos las coordenadas para cada tipo de circulo
			for k in range(2, 8):
				if board[x][y] == k and board[x+1][y+1] == k and board[x+2][y+2] == k and board[x+3][y+3] == k and board[x+4][y+4] == k:
					for i in range(5):
						DibujarObjeto(panel, 0, x+i, y+i, caja)
						board[x+i][y+i] = 0
						
	# POSCONDICION
	assert(True)	
	
def ProcesarCuadros(panel: 'Pantalla', board: [[int]], caja: int) -> 'void':
	# Funcion para revisar si existen rectangulos de al menos 2x2 de figuras de cuadros
	# var x, y: int
	
	# PRECONDICION
	assert(not FinDeJuego)
	
	# Cuadro 3x3
	# Cota: 7 - i
	for x in range(7):
		# Cota 7 - i
		for y in range(7):
			if (board[x][y] == 1 and board[x+1][y] == 1 and board[x][y+1] == 1 and 
				board[x+1][y+1] == 1 and board[x+2][y] == 1 and board[x+2][y+1] and 
				board[x+2][y] == 1 and board[x+2][y+1] and board[x+2][y+2]):
				board[x][y] = 0
				DibujarObjeto(panel, 0, x, y, caja)
				board[x+1][y] = 0
				DibujarObjeto(panel, 0, x+1, y, caja)
				board[x][y+1] = 0
				DibujarObjeto(panel, 0, x, y+1, caja)
				board[x+1][y+1] = 0
				DibujarObjeto(panel, 0, x+1, y+1, caja)
				board[x+2][y] = 0 
				DibujarObjeto(panel, 0, x+2, y, caja)
				board[x+2][y+1] = 0
				DibujarObjeto(panel, 0, x+2, y+1, caja)
				board[x][y+2] = 0 
				DibujarObjeto(panel, 0, x, y+2, caja)
				board[x+1][y+2] = 0
				DibujarObjeto(panel, 0, x+1, y+2, caja)
				board[x+2][y+2] = 0
				DibujarObjeto(panel, 0, x+2, y+2, caja)
	
	# Cuadro 3x2
	# Cota: 7 - i
	for x in range(7):
		# Cota 8 - i
		for y in range(8):
			if (board[x][y] == 1 and board[x+1][y] == 1 and board[x][y+1] == 1 and 
				board[x+1][y+1] == 1 and board[x+2][y] == 1 and board[x+2][y+1]):
				board[x][y] = 0
				DibujarObjeto(panel, 0, x, y, caja)
				board[x+1][y] = 0
				DibujarObjeto(panel, 0, x+1, y, caja)
				board[x][y+1] = 0
				DibujarObjeto(panel, 0, x, y+1, caja)
				board[x+1][y+1] = 0
				DibujarObjeto(panel, 0, x+1, y+1, caja)
				board[x+2][y] = 0 
				DibujarObjeto(panel, 0, x+2, y, caja)
				board[x+2][y+1] = 0
				DibujarObjeto(panel, 0, x+2, y+1, caja)
				
	# Cuadro 2x3
	# Cota: 8 - i
	for x in range(8):
		# Cota 7 - i
		for y in range(7):
			if (board[x][y] == 1 and board[x+1][y] == 1 and board[x][y+1] == 1 and 
				board[x+1][y+1] == 1 and board[x][y+2] == 1 and board[x+1][y+2]):
				board[x][y] = 0
				DibujarObjeto(panel, 0, x, y, caja)
				board[x+1][y] = 0
				DibujarObjeto(panel, 0, x+1, y, caja)
				board[x][y+1] = 0
				DibujarObjeto(panel, 0, x, y+1, caja)
				board[x+1][y+1] = 0
				DibujarObjeto(panel, 0, x+1, y+1, caja)
				board[x][y+2] = 0 
				DibujarObjeto(panel, 0, x, y+2, caja)
				board[x+1][y+2] = 0
				DibujarObjeto(panel, 0, x+1, y+2, caja)
	
	# Cuadro 2x2
	# Cota: 8 - i
	for x in range(8):
		# Cota 8 - i
		for y in range(8):
			if board[x][y] == 1 and board[x+1][y] == 1 and board[x][y+1] == 1 and board[x+1][y+1] == 1:
				board[x][y] = 0
				DibujarObjeto(panel, 0, x, y, caja)
				board[x+1][y] = 0
				DibujarObjeto(panel, 0, x+1, y, caja)
				board[x][y+1] = 0
				DibujarObjeto(panel, 0, x, y+1, caja)
				board[x+1][y+1] = 0
				DibujarObjeto(panel, 0, x+1, y+1, caja)
	
	# POSCONDICION
	assert(True)

def ProcesarObjetosDelTablero(panel: 'Pantalla', board: [[int]], score: int, caja: int) -> int:
	# Funcion para realizar la comprobacion de si existen figuras para eliminar del tablero
	# var objAntesDelTurno, objDespDelTurno, x, y: int
	
	# PRECONDICION
	assert(not FinDeJuego)
	
	# Contamos cuantos objetos hay
	objAntesDelTurno = ContarObjetosActuales(board)
	
	# Revisamos los cuadrados
	ProcesarCuadros(panel, board, caja)
				
	# Revisamos los circulos
	ProcesarCirculos(panel, board, caja)
	
	# Contamos cuantos objetos quedaron despues de procesar
	objDespDelTurno = ContarObjetosActuales(board)
	
	# Asignamos el puntaje de acuerdo a lo eliminado
	if objAntesDelTurno - objDespDelTurno == 4:
		score = score + 5
	elif objAntesDelTurno - objDespDelTurno == 5:
		score = score + 10
	elif objAntesDelTurno - objDespDelTurno == 6:
		score = score + 12
	elif objAntesDelTurno - objDespDelTurno == 7:
		score = score + 18
	elif objAntesDelTurno - objDespDelTurno >= 8:
		score = score + 40
	
	# Se actualiza el marcador del puntaje
	ActualizarPuntaje(panel, score, caja)
	
	return objAntesDelTurno, score
	
def ActualizarPuntaje(panel: 'Pantalla', score: int, caja: int) -> 'void':
	# Funcion para actualizar y mostrar el puntaje luego de cada movimiento
	# PRECONDICION
	assert(score >= 0)
	# var izq, tope: int
	
	izq, tope = EsqIzqEnPix(6, -5, caja)
	pygame.draw.rect(panel, (190, 238, 190), (izq, tope, 3*caja+5, 3*caja+5))
	
	fontObj = pygame.font.Font('freesansbold.ttf', 20)
	text1SurfaceObj = fontObj.render('Puntaje: ' + str(score), True, 
										(0, 0, 0))
	text1RectObj = text1SurfaceObj.get_rect()
	text1RectObj.center = (375, 50)
	panel.blit(text1SurfaceObj, text1RectObj)
	
	# POSCONDICION
	assert(True)
	
def ContarObjetosActuales(board: 'Pantalla') -> int:
	# Funcion que permite obtener la cantidad de objetos actuales en el tablero
	#PRECONDICION 
	assert(not FinDeJuego)
	
	#var num: int
	
	num = sum(board[x][y] != 0 for x in range(9) for y in range(9))
	
	# POSTCONDICION
	assert(num == sum(board[x][y] != 0 for x in range(9) for y in range(9)))
	
	return num
	
def NoSeEliminoObjeto(board: [[int]], objAntesTurno: int) -> bool:
	# Funcion que compara los objetos antes y despues del turno para determinar
	# si se elimino alguno.
	# var objDespTurno: int
	# var noSeElimino: bool
	
	# PRECONDICION
	assert(objAntesTurno >= 0)
	
	objDespTurno = ContarObjetosActuales(board)
	
	if objAntesTurno - objDespTurno == 0:
		noSeElimino = True
	elif objAntesTurno - objDespTurno != 0:
		noSeElimino = False
	
	# POSCONDICION: 
	assert(not(objAntesTurno - objDespTurno == 0) or (noSeElimino == True))
	assert(not(objAntesTurno - objDespTurno != 0) or (noSeElimino == False))
	
	return noSeElimino
	
def ProcesarFinDelJuego(board: [[int]], puntos: int) -> 'void':
	# Funcion para realizar el cierre del juego, revisa y actualiza el record
	# PRECONDICION
	assert(DeterminarFinDeJuego(board))
	
	# var record: int
	
	record = obtRecord(board)
	print("-------------------------------------")
	print("FIN DEL JUEGO. EL TABLERO ESTÁ LLENO.")
	
	if puntos > record:
		print("SU PUNTAJE FUE: ", puntos)
		print("EL RECORD ACTUAL ES: " + str(record))
		print("-------------------------------------")
		print("¡FELICIDADES! ¡OBTUVISTE UN NUEVO RECORD DE PUNTAJE!")
		print("-------------------------------------")
		updRecord(puntos)
	else:
		print("SU PUNTAJE FUE: ", puntos)
		print("-------------------------------------")
		print("EL RECORD ACTUAL ES: " + str(record))
		print("-------------------------------------")
		
	# POSCONDICION
	assert(True)
	
def obtRecord(board: [[int]]) -> int:
	# Recuperar el record de puntuacion del archivo.
	# PRECONDICION 
	assert(DeterminarFinDeJuego(board))
	# var data: str
	# var record: int
	
	with open('record.txt', 'r') as f:
		data = f.readline()
		record = int(data.rstrip('\n'))
	f.closed	
	return record
	
	# POSCONDICION 
	assert(f.closed())
	
def updRecord(nuevo: int) -> 'void':
	# Si se obtuvo una mayor puntuacion que el record, lo actualizamos
	# PRECONDICION 
	assert(nuevo > obtRecord())
	
	with open('record.txt', 'w') as f:
		f.write(str(nuevo))
	f.closed		
	
	# POSCONDICION 
	assert(f.closed())
	
# Variables

# FinDeJuego: bool
# puntaje: int
# jugada: array[0,4) of int
# proximosObjetos: array[0,3) of int
# tablero: array[0,9) of array[0,9) of int
# PANEL: Objeto pantalla de pygame
# ANCHVENTANA, ALTVENTANA, ANCHTABLERO, ALTTABLERO, CAJA: int
# GRIS, BLANCO, ROJO, VERDE, NEGRO, MORADO, NARANJA, AZUL, AMARILLO: tuplas
# figurasJuego: array[0,8) de tuplas[0,2)

############################
# Inicializacion del juego #
############################

# Valores iniciales generales del juego
FinDeJuego = False
puntaje = 0
jugada = []
proximosObjetos = []

# Datos de la ventana y tablero
ANCHVENTANA = 480
ALTVENTANA = 550 
ANCHTABLERO = 360 
ALTTABLERO = 360
CAJA = 40

# En el tablero 0 representa que no hay ningun elemento, 1 representa
# el cuadrado, y de 2 a 7 las bolas de colores. Por lo tanto inicializamos
# el tablero vacio.
# Matriz 9x9
tablero = [
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0]
			]

# Colores que vamos a usar 
MARRON = (139, 105, 20)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
NARANJA = (255, 128, 0)
MORADO = (159, 14, 159)
NEGRO = (0, 0, 0)
FONDO = (190, 238, 190)

# Objetos del juego
figurasJuego = [
				('espacio', FONDO), ('cuadro', MARRON), ('bola', ROJO), 
				('bola', VERDE), ('bola', AZUL), ('bola', AMARILLO), 
				('bola', NARANJA), ('bola', MORADO)
				]
				
# Iniciamos el modulo de pygame para usarlo			
pygame.init()

# Creamos la ventana grafica del juego
PANEL = pygame.display.set_mode((ANCHVENTANA, ALTVENTANA), 0, 32)

InicializarGraficos(PANEL, FONDO, NEGRO, ANCHTABLERO, ALTTABLERO)
InicializarTablero(PANEL, tablero, CAJA)
proximosObjetos = ObtenerProxObjetos(PANEL, tablero, CAJA) 

# Ciclo principal del juego
while not FinDeJuego:
	pygame.display.update()
	jugada = ObtenerJugada(tablero)
	MoverObjeto(PANEL, tablero, jugada, CAJA)
	pygame.display.update()
	objAntes, puntaje = ProcesarObjetosDelTablero(PANEL, tablero, puntaje, CAJA)
	pygame.display.update()	
	if NoSeEliminoObjeto(tablero, objAntes):
		AgregarProxObjetos(PANEL, tablero, proximosObjetos, CAJA)
		proximosObjetos = ObtenerProxObjetos(PANEL, tablero, CAJA) 
		FinDeJuego = DeterminarFinDeJuego(tablero)
	pygame.display.update()
	# Invariante
	assert(FinDeJuego == DeterminarFinDeJuego(tablero))
ProcesarFinDelJuego(tablero, puntaje)

