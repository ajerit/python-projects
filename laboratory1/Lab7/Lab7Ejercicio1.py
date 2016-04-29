#
# Adolfo Jeritson. 12-10523
#
# Descripcion: Lee, ejecuta y guarda un juego de lineas de colores y rectangulos.
#
import random, sys

# Analisis Descendente
def CargarJuego(nombre: str) -> 'void':
	def CargarProximosObjetos(nombre: str):
		with open(nombre, 'r') as f:
			data = f.readlines()
			prox = data[0].rstrip('\n')
			objetos = prox.split(" ")
		f.closed	
		return objetos
	
	def CargarTablero(nombre: str):
		board = []
		with open(nombre, 'r') as f:
			data = f.readlines()
			for i in range(1,10):
				fila = data[i].strip('\n')
				filaa = fila.split(" ")
				board.append(filaa)
			f.closed	
		return board
	
	def CargarPuntaje(nombre: str):
			puntuacion = 0
			with open(nombre, 'r') as f:
				data = f.readlines()
				puntuacion = int(data[10].rstrip('\n'))
			f.closed
			return puntuacion
			
	proxObjetos = CargarProximosObjetos(nombre)
	tablero = CargarTablero(nombre)
	puntuacion = CargarPuntaje(nombre)
	
	return proxObjetos, tablero, puntuacion
	
def EjecutarJuego(jugadas: str, board, prox) -> 'void':
	movs = []
	with open(jugadas, 'r') as f:
		movs = f.readlines()
	f.closed
	
	F = open('proxobj.txt', 'w')
	
	for i in range(len(movs)):
		movs[i] = movs[i].rstrip('\n')
		jActual = movs[i]

		x1, y1, x2, y2 = int(jActual[0]), int(jActual[2]), int(jActual[4]), int(jActual[6])
		
		# Muevo objeto de la jugada
		if board[x1][y1] != "_":
			objMover = str(board[x1][y1])
			board[x1][y1] = "_"
			board[x2][y2] = objMover
		else:
			print("ERROR, espacio vacio.")
			print(x1)
			print(y1)
			sys.exit()
		
		# Agrego los proximos objetos al tablero
		for i in range(len(prox)):
			x3, y3 = random.randint(0,8), random.randint(0,8)
			while board[x3][y3] != "_":
				x3, y3 = random.randint(0,8), random.randint(0,8)
			board[x3][y3] = prox[i]	
		
		# Genero nuevo prox objetos
		prox = [str(random.randint(0,6)), str(random.randint(0,6))]
		
		cont0 = sum(1 for x in range(9) for y in range(9) if board[x][y] == "0")
		cont1 = sum(1 for x in range(9) for y in range(9) if board[x][y] == "1")
		cont2 = sum(1 for x in range(9) for y in range(9) if board[x][y] == "2")
		cont3 = sum(1 for x in range(9) for y in range(9) if board[x][y] == "3")
		cont4 = sum(1 for x in range(9) for y in range(9) if board[x][y] == "4")
		cont5 = sum(1 for x in range(9) for y in range(9) if board[x][y] == "5")
		cont6 = sum(1 for x in range(9) for y in range(9) if board[x][y] == "6")
		
		nuevo = min(cont0, cont1, cont2, cont3, cont4, cont5, cont6)
		
		if nuevo == cont0:
			prox.append(str(0))
		elif nuevo == cont1:
			prox.append(str(1))
		elif nuevo == cont2:
			prox.append(str(2))
		elif nuevo == cont3:
			prox.append(str(3))
		elif nuevo == cont4:
			prox.append(str(4))
		elif nuevo == cont5:
			prox.append(str(5))
		elif nuevo == cont6:
			prox.append(str(6))
			
		F.write(" ".join(prox))
		F.write("\n")
		
	
	F.close()		
	
	return prox

def GuardarJuego(nombre: str, board: [str], objetos: [str], puntos: int) -> 'void':
	def GuardarProximosObjetos(objetos):
		for i in range(3):
			objetos[i] = str(objetos[i])
		f.write(" ".join(objetos))
		f.write("\n")
		
	def GuardarTablero(board):
		for i in range(9):
			f.write(" ".join(board[i]))
			f.write("\n")	
			
	def GuardarPuntaje(puntos):
		f.write(str(puntos))
		
	with open(nombre, 'w') as f:
		GuardarProximosObjetos(objetos)
		GuardarTablero(board)
		GuardarPuntaje(puntos)
	f.closed
				
		
# Valores iniciales
tablero = []
puntaje = 0
proxObjetos = []
archivo = ""

while True:
	print("Eliga que opcion quiere hacer: ")
	opcion = input("LEER / EJECUTAR / GUARDAR >> ")
	print("----------------------------")
	
	if opcion.upper() == "LEER":
		archivo = input("Inserte nombre del archivo del juego a Cargar >> ")
		proxObjetos, tablero, puntaje = CargarJuego(archivo)
		print("Juego cargado exitosamente.")
		print(proxObjetos)
		print("----------------------------")
		
	elif opcion.upper() == "GUARDAR":
		if tablero == []:
			print("Primero debe cargar un juego, vuelva a intentar.")
			print("----------------------------")
		else:
			archivo = input("Inserte nombre del archivo del juego a Guardar >> ")
			GuardarJuego(archivo, tablero, proxObjetos, puntaje)
			print("Juego guardado exitosamente.")
			print("----------------------------")
			sys.exit()
			
	elif opcion.upper() == "EJECUTAR":
		if tablero == []:
			print("Primero debe cargar un juego, vuelva a intentar.")
			print("----------------------------")
		else:
			archivo = input("Inserte nombre del archivo de las jugadas >> ")
			proxObjetos = EjecutarJuego(archivo, tablero, proxObjetos)
			print("Jugadas realizadas exitosamente")
			print("----------------------------")
			
	elif opcion.upper() == "SALIR":
		sys.exit()
	
	else:
		print("OPCION NO VALIDA, VUELVA A INTENTAR.")
		print("------------------------------------")
		
