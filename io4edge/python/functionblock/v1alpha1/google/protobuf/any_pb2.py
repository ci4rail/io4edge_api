# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: functionblock/v1alpha1/google/protobuf/any.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='functionblock/v1alpha1/google/protobuf/any.proto',
  package='google.protobuf',
  syntax='proto3',
  serialized_options=_b('\n\023com.google.protobufB\010AnyProtoP\001Z,google.golang.org/protobuf/types/known/anypb\242\002\003GPB\252\002\036Google.Protobuf.WellKnownTypes'),
  serialized_pb=_b('\n0functionblock/v1alpha1/google/protobuf/any.proto\x12\x0fgoogle.protobuf\"&\n\x03\x41ny\x12\x10\n\x08type_url\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x42v\n\x13\x63om.google.protobufB\x08\x41nyProtoP\x01Z,google.golang.org/protobuf/types/known/anypb\xa2\x02\x03GPB\xaa\x02\x1eGoogle.Protobuf.WellKnownTypesb\x06proto3')
)




_ANY = _descriptor.Descriptor(
  name='Any',
  full_name='google.protobuf.Any',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_url', full_name='google.protobuf.Any.type_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b('').decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='google.protobuf.Any.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(''),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['Any'] = _ANY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Any = _reflection.GeneratedProtocolMessageType('Any', (_message.Message,), dict(
  DESCRIPTOR = _ANY,
  __module__ = 'functionblock.v1alpha1.google.protobuf.any_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Any)
  ))
_sym_db.RegisterMessage(Any)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
