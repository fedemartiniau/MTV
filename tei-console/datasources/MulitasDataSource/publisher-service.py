#!/usr/bin/env python
import pika
import time
from DummyTelemetryGenerator import *

dtg = DummyTelemetryGenerator()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

try:
	while True:
		dtg.tick(0.5)
		dc = dtg.generate(10)
		channel.basic_publish(exchange='tei',routing_key='hello',body=dc.SerializeToString())
		print(" [x] Sent: ", dc.__str__() )
		time.sleep(1)
except (KeyboardInterrupt, SystemExit):
	print("Stopping...")
connection.close()