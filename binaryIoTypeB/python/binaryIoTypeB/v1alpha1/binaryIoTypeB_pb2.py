# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: binaryIoTypeB/v1alpha1/binaryIoTypeB.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='binaryIoTypeB/v1alpha1/binaryIoTypeB.proto',
  package='binaryIoTypeB',
  syntax='proto3',
  serialized_options=_b('Z\026binaryIoTypeB/v1alpha1'),
  serialized_pb=_b('\n*binaryIoTypeB/v1alpha1/binaryIoTypeB.proto\x12\rbinaryIoTypeB\"\x12\n\x10\x43onfigurationSet\"\x1a\n\x18\x43onfigurationSetResponse\"\x12\n\x10\x43onfigurationGet\"\x1a\n\x18\x43onfigurationGetResponse\"\x17\n\x15\x43onfigurationDescribe\"T\n\rChannelConfig\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\x07\x12\x32\n\tdirection\x18\x02 \x01(\x0e\x32\x1f.binaryIoTypeB.ChannelDirection\"T\n\x1d\x43onfigurationDescribeResponse\x12\x33\n\rchannelConfig\x18\x01 \x03(\x0b\x32\x1c.binaryIoTypeB.ChannelConfig\"\xd1\x01\n\x15\x43onfigurationResponse\x12\x36\n\x03get\x18\x01 \x01(\x0b\x32\'.binaryIoTypeB.ConfigurationGetResponseH\x00\x12\x36\n\x03set\x18\x02 \x01(\x0b\x32\'.binaryIoTypeB.ConfigurationSetResponseH\x00\x12@\n\x08\x64\x65scribe\x18\x03 \x01(\x0b\x32,.binaryIoTypeB.ConfigurationDescribeResponseH\x00\x42\x06\n\x04type\"\x1c\n\tGetSingle\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\x07\"\x16\n\x06GetAll\x12\x0c\n\x04mask\x18\x01 \x01(\x07\"n\n\x12\x46unctionControlGet\x12*\n\x06single\x18\x01 \x01(\x0b\x32\x18.binaryIoTypeB.GetSingleH\x00\x12$\n\x03\x61ll\x18\x02 \x01(\x0b\x32\x15.binaryIoTypeB.GetAllH\x00\x42\x06\n\x04type\"+\n\tSetSingle\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\x07\x12\r\n\x05state\x18\x02 \x01(\x08\"&\n\x06SetAll\x12\x0e\n\x06values\x18\x01 \x01(\x07\x12\x0c\n\x04mask\x18\x02 \x01(\x07\"n\n\x12\x46unctionControlSet\x12*\n\x06single\x18\x01 \x01(\x0b\x32\x18.binaryIoTypeB.SetSingleH\x00\x12$\n\x03\x61ll\x18\x02 \x01(\x0b\x32\x15.binaryIoTypeB.SetAllH\x00\x42\x06\n\x04type\"3\n\x11GetSingleResponse\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\x07\x12\r\n\x05state\x18\x02 \x01(\x08\" \n\x0eGetAllResponse\x12\x0e\n\x06inputs\x18\x01 \x01(\x07\"\x86\x01\n\x1a\x46unctionControlGetResponse\x12\x32\n\x06single\x18\x01 \x01(\x0b\x32 .binaryIoTypeB.GetSingleResponseH\x00\x12,\n\x03\x61ll\x18\x02 \x01(\x0b\x32\x1d.binaryIoTypeB.GetAllResponseH\x00\x42\x06\n\x04type\"\x13\n\x11SetSingleResponse\"\x10\n\x0eSetAllResponse\"\x86\x01\n\x1a\x46unctionControlSetResponse\x12\x32\n\x06single\x18\x01 \x01(\x0b\x32 .binaryIoTypeB.SetSingleResponseH\x00\x12,\n\x03\x61ll\x18\x02 \x01(\x0b\x32\x1d.binaryIoTypeB.SetAllResponseH\x00\x42\x06\n\x04type\"\x14\n\x12StreamControlStart\"\x08\n\x06Sample\"\x0c\n\nStreamData*e\n\x10\x43hannelDirection\x12\x17\n\x13\x42INARYIOTYPEB_INPUT\x10\x00\x12\x18\n\x14\x42INARYIOTYPEB_OUTPUT\x10\x01\x12\x1e\n\x1a\x42INARYIOTYPEB_INPUT_OUTPUT\x10\x02\x42\x18Z\x16\x62inaryIoTypeB/v1alpha1b\x06proto3')
)

_CHANNELDIRECTION = _descriptor.EnumDescriptor(
  name='ChannelDirection',
  full_name='binaryIoTypeB.ChannelDirection',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BINARYIOTYPEB_INPUT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BINARYIOTYPEB_OUTPUT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BINARYIOTYPEB_INPUT_OUTPUT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1375,
  serialized_end=1476,
)
_sym_db.RegisterEnumDescriptor(_CHANNELDIRECTION)

ChannelDirection = enum_type_wrapper.EnumTypeWrapper(_CHANNELDIRECTION)
BINARYIOTYPEB_INPUT = 0
BINARYIOTYPEB_OUTPUT = 1
BINARYIOTYPEB_INPUT_OUTPUT = 2



_CONFIGURATIONSET = _descriptor.Descriptor(
  name='ConfigurationSet',
  full_name='binaryIoTypeB.ConfigurationSet',
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
  serialized_start=61,
  serialized_end=79,
)


_CONFIGURATIONSETRESPONSE = _descriptor.Descriptor(
  name='ConfigurationSetResponse',
  full_name='binaryIoTypeB.ConfigurationSetResponse',
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
  serialized_start=81,
  serialized_end=107,
)


_CONFIGURATIONGET = _descriptor.Descriptor(
  name='ConfigurationGet',
  full_name='binaryIoTypeB.ConfigurationGet',
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
  serialized_start=109,
  serialized_end=127,
)


_CONFIGURATIONGETRESPONSE = _descriptor.Descriptor(
  name='ConfigurationGetResponse',
  full_name='binaryIoTypeB.ConfigurationGetResponse',
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
  serialized_start=129,
  serialized_end=155,
)


_CONFIGURATIONDESCRIBE = _descriptor.Descriptor(
  name='ConfigurationDescribe',
  full_name='binaryIoTypeB.ConfigurationDescribe',
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
  serialized_start=157,
  serialized_end=180,
)


_CHANNELCONFIG = _descriptor.Descriptor(
  name='ChannelConfig',
  full_name='binaryIoTypeB.ChannelConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='binaryIoTypeB.ChannelConfig.channel', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='binaryIoTypeB.ChannelConfig.direction', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=182,
  serialized_end=266,
)


_CONFIGURATIONDESCRIBERESPONSE = _descriptor.Descriptor(
  name='ConfigurationDescribeResponse',
  full_name='binaryIoTypeB.ConfigurationDescribeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channelConfig', full_name='binaryIoTypeB.ConfigurationDescribeResponse.channelConfig', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=268,
  serialized_end=352,
)


_CONFIGURATIONRESPONSE = _descriptor.Descriptor(
  name='ConfigurationResponse',
  full_name='binaryIoTypeB.ConfigurationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='get', full_name='binaryIoTypeB.ConfigurationResponse.get', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set', full_name='binaryIoTypeB.ConfigurationResponse.set', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='describe', full_name='binaryIoTypeB.ConfigurationResponse.describe', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
      name='type', full_name='binaryIoTypeB.ConfigurationResponse.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=355,
  serialized_end=564,
)


_GETSINGLE = _descriptor.Descriptor(
  name='GetSingle',
  full_name='binaryIoTypeB.GetSingle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='binaryIoTypeB.GetSingle.channel', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=566,
  serialized_end=594,
)


_GETALL = _descriptor.Descriptor(
  name='GetAll',
  full_name='binaryIoTypeB.GetAll',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mask', full_name='binaryIoTypeB.GetAll.mask', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=596,
  serialized_end=618,
)


_FUNCTIONCONTROLGET = _descriptor.Descriptor(
  name='FunctionControlGet',
  full_name='binaryIoTypeB.FunctionControlGet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='single', full_name='binaryIoTypeB.FunctionControlGet.single', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all', full_name='binaryIoTypeB.FunctionControlGet.all', index=1,
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
      name='type', full_name='binaryIoTypeB.FunctionControlGet.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=620,
  serialized_end=730,
)


_SETSINGLE = _descriptor.Descriptor(
  name='SetSingle',
  full_name='binaryIoTypeB.SetSingle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='binaryIoTypeB.SetSingle.channel', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='binaryIoTypeB.SetSingle.state', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=732,
  serialized_end=775,
)


_SETALL = _descriptor.Descriptor(
  name='SetAll',
  full_name='binaryIoTypeB.SetAll',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='binaryIoTypeB.SetAll.values', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mask', full_name='binaryIoTypeB.SetAll.mask', index=1,
      number=2, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=777,
  serialized_end=815,
)


_FUNCTIONCONTROLSET = _descriptor.Descriptor(
  name='FunctionControlSet',
  full_name='binaryIoTypeB.FunctionControlSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='single', full_name='binaryIoTypeB.FunctionControlSet.single', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all', full_name='binaryIoTypeB.FunctionControlSet.all', index=1,
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
      name='type', full_name='binaryIoTypeB.FunctionControlSet.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=817,
  serialized_end=927,
)


_GETSINGLERESPONSE = _descriptor.Descriptor(
  name='GetSingleResponse',
  full_name='binaryIoTypeB.GetSingleResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='binaryIoTypeB.GetSingleResponse.channel', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='binaryIoTypeB.GetSingleResponse.state', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=929,
  serialized_end=980,
)


_GETALLRESPONSE = _descriptor.Descriptor(
  name='GetAllResponse',
  full_name='binaryIoTypeB.GetAllResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inputs', full_name='binaryIoTypeB.GetAllResponse.inputs', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=982,
  serialized_end=1014,
)


_FUNCTIONCONTROLGETRESPONSE = _descriptor.Descriptor(
  name='FunctionControlGetResponse',
  full_name='binaryIoTypeB.FunctionControlGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='single', full_name='binaryIoTypeB.FunctionControlGetResponse.single', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all', full_name='binaryIoTypeB.FunctionControlGetResponse.all', index=1,
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
      name='type', full_name='binaryIoTypeB.FunctionControlGetResponse.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1017,
  serialized_end=1151,
)


_SETSINGLERESPONSE = _descriptor.Descriptor(
  name='SetSingleResponse',
  full_name='binaryIoTypeB.SetSingleResponse',
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
  serialized_start=1153,
  serialized_end=1172,
)


_SETALLRESPONSE = _descriptor.Descriptor(
  name='SetAllResponse',
  full_name='binaryIoTypeB.SetAllResponse',
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
  serialized_start=1174,
  serialized_end=1190,
)


_FUNCTIONCONTROLSETRESPONSE = _descriptor.Descriptor(
  name='FunctionControlSetResponse',
  full_name='binaryIoTypeB.FunctionControlSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='single', full_name='binaryIoTypeB.FunctionControlSetResponse.single', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all', full_name='binaryIoTypeB.FunctionControlSetResponse.all', index=1,
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
      name='type', full_name='binaryIoTypeB.FunctionControlSetResponse.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1193,
  serialized_end=1327,
)


_STREAMCONTROLSTART = _descriptor.Descriptor(
  name='StreamControlStart',
  full_name='binaryIoTypeB.StreamControlStart',
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
  serialized_start=1329,
  serialized_end=1349,
)


_SAMPLE = _descriptor.Descriptor(
  name='Sample',
  full_name='binaryIoTypeB.Sample',
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
  serialized_start=1351,
  serialized_end=1359,
)


_STREAMDATA = _descriptor.Descriptor(
  name='StreamData',
  full_name='binaryIoTypeB.StreamData',
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
  serialized_start=1361,
  serialized_end=1373,
)

_CHANNELCONFIG.fields_by_name['direction'].enum_type = _CHANNELDIRECTION
_CONFIGURATIONDESCRIBERESPONSE.fields_by_name['channelConfig'].message_type = _CHANNELCONFIG
_CONFIGURATIONRESPONSE.fields_by_name['get'].message_type = _CONFIGURATIONGETRESPONSE
_CONFIGURATIONRESPONSE.fields_by_name['set'].message_type = _CONFIGURATIONSETRESPONSE
_CONFIGURATIONRESPONSE.fields_by_name['describe'].message_type = _CONFIGURATIONDESCRIBERESPONSE
_CONFIGURATIONRESPONSE.oneofs_by_name['type'].fields.append(
  _CONFIGURATIONRESPONSE.fields_by_name['get'])
_CONFIGURATIONRESPONSE.fields_by_name['get'].containing_oneof = _CONFIGURATIONRESPONSE.oneofs_by_name['type']
_CONFIGURATIONRESPONSE.oneofs_by_name['type'].fields.append(
  _CONFIGURATIONRESPONSE.fields_by_name['set'])
_CONFIGURATIONRESPONSE.fields_by_name['set'].containing_oneof = _CONFIGURATIONRESPONSE.oneofs_by_name['type']
_CONFIGURATIONRESPONSE.oneofs_by_name['type'].fields.append(
  _CONFIGURATIONRESPONSE.fields_by_name['describe'])
_CONFIGURATIONRESPONSE.fields_by_name['describe'].containing_oneof = _CONFIGURATIONRESPONSE.oneofs_by_name['type']
_FUNCTIONCONTROLGET.fields_by_name['single'].message_type = _GETSINGLE
_FUNCTIONCONTROLGET.fields_by_name['all'].message_type = _GETALL
_FUNCTIONCONTROLGET.oneofs_by_name['type'].fields.append(
  _FUNCTIONCONTROLGET.fields_by_name['single'])
_FUNCTIONCONTROLGET.fields_by_name['single'].containing_oneof = _FUNCTIONCONTROLGET.oneofs_by_name['type']
_FUNCTIONCONTROLGET.oneofs_by_name['type'].fields.append(
  _FUNCTIONCONTROLGET.fields_by_name['all'])
_FUNCTIONCONTROLGET.fields_by_name['all'].containing_oneof = _FUNCTIONCONTROLGET.oneofs_by_name['type']
_FUNCTIONCONTROLSET.fields_by_name['single'].message_type = _SETSINGLE
_FUNCTIONCONTROLSET.fields_by_name['all'].message_type = _SETALL
_FUNCTIONCONTROLSET.oneofs_by_name['type'].fields.append(
  _FUNCTIONCONTROLSET.fields_by_name['single'])
_FUNCTIONCONTROLSET.fields_by_name['single'].containing_oneof = _FUNCTIONCONTROLSET.oneofs_by_name['type']
_FUNCTIONCONTROLSET.oneofs_by_name['type'].fields.append(
  _FUNCTIONCONTROLSET.fields_by_name['all'])
_FUNCTIONCONTROLSET.fields_by_name['all'].containing_oneof = _FUNCTIONCONTROLSET.oneofs_by_name['type']
_FUNCTIONCONTROLGETRESPONSE.fields_by_name['single'].message_type = _GETSINGLERESPONSE
_FUNCTIONCONTROLGETRESPONSE.fields_by_name['all'].message_type = _GETALLRESPONSE
_FUNCTIONCONTROLGETRESPONSE.oneofs_by_name['type'].fields.append(
  _FUNCTIONCONTROLGETRESPONSE.fields_by_name['single'])
_FUNCTIONCONTROLGETRESPONSE.fields_by_name['single'].containing_oneof = _FUNCTIONCONTROLGETRESPONSE.oneofs_by_name['type']
_FUNCTIONCONTROLGETRESPONSE.oneofs_by_name['type'].fields.append(
  _FUNCTIONCONTROLGETRESPONSE.fields_by_name['all'])
_FUNCTIONCONTROLGETRESPONSE.fields_by_name['all'].containing_oneof = _FUNCTIONCONTROLGETRESPONSE.oneofs_by_name['type']
_FUNCTIONCONTROLSETRESPONSE.fields_by_name['single'].message_type = _SETSINGLERESPONSE
_FUNCTIONCONTROLSETRESPONSE.fields_by_name['all'].message_type = _SETALLRESPONSE
_FUNCTIONCONTROLSETRESPONSE.oneofs_by_name['type'].fields.append(
  _FUNCTIONCONTROLSETRESPONSE.fields_by_name['single'])
_FUNCTIONCONTROLSETRESPONSE.fields_by_name['single'].containing_oneof = _FUNCTIONCONTROLSETRESPONSE.oneofs_by_name['type']
_FUNCTIONCONTROLSETRESPONSE.oneofs_by_name['type'].fields.append(
  _FUNCTIONCONTROLSETRESPONSE.fields_by_name['all'])
_FUNCTIONCONTROLSETRESPONSE.fields_by_name['all'].containing_oneof = _FUNCTIONCONTROLSETRESPONSE.oneofs_by_name['type']
DESCRIPTOR.message_types_by_name['ConfigurationSet'] = _CONFIGURATIONSET
DESCRIPTOR.message_types_by_name['ConfigurationSetResponse'] = _CONFIGURATIONSETRESPONSE
DESCRIPTOR.message_types_by_name['ConfigurationGet'] = _CONFIGURATIONGET
DESCRIPTOR.message_types_by_name['ConfigurationGetResponse'] = _CONFIGURATIONGETRESPONSE
DESCRIPTOR.message_types_by_name['ConfigurationDescribe'] = _CONFIGURATIONDESCRIBE
DESCRIPTOR.message_types_by_name['ChannelConfig'] = _CHANNELCONFIG
DESCRIPTOR.message_types_by_name['ConfigurationDescribeResponse'] = _CONFIGURATIONDESCRIBERESPONSE
DESCRIPTOR.message_types_by_name['ConfigurationResponse'] = _CONFIGURATIONRESPONSE
DESCRIPTOR.message_types_by_name['GetSingle'] = _GETSINGLE
DESCRIPTOR.message_types_by_name['GetAll'] = _GETALL
DESCRIPTOR.message_types_by_name['FunctionControlGet'] = _FUNCTIONCONTROLGET
DESCRIPTOR.message_types_by_name['SetSingle'] = _SETSINGLE
DESCRIPTOR.message_types_by_name['SetAll'] = _SETALL
DESCRIPTOR.message_types_by_name['FunctionControlSet'] = _FUNCTIONCONTROLSET
DESCRIPTOR.message_types_by_name['GetSingleResponse'] = _GETSINGLERESPONSE
DESCRIPTOR.message_types_by_name['GetAllResponse'] = _GETALLRESPONSE
DESCRIPTOR.message_types_by_name['FunctionControlGetResponse'] = _FUNCTIONCONTROLGETRESPONSE
DESCRIPTOR.message_types_by_name['SetSingleResponse'] = _SETSINGLERESPONSE
DESCRIPTOR.message_types_by_name['SetAllResponse'] = _SETALLRESPONSE
DESCRIPTOR.message_types_by_name['FunctionControlSetResponse'] = _FUNCTIONCONTROLSETRESPONSE
DESCRIPTOR.message_types_by_name['StreamControlStart'] = _STREAMCONTROLSTART
DESCRIPTOR.message_types_by_name['Sample'] = _SAMPLE
DESCRIPTOR.message_types_by_name['StreamData'] = _STREAMDATA
DESCRIPTOR.enum_types_by_name['ChannelDirection'] = _CHANNELDIRECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigurationSet = _reflection.GeneratedProtocolMessageType('ConfigurationSet', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONSET,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.ConfigurationSet)
  ))
_sym_db.RegisterMessage(ConfigurationSet)

ConfigurationSetResponse = _reflection.GeneratedProtocolMessageType('ConfigurationSetResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONSETRESPONSE,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.ConfigurationSetResponse)
  ))
_sym_db.RegisterMessage(ConfigurationSetResponse)

ConfigurationGet = _reflection.GeneratedProtocolMessageType('ConfigurationGet', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONGET,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.ConfigurationGet)
  ))
_sym_db.RegisterMessage(ConfigurationGet)

ConfigurationGetResponse = _reflection.GeneratedProtocolMessageType('ConfigurationGetResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONGETRESPONSE,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.ConfigurationGetResponse)
  ))
_sym_db.RegisterMessage(ConfigurationGetResponse)

ConfigurationDescribe = _reflection.GeneratedProtocolMessageType('ConfigurationDescribe', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONDESCRIBE,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.ConfigurationDescribe)
  ))
_sym_db.RegisterMessage(ConfigurationDescribe)

ChannelConfig = _reflection.GeneratedProtocolMessageType('ChannelConfig', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELCONFIG,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.ChannelConfig)
  ))
_sym_db.RegisterMessage(ChannelConfig)

ConfigurationDescribeResponse = _reflection.GeneratedProtocolMessageType('ConfigurationDescribeResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONDESCRIBERESPONSE,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.ConfigurationDescribeResponse)
  ))
_sym_db.RegisterMessage(ConfigurationDescribeResponse)

ConfigurationResponse = _reflection.GeneratedProtocolMessageType('ConfigurationResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONRESPONSE,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.ConfigurationResponse)
  ))
_sym_db.RegisterMessage(ConfigurationResponse)

GetSingle = _reflection.GeneratedProtocolMessageType('GetSingle', (_message.Message,), dict(
  DESCRIPTOR = _GETSINGLE,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.GetSingle)
  ))
_sym_db.RegisterMessage(GetSingle)

GetAll = _reflection.GeneratedProtocolMessageType('GetAll', (_message.Message,), dict(
  DESCRIPTOR = _GETALL,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.GetAll)
  ))
_sym_db.RegisterMessage(GetAll)

FunctionControlGet = _reflection.GeneratedProtocolMessageType('FunctionControlGet', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONCONTROLGET,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.FunctionControlGet)
  ))
_sym_db.RegisterMessage(FunctionControlGet)

SetSingle = _reflection.GeneratedProtocolMessageType('SetSingle', (_message.Message,), dict(
  DESCRIPTOR = _SETSINGLE,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.SetSingle)
  ))
_sym_db.RegisterMessage(SetSingle)

SetAll = _reflection.GeneratedProtocolMessageType('SetAll', (_message.Message,), dict(
  DESCRIPTOR = _SETALL,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.SetAll)
  ))
_sym_db.RegisterMessage(SetAll)

FunctionControlSet = _reflection.GeneratedProtocolMessageType('FunctionControlSet', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONCONTROLSET,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.FunctionControlSet)
  ))
_sym_db.RegisterMessage(FunctionControlSet)

GetSingleResponse = _reflection.GeneratedProtocolMessageType('GetSingleResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETSINGLERESPONSE,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.GetSingleResponse)
  ))
_sym_db.RegisterMessage(GetSingleResponse)

GetAllResponse = _reflection.GeneratedProtocolMessageType('GetAllResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETALLRESPONSE,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.GetAllResponse)
  ))
_sym_db.RegisterMessage(GetAllResponse)

FunctionControlGetResponse = _reflection.GeneratedProtocolMessageType('FunctionControlGetResponse', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONCONTROLGETRESPONSE,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.FunctionControlGetResponse)
  ))
_sym_db.RegisterMessage(FunctionControlGetResponse)

SetSingleResponse = _reflection.GeneratedProtocolMessageType('SetSingleResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETSINGLERESPONSE,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.SetSingleResponse)
  ))
_sym_db.RegisterMessage(SetSingleResponse)

SetAllResponse = _reflection.GeneratedProtocolMessageType('SetAllResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETALLRESPONSE,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.SetAllResponse)
  ))
_sym_db.RegisterMessage(SetAllResponse)

FunctionControlSetResponse = _reflection.GeneratedProtocolMessageType('FunctionControlSetResponse', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONCONTROLSETRESPONSE,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.FunctionControlSetResponse)
  ))
_sym_db.RegisterMessage(FunctionControlSetResponse)

StreamControlStart = _reflection.GeneratedProtocolMessageType('StreamControlStart', (_message.Message,), dict(
  DESCRIPTOR = _STREAMCONTROLSTART,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.StreamControlStart)
  ))
_sym_db.RegisterMessage(StreamControlStart)

Sample = _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLE,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.Sample)
  ))
_sym_db.RegisterMessage(Sample)

StreamData = _reflection.GeneratedProtocolMessageType('StreamData', (_message.Message,), dict(
  DESCRIPTOR = _STREAMDATA,
  __module__ = 'binaryIoTypeB.v1alpha1.binaryIoTypeB_pb2'
  # @@protoc_insertion_point(class_scope:binaryIoTypeB.StreamData)
  ))
_sym_db.RegisterMessage(StreamData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)