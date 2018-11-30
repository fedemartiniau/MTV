#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = "Multi Widgets"
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
import random
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
MSG_ERROR_AL_GENARAR_PLOT = 'ERROR 001: '+__title__+ ' Error al intentar armar el plot'
MSG_ERROR_AL_ACTUALIZAR_PLOT = 'ERROR 002: '+__title__+ ' Error al intentar actualizar el plot'
#################################################################################################################################################################
###### FUNCION PRINCIPAL ######
class MultiPlotWidgets(QWidget):
    def __init__(self, context,tab_contents,widget,propiedades_recuadro):
        try:
            self.context = context
            self.variables = []
            self.titulo = widget.attrib["title"]
            self.propiedades_variables = {}            

            #-------------------------------------------
            for tmyvar in widget.iter('tmyvar'):
                self.variables.append(tmyvar.attrib["name"])
                propiedades = {}
                                
                propiedades['comparar'] = tmyvar.attrib["compare"]
                if (propiedades['comparar'] == 'True'):
                    propiedades['max'] =  int(tmyvar.attrib["max"])
                    propiedades['min']=  int(tmyvar.attrib["min"])
                    propiedades['color-true'] =  (tmyvar.attrib["color-nominal"])
                    propiedades['color-false']=  (tmyvar.attrib["color-error"]) 
                    propiedades['sombra'] =  (tmyvar.attrib["sombra"]) 
                    propiedades['color-sombra'] =  (tmyvar.attrib["color-sombra"]) 
                    
                self.propiedades_variables[tmyvar.attrib["name"]] = propiedades
                
            #-------------------------------------------    
            self.sc = MyDynamicMplCanvas(self.context,self.propiedades_variables,self.titulo, width=5, height=5)
            self.sc.set_title = 'Plot'
            tab_contents.addWidget(self.sc,propiedades_recuadro["gillaY"],propiedades_recuadro["gillaX"],propiedades_recuadro["filas"],propiedades_recuadro["columnas"])
   
            return  
        except:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n Error:')
            print(MSG_ERROR_AL_GENARAR_PLOT.format())
            print(tb.format_exc())
            return 
        
    #--------------------------------------------------------------------------------------------------------         
    def update(self,draw):
        try:
            
            self.sc.update_figure()
            if(draw):
                self.sc.draw_plot()
            pass    
            return  
        except:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n Error:')
            print(MSG_ERROR_AL_ACTUALIZAR_PLOT.format())
            print(tb.format_exc())
            return 
    #--------------------------------------------------------------------------------------------------------         
    def update_data(self):
        try:
            
            self.sc.update_figure()
            pass    
            return  
        except:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n Error:')
            print(MSG_ERROR_AL_ACTUALIZAR_PLOT.format())
            print(tb.format_exc())
            return 
        
    
#--------------------------------------------------------------------------------------------------------    
class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        
        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding,QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        

    #-------------------------------------------------------------------------------------------------------- 
    def compute_initial_figure(self):
        pass

#--------------------------------------------------------------------------------------------------------
class MyDynamicMplCanvas(MyMplCanvas):
    """A canvas that updates itself every second with a new plot."""
    def __init__(self,context,variables,titulo, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)

        self.context = context
        self.variables = variables

        self.bufsize = 100
        self.historial_variable = {}
        self.historial_variable['y'] = {}
        self.historial_variable['x'] = {}
        
        self.historial_variable['pausaX'] = {}
        self.historial_variable['pausaY'] = {}
        
        self.historial_variable['x'] = np.zeros(self.bufsize)
        
        for i in range(self.bufsize):
            self.historial_variable['x'][i] = context['TIMESTAMP']
            self.historial_variable['pausaX'][i] = context['TIMESTAMP']
            
            
        for variable_nombre in self.variables.keys():
            self.historial_variable['y'][variable_nombre] = np.zeros(self.bufsize)
            self.historial_variable['pausaY'][variable_nombre] = np.zeros(self.bufsize)
            
        
        self.titulo = titulo
    #--------------------------------------------------------------------------------------------------------    
    def compute_initial_figure(self):
        return
    
    #--------------------------------------------------------------------------------------------------------    
    def set_title(self,title):
        self.title=title
    
    #--------------------------------------------------------------------------------------------------------   
    def update_figure(self):
        self.historial_variable['x'] = np.roll(self.historial_variable['x'],-1)
        self.historial_variable['x'][self.bufsize-1] = self.context['TIMESTAMP']
        
        for variable_nombre in self.variables:
            self.historial_variable['y'][variable_nombre] = np.roll(self.historial_variable['y'][variable_nombre],-1) 
            self.historial_variable['y'][variable_nombre][self.bufsize-1] = self.context[variable_nombre]
        

    #--------------------------------------------------------------------------------------------------------         
    def draw_plot(self):
        self.axes.clear()  

        nombreVar=''
        for variable_nombre in self.variables.keys():         
            self.axes.plot( self.historial_variable['x'],self.historial_variable['y'][variable_nombre],label=variable_nombre)
            nombreVar=variable_nombre
        
        if (self.variables[nombreVar]['comparar'] == 'True'):
            self.axes.set_facecolor(self.getBackGroundColot(self.context[nombreVar],self.variables[nombreVar]['max'],self.variables[nombreVar]['min'],self.variables[nombreVar]['color-true'],self.variables[nombreVar]['color-false']))
            if (self.variables[nombreVar]['sombra'] == 'True'):
                self.axes.fill_between(self.historial_variable['x'], self.historial_variable['y'][variable_nombre], facecolor=self.variables[nombreVar]['color-sombra'], interpolate=True)

        self.axes.set_title(self.titulo)
        self.axes.set_xlabel("X")
        self.axes.set_ylabel("Y")
        self.axes.legend(loc='upper left')
        self.axes.grid(which="both",axis="both")              
        self.draw()  
    
    #-------------------------------------------------------------------------------------------------------- 
    def getBackGroundColot(self,value,maximo,minimo,colorT,colorF):
        '''     Obtengo el color a partir del valor de la variable  '''
        color = colorT
        if (value >= maximo):
            color = colorF
        elif (value <= minimo):
            color = colorF   
        return(color)
   
    