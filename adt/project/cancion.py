# -*- coding: utf-8 -*-
# Adolfo Jeritson 12-10523
# Mathias San Miguel 13-11310
# Laboratorio de Algoritmos y Estructuras 2 - Proyecto 2
# Implementacion del TAD Cancion
        
        
class Cancion:
    # Metodo que inicializa un objeto de la clase Cancion
    def __init__(self, titulo, artista,genero=None, archivo=None):
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.archivo = archivo
    
    # Metodo para que el TAD pueda mostrar representacion
    def __repr__(self):
        return repr((self.titulo, self.artista, self.genero, self.archivo))
    
    # Metodo que verifica si la cancion es igual a otra dada
    def es_igual(self, cancion2):
        return self.titulo == cancion2.titulo and self.artista == cancion2.artista

    # Metodo que verifica si la cancion es menor a otra dada segun el artista
    def esmenor_artista(self, cancion2):
        if self.artista < cancion2.artista:
            return True
        elif self.artista == cancion2.artista and self.titulo < cancion2.titulo:
            return True
        return False
    
    # Metodo que verifica si la cancion es menor a otra dada segun el titulo
    def esmenor_titulo(self, cancion2):
        if self.titulo < cancion2.titulo:
            return True
        elif self.titulo == cancion2.titulo and self.artista < cancion2.artista:
            return True
        return False
    
    # Metodo para obtener el titulo de la cancion
    def get_titulo(self):
        return self.titulo
    
    # Metodo para obtener el genero de la cancion
    def get_genero(self):
        return self.genero
        
    # Metodo para obtener el artista de la cancion    
    def get_artista(self):
        return self.artista
    
    # Metodo para obtener el archivo de la cancion    
    def get_archivo(self):
        return self.archivo


