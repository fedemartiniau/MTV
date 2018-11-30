#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = "tabs"
__version__ = "v0.0.1"
__proyecto__ = ""
__company__ = "INVAP S.E."
__status__ = "Desarrollo"
__description___=''' 
            Este script hace la creacioacion y carga de los tabs a partr del obeto xml que le llega
    '''
__author__ = 'Federico Martiniau'
__copyright__ = "Copyright 2018, INVAP S.E."
__credits__ = ["Nicolas Horro","Federico Martiniau"]
__destails__='''   '''

# ###### IMPORTS ######
import sys
import matplotlib
import traceback as tb

matplotlib.use("Qt5Agg")

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar

import numpy as np
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


# ###### IMPORTS PROPIOS ######
from widgets.label_widgets import LabelWidgets 
from widgets.multiplot_widgets import MultiPlotWidgets
from widgets.grid_widgets import GridWidgets

# ###### ERRORES ######
# Todos los mensajes de error y los alertas deben estar identificados con un número (código) único para el script 

MSG_ERROR_GENERAL = 'ERROR 000: Error inesperado al ejecutar el script'+' '+__title__
MSG_ERROR_BUSACAR_TAB_EN_XML = 'ERROR 001: '+__title__+ ' Error al intentar buscar los tags "TAB" en el archivo XML {}'
MSG_ERROR_BUSACAR_WIDGET_EN_XML = 'ERROR 002: '+__title__+ ' Error al intentar buscar los tags "WIDGET" en el archivo XML {}'
##################################################################################################################################################################
# ###### FUNCION PRINCIPAL ######
class MainTabViewWidget(QWidget):
 
    def __init__(self, parent,root_xml):   
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.context = parent.context
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab_contents = {}
        self.ui_contents = {}
        
        # Obtener lista TABS
        resultado = self.get_tab_list(root_xml)
        if resultado["Error"]:
            sys.exit()
        
        self.tab_list =  resultado["Result"]
        
    
        for tab_name in self.tab_list.keys():
            self.get_widget(self.tab_list[tab_name])
            

        # Add tabs to widget        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
        return
    

    #--------------------------------------------------------------------------------------------------------    
    def get_tab_list(self,root_xml):
        try:
            tab_list = {}
            
            for tab in root_xml.iter('tab'):  
                tab_list[tab.attrib["name"]]=tab
     
     
            return {"Error":False,"Result":tab_list}
        except:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n Error:')
            print(MSG_ERROR_BUSACAR_TAB_EN_XML.format('tab'))
            print(tb.format_exc())
            return {"Error":True,"Result":MSG_ERROR_BUSACAR_TAB_EN_XML.format('tab') + '\n' + tb.format_exc()}
    #--------------------------------------------------------------------------------------------------------    
    def update(self):
        try:            
            for tab_name in self.ui_contents.keys(): 
                if(self.tabs.tabText(self.tabs.currentIndex()) == tab_name ):
                    draw = True
                else:
                    draw = False
                    
                for widget in self.ui_contents[tab_name]['widgets']:  
                    widget.update(draw)
     
     
            return {"Error":False,"Result":''}
        except:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n Error:')
            print(MSG_ERROR_BUSACAR_TAB_EN_XML.format('tab'))
            print(tb.format_exc())
            return {"Error":True,"Result":MSG_ERROR_BUSACAR_TAB_EN_XML.format('tab') + '\n' + tb.format_exc()}        
    #--------------------------------------------------------------------------------------------------------    
    def get_widget(self,tab_xml):
        try:
            tab_name = tab_xml.attrib["name"]
            
            self.ui_contents[tab_name] = {}
            self.ui_contents[tab_name]['widgets'] = []
            self.ui_contents[tab_name]['tab'] = QWidget()
            self.ui_contents[tab_name]['tab'].layout = QVBoxLayout(self)
            self.gridLayout = QGridLayout()
            self.gridLayout.setColumnStretch(1, 6)
            self.gridLayout.setColumnStretch(2, 6)
            self.gridLayout.setColumnStretch(3, 6)
            self.gridLayout.setColumnStretch(4, 6)
            
            
            for recuadro in tab_xml.iter('recuadro'):
                propiedades_recuadro = {}
                propiedades_recuadro["gillaX"] = int(recuadro.attrib["gillaX"])
                propiedades_recuadro["gillaY"] = int(recuadro.attrib["gillaY"])
                propiedades_recuadro["filas"] = int(recuadro.attrib["filas"])
                propiedades_recuadro["columnas"] = int(recuadro.attrib["columnas"])
                
                for widget in recuadro.iter('widget'):
                    if (widget.attrib["type"] == 'Label'):
                        self.ui_contents[tab_name]['widgets'].append(LabelWidgets(self.context,self.gridLayout,widget,propiedades_recuadro))
                        pass
                    elif (widget.attrib["type"] == 'Plot'):
                        self.ui_contents[tab_name]['widgets'].append(PlotWidgets(self.context,self.gridLayout,widget,propiedades_recuadro))
                        pass  
                    elif (widget.attrib["type"] == 'MultiPlot'):
                        self.ui_contents[tab_name]['widgets'].append(MultiPlotWidgets(self.context,self.gridLayout,widget,propiedades_recuadro))
                        pass                  
                    elif (widget.attrib["type"] == 'Grid'):
                        self.ui_contents[tab_name]['widgets'].append(GridWidgets(self.context,self.gridLayout,widget,propiedades_recuadro))
                        pass
                    elif (widget.attrib["type"] == 'tetris'):
                        self.ui_contents[tab_name]['widgets'].append(TetrisWidget(self.context,self.gridLayout,widget,propiedades_recuadro))
                        pass
 
            self.ui_contents[tab_name]['tab'].setLayout(self.gridLayout)
            self.tabs.addTab(self.ui_contents[tab_name]['tab'], tab_name)
            
            return {"Error":False,"Result":True}
        except:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n Error:')
            print(MSG_ERROR_BUSACAR_WIDGET_EN_XML.format('widget'))
            print(tb.format_exc())
            return {"Error":True,"Result":MSG_ERROR_BUSACAR_WIDGET_EN_XML.format('widget') + '\n' + tb.format_exc()}
        
        
    #--------------------------------------------------------------------------------------------------------    

        
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
