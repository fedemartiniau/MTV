import sys
sys.path.append('./datasources/MulitasDataSource/mulitas_protobuf')
from datasources.MulitasDataSource.MulitasDataSource import *

context = {}

mds = MulitasDataSource(context)

try:
	input("Press enter to continue")
except SyntaxError:
	pass

mds.stop()
print("Ended gracefully")