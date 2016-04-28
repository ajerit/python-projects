#! /usr/bin/python
# -*- coding: utf-8 -*-
# Adolfo Jeritson 12-10523
# Mathias San Miguel 13-11310
# Laboratorio de Algoritmos y Estructuras 2 - Proyecto 2
# Implementacion del TAD Reproductor, abstrayendo la interfaz grafica.

from PyQt4.phonon import Phonon
from cancion import *
from listarep import *


class Reproductor:
    # Inicializacion del reproductor, se guarda la lista de reproduccion
    # la cancion actual y el manejo de la clase phonon para reproducir musica
    def __init__(self, listaRep):
        self.listaRep = listaRep
        self.cancion_actual = listaRep._head
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory)
        self.phonon = Phonon.MediaObject()
        self.phonon = Phonon.createPlayer(Phonon.MusicCategory)
        Phonon.createPath(self.phonon, self.audioOutput)
        self.phonon.setCurrentSource(Phonon.MediaSource(self.cancion_actual.song.archivo))
    
    # Funcion para empezar a reproducir la cancion actual
    def play(self):
        if self.listaRep is not None:
            self.phonon.play()
        
    # Funcion para detener la reproducción la cancion actual
    def stop(self):
        if self.listaRep is not None:
            self.phonon.stop()
    
    # Funcion para pausar la reproducción la cancion actual
    def pause(self):
        if self.listaRep is not None:
            self.phonon.pause()
    
    # Funcion para mover la cancion actual a la siguiente en la lista
    def siguiente(self):
        if self.listaRep is not None:
            e = self.esta_reproduciendo()
            self.cancion_actual = self.cancion_actual._next
            self.phonon.setCurrentSource(Phonon.MediaSource(self.cancion_actual.song.archivo))
            if e: self.play()
            return self.cancion_actual.song
    
    # Funcion para mover la cancion actual a la anterior en la lista    
    def atras(self):
        if self.listaRep is not None:
            e = self.esta_reproduciendo()
            self.cancion_actual = self.cancion_actual._prev
            self.phonon.setCurrentSource(Phonon.MediaSource(self.cancion_actual.song.archivo))
            if e: self.play()
            return self.cancion_actual.song
    
    # Funcion que recibe una lista de reproducción para que sea la lista
    # actual del reproductor
    def set_lista(self, newlista):
        self.listaRep = newlista
        if newlista is None:
            self.cancion_actual = ListRepNode(Cancion("",""))
        else:
            self.cancion_actual = newlista._head
            self.phonon.setCurrentSource(Phonon.MediaSource(self.cancion_actual.song.archivo))
    
    # Funcion que verifica si actualmente hay alguna canción en reproducción
    def esta_reproduciendo(self):
        return self.phonon.state() == Phonon.PlayingState
        
        
