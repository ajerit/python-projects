# -*- coding: utf-8 -*-
# Adolfo Jeritson 12-10523
# Mathias San Miguel 13-11310
# Laboratorio de Algoritmos y Estructuras 2 - Proyecto 2
# Implementación del Cliente para reproducir musica

import sys, threading
from rep import *
from indice import *
from gui import *

def parseArgs(args):
    msg = "Error en la linea de comando:\npython reproductor.py <archivo>"
    if len(args) != 2:
        print(msg)
        sys.exit(1)
    return args[1]

def leerArchivo(archivo):
    canciones = []
    with open(archivo, 'r') as f:
        for line in f:
            canciones.append(line.rstrip('\n').split('\t'))
    lis = ListaReproduccion()
    for song in canciones:
        lis.agregar(Cancion(song[0], song[1], song[2], song[3]))
    return lis

def inicializar_cliente(listaRep):
    appRepr = Reproductor(listaRep)
    appWindow = AppWindow(appRepr)
    appWindow.actCur()
    appWindow.actList()
    indGen = Indice()
    indArt = Indice()
    cur = listaRep._head
    for i in range(len(listaRep)):
        indGen.agregar(cur.song.genero, cur.song)
        indArt.agregar(cur.song.artista, cur.song)
        cur = cur._next
    
    return (appRepr, appWindow, indGen, indArt)
    
def restaurar_lista_original(rep, archivo):
    lista = leerArchivo(archivo)
    rep.set_lista(lista)
    
def eliminar_cancion(rep, cancion):
    rep.listaRep.eliminar(cancion)

def ordenar_por_titulo(rep):
    rep.listaRep.ordenar_titulo()

def ordenar_por_artista(rep):
    rep.listaRep.ordenar_artista()

def buscar_por_genero(rep, ind, gen):
    rep.set_lista(ind.buscar(gen))

def buscar_por_artista(rep,ind,art):
    rep.set_lista(ind.buscar(art))

def importar(archivo, rep, indGen, indArt):
    aimportar = []
    with open(archivo, 'r') as f:
        for line in f:
            aimportar.append(line.rstrip('\n').split('\t'))
    for song in aimportar:
        chanson = Cancion(song[0], song[1], song[2], song[3])
        rep.listaRep.agregar(chanson)
        indGen.agregar(chanson.genero, chanson)
        indArt.agregar(chanson.artista, chanson)
    rep.set_lista(rep.listaRep)

if __name__ == "__main__":
    threading.stack_size(67108864)
    newApp = QApplication(sys.argv)
    songsFile = parseArgs(sys.argv)
    lista = leerArchivo(songsFile)
    reproductor, interfaz, indGen, indArt = inicializar_cliente(lista)
    interfaz.show()
    
    
    # Main loop
    while True:
        print("¿Que desea hacer?")
        print("CANCIONES:  1. IMPORTAR     2.ELIMINAR")
        print("ORDENAR:    3. POR TITULO   4.POR ARTISTA")
        print("BUSCAR:     5. ARTISTA      6.GENERO")
        print("            7. RESTAURAR")
        print("            0. SALIR")
        
        userChoice = raw_input(">> ")
        t = None
        # Verificamos que no este bloqueado por reproduccion
        if reproductor.esta_reproduciendo():
            print("\n[!] No pueden realizar operaciones mientras se reproduce una cancion.\n")
        else:
            try: 
                if userChoice == "0":
                    raise SystemExit
                    
                elif userChoice.upper() == "IMPORTAR" or userChoice=="1":
                    file = raw_input("Path de archivo a importar: ")
                    importar(file, reproductor, indGen, indArt)

                elif userChoice.upper() == "ELIMINAR" or userChoice=="2":
                    userTitle = raw_input("Inserte el nombre de la canción >> ")
                    userArtist = raw_input("Inserte el nombre del artista >> ")
                    userSong = Cancion(userTitle, userArtist)
                    eliminar_cancion(reproductor, userSong)
                    
                elif userChoice.upper() == "POR TITULO" or userChoice=="3":
                    t = threading.Thread(target=ordenar_por_titulo, args=[reproductor])
                    t.start()

                elif userChoice.upper() == "POR ARTISTA" or userChoice=="4":
                    t = threading.Thread(target=ordenar_por_artista, args=[reproductor])
                    t.start()

                elif userChoice.upper() == "ARTISTA" or userChoice=="5":
                    userInput = raw_input("Inserte el artista >> ")
                    buscar_por_artista(reproductor,indArt,userInput)

                elif userChoice.upper() == "GENERO" or userChoice=="6":
                    userInput = raw_input("Inserte el genero >> ")
                    buscar_por_artista(reproductor,indGen,userInput)

                elif userChoice.upper() == "RESTAURAR" or userChoice=="7":
                    restaurar_lista_original(reproductor, sys.argv[1])
                    
            except SystemExit:
                sys.exit()
            except:
                print("\n[!] Opción no válida, vuelva a intentarlo.\n")
        
        if t is not None:
            while(t.isAlive()): pass
        interfaz.actCur()
        interfaz.actList()

    sys.exit(interfaz.exec_())
