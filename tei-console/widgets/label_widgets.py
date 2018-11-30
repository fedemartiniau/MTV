#!/usr/bin/env python
# -*- coding: utf-8 -*-
__title__ = "Label Widgets"
__version__ = "v0.0.1"
__proyecto__ = ""
__company__ = "INVAP S.E."
__status__ = "Desarrollo"
__description___=''' 
            La idea de este script es que tenga la capacidad de armar un label y agregarlo al tab actal.
 '''
__author__ = 'Federico Martiniau'
__copyright__ = "Copyright 2018, INVAP S.E."
__credits__ = ["Nicolas Horro","Federico Martiniau"]
__destails__='''   '''

# ###### IMPORTS ######
import sys
import traceback as tb
import random
import xml.etree.ElementTree as et
import datetime
#QT imports
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import *
from PyQt5.QtCore import *

# ###### IMPORTS PROPIOS ######
# ###### VARIABLES ESTATICAS ######
# ###### ERRORES ######
# Todos los mensajes de error y los alertas deben estar identificados con un número (código) único para el script 

MSG_ERROR_GENERAL = 'ERROR 000: Error inesperado al ejecutar el script'+' '+__title__
MSG_ERROR_AL_GENARAR_LABET = 'ERROR 001: '+__title__+ ' Error al intentar armar el label'
MSG_ERROR_AL_ACTUALIZAR_LABET = 'ERROR 002: '+__title__+ ' Error al intentar actualizar el label'
#################################################################################################################################################################
###### FUNCION PRINCIPAL ######
class LabelWidgets(QWidget):
    def __init__(self, context,tab_contents,widget,propiedades_recuadro):
        try:
            self.labels = {}
            self.context = context                  
            
            for tmyvar in widget.iter('tmyvar'):
                
                self.labels[tmyvar.attrib["name"]] = QLabel()
                self.labels[tmyvar.attrib["name"]].setText("{}: {}".format(tmyvar.attrib["name"],self.context[tmyvar.attrib["name"]]))

                tab_contents.addWidget(self.labels[tmyvar.attrib["name"]],propiedades_recuadro["gillaY"],propiedades_recuadro["gillaX"],propiedades_recuadro["filas"],propiedades_recuadro["columnas"])
            

        except:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n Error:')
            print(MSG_ERROR_AL_GENARAR_LABET.format())
            print(tb.format_exc())
            return 
        
    #--------------------------------------------------------------------------------------------------------         
    def update(self,draw):
        try:
            
            for label in self.labels.keys():
                self.labels[label].setText("{}: {}".format(label,self.context[label]))
                
            return  
        except:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n Error:')
            print(MSG_ERROR_AL_ACTUALIZAR_LABET.format())
            print(tb.format_exc())
            return         
    
    
    
    
    
    