# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: inventory/v1alpha1/io4edge_inventory.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='inventory/v1alpha1/io4edge_inventory.proto',
  package='io4edgeInventory',
  syntax='proto3',
  serialized_options=b'Z\022inventory/v1alpha1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n*inventory/v1alpha1/io4edge_inventory.proto\x12\x10io4edgeInventory\"C\n\x04Unit\x12\x14\n\x0croot_article\x18\x01 \x01(\t\x12\x15\n\rmajor_version\x18\x02 \x01(\r\x12\x0e\n\x06serial\x18\x03 \x01(\tB\x14Z\x12inventory/v1alpha1b\x06proto3'
)




_UNIT = _descriptor.Descriptor(
  name='Unit',
  full_name='io4edgeInventory.Unit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='root_article', full_name='io4edgeInventory.Unit.root_article', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='major_version', full_name='io4edgeInventory.Unit.major_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serial', full_name='io4edgeInventory.Unit.serial', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=64,
  serialized_end=131,
)

DESCRIPTOR.message_types_by_name['Unit'] = _UNIT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Unit = _reflection.GeneratedProtocolMessageType('Unit', (_message.Message,), {
  'DESCRIPTOR' : _UNIT,
  '__module__' : 'inventory.v1alpha1.io4edge_inventory_pb2'
  # @@protoc_insertion_point(class_scope:io4edgeInventory.Unit)
  })
_sym_db.RegisterMessage(Unit)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
