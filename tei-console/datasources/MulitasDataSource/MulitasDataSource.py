import sys
import pika
import threading
import signal
import time
import numpy as np
sys.path.append("./MulitasDataSource/mulitas_protobuf")

from datasources.MulitasDataSource.mulitas_protobuf.data_collection_pb2 import *
from datasources.MulitasDataSource.mulitas_protobuf.tmy_variable_pb2 import *
from datasources.MulitasDataSource.mulitas_protobuf.measurement_unit_pb2 import *
from datasources.MulitasDataSource.mulitas_protobuf.datatypes_pb2 import *


class MulitasDataSource(threading.Thread):

	def __init__(self,context, host='localhost', port = 5672, user="admin", password="admin", exchange='mulitas.example', routing_key='variable1'):
		threading.Thread.__init__(self)
		self.context = context
		credentials = pika.PlainCredentials( user, password )
		self.connection = pika.BlockingConnection( pika.ConnectionParameters(host,port,"/",credentials) )
		self.channel = self.connection.channel()
		result = self.channel.queue_declare(exclusive=True)
		queue_name = result.method.queue
		self.channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=routing_key)
		self.channel.basic_consume(self.callback, queue=queue_name, no_ack=True)
		self.start()

	def callback(self,ch, method, properties, body):
		dc = DataCollection()
		dc.ParseFromString(body)

		for dcr in dc.record_list:
			if VARIABLE == dcr.type:
				if VariableType_AMOUNT == dcr.variable.data_type:
					self.context[dcr.variable.variable_fqvn] = dcr.variable.amountMeasurement.value.floatinPointValue.value
		self.context["TIMESTAMP"] = int(round(time.time() * 1000))
		#print(self.context)

	def run(self):
		print(' [] Waiting for messages.')
		self.channel.start_consuming()

	def stop(self):
		self.channel.stop_consuming()
		self.channel.close()
		self.join()