#! /usr/bin/python
# -*- coding: utf-8 -*-
# Adolfo Jeritson 12-10523
# Mathias San Miguel 13-11310
# Laboratorio de Algoritmos y Estructuras 2 - Proyecto 2
# TAD Interfaz Grafica para el reproductor de musica
import sys
import PyQt4
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtCore import Qt
from PyQt4.QtGui import *


class AppWindow(QWidget):
    def __init__(self, appRepr):
        super(AppWindow, self).__init__()

        # Esqueleto de la ventana
        self.setWindowTitle("Reproductor de Musica") 

        self.setGeometry(650, 450, 350,140)
        self.setFixedSize(350, 200)
        self.setMinimumHeight(80)
        
        self.palette = QPalette()
        self.palette.setColor(QPalette.Background, Qt.gray)
        self.setPalette(self.palette)
        self.setAutoFillBackground(True)


        # Panel de cancion actual
        self.current = QLabel(self)
        self.current.move(50, 60)
        self.current.setFixedSize(250,30)
        self.current.setText("\"" + appRepr.cancion_actual.song.titulo + "\" - " + appRepr.cancion_actual.song.artista)
        self.current.setAlignment(Qt.AlignCenter)
        self.current.setStyleSheet("font-size:15px;background:rgba(60,60,60,200);border: 8px #333333 solid;color:white;font-weight:bold;") 

        # Botones de reproduccion
        self.Bplay = QPushButton('>', self)
        self.Bplay.released.connect(self.onClickPlay)
        self.Bplay.setFixedSize(50,50)
        self.Bplay.move(150, 0)
        self.Bplay.setStyleSheet("font-size:30px;background-color:#333333;border: none;color:#ccc;font-weight:bold;") 

        self.Bpause = QPushButton('||', self)
        self.Bpause.released.connect(self.onClickPause)
        self.Bpause.setFixedSize(50,50)
        self.Bpause.move(100, 0)
        self.Bpause.setStyleSheet("font-size:30px;background-color:#333333;border: 4px solid gray;border-right:none;border-left:8px;color:#ccc;font-weight:bold;") 
 

        self.Bstop = QPushButton('[]', self)
        self.Bstop.released.connect(self.onClickStop)
        self.Bstop.setFixedSize(50,50)
        self.Bstop.move(200, 0) 
        self.Bstop.setStyleSheet("font-size:30px;background-color:#333333;border: 4px solid gray;border-right:8px;border-left:none;color:white;font-weight:bold;") 


        # Botones de atras/siguiente
        self.Batras = QPushButton('<<', self)
        self.Batras.released.connect(self.onClickPrev)
        self.Batras.setFixedSize(50,30)
        self.Batras.move(0, 60) 
        self.Batras.setStyleSheet("font-size:20px;background-color:#333333;border: none;color:white;font-weight:bold;") 


        self.Bsiguiente = QPushButton('>>', self)
        self.Bsiguiente.released.connect(self.onClickNext)
        self.Bsiguiente.setFixedSize(50,30)
        self.Bsiguiente.move(300, 60) 
        self.Bsiguiente.setStyleSheet("font-size:20px;background-color:#333333;border: none;color:white;font-weight:bold;") 

        self.Bplay.setFocusPolicy(Qt.NoFocus)
        self.Bpause.setFocusPolicy(Qt.NoFocus)  
        self.Bstop.setFocusPolicy(Qt.NoFocus)
        self.Batras.setFocusPolicy(Qt.NoFocus)        
        self.Bsiguiente.setFocusPolicy(Qt.NoFocus)

        # Panel de canciones siguientes

        self.palette = QPalette()
        self.palette.setColor(QPalette.Background, Qt.white)
        
        self.scroll = QListWidget(self)
        self.scroll.setPalette(self.palette)
        self.scroll.move(0, 90)
        self.scroll.resize(350,110)
        # self.scroll.setWidgetResizable(True)
        # self.scroll.setFrameStyle(QFrame.NoFrame)
        # self.scroll.setFrameShadow(QFrame.Plain)

        
        cur = appRepr.listaRep._head
        for i in range(len(appRepr.listaRep)):
            s = cur.song.titulo + " - " + cur.song.artista
            self.scroll.addItem(s)
            cur = cur._next
            
        # Reproductor asociado a la interfaz
        self.appRepr = appRepr
        
    def closeEvent(self,event):
        result = QMessageBox.question(self,
                      "Confirmando intenciones...",
                      "Estas seguro de que quieres salir ?",
                      QMessageBox.Yes| QMessageBox.No)
        event.ignore()
        
        if result == QMessageBox.Yes:
            sys.exit()

    # Slots para los eventos
    @pyqtSlot()
    def onClickPlay(self):
        self.appRepr.play()
        self.Bplay.setStyleSheet("font-size:30px;background-color:#333333;border: none;color:#fff;font-weight:bold;") 
        self.Bpause.setStyleSheet("font-size:30px;background-color:#333333;border: 4px solid gray;border-right:none;border-left:8px;color:#ccc;font-weight:bold;") 
        self.Bstop.setStyleSheet("font-size:30px;background-color:#333333;border: 4px solid gray;border-right:8px;border-left:none;color:#ccc;font-weight:bold;") 
        self.update()

    @pyqtSlot()
    def onClickPause(self):
        self.appRepr.pause()
        self.Bplay.setStyleSheet("font-size:30px;background-color:#333333;border: none;color:#ccc;font-weight:bold;") 
        self.Bpause.setStyleSheet("font-size:30px;background-color:#333333;border: 4px solid gray;border-right:none;border-left:8px;color:#fff;font-weight:bold;") 
        self.Bstop.setStyleSheet("font-size:30px;background-color:#333333;border: 4px solid gray;border-right:8px;border-left:none;color:#ccc;font-weight:bold;") 
        self.update()
        
    @pyqtSlot()
    def onClickStop(self):
        self.appRepr.stop()
        self.Bplay.setStyleSheet("font-size:30px;background-color:#333333;border: none;color:#ccc;font-weight:bold;") 
        self.Bpause.setStyleSheet("font-size:30px;background-color:#333333;border: 4px solid gray;border-right:none;border-left:8px;color:#ccc;font-weight:bold;") 
        self.Bstop.setStyleSheet("font-size:30px;background-color:#333333;border: 4px solid gray;border-right:8px;border-left:none;color:#fff;font-weight:bold;") 
        self.update()

    @pyqtSlot()
    def onClickNext(self):
        self.appRepr.siguiente()
        self.actCur()
        
    @pyqtSlot()
    def onClickPrev(self):
        self.appRepr.atras()
        self.actCur()
    
    # Funcion que permite mostrar y actualizar la cancion actual    
    def actCur(self):       
        self.current.setText("\"" + self.appRepr.cancion_actual.song.titulo + "\" - " + self.appRepr.cancion_actual.song.artista)
        self.update()
        
    def actList(self):
        self.scroll.clear()
        
        if self.appRepr.listaRep is None:
            s = "No se encontro nada con la busqueda."
            self.scroll.addItem(s)
        else:
            a = 1
            cur = self.appRepr.listaRep._head
            for i in range(len(self.appRepr.listaRep)):
                if cur is not None:
                    a+=1
                    s = cur.song.titulo + " - " + cur.song.artista
                    self.scroll.addItem(s)
                    cur = cur._next
                    
        self.update()

