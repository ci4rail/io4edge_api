# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: functionblock/v1alpha1/io4edge_functionblock.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='functionblock/v1alpha1/io4edge_functionblock.proto',
  package='functionblock',
  syntax='proto3',
  serialized_options=_b('Z\026functionblock/v1alpha1'),
  serialized_pb=_b('\n2functionblock/v1alpha1/io4edge_functionblock.proto\x12\rfunctionblock\x1a\x19google/protobuf/any.proto\"\x18\n\x07\x43ontext\x12\r\n\x05value\x18\x01 \x01(\t\"\xe3\x01\n\x07\x43ommand\x12\'\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x16.functionblock.Context\x12\x35\n\rConfiguration\x18\x02 \x01(\x0b\x32\x1c.functionblock.ConfigurationH\x00\x12\x39\n\x0f\x66unctionControl\x18\x03 \x01(\x0b\x32\x1e.functionblock.FunctionControlH\x00\x12\x35\n\rstreamControl\x18\x04 \x01(\x0b\x32\x1c.functionblock.StreamControlH\x00\x42\x06\n\x04type\"\xe4\x01\n\rConfiguration\x12@\n functionSpecificConfigurationSet\x18\n \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12@\n functionSpecificConfigurationGet\x18\x14 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12\x45\n%functionSpecificConfigurationDescribe\x18\x1e \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x08\n\x06\x61\x63tion\"\xa3\x01\n\x0f\x46unctionControl\x12\x42\n\"functionSpecificFunctionControlSet\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12\x42\n\"functionSpecificFunctionControlGet\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x08\n\x06\x61\x63tion\"\xbb\x01\n\x12StreamControlStart\x12\x15\n\rbucketSamples\x18\x01 \x01(\x07\x12\x19\n\x11keepaliveInterval\x18\x02 \x01(\x07\x12\x17\n\x0f\x62ufferedSamples\x18\x03 \x01(\x07\x12@\n\"functionSpecificStreamControlStart\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x18\n\x10low_latency_mode\x18\x05 \x01(\x08\"\x13\n\x11StreamControlStop\"\x7f\n\rStreamControl\x12\x32\n\x05start\x18\x01 \x01(\x0b\x32!.functionblock.StreamControlStartH\x00\x12\x30\n\x04stop\x18\x02 \x01(\x0b\x32 .functionblock.StreamControlStopH\x00\x42\x08\n\x06\x61\x63tion\"\x16\n\x05\x45rror\x12\r\n\x05\x65rror\x18\x01 \x01(\t\"\xec\x01\n\x15\x43onfigurationResponse\x12@\n functionSpecificConfigurationSet\x18\n \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12@\n functionSpecificConfigurationGet\x18\x14 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12\x45\n%functionSpecificConfigurationDescribe\x18\x1e \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x08\n\x06\x61\x63tion\"\xab\x01\n\x17\x46unctionControlResponse\x12\x42\n\"functionSpecificFunctionControlSet\x18\x01 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x12\x42\n\"functionSpecificFunctionControlGet\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyH\x00\x42\x08\n\x06\x61\x63tion\"\x17\n\x15StreamControlResponse\"u\n\nStreamData\x12\x1b\n\x13\x64\x65liveryTimestampUs\x18\x01 \x01(\x06\x12\x10\n\x08sequence\x18\x02 \x01(\x07\x12\x38\n\x1a\x66unctionSpecificStreamData\x18\n \x01(\x0b\x32\x14.google.protobuf.Any\"\xf5\x02\n\x08Response\x12\'\n\x07\x63ontext\x18\x01 \x01(\x0b\x32\x16.functionblock.Context\x12%\n\x06status\x18\x02 \x01(\x0e\x32\x15.functionblock.Status\x12#\n\x05\x65rror\x18\x03 \x01(\x0b\x32\x14.functionblock.Error\x12=\n\rConfiguration\x18\x04 \x01(\x0b\x32$.functionblock.ConfigurationResponseH\x00\x12\x41\n\x0f\x66unctionControl\x18\x05 \x01(\x0b\x32&.functionblock.FunctionControlResponseH\x00\x12=\n\rstreamControl\x18\x06 \x01(\x0b\x32$.functionblock.StreamControlResponseH\x00\x12+\n\x06stream\x18\x07 \x01(\x0b\x32\x19.functionblock.StreamDataH\x00\x42\x06\n\x04type*\xf5\x01\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\x14\n\x10UNSPECIFIC_ERROR\x10\x01\x12\x13\n\x0fUNKNOWN_COMMAND\x10\x02\x12\x13\n\x0fNOT_IMPLEMENTED\x10\x03\x12\x10\n\x0cWRONG_CLIENT\x10\x04\x12\x15\n\x11INVALID_PARAMETER\x10\x05\x12\x0c\n\x08HW_FAULT\x10\x06\x12\x1a\n\x16STREAM_ALREADY_STARTED\x10\x07\x12\x1a\n\x16STREAM_ALREADY_STOPPED\x10\x08\x12\x17\n\x13STREAM_START_FAILED\x10\t\x12\x1b\n\x17TEMPORARILY_UNAVAILABLE\x10\nB\x18Z\x16\x66unctionblock/v1alpha1b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])

_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='functionblock.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIC_ERROR', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_COMMAND', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_IMPLEMENTED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WRONG_CLIENT', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PARAMETER', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HW_FAULT', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STREAM_ALREADY_STARTED', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STREAM_ALREADY_STOPPED', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STREAM_START_FAILED', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEMPORARILY_UNAVAILABLE', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2047,
  serialized_end=2292,
)
_sym_db.RegisterEnumDescriptor(_STATUS)

Status = enum_type_wrapper.EnumTypeWrapper(_STATUS)
OK = 0
UNSPECIFIC_ERROR = 1
UNKNOWN_COMMAND = 2
NOT_IMPLEMENTED = 3
WRONG_CLIENT = 4
INVALID_PARAMETER = 5
HW_FAULT = 6
STREAM_ALREADY_STARTED = 7
STREAM_ALREADY_STOPPED = 8
STREAM_START_FAILED = 9
TEMPORARILY_UNAVAILABLE = 10



_CONTEXT = _descriptor.Descriptor(
  name='Context',
  full_name='functionblock.Context',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='functionblock.Context.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=96,
  serialized_end=120,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='functionblock.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='functionblock.Command.context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Configuration', full_name='functionblock.Command.Configuration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functionControl', full_name='functionblock.Command.functionControl', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='streamControl', full_name='functionblock.Command.streamControl', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='type', full_name='functionblock.Command.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=123,
  serialized_end=350,
)


_CONFIGURATION = _descriptor.Descriptor(
  name='Configuration',
  full_name='functionblock.Configuration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='functionSpecificConfigurationSet', full_name='functionblock.Configuration.functionSpecificConfigurationSet', index=0,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functionSpecificConfigurationGet', full_name='functionblock.Configuration.functionSpecificConfigurationGet', index=1,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functionSpecificConfigurationDescribe', full_name='functionblock.Configuration.functionSpecificConfigurationDescribe', index=2,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='action', full_name='functionblock.Configuration.action',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=353,
  serialized_end=581,
)


_FUNCTIONCONTROL = _descriptor.Descriptor(
  name='FunctionControl',
  full_name='functionblock.FunctionControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='functionSpecificFunctionControlSet', full_name='functionblock.FunctionControl.functionSpecificFunctionControlSet', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functionSpecificFunctionControlGet', full_name='functionblock.FunctionControl.functionSpecificFunctionControlGet', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='action', full_name='functionblock.FunctionControl.action',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=584,
  serialized_end=747,
)


_STREAMCONTROLSTART = _descriptor.Descriptor(
  name='StreamControlStart',
  full_name='functionblock.StreamControlStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucketSamples', full_name='functionblock.StreamControlStart.bucketSamples', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='keepaliveInterval', full_name='functionblock.StreamControlStart.keepaliveInterval', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bufferedSamples', full_name='functionblock.StreamControlStart.bufferedSamples', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functionSpecificStreamControlStart', full_name='functionblock.StreamControlStart.functionSpecificStreamControlStart', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low_latency_mode', full_name='functionblock.StreamControlStart.low_latency_mode', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=750,
  serialized_end=937,
)


_STREAMCONTROLSTOP = _descriptor.Descriptor(
  name='StreamControlStop',
  full_name='functionblock.StreamControlStop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=939,
  serialized_end=958,
)


_STREAMCONTROL = _descriptor.Descriptor(
  name='StreamControl',
  full_name='functionblock.StreamControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='functionblock.StreamControl.start', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stop', full_name='functionblock.StreamControl.stop', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='action', full_name='functionblock.StreamControl.action',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=960,
  serialized_end=1087,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='functionblock.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='functionblock.Error.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1089,
  serialized_end=1111,
)


_CONFIGURATIONRESPONSE = _descriptor.Descriptor(
  name='ConfigurationResponse',
  full_name='functionblock.ConfigurationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='functionSpecificConfigurationSet', full_name='functionblock.ConfigurationResponse.functionSpecificConfigurationSet', index=0,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functionSpecificConfigurationGet', full_name='functionblock.ConfigurationResponse.functionSpecificConfigurationGet', index=1,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functionSpecificConfigurationDescribe', full_name='functionblock.ConfigurationResponse.functionSpecificConfigurationDescribe', index=2,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='action', full_name='functionblock.ConfigurationResponse.action',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1114,
  serialized_end=1350,
)


_FUNCTIONCONTROLRESPONSE = _descriptor.Descriptor(
  name='FunctionControlResponse',
  full_name='functionblock.FunctionControlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='functionSpecificFunctionControlSet', full_name='functionblock.FunctionControlResponse.functionSpecificFunctionControlSet', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functionSpecificFunctionControlGet', full_name='functionblock.FunctionControlResponse.functionSpecificFunctionControlGet', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='action', full_name='functionblock.FunctionControlResponse.action',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1353,
  serialized_end=1524,
)


_STREAMCONTROLRESPONSE = _descriptor.Descriptor(
  name='StreamControlResponse',
  full_name='functionblock.StreamControlResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1526,
  serialized_end=1549,
)


_STREAMDATA = _descriptor.Descriptor(
  name='StreamData',
  full_name='functionblock.StreamData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='deliveryTimestampUs', full_name='functionblock.StreamData.deliveryTimestampUs', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sequence', full_name='functionblock.StreamData.sequence', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functionSpecificStreamData', full_name='functionblock.StreamData.functionSpecificStreamData', index=2,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1551,
  serialized_end=1668,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='functionblock.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='context', full_name='functionblock.Response.context', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='functionblock.Response.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='functionblock.Response.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Configuration', full_name='functionblock.Response.Configuration', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='functionControl', full_name='functionblock.Response.functionControl', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='streamControl', full_name='functionblock.Response.streamControl', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stream', full_name='functionblock.Response.stream', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='type', full_name='functionblock.Response.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1671,
  serialized_end=2044,
)

_COMMAND.fields_by_name['context'].message_type = _CONTEXT
_COMMAND.fields_by_name['Configuration'].message_type = _CONFIGURATION
_COMMAND.fields_by_name['functionControl'].message_type = _FUNCTIONCONTROL
_COMMAND.fields_by_name['streamControl'].message_type = _STREAMCONTROL
_COMMAND.oneofs_by_name['type'].fields.append(
  _COMMAND.fields_by_name['Configuration'])
_COMMAND.fields_by_name['Configuration'].containing_oneof = _COMMAND.oneofs_by_name['type']
_COMMAND.oneofs_by_name['type'].fields.append(
  _COMMAND.fields_by_name['functionControl'])
_COMMAND.fields_by_name['functionControl'].containing_oneof = _COMMAND.oneofs_by_name['type']
_COMMAND.oneofs_by_name['type'].fields.append(
  _COMMAND.fields_by_name['streamControl'])
_COMMAND.fields_by_name['streamControl'].containing_oneof = _COMMAND.oneofs_by_name['type']
_CONFIGURATION.fields_by_name['functionSpecificConfigurationSet'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CONFIGURATION.fields_by_name['functionSpecificConfigurationGet'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CONFIGURATION.fields_by_name['functionSpecificConfigurationDescribe'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CONFIGURATION.oneofs_by_name['action'].fields.append(
  _CONFIGURATION.fields_by_name['functionSpecificConfigurationSet'])
_CONFIGURATION.fields_by_name['functionSpecificConfigurationSet'].containing_oneof = _CONFIGURATION.oneofs_by_name['action']
_CONFIGURATION.oneofs_by_name['action'].fields.append(
  _CONFIGURATION.fields_by_name['functionSpecificConfigurationGet'])
_CONFIGURATION.fields_by_name['functionSpecificConfigurationGet'].containing_oneof = _CONFIGURATION.oneofs_by_name['action']
_CONFIGURATION.oneofs_by_name['action'].fields.append(
  _CONFIGURATION.fields_by_name['functionSpecificConfigurationDescribe'])
_CONFIGURATION.fields_by_name['functionSpecificConfigurationDescribe'].containing_oneof = _CONFIGURATION.oneofs_by_name['action']
_FUNCTIONCONTROL.fields_by_name['functionSpecificFunctionControlSet'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_FUNCTIONCONTROL.fields_by_name['functionSpecificFunctionControlGet'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_FUNCTIONCONTROL.oneofs_by_name['action'].fields.append(
  _FUNCTIONCONTROL.fields_by_name['functionSpecificFunctionControlSet'])
_FUNCTIONCONTROL.fields_by_name['functionSpecificFunctionControlSet'].containing_oneof = _FUNCTIONCONTROL.oneofs_by_name['action']
_FUNCTIONCONTROL.oneofs_by_name['action'].fields.append(
  _FUNCTIONCONTROL.fields_by_name['functionSpecificFunctionControlGet'])
_FUNCTIONCONTROL.fields_by_name['functionSpecificFunctionControlGet'].containing_oneof = _FUNCTIONCONTROL.oneofs_by_name['action']
_STREAMCONTROLSTART.fields_by_name['functionSpecificStreamControlStart'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_STREAMCONTROL.fields_by_name['start'].message_type = _STREAMCONTROLSTART
_STREAMCONTROL.fields_by_name['stop'].message_type = _STREAMCONTROLSTOP
_STREAMCONTROL.oneofs_by_name['action'].fields.append(
  _STREAMCONTROL.fields_by_name['start'])
_STREAMCONTROL.fields_by_name['start'].containing_oneof = _STREAMCONTROL.oneofs_by_name['action']
_STREAMCONTROL.oneofs_by_name['action'].fields.append(
  _STREAMCONTROL.fields_by_name['stop'])
_STREAMCONTROL.fields_by_name['stop'].containing_oneof = _STREAMCONTROL.oneofs_by_name['action']
_CONFIGURATIONRESPONSE.fields_by_name['functionSpecificConfigurationSet'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CONFIGURATIONRESPONSE.fields_by_name['functionSpecificConfigurationGet'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CONFIGURATIONRESPONSE.fields_by_name['functionSpecificConfigurationDescribe'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CONFIGURATIONRESPONSE.oneofs_by_name['action'].fields.append(
  _CONFIGURATIONRESPONSE.fields_by_name['functionSpecificConfigurationSet'])
_CONFIGURATIONRESPONSE.fields_by_name['functionSpecificConfigurationSet'].containing_oneof = _CONFIGURATIONRESPONSE.oneofs_by_name['action']
_CONFIGURATIONRESPONSE.oneofs_by_name['action'].fields.append(
  _CONFIGURATIONRESPONSE.fields_by_name['functionSpecificConfigurationGet'])
_CONFIGURATIONRESPONSE.fields_by_name['functionSpecificConfigurationGet'].containing_oneof = _CONFIGURATIONRESPONSE.oneofs_by_name['action']
_CONFIGURATIONRESPONSE.oneofs_by_name['action'].fields.append(
  _CONFIGURATIONRESPONSE.fields_by_name['functionSpecificConfigurationDescribe'])
_CONFIGURATIONRESPONSE.fields_by_name['functionSpecificConfigurationDescribe'].containing_oneof = _CONFIGURATIONRESPONSE.oneofs_by_name['action']
_FUNCTIONCONTROLRESPONSE.fields_by_name['functionSpecificFunctionControlSet'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_FUNCTIONCONTROLRESPONSE.fields_by_name['functionSpecificFunctionControlGet'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_FUNCTIONCONTROLRESPONSE.oneofs_by_name['action'].fields.append(
  _FUNCTIONCONTROLRESPONSE.fields_by_name['functionSpecificFunctionControlSet'])
_FUNCTIONCONTROLRESPONSE.fields_by_name['functionSpecificFunctionControlSet'].containing_oneof = _FUNCTIONCONTROLRESPONSE.oneofs_by_name['action']
_FUNCTIONCONTROLRESPONSE.oneofs_by_name['action'].fields.append(
  _FUNCTIONCONTROLRESPONSE.fields_by_name['functionSpecificFunctionControlGet'])
_FUNCTIONCONTROLRESPONSE.fields_by_name['functionSpecificFunctionControlGet'].containing_oneof = _FUNCTIONCONTROLRESPONSE.oneofs_by_name['action']
_STREAMDATA.fields_by_name['functionSpecificStreamData'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_RESPONSE.fields_by_name['context'].message_type = _CONTEXT
_RESPONSE.fields_by_name['status'].enum_type = _STATUS
_RESPONSE.fields_by_name['error'].message_type = _ERROR
_RESPONSE.fields_by_name['Configuration'].message_type = _CONFIGURATIONRESPONSE
_RESPONSE.fields_by_name['functionControl'].message_type = _FUNCTIONCONTROLRESPONSE
_RESPONSE.fields_by_name['streamControl'].message_type = _STREAMCONTROLRESPONSE
_RESPONSE.fields_by_name['stream'].message_type = _STREAMDATA
_RESPONSE.oneofs_by_name['type'].fields.append(
  _RESPONSE.fields_by_name['Configuration'])
_RESPONSE.fields_by_name['Configuration'].containing_oneof = _RESPONSE.oneofs_by_name['type']
_RESPONSE.oneofs_by_name['type'].fields.append(
  _RESPONSE.fields_by_name['functionControl'])
_RESPONSE.fields_by_name['functionControl'].containing_oneof = _RESPONSE.oneofs_by_name['type']
_RESPONSE.oneofs_by_name['type'].fields.append(
  _RESPONSE.fields_by_name['streamControl'])
_RESPONSE.fields_by_name['streamControl'].containing_oneof = _RESPONSE.oneofs_by_name['type']
_RESPONSE.oneofs_by_name['type'].fields.append(
  _RESPONSE.fields_by_name['stream'])
_RESPONSE.fields_by_name['stream'].containing_oneof = _RESPONSE.oneofs_by_name['type']
DESCRIPTOR.message_types_by_name['Context'] = _CONTEXT
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Configuration'] = _CONFIGURATION
DESCRIPTOR.message_types_by_name['FunctionControl'] = _FUNCTIONCONTROL
DESCRIPTOR.message_types_by_name['StreamControlStart'] = _STREAMCONTROLSTART
DESCRIPTOR.message_types_by_name['StreamControlStop'] = _STREAMCONTROLSTOP
DESCRIPTOR.message_types_by_name['StreamControl'] = _STREAMCONTROL
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['ConfigurationResponse'] = _CONFIGURATIONRESPONSE
DESCRIPTOR.message_types_by_name['FunctionControlResponse'] = _FUNCTIONCONTROLRESPONSE
DESCRIPTOR.message_types_by_name['StreamControlResponse'] = _STREAMCONTROLRESPONSE
DESCRIPTOR.message_types_by_name['StreamData'] = _STREAMDATA
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.enum_types_by_name['Status'] = _STATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Context = _reflection.GeneratedProtocolMessageType('Context', (_message.Message,), dict(
  DESCRIPTOR = _CONTEXT,
  __module__ = 'functionblock.v1alpha1.io4edge_functionblock_pb2'
  # @@protoc_insertion_point(class_scope:functionblock.Context)
  ))
_sym_db.RegisterMessage(Context)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND,
  __module__ = 'functionblock.v1alpha1.io4edge_functionblock_pb2'
  # @@protoc_insertion_point(class_scope:functionblock.Command)
  ))
_sym_db.RegisterMessage(Command)

Configuration = _reflection.GeneratedProtocolMessageType('Configuration', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATION,
  __module__ = 'functionblock.v1alpha1.io4edge_functionblock_pb2'
  # @@protoc_insertion_point(class_scope:functionblock.Configuration)
  ))
_sym_db.RegisterMessage(Configuration)

FunctionControl = _reflection.GeneratedProtocolMessageType('FunctionControl', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONCONTROL,
  __module__ = 'functionblock.v1alpha1.io4edge_functionblock_pb2'
  # @@protoc_insertion_point(class_scope:functionblock.FunctionControl)
  ))
_sym_db.RegisterMessage(FunctionControl)

StreamControlStart = _reflection.GeneratedProtocolMessageType('StreamControlStart', (_message.Message,), dict(
  DESCRIPTOR = _STREAMCONTROLSTART,
  __module__ = 'functionblock.v1alpha1.io4edge_functionblock_pb2'
  # @@protoc_insertion_point(class_scope:functionblock.StreamControlStart)
  ))
_sym_db.RegisterMessage(StreamControlStart)

StreamControlStop = _reflection.GeneratedProtocolMessageType('StreamControlStop', (_message.Message,), dict(
  DESCRIPTOR = _STREAMCONTROLSTOP,
  __module__ = 'functionblock.v1alpha1.io4edge_functionblock_pb2'
  # @@protoc_insertion_point(class_scope:functionblock.StreamControlStop)
  ))
_sym_db.RegisterMessage(StreamControlStop)

StreamControl = _reflection.GeneratedProtocolMessageType('StreamControl', (_message.Message,), dict(
  DESCRIPTOR = _STREAMCONTROL,
  __module__ = 'functionblock.v1alpha1.io4edge_functionblock_pb2'
  # @@protoc_insertion_point(class_scope:functionblock.StreamControl)
  ))
_sym_db.RegisterMessage(StreamControl)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'functionblock.v1alpha1.io4edge_functionblock_pb2'
  # @@protoc_insertion_point(class_scope:functionblock.Error)
  ))
_sym_db.RegisterMessage(Error)

ConfigurationResponse = _reflection.GeneratedProtocolMessageType('ConfigurationResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONRESPONSE,
  __module__ = 'functionblock.v1alpha1.io4edge_functionblock_pb2'
  # @@protoc_insertion_point(class_scope:functionblock.ConfigurationResponse)
  ))
_sym_db.RegisterMessage(ConfigurationResponse)

FunctionControlResponse = _reflection.GeneratedProtocolMessageType('FunctionControlResponse', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONCONTROLRESPONSE,
  __module__ = 'functionblock.v1alpha1.io4edge_functionblock_pb2'
  # @@protoc_insertion_point(class_scope:functionblock.FunctionControlResponse)
  ))
_sym_db.RegisterMessage(FunctionControlResponse)

StreamControlResponse = _reflection.GeneratedProtocolMessageType('StreamControlResponse', (_message.Message,), dict(
  DESCRIPTOR = _STREAMCONTROLRESPONSE,
  __module__ = 'functionblock.v1alpha1.io4edge_functionblock_pb2'
  # @@protoc_insertion_point(class_scope:functionblock.StreamControlResponse)
  ))
_sym_db.RegisterMessage(StreamControlResponse)

StreamData = _reflection.GeneratedProtocolMessageType('StreamData', (_message.Message,), dict(
  DESCRIPTOR = _STREAMDATA,
  __module__ = 'functionblock.v1alpha1.io4edge_functionblock_pb2'
  # @@protoc_insertion_point(class_scope:functionblock.StreamData)
  ))
_sym_db.RegisterMessage(StreamData)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'functionblock.v1alpha1.io4edge_functionblock_pb2'
  # @@protoc_insertion_point(class_scope:functionblock.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)