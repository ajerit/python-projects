# Adolfo Jeritson. 2015
# NOTAS MASTER V1.2
# FEATURES:
# + AÑADIR NOTAS Y CODIGO DE LA MATERIA CORRESPONDIENTE
# + NO VERIFICA SI LOS DATOS SON CORRECTOS (NOTAS DEL 1 AL 5, ETC)
# + MUESTRA UNA LISTA DE TODAS LAS MATERIAS EN LA DB SIN OPCIONES 
# + SE PUEDE MODIFICAR LA NOTA DE UNA MATERIA ESPECIFICA
#
#
import sys

# Variables del programa
path = 'db_notas.txt'
fin = False
v = "1.1"

def ComprobarCarga(mat, nota):
	if len(mat) == 6 and 1 <= nota and nota <= 5:
		with open(path, 'r') as f:
			data = f.readlines()
			num_lineas = sum(1 for line in open(path))
		f.closed
		lineas = [line.rstrip('\n') for line in data]
		
		if all(lineas[x][0:6].upper() != mat for x in range(1,num_lineas)):
			return True
		else:
			print("********************************************")
			print("LA MATERIA YA EXISTE, NO SE PUEDE REPETIR.")
			return False
	else:
		return False	
		
def CargarDatos():
	print("Inserte los datos necesarios a continuacion")
	idmat = input("Codigo materia >> ").upper()
	note = input("Nota en la materia >> ")
	
	if ComprobarCarga(idmat, int(note)):
		print("----------------------------------------------------------------")
		print("Por favor verifique los datos")
		print("CODIGO: " + idmat)
		print("NOTA: " + note)
		correct = input("Los datos son correctos?: (T/F) >> ")
		print("----------------------------------------------------------------")
	
		if correct.upper() == "T":
			with open(path, 'r') as f:
				data = f.readlines()
			f.closed
			
			data = [line.rstrip('\n') for line in data]
			data.append(idmat+" "+note)
			
			with open(path, 'w') as f:
				f.write('\n'.join(data))
			f.closed
			
			if f.closed:
				print("Operacion exitosa.")
		else:
			print("********************************************")
			print("INTENTE DE NUEVO.")
			print("----------------------------------------------------------------")
	else:
		print("********************************************")
		print("LOS DATOS INTRODUCIDOS NO SON VALIDOS.")
					
def LeerDatos():
	print("En la V"+v+" se leen y se muestran todas las notas que hay en la db:\n")
	
	with open(path, 'r') as f:
		lineas = f.readlines()
		num_lineas = sum(1 for line in open(path))
		for x in range(1, num_lineas):
			print("MATERIA: " + lineas[x][0:6] +" / " + "NOTA: " + lineas[x][7:8])
	f.closed
	
def ModificarDatos():
	idmat = input("Inserte codigo de materia a modificar >> ").upper()
	poslista = -1
	with open(path, 'r') as f:
		data = f.readlines()
		num_lineas = sum(1 for line in open(path))
	f.closed
	lineas = [line.rstrip('\n') for line in data]
	for x in range(1, num_lineas):
		if lineas[x][0:6].upper() == idmat:
			poslista = x
			break
				
	if poslista == -1:
		print("********************************************")
		print("No se encontro la materia en la DB.")
	else:
		dbmat = lineas[poslista][0:6].upper()
		dbnota = lineas[poslista][7:8]
		print("Materia "+dbmat+" encontrada, la nota registrada es: "+dbnota)
		print("------------------------------")
			
		newnota = input("Inserte nueva nota para la materia >> ")
		lineas[poslista] = dbmat + " " + newnota
		print("------------------------------")
		
		with open(path, 'w') as f:
			f.write('\n'.join(lineas))
		f.closed
		print("Nueva nota cargada, ahora la nota de "+dbmat+" es "+lineas[poslista][7:8])

while not fin:	
	print("----------------------------------------------------------------")
	print("Bienvenido al administrador de notas v"+v)
	print("Seleccione la operacion que desea realizar: (Cargar/Modificar/Leer)")
	accion = input(">> ")
	print("----------------------------------------------------------------")
	
	if accion.upper() == "CARGAR":
		CargarDatos()
	
	elif accion.upper() == "MODIFICAR":
		ModificarDatos()
		
	elif accion.upper() == "LEER":
		LeerDatos()
	
	elif accion.upper() == "SALIR":
		print("Bye")
		print("----------------------------------------------------------------")
		sys.exit()
	else:
		print("OPCION NO VALIDA, INTENTE DE NUEVO.")
