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




class TetrisWidget(QWidget):
    def __init__(self, context,tab_contents,widget,propiedades_recuadro):
        QWidget.__init__(self, parent)
        self.setup()
        # Create an PyQT4 application object.
#        a = QApplication(sys.argv)       
         
        # The QWidget widget is the base class of all user interface objects in PyQt4.
        w = QWidget()
        # Create progressBar. 
        bar = QProgBar(w)
        bar.resize(320,50)    
        bar.setValue(0)
        bar.move(0,20)
         
        # create timer for progressBar
        timer = QTimer()
        bar.connect(timer,SIGNAL("timeout()"),bar,SLOT("increaseValue()"))
        timer.start(400) 
         
        # Show window
        tab_contents.addWidget(w,1,1,1,1) 
        return

    def update(self,draw):
        try:
            
            self.sc.update_figure()
            if(draw):
                self.sc.draw_plot()
            pass    
            return  
        except:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n Error:')
            return 