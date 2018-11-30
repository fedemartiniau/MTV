import threading
import time
import random
from PyQt5.QtCore import pyqtSlot, QThread
import numpy as np

# Concepto cada DataSource se ejecuta en un hilo independiente y actualiza alguna TMY en el contexto
#
#
class DummyDataSource(QThread):
    def __init__(self, context, params):
        QThread.__init__(self)
		
        """
			Contexto: diccionario global en el que publica variables recibidas
			Params: parámetros del DataSource (de conección si es Rabbit, de configuración si es BTE, etc. Puede ser un nodo XML)
		"""
        self.context = context
        self.t = 0
        # Es responsable de crear sus variables en el contexto
        self.context["VARIABLE_DUMMY_1"] = 10
        self.context["VARIABLE_DUMMY_2"] = 20
        self.context["VARIABLE_DUMMY_3"] = 30
        self.context["VARIABLE_DUMMY_4"] = 1
        self.context["VARIABLE_DUMMY_t1"] = "VARIABLE_DUMMY_1"
        self.context["VARIABLE_DUMMY_t2"] = "VARIABLE_DUMMY_2"
        self.context["VARIABLE_DUMMY_t3"] = "VARIABLE_DUMMY_3"
        self.context["VARIABLE_DUMMY_t4"] = "VARIABLE_DUMMY_4"
        self.context["VARIABLE_DUMMY_5"] = 2
        self.context["VARIABLE_DUMMY_6"] = 3
        self.context["VARIABLE_DUMMY_7"] = 3
        self.context["VARIABLE_DUMMY_8"] = 3
        self.context["VARIABLE_DUMMY_t5"] = "VARIABLE_DUMMY_5"
        self.context["VARIABLE_DUMMY_t6"] = "VARIABLE_DUMMY_6"
        self.context["VARIABLE_DUMMY_t7"] = "VARIABLE_DUMMY_7"
        self.context["VARIABLE_DUMMY_t8"] = "VARIABLE_DUMMY_8"
        self.context["PTU_N"] = 0
        self.context["PTU_R"] = 0
        
        self.context["var_1"] = 0
        self.context["var_2"] = 0
        
        self.context["Cotroller_Status_01"] = 0
        self.context["Cotroller_Status_02"] = 0
        self.context["Cotroller_Status_03"] = 0
        self.context["Cotroller_Status_04"] = 0
        self.context["Cotroller_Status_05"] = 0
        self.context["Cotroller_Status_06"] = 0
        self.context["Cotroller_Status_07"] = 0
        self.context["Cotroller_Status_08"] = 0
        self.context["Cotroller_Status_09"] = 0
        self.context["Cotroller_Status_10"] = 0
        self.context["Cotroller_Status_11"] = 0
        self.context["Cotroller_Status_12"] = 0
        self.context["Cotroller_Status_13"] = 0
        self.context["Cotroller_Status_14"] = 0
        self.context["Cotroller_Status_15"] = 0
        self.context["Cotroller_Status_16"] = 0
        self.context["Cotroller_Status_17"] = 0
        self.context["Cotroller_Status_18"] = 0
        self.context["Cotroller_Status_19"] = 0
        self.context["Cotroller_Status_20"] = 0
        
        self.context["Status_1"] = 'ERROR'
        self.context["Status_2"] = 'ERROR'
        self.context["Status_3"] = 'True'
        self.context["Status_4"] = 'True'
        
        self.context["CANvap_Mode_01"] = 0
        self.context["CANvap_Mode_02"] = 0
        self.context["CANvap_Mode_03"] = 0
        self.context["CANvap_Mode_04"] = 0
        self.context["CANvap_Mode_05"] = 0
        self.context["CANvap_Mode_06"] = 0
        self.context["CANvap_Mode_07"] = 0
        self.context["CANvap_Mode_08"] = 0
        self.context["CANvap_Mode_09"] = 0
        self.context["CANvap_Mode_10"] = 1
        self.context["CANvap_Mode_11"] = 1
        self.context["CANvap_Mode_12"] = 1
        self.context["CANvap_Mode_13"] = 1
        self.context["CANvap_Mode_14"] = 0
        self.context["CANvap_Mode_15"] = 0
        self.context["CANvap_Mode_16"] = 0
        self.context["CANvap_Mode_17"] = 0
        self.context["CANvap_Mode_18"] = 0
        self.context["CANvap_Mode_19"] = 0
        self.context["CANvap_Mode_20"] = 0
        
        
        self.context["Alarm_Count_01"] = 0
        self.context["Alarm_Count_02"] = 0
        self.context["Alarm_Count_03"] = 0
        self.context["Alarm_Count_04"] = 0
        self.context["Alarm_Count_05"] = 0
        self.context["Alarm_Count_06"] = 0
        self.context["Alarm_Count_07"] = 0
        self.context["Alarm_Count_08"] = 0
        self.context["Alarm_Count_09"] = 0
        self.context["Alarm_Count_10"] = 0
        self.context["Alarm_Count_11"] = 0
        self.context["Alarm_Count_12"] = 0
        self.context["Alarm_Count_13"] = 0
        self.context["Alarm_Count_14"] = 0
        self.context["Alarm_Count_15"] = 0
        self.context["Alarm_Count_16"] = 0
        self.context["Alarm_Count_17"] = 0
        self.context["Alarm_Count_18"] = 0
        self.context["Alarm_Count_19"] = 0
        self.context["Alarm_Count_20"] = 0
        
        self.context["SYNC_status_01"] = 0
        self.context["SYNC_status_02"] = 0
        self.context["SYNC_status_03"] = 0
        self.context["SYNC_status_04"] = 0
        self.context["SYNC_status_05"] = 0
        self.context["SYNC_status_06"] = 0
        self.context["SYNC_status_07"] = 0
        self.context["SYNC_status_08"] = 0
        self.context["SYNC_status_09"] = 0
        self.context["SYNC_status_10"] = 0
        self.context["SYNC_status_11"] = 0
        self.context["SYNC_status_12"] = 0
        self.context["SYNC_status_13"] = 0
        self.context["SYNC_status_14"] = 0
        self.context["SYNC_status_15"] = 0
        self.context["SYNC_status_16"] = 0
        self.context["SYNC_status_17"] = 0
        self.context["SYNC_status_18"] = 0
        self.context["SYNC_status_19"] = 0
        self.context["SYNC_status_20"] = 0
        
        self.context["Active_Bus_01"] = 0
        self.context["Active_Bus_02"] = 0
        self.context["Active_Bus_03"] = 0
        self.context["Active_Bus_04"] = 0
        self.context["Active_Bus_05"] = 0
        self.context["Active_Bus_06"] = 0
        self.context["Active_Bus_07"] = 0
        self.context["Active_Bus_08"] = 0
        self.context["Active_Bus_09"] = 0
        self.context["Active_Bus_10"] = 0
        self.context["Active_Bus_11"] = 0
        self.context["Active_Bus_12"] = 0
        self.context["Active_Bus_13"] = 0
        self.context["Active_Bus_14"] = 0
        self.context["Active_Bus_15"] = 0
        self.context["Active_Bus_16"] = 0
        self.context["Active_Bus_17"] = 0
        self.context["Active_Bus_18"] = 0
        self.context["Active_Bus_19"] = 0
        self.context["Active_Bus_20"] = 0
        
        self.context["TIMESTAMP"] = (round(time.time() * 1000))
        self.runs = True
        self.start()
        return

    def __del__(self):
        self.wait()		

    def run(self):
        while (self.runs == True):
            self.t = self.t + (1/1000)
            self.context["VARIABLE_DUMMY_5"] = self.context["VARIABLE_DUMMY_5"] + 9*np.sin(2*np.pi*5*(self.t))
            self.context["VARIABLE_DUMMY_6"] = self.context["VARIABLE_DUMMY_6"] + 8*np.cos(2*np.pi*10*(self.t))
            self.context["VARIABLE_DUMMY_7"] = self.context["VARIABLE_DUMMY_7"] + 7*np.sin(2*np.pi*15*(self.t))
            self.context["VARIABLE_DUMMY_8"] = self.context["VARIABLE_DUMMY_8"] + 6*np.cos(2*np.pi*70*(self.t))
            self.context["TIMESTAMP"] = int(round(time.time() * 1000))
            
            if (random.randint(0,50) == 5):
                self.context["VARIABLE_DUMMY_1"] = self.context["VARIABLE_DUMMY_1"] + random.randint(1,11)
                self.context["VARIABLE_DUMMY_2"] = self.context["VARIABLE_DUMMY_2"] + random.randint(1,21)
                self.context["VARIABLE_DUMMY_3"] = self.context["VARIABLE_DUMMY_3"] + random.randint(1,31)
                self.context["VARIABLE_DUMMY_4"] = self.context["VARIABLE_DUMMY_4"] + random.randint(1,41)
    
                self.context["PTU_N"] = self.context["PTU_N"] + (random.randint(-50,50))
                self.context["PTU_R"] = self.context["PTU_R"] + (random.randint(-50,50))
                self.context["var_1"] = (random.randint(0,50))
                self.context["var_2"] = (random.randint(0,50))
                
                
                self.context["Cotroller_Status_01"] = random.randint(-50,50)
                self.context["Cotroller_Status_02"] = random.randint(-50,50)
                self.context["Cotroller_Status_03"] = random.randint(-50,50)
                self.context["Cotroller_Status_04"] = random.randint(-50,50)
                self.context["Cotroller_Status_05"] = random.randint(-50,50)
                self.context["Cotroller_Status_06"] = random.randint(-50,50)
                self.context["Cotroller_Status_07"] = random.randint(-50,50)
                self.context["Cotroller_Status_08"] = random.randint(-50,50)
                self.context["Cotroller_Status_09"] = random.randint(-50,50)
                self.context["Cotroller_Status_10"] = random.randint(-50,50)
                self.context["Cotroller_Status_11"] = random.randint(-50,50)
                self.context["Cotroller_Status_12"] = random.randint(-50,50)
                self.context["Cotroller_Status_13"] = random.randint(-50,50)
                self.context["Cotroller_Status_14"] = random.randint(-50,50)
                self.context["Cotroller_Status_15"] = random.randint(-50,50)
                self.context["Cotroller_Status_16"] = random.randint(-50,50)
                self.context["Cotroller_Status_17"] = random.randint(-50,50)
                self.context["Cotroller_Status_18"] = random.randint(-50,50)
                self.context["Cotroller_Status_19"] = random.randint(-50,50)
                self.context["Cotroller_Status_20"] = random.randint(-50,50)
                
                self.context["CANvap_Mode_01"] = random.randint(-10,10)
                self.context["CANvap_Mode_02"] = random.randint(-10,10)
                self.context["CANvap_Mode_03"] = random.randint(-10,10)
                self.context["CANvap_Mode_04"] = random.randint(-10,10)
                self.context["CANvap_Mode_05"] = random.randint(-10,10)
                self.context["CANvap_Mode_06"] = random.randint(-10,10)
                self.context["CANvap_Mode_07"] = random.randint(-10,10)
                self.context["CANvap_Mode_08"] = random.randint(-10,10)
                self.context["CANvap_Mode_09"] = random.randint(-10,10)
                self.context["CANvap_Mode_10"] = random.randint(-10,10)
                self.context["CANvap_Mode_11"] = random.randint(-10,10)
                self.context["CANvap_Mode_12"] = random.randint(-10,10)
                self.context["CANvap_Mode_13"] = random.randint(-10,10)
                self.context["CANvap_Mode_14"] = random.randint(-10,10)
                self.context["CANvap_Mode_15"] = random.randint(-10,10)
                self.context["CANvap_Mode_16"] = random.randint(-10,10)
                self.context["CANvap_Mode_17"] = random.randint(-10,10)
                self.context["CANvap_Mode_18"] = random.randint(-10,10)
                self.context["CANvap_Mode_19"] = random.randint(-10,10)
                self.context["CANvap_Mode_20"] = random.randint(-10,10)
                
                self.context["Alarm_Count_01"] += random.randint(0,1)
                self.context["Alarm_Count_02"] += random.randint(0,1)
                self.context["Alarm_Count_03"] += random.randint(0,1)
                self.context["Alarm_Count_04"] += random.randint(0,1)
                self.context["Alarm_Count_05"] += random.randint(0,1)
                self.context["Alarm_Count_06"] += random.randint(0,1)
                self.context["Alarm_Count_07"] += random.randint(0,1)
                self.context["Alarm_Count_08"] += random.randint(0,1)
                self.context["Alarm_Count_09"] += random.randint(0,1)
                self.context["Alarm_Count_10"] += random.randint(0,1)
                self.context["Alarm_Count_11"] += random.randint(0,1)
                self.context["Alarm_Count_12"] += random.randint(0,1)
                self.context["Alarm_Count_13"] += random.randint(0,1)
                self.context["Alarm_Count_14"] += random.randint(0,1)
                self.context["Alarm_Count_15"] += random.randint(0,1)
                self.context["Alarm_Count_16"] += random.randint(0,1)
                self.context["Alarm_Count_17"] += random.randint(0,1)
                self.context["Alarm_Count_18"] += random.randint(0,1)
                self.context["Alarm_Count_19"] += random.randint(0,1)
                self.context["Alarm_Count_20"] += random.randint(0,1)
                
        
                self.context["SYNC_status_01"] = random.randint(0,1)
                self.context["SYNC_status_02"] = random.randint(0,1)
                self.context["SYNC_status_03"] = random.randint(0,1)
                self.context["SYNC_status_04"] = random.randint(0,1)
                self.context["SYNC_status_05"] = random.randint(0,1)
                self.context["SYNC_status_06"] = random.randint(0,1)
                self.context["SYNC_status_07"] = random.randint(0,1)
                self.context["SYNC_status_08"] = random.randint(0,1)
                self.context["SYNC_status_09"] = random.randint(0,1)
                self.context["SYNC_status_10"] = random.randint(0,1)
                self.context["SYNC_status_11"] = random.randint(0,1)
                self.context["SYNC_status_12"] = random.randint(0,1)
                self.context["SYNC_status_13"] = random.randint(0,1)
                self.context["SYNC_status_14"] = random.randint(0,1)
                self.context["SYNC_status_15"] = random.randint(0,1)
                self.context["SYNC_status_16"] = random.randint(0,1)
                self.context["SYNC_status_17"] = random.randint(0,1)
                self.context["SYNC_status_18"] = random.randint(0,1)
                self.context["SYNC_status_19"] = random.randint(0,1)
                self.context["SYNC_status_20"] = random.randint(0,1)
                
                self.context["Active_Bus_01"] = random.randint(0,1)
                self.context["Active_Bus_02"] = random.randint(0,1)
                self.context["Active_Bus_03"] = random.randint(0,1)
                self.context["Active_Bus_04"] = random.randint(0,1)
                self.context["Active_Bus_05"] = random.randint(0,1)
                self.context["Active_Bus_06"] = random.randint(0,1)
                self.context["Active_Bus_07"] = random.randint(0,1)
                self.context["Active_Bus_08"] = random.randint(0,1)
                self.context["Active_Bus_09"] = random.randint(0,1)
                self.context["Active_Bus_10"] = random.randint(0,1)
                self.context["Active_Bus_11"] = random.randint(0,1)
                self.context["Active_Bus_12"] = random.randint(0,1)
                self.context["Active_Bus_13"] = random.randint(0,1)
                self.context["Active_Bus_14"] = random.randint(0,1)
                self.context["Active_Bus_15"] = random.randint(0,1)
                self.context["Active_Bus_16"] = random.randint(0,1)
                self.context["Active_Bus_17"] = random.randint(0,1)
                self.context["Active_Bus_18"] = random.randint(0,1)
                self.context["Active_Bus_19"] = random.randint(0,1)
                self.context["Active_Bus_20"] = random.randint(0,1)
                
                if(random.randint(0,4)==3):
                    self.context["Status_1"] = 'ERROR'
                else:
                    self.context["Status_1"] = 'OK'
                
                if(random.randint(0,5)==3):
                    self.context["Status_2"] = 'ERROR'
                else:
                    self.context["Status_2"] = 'OK'
                
                if(random.randint(0,6)==3):
                    self.context["Status_3"] = 'False'
                else:
                    self.context["Status_3"] = 'True'
                
                if(random.randint(0,10)==3):
                    self.context["Status_4"] = 'False'
                else:
                    self.context["Status_4"] = 'True'
                
            time.sleep(1/100)

    def stop(self):
        self.runs = False