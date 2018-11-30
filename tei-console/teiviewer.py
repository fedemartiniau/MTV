#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = "VT (Visor de Telemetría)"
__version__ = "v0.0.1"
__proyecto__ = ""
__company__ = "INVAP S.E."
__status__ = "Desarrollo"
__description___='''
        Este es el script principal que inicializa todo
        * valida y lee el archivo xml que pasa como objetos al armador de tabs
        * inicia el main window que despues pasa para que sea cargado
  '''
__author__ = 'Nicolas Horro y Federico Martiniau'
__copyright__ = "Copyright 2018, INVAP S.E."
__credits__ = ["Nicolas Horro","Federico Martiniau"]
__destails__='''   '''

# ###### IMPORTS ######
import sys
import traceback as tb
import xml.etree.ElementTree as et

#QT imports
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtWidgets import QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QTimer

# ###### IMPORTS PROPIOS ######
# Data Sources
from datasources.dummy import DummyDataSource
#from datasources.MulitasDataSource.MulitasDataSource import *

# Widgets
from widgets.tabs import MainTabViewWidget

# ###### VARIABLES ESTATICAS ######
TMY_REFRESH_INTERVAL_IN_MS = (50) # 1 updates/sec
RUTA_ARCHIVO_XML = 'config.xml'

# ###### ERRORES ######
# Todos los mensajes de error y los alertas deben estar identificados con un número (código) único para el script 

MSG_ERROR_GENERAL = 'ERROR 000: Error inesperado al ejecutar el script'+' '+__title__
MSG_ERROR_ABRIR_XML = 'ERROR 001: '+__title__+ ' Error al intentar abrir el archivo XML {}'
 
##################################################################################################################################################################
# ###### FUNCION PRINCIPAL ######
class App(QMainWindow): 

    def __init__(self):
        super().__init__()
        self.title = __title__ + ' ' + __version__
        self.setWindowTitle(self.title)
        
        # Leer XML
        resultado = open_XML(RUTA_ARCHIVO_XML)
        if resultado["Error"]:
            sys.exit()
        
        root_xml =  resultado["Result"]
        
        # Instanciación de DataSources
        # 1. Crear un "contexto", o suerte de "repositorio global" de variables de tmy al que todos (datasources y widgets pueden acceder)  
        self.context = {}
        self.ds = DummyDataSource(context=self.context,params=None)
        #self.ds = MulitasDataSource(context=self.context)
        
        # Componente o ventana principal (puede separarse en una clase o vivir acá)
        # 1. Cargar XML e instanciar componente principal que contiene todas las pestañas
        # 2. Por cada pestaña, agregar un layout básico e instanciar cada widget ( luego será un factory o similar, ahora no importa)
        #    Observación: probablemente interese tener indexados widgets por pestaña. para saber si un widget está en una pestaña activa
        # 3. Finalmente, conectar un método update() a un timer que:
        #      3.1 Llama al método update de cada widget indicando si tiene que redibujarse (está en pestaña visible o no)        
        
        self.table_widget = MainTabViewWidget(self,root_xml)
        self.setCentralWidget(self.table_widget) 
        self.showMaximized()
#        self.showMaximized()


        # Asociar la función update general a un timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(TMY_REFRESH_INTERVAL_IN_MS)
        
    #--------------------------------------------------------------------------------------------------------    
    def update(self):        
        # TODO
        # LLamar la función update() para todos los widgets, 
        # indicando si deben redibujarse (porque están en una pestaña visible) o no
        # print(self.context)
        self.table_widget.update()
        # sólo para debug, borrar
        pass
        
        
##---------------------------------------------------------------------------------------------------------------------------------------------------------
##---------------------------------------------------------------------------------------------------------------------------------------------------------		
# ###### FUNCIONES SECUNDARIAS ######
def open_XML(xml):
    ''' Abre un archivo xml y devuelve la posición del tag raíz  '''
    try:
        tree = et.parse(xml)
        root = tree.getroot() 
        return {"Error":False,"Result":root}      
    except:
        print_msg('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n Error:')
        print_msg(MSG_ERROR_ABRIR_XML.format(xml))
        print_msg(tb.format_exc())
        return {"Error":True,"Result":MSG_ERROR_ABRIR_XML.format(xml) + '\n' + tb.format_exc()}        
#------------------------------------------------------------------------------------------------------------------------------------------------------------
def print_msg(MSG):
    ''' se encarga de imprimir en forma correcta todo lo que se debe mostrar por pantalla '''
    for linea in MSG.split('\n'):
        print('\r'+linea.strip('\n'))
    return

#------------------------------------------------------------------------------------------------------------------------------------------------------------     
# ###### FUNCION DEBUG ######
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())