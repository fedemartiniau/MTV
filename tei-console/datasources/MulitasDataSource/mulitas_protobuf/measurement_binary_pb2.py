# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: measurement-binary.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import metadata_pb2 as metadata__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='measurement-binary.proto',
  package='measurement.binary',
  syntax='proto2',
  serialized_pb=_b('\n\x18measurement-binary.proto\x12\x12measurement.binary\x1a\x0emetadata.proto\"V\n\x11\x42inaryMeasurement\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\r\n\x05valid\x18\x02 \x01(\x08\x12$\n\x08metadata\x18\x0f \x01(\x0b\x32\x12.metadata.MetadataB;\n9com.invap.mulitas.serialization.impl.protobuf.measurement')
  ,
  dependencies=[metadata__pb2.DESCRIPTOR,])




_BINARYMEASUREMENT = _descriptor.Descriptor(
  name='BinaryMeasurement',
  full_name='measurement.binary.BinaryMeasurement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='measurement.binary.BinaryMeasurement.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='valid', full_name='measurement.binary.BinaryMeasurement.valid', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='measurement.binary.BinaryMeasurement.metadata', index=2,
      number=15, type=11, cpp_type=10, label=1,
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
  serialized_start=64,
  serialized_end=150,
)

_BINARYMEASUREMENT.fields_by_name['metadata'].message_type = metadata__pb2._METADATA
DESCRIPTOR.message_types_by_name['BinaryMeasurement'] = _BINARYMEASUREMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BinaryMeasurement = _reflection.GeneratedProtocolMessageType('BinaryMeasurement', (_message.Message,), dict(
  DESCRIPTOR = _BINARYMEASUREMENT,
  __module__ = 'measurement_binary_pb2'
  # @@protoc_insertion_point(class_scope:measurement.binary.BinaryMeasurement)
  ))
_sym_db.RegisterMessage(BinaryMeasurement)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n9com.invap.mulitas.serialization.impl.protobuf.measurement'))
# @@protoc_insertion_point(module_scope)
