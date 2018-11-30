import sys
import numpy as np
sys.path.append("./mulitas_protobuf/")

from mulitas_protobuf.data_collection_pb2 import *
from mulitas_protobuf.tmy_variable_pb2 import *
from mulitas_protobuf.measurement_unit_pb2 import *
from mulitas_protobuf.datatypes_pb2 import *

class DummyTelemetryGenerator:
	def __init__(self):
		self.t = 0
		self.freq = 10
		self.dt = 0.1

	def tick(self,dt):
		self.t = self.t + dt

	def generate(self, n):
		dc = DataCollection()		
		for i in range(n):
			v = Variable()
			v.variable_fqvn = "VARIABLE_DUMMY_"+str(i)
			v.data_type = VariableType_AMOUNT
			v.amountMeasurement.value.floatinPointValue.value = 100.0*np.sin((self.freq*self.t)/(2*np.pi))
			#v.amountMeasurement.value.valid
			#v.amountMeasurement.value.unit
			#v.amountMeasurement.value.unit_prefix
			#v.amountMeasurement.value.error
			dcr = DataCollectionRecord()
			dcr.type = VARIABLE
			dcr.variable.CopyFrom(v)
			dc.record_list.extend([dcr])
		return dc
		#return dc.SerializeToString()