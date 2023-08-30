# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core_api/v1alpha2/io4edge_core_api.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='core_api/v1alpha2/io4edge_core_api.proto',
  package='io4edgeCoreApi',
  syntax='proto3',
  serialized_options=b'Z\021core_api/v1alpha2',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(core_api/v1alpha2/io4edge_core_api.proto\x12\x0eio4edgeCoreApi\"U\n\x18LoadFirmwareChunkCommand\x12\x14\n\x0c\x63hunk_number\x18\x01 \x01(\r\x12\x15\n\ris_last_chunk\x18\x02 \x01(\x08\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"}\n$ProgramHardwareIdentificationCommand\x12\x11\n\tsignature\x18\x01 \x01(\t\x12\x14\n\x0croot_article\x18\x02 \x01(\t\x12\x15\n\rmajor_version\x18\x03 \x01(\r\x12\x15\n\rserial_number\x18\x04 \x01(\t\"<\n\x1dSetPersistentParameterCommand\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"-\n\x1dGetPersistentParameterCommand\x12\x0c\n\x04name\x18\x01 \x01(\t\">\n\x19ReadPartitionChunkCommand\x12\x11\n\tpart_name\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\r\"^\n\x18IdentifyHardwareResponse\x12\x14\n\x0croot_article\x18\x01 \x01(\t\x12\x15\n\rmajor_version\x18\x02 \x01(\r\x12\x15\n\rserial_number\x18\x03 \x01(\t\"9\n\x18IdentifyFirmwareResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"/\n\x1eGetPersistentParameterResponse\x12\r\n\x05value\x18\x01 \x01(\t\"M\n\x1aReadPartitionChunkResponse\x12\x11\n\tpart_name\x18\x01 \x01(\t\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"%\n\x13ResetReasonResponse\x12\x0e\n\x06reason\x18\x01 \x01(\t\"\xd7\x03\n\x0b\x43oreCommand\x12%\n\x02id\x18\x01 \x01(\x0e\x32\x19.io4edgeCoreApi.CommandId\x12G\n\x13load_firmware_chunk\x18\x02 \x01(\x0b\x32(.io4edgeCoreApi.LoadFirmwareChunkCommandH\x00\x12_\n\x1fprogram_hardware_identification\x18\x03 \x01(\x0b\x32\x34.io4edgeCoreApi.ProgramHardwareIdentificationCommandH\x00\x12Q\n\x18set_persistent_parameter\x18\x04 \x01(\x0b\x32-.io4edgeCoreApi.SetPersistentParameterCommandH\x00\x12Q\n\x18get_persistent_parameter\x18\x05 \x01(\x0b\x32-.io4edgeCoreApi.GetPersistentParameterCommandH\x00\x12I\n\x14read_partition_chunk\x18\x06 \x01(\x0b\x32).io4edgeCoreApi.ReadPartitionChunkCommandH\x00\x42\x06\n\x04\x64\x61ta\"\xe4\x03\n\x0c\x43oreResponse\x12%\n\x02id\x18\x01 \x01(\x0e\x32\x19.io4edgeCoreApi.CommandId\x12&\n\x06status\x18\x02 \x01(\x0e\x32\x16.io4edgeCoreApi.Status\x12\x16\n\x0erestarting_now\x18\x03 \x01(\x08\x12\x45\n\x11identify_hardware\x18\x04 \x01(\x0b\x32(.io4edgeCoreApi.IdentifyHardwareResponseH\x00\x12\x45\n\x11identify_firmware\x18\x05 \x01(\x0b\x32(.io4edgeCoreApi.IdentifyFirmwareResponseH\x00\x12N\n\x14persistent_parameter\x18\x06 \x01(\x0b\x32..io4edgeCoreApi.GetPersistentParameterResponseH\x00\x12J\n\x14read_partition_chunk\x18\x07 \x01(\x0b\x32*.io4edgeCoreApi.ReadPartitionChunkResponseH\x00\x12;\n\x0creset_reason\x18\x08 \x01(\x0b\x32#.io4edgeCoreApi.ResetReasonResponseH\x00\x42\x06\n\x04\x64\x61ta*\xf0\x01\n\tCommandId\x12\x15\n\x11IDENTIFY_HARDWARE\x10\x00\x12\x15\n\x11IDENTIFY_FIRMWARE\x10\x01\x12\x17\n\x13LOAD_FIRMWARE_CHUNK\x10\x02\x12#\n\x1fPROGRAM_HARDWARE_IDENTIFICATION\x10\x03\x12\x0b\n\x07RESTART\x10\x04\x12\x1c\n\x18SET_PERSISTENT_PARAMETER\x10\x05\x12\x1c\n\x18GET_PERSISTENT_PARAMETER\x10\x06\x12\x18\n\x14READ_PARTITION_CHUNK\x10\x07\x12\x14\n\x10GET_RESET_REASON\x10\x08*\xd8\x01\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x13\n\x0fUNKNOWN_COMMAND\x10\x01\x12\x15\n\x11ILLEGAL_PARAMETER\x10\x02\x12\x11\n\rBAD_CHUNK_SEQ\x10\x03\x12\x12\n\x0e\x42\x41\x44_CHUNK_SIZE\x10\x04\x12\x12\n\x0eNOT_COMPATIBLE\x10\x05\x12\x12\n\x0eINTERNAL_ERROR\x10\x06\x12\x15\n\x11PROGRAMMING_ERROR\x10\x07\x12\x13\n\x0fNO_HW_INVENTORY\x10\x08\x12\x1f\n\x1bTHIS_VERSION_FAILED_ALREADY\x10\tB\x13Z\x11\x63ore_api/v1alpha2b\x06proto3'
)

_COMMANDID = _descriptor.EnumDescriptor(
  name='CommandId',
  full_name='io4edgeCoreApi.CommandId',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='IDENTIFY_HARDWARE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IDENTIFY_FIRMWARE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LOAD_FIRMWARE_CHUNK', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROGRAM_HARDWARE_IDENTIFICATION', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RESTART', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SET_PERSISTENT_PARAMETER', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GET_PERSISTENT_PARAMETER', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='READ_PARTITION_CHUNK', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GET_RESET_REASON', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1731,
  serialized_end=1971,
)
_sym_db.RegisterEnumDescriptor(_COMMANDID)

CommandId = enum_type_wrapper.EnumTypeWrapper(_COMMANDID)
_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='io4edgeCoreApi.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_COMMAND', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ILLEGAL_PARAMETER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BAD_CHUNK_SEQ', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BAD_CHUNK_SIZE', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_COMPATIBLE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PROGRAMMING_ERROR', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NO_HW_INVENTORY', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='THIS_VERSION_FAILED_ALREADY', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1974,
  serialized_end=2190,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
IDENTIFY_HARDWARE = 0
IDENTIFY_FIRMWARE = 1
LOAD_FIRMWARE_CHUNK = 2
PROGRAM_HARDWARE_IDENTIFICATION = 3
RESTART = 4
SET_PERSISTENT_PARAMETER = 5
GET_PERSISTENT_PARAMETER = 6
READ_PARTITION_CHUNK = 7
GET_RESET_REASON = 8
OK = 0
UNKNOWN_COMMAND = 1
ILLEGAL_PARAMETER = 2
BAD_CHUNK_SEQ = 3
BAD_CHUNK_SIZE = 4
NOT_COMPATIBLE = 5
INTERNAL_ERROR = 6
PROGRAMMING_ERROR = 7
NO_HW_INVENTORY = 8
THIS_VERSION_FAILED_ALREADY = 9



_LOADFIRMWARECHUNKCOMMAND = _descriptor.Descriptor(
  name='LoadFirmwareChunkCommand',
  full_name='io4edgeCoreApi.LoadFirmwareChunkCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='chunk_number', full_name='io4edgeCoreApi.LoadFirmwareChunkCommand.chunk_number', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_last_chunk', full_name='io4edgeCoreApi.LoadFirmwareChunkCommand.is_last_chunk', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='io4edgeCoreApi.LoadFirmwareChunkCommand.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=60,
  serialized_end=145,
)


_PROGRAMHARDWAREIDENTIFICATIONCOMMAND = _descriptor.Descriptor(
  name='ProgramHardwareIdentificationCommand',
  full_name='io4edgeCoreApi.ProgramHardwareIdentificationCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature', full_name='io4edgeCoreApi.ProgramHardwareIdentificationCommand.signature', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='root_article', full_name='io4edgeCoreApi.ProgramHardwareIdentificationCommand.root_article', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='major_version', full_name='io4edgeCoreApi.ProgramHardwareIdentificationCommand.major_version', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='io4edgeCoreApi.ProgramHardwareIdentificationCommand.serial_number', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=147,
  serialized_end=272,
)


_SETPERSISTENTPARAMETERCOMMAND = _descriptor.Descriptor(
  name='SetPersistentParameterCommand',
  full_name='io4edgeCoreApi.SetPersistentParameterCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='io4edgeCoreApi.SetPersistentParameterCommand.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='io4edgeCoreApi.SetPersistentParameterCommand.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=274,
  serialized_end=334,
)


_GETPERSISTENTPARAMETERCOMMAND = _descriptor.Descriptor(
  name='GetPersistentParameterCommand',
  full_name='io4edgeCoreApi.GetPersistentParameterCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='io4edgeCoreApi.GetPersistentParameterCommand.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=336,
  serialized_end=381,
)


_READPARTITIONCHUNKCOMMAND = _descriptor.Descriptor(
  name='ReadPartitionChunkCommand',
  full_name='io4edgeCoreApi.ReadPartitionChunkCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='part_name', full_name='io4edgeCoreApi.ReadPartitionChunkCommand.part_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='io4edgeCoreApi.ReadPartitionChunkCommand.offset', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=383,
  serialized_end=445,
)


_IDENTIFYHARDWARERESPONSE = _descriptor.Descriptor(
  name='IdentifyHardwareResponse',
  full_name='io4edgeCoreApi.IdentifyHardwareResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='root_article', full_name='io4edgeCoreApi.IdentifyHardwareResponse.root_article', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='major_version', full_name='io4edgeCoreApi.IdentifyHardwareResponse.major_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serial_number', full_name='io4edgeCoreApi.IdentifyHardwareResponse.serial_number', index=2,
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
  serialized_start=447,
  serialized_end=541,
)


_IDENTIFYFIRMWARERESPONSE = _descriptor.Descriptor(
  name='IdentifyFirmwareResponse',
  full_name='io4edgeCoreApi.IdentifyFirmwareResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='io4edgeCoreApi.IdentifyFirmwareResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='io4edgeCoreApi.IdentifyFirmwareResponse.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=543,
  serialized_end=600,
)


_GETPERSISTENTPARAMETERRESPONSE = _descriptor.Descriptor(
  name='GetPersistentParameterResponse',
  full_name='io4edgeCoreApi.GetPersistentParameterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='io4edgeCoreApi.GetPersistentParameterResponse.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=602,
  serialized_end=649,
)


_READPARTITIONCHUNKRESPONSE = _descriptor.Descriptor(
  name='ReadPartitionChunkResponse',
  full_name='io4edgeCoreApi.ReadPartitionChunkResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='part_name', full_name='io4edgeCoreApi.ReadPartitionChunkResponse.part_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='offset', full_name='io4edgeCoreApi.ReadPartitionChunkResponse.offset', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='io4edgeCoreApi.ReadPartitionChunkResponse.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=651,
  serialized_end=728,
)


_RESETREASONRESPONSE = _descriptor.Descriptor(
  name='ResetReasonResponse',
  full_name='io4edgeCoreApi.ResetReasonResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reason', full_name='io4edgeCoreApi.ResetReasonResponse.reason', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=730,
  serialized_end=767,
)


_CORECOMMAND = _descriptor.Descriptor(
  name='CoreCommand',
  full_name='io4edgeCoreApi.CoreCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='io4edgeCoreApi.CoreCommand.id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='load_firmware_chunk', full_name='io4edgeCoreApi.CoreCommand.load_firmware_chunk', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='program_hardware_identification', full_name='io4edgeCoreApi.CoreCommand.program_hardware_identification', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='set_persistent_parameter', full_name='io4edgeCoreApi.CoreCommand.set_persistent_parameter', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='get_persistent_parameter', full_name='io4edgeCoreApi.CoreCommand.get_persistent_parameter', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='read_partition_chunk', full_name='io4edgeCoreApi.CoreCommand.read_partition_chunk', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='data', full_name='io4edgeCoreApi.CoreCommand.data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=770,
  serialized_end=1241,
)


_CORERESPONSE = _descriptor.Descriptor(
  name='CoreResponse',
  full_name='io4edgeCoreApi.CoreResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='io4edgeCoreApi.CoreResponse.id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='io4edgeCoreApi.CoreResponse.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='restarting_now', full_name='io4edgeCoreApi.CoreResponse.restarting_now', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identify_hardware', full_name='io4edgeCoreApi.CoreResponse.identify_hardware', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='identify_firmware', full_name='io4edgeCoreApi.CoreResponse.identify_firmware', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='persistent_parameter', full_name='io4edgeCoreApi.CoreResponse.persistent_parameter', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='read_partition_chunk', full_name='io4edgeCoreApi.CoreResponse.read_partition_chunk', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reset_reason', full_name='io4edgeCoreApi.CoreResponse.reset_reason', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='data', full_name='io4edgeCoreApi.CoreResponse.data',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=1244,
  serialized_end=1728,
)

_CORECOMMAND.fields_by_name['id'].enum_type = _COMMANDID
_CORECOMMAND.fields_by_name['load_firmware_chunk'].message_type = _LOADFIRMWARECHUNKCOMMAND
_CORECOMMAND.fields_by_name['program_hardware_identification'].message_type = _PROGRAMHARDWAREIDENTIFICATIONCOMMAND
_CORECOMMAND.fields_by_name['set_persistent_parameter'].message_type = _SETPERSISTENTPARAMETERCOMMAND
_CORECOMMAND.fields_by_name['get_persistent_parameter'].message_type = _GETPERSISTENTPARAMETERCOMMAND
_CORECOMMAND.fields_by_name['read_partition_chunk'].message_type = _READPARTITIONCHUNKCOMMAND
_CORECOMMAND.oneofs_by_name['data'].fields.append(
  _CORECOMMAND.fields_by_name['load_firmware_chunk'])
_CORECOMMAND.fields_by_name['load_firmware_chunk'].containing_oneof = _CORECOMMAND.oneofs_by_name['data']
_CORECOMMAND.oneofs_by_name['data'].fields.append(
  _CORECOMMAND.fields_by_name['program_hardware_identification'])
_CORECOMMAND.fields_by_name['program_hardware_identification'].containing_oneof = _CORECOMMAND.oneofs_by_name['data']
_CORECOMMAND.oneofs_by_name['data'].fields.append(
  _CORECOMMAND.fields_by_name['set_persistent_parameter'])
_CORECOMMAND.fields_by_name['set_persistent_parameter'].containing_oneof = _CORECOMMAND.oneofs_by_name['data']
_CORECOMMAND.oneofs_by_name['data'].fields.append(
  _CORECOMMAND.fields_by_name['get_persistent_parameter'])
_CORECOMMAND.fields_by_name['get_persistent_parameter'].containing_oneof = _CORECOMMAND.oneofs_by_name['data']
_CORECOMMAND.oneofs_by_name['data'].fields.append(
  _CORECOMMAND.fields_by_name['read_partition_chunk'])
_CORECOMMAND.fields_by_name['read_partition_chunk'].containing_oneof = _CORECOMMAND.oneofs_by_name['data']
_CORERESPONSE.fields_by_name['id'].enum_type = _COMMANDID
_CORERESPONSE.fields_by_name['status'].enum_type = _STATUS
_CORERESPONSE.fields_by_name['identify_hardware'].message_type = _IDENTIFYHARDWARERESPONSE
_CORERESPONSE.fields_by_name['identify_firmware'].message_type = _IDENTIFYFIRMWARERESPONSE
_CORERESPONSE.fields_by_name['persistent_parameter'].message_type = _GETPERSISTENTPARAMETERRESPONSE
_CORERESPONSE.fields_by_name['read_partition_chunk'].message_type = _READPARTITIONCHUNKRESPONSE
_CORERESPONSE.fields_by_name['reset_reason'].message_type = _RESETREASONRESPONSE
_CORERESPONSE.oneofs_by_name['data'].fields.append(
  _CORERESPONSE.fields_by_name['identify_hardware'])
_CORERESPONSE.fields_by_name['identify_hardware'].containing_oneof = _CORERESPONSE.oneofs_by_name['data']
_CORERESPONSE.oneofs_by_name['data'].fields.append(
  _CORERESPONSE.fields_by_name['identify_firmware'])
_CORERESPONSE.fields_by_name['identify_firmware'].containing_oneof = _CORERESPONSE.oneofs_by_name['data']
_CORERESPONSE.oneofs_by_name['data'].fields.append(
  _CORERESPONSE.fields_by_name['persistent_parameter'])
_CORERESPONSE.fields_by_name['persistent_parameter'].containing_oneof = _CORERESPONSE.oneofs_by_name['data']
_CORERESPONSE.oneofs_by_name['data'].fields.append(
  _CORERESPONSE.fields_by_name['read_partition_chunk'])
_CORERESPONSE.fields_by_name['read_partition_chunk'].containing_oneof = _CORERESPONSE.oneofs_by_name['data']
_CORERESPONSE.oneofs_by_name['data'].fields.append(
  _CORERESPONSE.fields_by_name['reset_reason'])
_CORERESPONSE.fields_by_name['reset_reason'].containing_oneof = _CORERESPONSE.oneofs_by_name['data']
DESCRIPTOR.message_types_by_name['LoadFirmwareChunkCommand'] = _LOADFIRMWARECHUNKCOMMAND
DESCRIPTOR.message_types_by_name['ProgramHardwareIdentificationCommand'] = _PROGRAMHARDWAREIDENTIFICATIONCOMMAND
DESCRIPTOR.message_types_by_name['SetPersistentParameterCommand'] = _SETPERSISTENTPARAMETERCOMMAND
DESCRIPTOR.message_types_by_name['GetPersistentParameterCommand'] = _GETPERSISTENTPARAMETERCOMMAND
DESCRIPTOR.message_types_by_name['ReadPartitionChunkCommand'] = _READPARTITIONCHUNKCOMMAND
DESCRIPTOR.message_types_by_name['IdentifyHardwareResponse'] = _IDENTIFYHARDWARERESPONSE
DESCRIPTOR.message_types_by_name['IdentifyFirmwareResponse'] = _IDENTIFYFIRMWARERESPONSE
DESCRIPTOR.message_types_by_name['GetPersistentParameterResponse'] = _GETPERSISTENTPARAMETERRESPONSE
DESCRIPTOR.message_types_by_name['ReadPartitionChunkResponse'] = _READPARTITIONCHUNKRESPONSE
DESCRIPTOR.message_types_by_name['ResetReasonResponse'] = _RESETREASONRESPONSE
DESCRIPTOR.message_types_by_name['CoreCommand'] = _CORECOMMAND
DESCRIPTOR.message_types_by_name['CoreResponse'] = _CORERESPONSE
DESCRIPTOR.enum_types_by_name['CommandId'] = _COMMANDID
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoadFirmwareChunkCommand = _reflection.GeneratedProtocolMessageType('LoadFirmwareChunkCommand', (_message.Message,), {
  'DESCRIPTOR' : _LOADFIRMWARECHUNKCOMMAND,
  '__module__' : 'core_api.v1alpha2.io4edge_core_api_pb2'
  # @@protoc_insertion_point(class_scope:io4edgeCoreApi.LoadFirmwareChunkCommand)
  })
_sym_db.RegisterMessage(LoadFirmwareChunkCommand)

ProgramHardwareIdentificationCommand = _reflection.GeneratedProtocolMessageType('ProgramHardwareIdentificationCommand', (_message.Message,), {
  'DESCRIPTOR' : _PROGRAMHARDWAREIDENTIFICATIONCOMMAND,
  '__module__' : 'core_api.v1alpha2.io4edge_core_api_pb2'
  # @@protoc_insertion_point(class_scope:io4edgeCoreApi.ProgramHardwareIdentificationCommand)
  })
_sym_db.RegisterMessage(ProgramHardwareIdentificationCommand)

SetPersistentParameterCommand = _reflection.GeneratedProtocolMessageType('SetPersistentParameterCommand', (_message.Message,), {
  'DESCRIPTOR' : _SETPERSISTENTPARAMETERCOMMAND,
  '__module__' : 'core_api.v1alpha2.io4edge_core_api_pb2'
  # @@protoc_insertion_point(class_scope:io4edgeCoreApi.SetPersistentParameterCommand)
  })
_sym_db.RegisterMessage(SetPersistentParameterCommand)

GetPersistentParameterCommand = _reflection.GeneratedProtocolMessageType('GetPersistentParameterCommand', (_message.Message,), {
  'DESCRIPTOR' : _GETPERSISTENTPARAMETERCOMMAND,
  '__module__' : 'core_api.v1alpha2.io4edge_core_api_pb2'
  # @@protoc_insertion_point(class_scope:io4edgeCoreApi.GetPersistentParameterCommand)
  })
_sym_db.RegisterMessage(GetPersistentParameterCommand)

ReadPartitionChunkCommand = _reflection.GeneratedProtocolMessageType('ReadPartitionChunkCommand', (_message.Message,), {
  'DESCRIPTOR' : _READPARTITIONCHUNKCOMMAND,
  '__module__' : 'core_api.v1alpha2.io4edge_core_api_pb2'
  # @@protoc_insertion_point(class_scope:io4edgeCoreApi.ReadPartitionChunkCommand)
  })
_sym_db.RegisterMessage(ReadPartitionChunkCommand)

IdentifyHardwareResponse = _reflection.GeneratedProtocolMessageType('IdentifyHardwareResponse', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFYHARDWARERESPONSE,
  '__module__' : 'core_api.v1alpha2.io4edge_core_api_pb2'
  # @@protoc_insertion_point(class_scope:io4edgeCoreApi.IdentifyHardwareResponse)
  })
_sym_db.RegisterMessage(IdentifyHardwareResponse)

IdentifyFirmwareResponse = _reflection.GeneratedProtocolMessageType('IdentifyFirmwareResponse', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFYFIRMWARERESPONSE,
  '__module__' : 'core_api.v1alpha2.io4edge_core_api_pb2'
  # @@protoc_insertion_point(class_scope:io4edgeCoreApi.IdentifyFirmwareResponse)
  })
_sym_db.RegisterMessage(IdentifyFirmwareResponse)

GetPersistentParameterResponse = _reflection.GeneratedProtocolMessageType('GetPersistentParameterResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETPERSISTENTPARAMETERRESPONSE,
  '__module__' : 'core_api.v1alpha2.io4edge_core_api_pb2'
  # @@protoc_insertion_point(class_scope:io4edgeCoreApi.GetPersistentParameterResponse)
  })
_sym_db.RegisterMessage(GetPersistentParameterResponse)

ReadPartitionChunkResponse = _reflection.GeneratedProtocolMessageType('ReadPartitionChunkResponse', (_message.Message,), {
  'DESCRIPTOR' : _READPARTITIONCHUNKRESPONSE,
  '__module__' : 'core_api.v1alpha2.io4edge_core_api_pb2'
  # @@protoc_insertion_point(class_scope:io4edgeCoreApi.ReadPartitionChunkResponse)
  })
_sym_db.RegisterMessage(ReadPartitionChunkResponse)

ResetReasonResponse = _reflection.GeneratedProtocolMessageType('ResetReasonResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESETREASONRESPONSE,
  '__module__' : 'core_api.v1alpha2.io4edge_core_api_pb2'
  # @@protoc_insertion_point(class_scope:io4edgeCoreApi.ResetReasonResponse)
  })
_sym_db.RegisterMessage(ResetReasonResponse)

CoreCommand = _reflection.GeneratedProtocolMessageType('CoreCommand', (_message.Message,), {
  'DESCRIPTOR' : _CORECOMMAND,
  '__module__' : 'core_api.v1alpha2.io4edge_core_api_pb2'
  # @@protoc_insertion_point(class_scope:io4edgeCoreApi.CoreCommand)
  })
_sym_db.RegisterMessage(CoreCommand)

CoreResponse = _reflection.GeneratedProtocolMessageType('CoreResponse', (_message.Message,), {
  'DESCRIPTOR' : _CORERESPONSE,
  '__module__' : 'core_api.v1alpha2.io4edge_core_api_pb2'
  # @@protoc_insertion_point(class_scope:io4edgeCoreApi.CoreResponse)
  })
_sym_db.RegisterMessage(CoreResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
