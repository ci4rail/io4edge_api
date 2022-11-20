# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: templateInterface/v1alpha1/templateInterface.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='templateInterface/v1alpha1/templateInterface.proto',
  package='templateInterface',
  syntax='proto3',
  serialized_options=_b('Z\032templateInterface/v1alpha1'),
  serialized_pb=_b('\n2templateInterface/v1alpha1/templateInterface.proto\x12\x11templateInterface\"\'\n\x10\x43onfigurationSet\x12\x13\n\x0bsample_rate\x18\x01 \x01(\x07\"\x1a\n\x18\x43onfigurationSetResponse\"\x12\n\x10\x43onfigurationGet\"/\n\x18\x43onfigurationGetResponse\x12\x13\n\x0bsample_rate\x18\x01 \x01(\x07\"\x17\n\x15\x43onfigurationDescribe\".\n\x1d\x43onfigurationDescribeResponse\x12\r\n\x05ident\x18\x01 \x01(\t\"\xdd\x01\n\x15\x43onfigurationResponse\x12:\n\x03get\x18\x01 \x01(\x0b\x32+.templateInterface.ConfigurationGetResponseH\x00\x12:\n\x03set\x18\x02 \x01(\x0b\x32+.templateInterface.ConfigurationSetResponseH\x00\x12\x44\n\x08\x64\x65scribe\x18\x03 \x01(\x0b\x32\x30.templateInterface.ConfigurationDescribeResponseH\x00\x42\x06\n\x04type\"\x14\n\x12\x46unctionControlGet\"#\n\x12\x46unctionControlSet\x12\r\n\x05value\x18\x01 \x01(\x07\"+\n\x1a\x46unctionControlGetResponse\x12\r\n\x05value\x18\x01 \x01(\x07\"\x1c\n\x1a\x46unctionControlSetResponse\"$\n\x12StreamControlStart\x12\x0e\n\x06modulo\x18\x01 \x01(\x07\"*\n\x06Sample\x12\x11\n\ttimestamp\x18\x01 \x01(\x06\x12\r\n\x05value\x18\x02 \x01(\x07\"8\n\nStreamData\x12*\n\x07samples\x18\x01 \x03(\x0b\x32\x19.templateInterface.SampleB\x1cZ\x1atemplateInterface/v1alpha1b\x06proto3')
)




_CONFIGURATIONSET = _descriptor.Descriptor(
  name='ConfigurationSet',
  full_name='templateInterface.ConfigurationSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sample_rate', full_name='templateInterface.ConfigurationSet.sample_rate', index=0,
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
  serialized_start=73,
  serialized_end=112,
)


_CONFIGURATIONSETRESPONSE = _descriptor.Descriptor(
  name='ConfigurationSetResponse',
  full_name='templateInterface.ConfigurationSetResponse',
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
  serialized_start=114,
  serialized_end=140,
)


_CONFIGURATIONGET = _descriptor.Descriptor(
  name='ConfigurationGet',
  full_name='templateInterface.ConfigurationGet',
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
  serialized_start=142,
  serialized_end=160,
)


_CONFIGURATIONGETRESPONSE = _descriptor.Descriptor(
  name='ConfigurationGetResponse',
  full_name='templateInterface.ConfigurationGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sample_rate', full_name='templateInterface.ConfigurationGetResponse.sample_rate', index=0,
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
  serialized_start=162,
  serialized_end=209,
)


_CONFIGURATIONDESCRIBE = _descriptor.Descriptor(
  name='ConfigurationDescribe',
  full_name='templateInterface.ConfigurationDescribe',
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
  serialized_start=211,
  serialized_end=234,
)


_CONFIGURATIONDESCRIBERESPONSE = _descriptor.Descriptor(
  name='ConfigurationDescribeResponse',
  full_name='templateInterface.ConfigurationDescribeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ident', full_name='templateInterface.ConfigurationDescribeResponse.ident', index=0,
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
  serialized_start=236,
  serialized_end=282,
)


_CONFIGURATIONRESPONSE = _descriptor.Descriptor(
  name='ConfigurationResponse',
  full_name='templateInterface.ConfigurationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='get', full_name='templateInterface.ConfigurationResponse.get', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='set', full_name='templateInterface.ConfigurationResponse.set', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='describe', full_name='templateInterface.ConfigurationResponse.describe', index=2,
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
      name='type', full_name='templateInterface.ConfigurationResponse.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=285,
  serialized_end=506,
)


_FUNCTIONCONTROLGET = _descriptor.Descriptor(
  name='FunctionControlGet',
  full_name='templateInterface.FunctionControlGet',
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
  serialized_start=508,
  serialized_end=528,
)


_FUNCTIONCONTROLSET = _descriptor.Descriptor(
  name='FunctionControlSet',
  full_name='templateInterface.FunctionControlSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='templateInterface.FunctionControlSet.value', index=0,
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
  serialized_start=530,
  serialized_end=565,
)


_FUNCTIONCONTROLGETRESPONSE = _descriptor.Descriptor(
  name='FunctionControlGetResponse',
  full_name='templateInterface.FunctionControlGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='templateInterface.FunctionControlGetResponse.value', index=0,
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
  serialized_start=567,
  serialized_end=610,
)


_FUNCTIONCONTROLSETRESPONSE = _descriptor.Descriptor(
  name='FunctionControlSetResponse',
  full_name='templateInterface.FunctionControlSetResponse',
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
  serialized_start=612,
  serialized_end=640,
)


_STREAMCONTROLSTART = _descriptor.Descriptor(
  name='StreamControlStart',
  full_name='templateInterface.StreamControlStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='modulo', full_name='templateInterface.StreamControlStart.modulo', index=0,
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
  serialized_start=642,
  serialized_end=678,
)


_SAMPLE = _descriptor.Descriptor(
  name='Sample',
  full_name='templateInterface.Sample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='templateInterface.Sample.timestamp', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='templateInterface.Sample.value', index=1,
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
  serialized_start=680,
  serialized_end=722,
)


_STREAMDATA = _descriptor.Descriptor(
  name='StreamData',
  full_name='templateInterface.StreamData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='samples', full_name='templateInterface.StreamData.samples', index=0,
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
  serialized_start=724,
  serialized_end=780,
)

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
_STREAMDATA.fields_by_name['samples'].message_type = _SAMPLE
DESCRIPTOR.message_types_by_name['ConfigurationSet'] = _CONFIGURATIONSET
DESCRIPTOR.message_types_by_name['ConfigurationSetResponse'] = _CONFIGURATIONSETRESPONSE
DESCRIPTOR.message_types_by_name['ConfigurationGet'] = _CONFIGURATIONGET
DESCRIPTOR.message_types_by_name['ConfigurationGetResponse'] = _CONFIGURATIONGETRESPONSE
DESCRIPTOR.message_types_by_name['ConfigurationDescribe'] = _CONFIGURATIONDESCRIBE
DESCRIPTOR.message_types_by_name['ConfigurationDescribeResponse'] = _CONFIGURATIONDESCRIBERESPONSE
DESCRIPTOR.message_types_by_name['ConfigurationResponse'] = _CONFIGURATIONRESPONSE
DESCRIPTOR.message_types_by_name['FunctionControlGet'] = _FUNCTIONCONTROLGET
DESCRIPTOR.message_types_by_name['FunctionControlSet'] = _FUNCTIONCONTROLSET
DESCRIPTOR.message_types_by_name['FunctionControlGetResponse'] = _FUNCTIONCONTROLGETRESPONSE
DESCRIPTOR.message_types_by_name['FunctionControlSetResponse'] = _FUNCTIONCONTROLSETRESPONSE
DESCRIPTOR.message_types_by_name['StreamControlStart'] = _STREAMCONTROLSTART
DESCRIPTOR.message_types_by_name['Sample'] = _SAMPLE
DESCRIPTOR.message_types_by_name['StreamData'] = _STREAMDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigurationSet = _reflection.GeneratedProtocolMessageType('ConfigurationSet', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONSET,
  __module__ = 'templateInterface.v1alpha1.templateInterface_pb2'
  # @@protoc_insertion_point(class_scope:templateInterface.ConfigurationSet)
  ))
_sym_db.RegisterMessage(ConfigurationSet)

ConfigurationSetResponse = _reflection.GeneratedProtocolMessageType('ConfigurationSetResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONSETRESPONSE,
  __module__ = 'templateInterface.v1alpha1.templateInterface_pb2'
  # @@protoc_insertion_point(class_scope:templateInterface.ConfigurationSetResponse)
  ))
_sym_db.RegisterMessage(ConfigurationSetResponse)

ConfigurationGet = _reflection.GeneratedProtocolMessageType('ConfigurationGet', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONGET,
  __module__ = 'templateInterface.v1alpha1.templateInterface_pb2'
  # @@protoc_insertion_point(class_scope:templateInterface.ConfigurationGet)
  ))
_sym_db.RegisterMessage(ConfigurationGet)

ConfigurationGetResponse = _reflection.GeneratedProtocolMessageType('ConfigurationGetResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONGETRESPONSE,
  __module__ = 'templateInterface.v1alpha1.templateInterface_pb2'
  # @@protoc_insertion_point(class_scope:templateInterface.ConfigurationGetResponse)
  ))
_sym_db.RegisterMessage(ConfigurationGetResponse)

ConfigurationDescribe = _reflection.GeneratedProtocolMessageType('ConfigurationDescribe', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONDESCRIBE,
  __module__ = 'templateInterface.v1alpha1.templateInterface_pb2'
  # @@protoc_insertion_point(class_scope:templateInterface.ConfigurationDescribe)
  ))
_sym_db.RegisterMessage(ConfigurationDescribe)

ConfigurationDescribeResponse = _reflection.GeneratedProtocolMessageType('ConfigurationDescribeResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONDESCRIBERESPONSE,
  __module__ = 'templateInterface.v1alpha1.templateInterface_pb2'
  # @@protoc_insertion_point(class_scope:templateInterface.ConfigurationDescribeResponse)
  ))
_sym_db.RegisterMessage(ConfigurationDescribeResponse)

ConfigurationResponse = _reflection.GeneratedProtocolMessageType('ConfigurationResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONFIGURATIONRESPONSE,
  __module__ = 'templateInterface.v1alpha1.templateInterface_pb2'
  # @@protoc_insertion_point(class_scope:templateInterface.ConfigurationResponse)
  ))
_sym_db.RegisterMessage(ConfigurationResponse)

FunctionControlGet = _reflection.GeneratedProtocolMessageType('FunctionControlGet', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONCONTROLGET,
  __module__ = 'templateInterface.v1alpha1.templateInterface_pb2'
  # @@protoc_insertion_point(class_scope:templateInterface.FunctionControlGet)
  ))
_sym_db.RegisterMessage(FunctionControlGet)

FunctionControlSet = _reflection.GeneratedProtocolMessageType('FunctionControlSet', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONCONTROLSET,
  __module__ = 'templateInterface.v1alpha1.templateInterface_pb2'
  # @@protoc_insertion_point(class_scope:templateInterface.FunctionControlSet)
  ))
_sym_db.RegisterMessage(FunctionControlSet)

FunctionControlGetResponse = _reflection.GeneratedProtocolMessageType('FunctionControlGetResponse', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONCONTROLGETRESPONSE,
  __module__ = 'templateInterface.v1alpha1.templateInterface_pb2'
  # @@protoc_insertion_point(class_scope:templateInterface.FunctionControlGetResponse)
  ))
_sym_db.RegisterMessage(FunctionControlGetResponse)

FunctionControlSetResponse = _reflection.GeneratedProtocolMessageType('FunctionControlSetResponse', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTIONCONTROLSETRESPONSE,
  __module__ = 'templateInterface.v1alpha1.templateInterface_pb2'
  # @@protoc_insertion_point(class_scope:templateInterface.FunctionControlSetResponse)
  ))
_sym_db.RegisterMessage(FunctionControlSetResponse)

StreamControlStart = _reflection.GeneratedProtocolMessageType('StreamControlStart', (_message.Message,), dict(
  DESCRIPTOR = _STREAMCONTROLSTART,
  __module__ = 'templateInterface.v1alpha1.templateInterface_pb2'
  # @@protoc_insertion_point(class_scope:templateInterface.StreamControlStart)
  ))
_sym_db.RegisterMessage(StreamControlStart)

Sample = _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLE,
  __module__ = 'templateInterface.v1alpha1.templateInterface_pb2'
  # @@protoc_insertion_point(class_scope:templateInterface.Sample)
  ))
_sym_db.RegisterMessage(Sample)

StreamData = _reflection.GeneratedProtocolMessageType('StreamData', (_message.Message,), dict(
  DESCRIPTOR = _STREAMDATA,
  __module__ = 'templateInterface.v1alpha1.templateInterface_pb2'
  # @@protoc_insertion_point(class_scope:templateInterface.StreamData)
  ))
_sym_db.RegisterMessage(StreamData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
