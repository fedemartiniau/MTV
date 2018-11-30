# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tmy-variable.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import measurement_alpha_pb2 as measurement__alpha__pb2
from . import measurement_amount_pb2 as measurement__amount__pb2
from . import measurement_binary_pb2 as measurement__binary__pb2
from . import measurement_logical_pb2 as measurement__logical__pb2
from . import measurement_unavail_pb2 as measurement__unavail__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tmy-variable.proto',
  package='tmy.variable',
  syntax='proto2',
  serialized_pb=_b('\n\x12tmy-variable.proto\x12\x0ctmy.variable\x1a\x17measurement-alpha.proto\x1a\x18measurement-amount.proto\x1a\x18measurement-binary.proto\x1a\x19measurement-logical.proto\x1a\x19measurement-unavail.proto\"\xb3\x03\n\x08Variable\x12\x15\n\rvariable_fqvn\x18\x01 \x01(\t\x12-\n\tdata_type\x18\x02 \x01(\x0e\x32\x1a.tmy.variable.VariableType\x12K\n\x17\x61lphanumericMeasurement\x18\x03 \x01(\x0b\x32*.measurement.alpha.AlphanumericMeasurement\x12@\n\x11\x61mountMeasurement\x18\x04 \x01(\x0b\x32%.measurement.amount.AmountMeasurement\x12@\n\x11\x62inaryMeasurement\x18\x05 \x01(\x0b\x32%.measurement.binary.BinaryMeasurement\x12\x43\n\x12\x62ooleanMeasurement\x18\x06 \x01(\x0b\x32\'.measurement.logical.BooleanMeasurement\x12K\n\x16unavailableMeasurement\x18\x07 \x01(\x0b\x32+.measurement.unavail.UnavailableMeasurement*\x97\x01\n\x0cVariableType\x12\x1c\n\x18VariableType_UNAVAILABLE\x10\x00\x12\x18\n\x14VariableType_BOOLEAN\x10\x01\x12\x17\n\x13VariableType_AMOUNT\x10\x02\x12\x1d\n\x19VariableType_ALPHANUMERIC\x10\x03\x12\x17\n\x13VariableType_BINARY\x10\x04\x42\x38\n6com.invap.mulitas.serialization.impl.protobuf.variable')
  ,
  dependencies=[measurement__alpha__pb2.DESCRIPTOR,measurement__amount__pb2.DESCRIPTOR,measurement__binary__pb2.DESCRIPTOR,measurement__logical__pb2.DESCRIPTOR,measurement__unavail__pb2.DESCRIPTOR,])

_VARIABLETYPE = _descriptor.EnumDescriptor(
  name='VariableType',
  full_name='tmy.variable.VariableType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VariableType_UNAVAILABLE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VariableType_BOOLEAN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VariableType_AMOUNT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VariableType_ALPHANUMERIC', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VariableType_BINARY', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=606,
  serialized_end=757,
)
_sym_db.RegisterEnumDescriptor(_VARIABLETYPE)

VariableType = enum_type_wrapper.EnumTypeWrapper(_VARIABLETYPE)
VariableType_UNAVAILABLE = 0
VariableType_BOOLEAN = 1
VariableType_AMOUNT = 2
VariableType_ALPHANUMERIC = 3
VariableType_BINARY = 4



_VARIABLE = _descriptor.Descriptor(
  name='Variable',
  full_name='tmy.variable.Variable',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='variable_fqvn', full_name='tmy.variable.Variable.variable_fqvn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='tmy.variable.Variable.data_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alphanumericMeasurement', full_name='tmy.variable.Variable.alphanumericMeasurement', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amountMeasurement', full_name='tmy.variable.Variable.amountMeasurement', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='binaryMeasurement', full_name='tmy.variable.Variable.binaryMeasurement', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='booleanMeasurement', full_name='tmy.variable.Variable.booleanMeasurement', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unavailableMeasurement', full_name='tmy.variable.Variable.unavailableMeasurement', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=168,
  serialized_end=603,
)

_VARIABLE.fields_by_name['data_type'].enum_type = _VARIABLETYPE
_VARIABLE.fields_by_name['alphanumericMeasurement'].message_type = measurement__alpha__pb2._ALPHANUMERICMEASUREMENT
_VARIABLE.fields_by_name['amountMeasurement'].message_type = measurement__amount__pb2._AMOUNTMEASUREMENT
_VARIABLE.fields_by_name['binaryMeasurement'].message_type = measurement__binary__pb2._BINARYMEASUREMENT
_VARIABLE.fields_by_name['booleanMeasurement'].message_type = measurement__logical__pb2._BOOLEANMEASUREMENT
_VARIABLE.fields_by_name['unavailableMeasurement'].message_type = measurement__unavail__pb2._UNAVAILABLEMEASUREMENT
DESCRIPTOR.message_types_by_name['Variable'] = _VARIABLE
DESCRIPTOR.enum_types_by_name['VariableType'] = _VARIABLETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Variable = _reflection.GeneratedProtocolMessageType('Variable', (_message.Message,), dict(
  DESCRIPTOR = _VARIABLE,
  __module__ = 'tmy_variable_pb2'
  # @@protoc_insertion_point(class_scope:tmy.variable.Variable)
  ))
_sym_db.RegisterMessage(Variable)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n6com.invap.mulitas.serialization.impl.protobuf.variable'))
# @@protoc_insertion_point(module_scope)
