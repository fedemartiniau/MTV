#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = "Grid Widgets"
__version__ = "v0.0.1"
__proyecto__ = ""
__company__ = "INVAP S.E."
__status__ = "Desarrollo"
__description___=''' 
            La idea de este script es que tenga la capacidad de armar un plot y agregarlo al tab actal.
 '''
__author__ = 'Federico Martiniau'
__copyright__ = "Copyright 2018, INVAP S.E."
__credits__ = ["Nicolas Horro","Federico Martiniau"]
__destails__='''   '''

# ###### IMPORTS ######
import sys
import traceback as tb
import xml.etree.ElementTree as et
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
#QT imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *

from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar

import numpy as np
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# ###### IMPORTS PROPIOS ######
# ###### VARIABLES ESTATICAS ######
# ###### ERRORES ######
# Todos los mensajes de error y los alertas deben estar identificados con un número (código) único para el script 

MSG_ERROR_GENERAL = 'ERROR 000: Error inesperado al ejecutar el script'+' '+__title__
MSG_ERROR_AL_GENARAR_GRID = 'ERROR 001: '+__title__+ ' Error al intentar armar el grid'
MSG_ERROR_AL_ACTUALIZAR_GRID = 'ERROR 002: '+__title__+ ' Error al intentar actualizar el grid' 
#################################################################################################################################################################
###### FUNCION PRINCIPAL ######
class GridWidgets(QWidget):
    def __init__(self, context,tab_contents,widget,propiedades_recuadro):
        try:
            self.tableWidget = QTableWidget()
            self.columns =  widget.attrib["columns"]
            self.rows =  widget.attrib["rows"]
            
            self.tableWidget.setRowCount(int(self.rows))
            self.tableWidget.setColumnCount(int(self.columns))
            
            self.var_position={}
            self.context = context
           
            for tmyvar in widget.iter('tmyvar'):
                propiedades = {}
                propiedades['column'] =  int(tmyvar.attrib["column"]) - 1
                propiedades['row'] =  int(tmyvar.attrib["row"]) - 1
                
                propiedades['type'] =  tmyvar.attrib["type"]
                propiedades['name'] =  tmyvar.attrib["name"]
                
                if (propiedades['type'] == "nuber"): 
                    propiedades['unidad'] =  tmyvar.attrib["unidad"]
                    propiedades['comparar'] = tmyvar.attrib["compare"]
                    
                    if (propiedades['comparar'] == 'True'):
                        propiedades['max'] = int(tmyvar.attrib["max"])
                        propiedades['min'] = int(tmyvar.attrib["min"])
                        propiedades['color-error'] =  tmyvar.attrib["color-error"]
                        propiedades['color-nominal']=  tmyvar.attrib["color-nominal"]
                    
                    self.var_position[tmyvar.attrib["name"]] = propiedades
                    self.tableWidget.setItem(self.var_position[tmyvar.attrib["name"]]['row'],self.var_position[tmyvar.attrib["name"]]['column'], QTableWidgetItem('{}{}'.format(self.context[tmyvar.attrib["name"]],propiedades["unidad"])))
                        
                elif (propiedades['type'] == "text"):
                    propiedades['comparar'] = tmyvar.attrib["compare"]
                    propiedades['unidad'] =  ""
                    if (propiedades['comparar'] == 'True'):
                        
                        valores = {}
                        lista_valores_colores = tmyvar.attrib["value"].split(';')
                        
                        for valorColor in lista_valores_colores:
                            valor_color = valorColor.split(':')
                            valores[valor_color[0]]=valor_color[1]
                        
                        propiedades['value'] = valores
                        
                        propiedades['color-nominal'] = tmyvar.attrib["color-nominal"]
                
                    self.var_position[tmyvar.attrib["name"]] = propiedades
                    self.tableWidget.setItem(self.var_position[tmyvar.attrib["name"]]['row'],self.var_position[tmyvar.attrib["name"]]['column'], QTableWidgetItem('{}'.format(self.context[tmyvar.attrib["name"]])))
                        
                elif (propiedades['type'] == "title"):
                    propiedades['color-text'] = tmyvar.attrib["color-text"]
                    propiedades['color-background'] = (tmyvar.attrib["color-background"])

                    self.tableWidget.setItem(propiedades['row'],propiedades['column'], QTableWidgetItem('{}'.format(propiedades["name"])))
                    
            
            self.tableWidget.move(0,0)
            tab_contents.addWidget(self.tableWidget,propiedades_recuadro["gillaY"],propiedades_recuadro["gillaX"],propiedades_recuadro["filas"],propiedades_recuadro["columnas"])
            self.tableWidget.resizeColumnsToContents() 
            return  
        
        except:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n Error:')
            print(MSG_ERROR_AL_GENARAR_GRID.format())
            print(tb.format_exc())
            return 
        
    #--------------------------------------------------------------------------------------------------------         
    def update(self,draw):
        try:
            pass
            for var_nombre in self.var_position.keys():                
                self.tableWidget.setItem(self.var_position[var_nombre]['row'],self.var_position[var_nombre]['column'], QTableWidgetItem('{}{}'.format(self.context[var_nombre],self.var_position[var_nombre]['unidad'])))
                
                if self.var_position[var_nombre]['comparar'] == 'True':
                    self.tableWidget.item(self.var_position[var_nombre]['row'],self.var_position[var_nombre]['column']).setBackground(self.getBackGroundColor(self.context[var_nombre],self.var_position[var_nombre]))
               
            return  
        except:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n Error:')
            print(MSG_ERROR_AL_ACTUALIZAR_GRID.format())
            print(tb.format_exc())
            return      

    #-------------------------------------------------------------------------------------------------------- 
    def getBackGroundColor(self,value,propiedades):
        '''     Obtengo el color a partir del valor de la variable  '''
        if (propiedades['type'] == "text"):
            if (value in propiedades['value'].keys()):
                color = propiedades['value'][value] 
            else:
                color = propiedades['color-nominal']
        elif (propiedades['type'] == "nuber"):
            
            color = propiedades['color-nominal']
            if (value >= propiedades['max']):
                color = propiedades['color-error']
            elif (value <= propiedades['min']):
                color = propiedades['color-error'] 
        return(QtGui.QColor(color)) 
        