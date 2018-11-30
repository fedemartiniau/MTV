# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: metadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import datatypes_pb2 as datatypes__pb2
from . import metadata_instrument_pb2 as metadata__instrument__pb2
from . import metadata_extra_pb2 as metadata__extra__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='metadata.proto',
  package='metadata',
  syntax='proto2',
  serialized_pb=_b('\n\x0emetadata.proto\x12\x08metadata\x1a\x0f\x64\x61tatypes.proto\x1a\x19metadata-instrument.proto\x1a\x14metadata-extra.proto\"\xe7\x01\n\x08Metadata\x12\x34\n\x16\x61\x63quisition_time_stamp\x18\x01 \x01(\x0b\x32\x14.datatypes.TimeStamp\x12\x44\n\x13instrument_metadata\x18\x02 \x01(\x0b\x32\'.metadata.instrument.InstrumentMetadata\x12\x10\n\x08lifetime\x18\x03 \x01(\x04\x12\x11\n\traw_value\x18\x04 \x01(\x0c\x12:\n\x0e\x65xtra_metadata\x18\x05 \x03(\x0b\x32\".metadata.extra.ExtraMetadataEntryBI\n6com.invap.mulitas.serialization.impl.protobuf.metadataB\x0fMetadataPackage')
  ,
  dependencies=[datatypes__pb2.DESCRIPTOR,metadata__instrument__pb2.DESCRIPTOR,metadata__extra__pb2.DESCRIPTOR,])




_METADATA = _descriptor.Descriptor(
  name='Metadata',
  full_name='metadata.Metadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acquisition_time_stamp', full_name='metadata.Metadata.acquisition_time_stamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='instrument_metadata', full_name='metadata.Metadata.instrument_metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lifetime', full_name='metadata.Metadata.lifetime', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw_value', full_name='metadata.Metadata.raw_value', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra_metadata', full_name='metadata.Metadata.extra_metadata', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=95,
  serialized_end=326,
)

_METADATA.fields_by_name['acquisition_time_stamp'].message_type = datatypes__pb2._TIMESTAMP
_METADATA.fields_by_name['instrument_metadata'].message_type = metadata__instrument__pb2._INSTRUMENTMETADATA
_METADATA.fields_by_name['extra_metadata'].message_type = metadata__extra__pb2._EXTRAMETADATAENTRY
DESCRIPTOR.message_types_by_name['Metadata'] = _METADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Metadata = _reflection.GeneratedProtocolMessageType('Metadata', (_message.Message,), dict(
  DESCRIPTOR = _METADATA,
  __module__ = 'metadata_pb2'
  # @@protoc_insertion_point(class_scope:metadata.Metadata)
  ))
_sym_db.RegisterMessage(Metadata)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n6com.invap.mulitas.serialization.impl.protobuf.metadataB\017MetadataPackage'))
# @@protoc_insertion_point(module_scope)
