# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: motionSensor/v1/motionSensor.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='motionSensor/v1/motionSensor.proto',
  package='motionSensor',
  syntax='proto3',
  serialized_options=b'Z\017motionSensor/v1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"motionSensor/v1/motionSensor.proto\x12\x0cmotionSensor\"\x80\x01\n\x10\x43onfigurationSet\x12\x1b\n\x13sample_rate_milliHz\x18\x01 \x01(\x07\x12\x14\n\x0c\x66ull_scale_g\x18\x02 \x01(\x05\x12\x1f\n\x17high_pass_filter_enable\x18\x03 \x01(\x08\x12\x18\n\x10\x62\x61nd_width_ratio\x18\x04 \x01(\x05\"\x1a\n\x18\x43onfigurationSetResponse\"\x12\n\x10\x43onfigurationGet\"\x88\x01\n\x18\x43onfigurationGetResponse\x12\x1b\n\x13sample_rate_millihz\x18\x01 \x01(\x07\x12\x14\n\x0c\x66ull_scale_g\x18\x02 \x01(\x05\x12\x1f\n\x17high_pass_filter_enable\x18\x03 \x01(\x08\x12\x18\n\x10\x62\x61nd_width_ratio\x18\x04 \x01(\x05\"\x17\n\x15\x43onfigurationDescribe\"\x1f\n\x1d\x43onfigurationDescribeResponse\"\x14\n\x12\x46unctionControlGet\"\x14\n\x12\x46unctionControlSet\"\x1c\n\x1a\x46unctionControlGetResponse\"\x1c\n\x1a\x46unctionControlSetResponse\"\x14\n\x12StreamControlStart\"<\n\x06Sample\x12\x11\n\ttimestamp\x18\x01 \x01(\x06\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x12\t\n\x01z\x18\x04 \x01(\x02\"3\n\nStreamData\x12%\n\x07samples\x18\x01 \x03(\x0b\x32\x14.motionSensor.SampleB\x11Z\x0fmotionSensor/v1b\x06proto3'
)




_CONFIGURATIONSET = _descriptor.Descriptor(
  name='ConfigurationSet',
  full_name='motionSensor.ConfigurationSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sample_rate_milliHz', full_name='motionSensor.ConfigurationSet.sample_rate_milliHz', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='full_scale_g', full_name='motionSensor.ConfigurationSet.full_scale_g', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='high_pass_filter_enable', full_name='motionSensor.ConfigurationSet.high_pass_filter_enable', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='band_width_ratio', full_name='motionSensor.ConfigurationSet.band_width_ratio', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=53,
  serialized_end=181,
)


_CONFIGURATIONSETRESPONSE = _descriptor.Descriptor(
  name='ConfigurationSetResponse',
  full_name='motionSensor.ConfigurationSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=183,
  serialized_end=209,
)


_CONFIGURATIONGET = _descriptor.Descriptor(
  name='ConfigurationGet',
  full_name='motionSensor.ConfigurationGet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_end=229,
)


_CONFIGURATIONGETRESPONSE = _descriptor.Descriptor(
  name='ConfigurationGetResponse',
  full_name='motionSensor.ConfigurationGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sample_rate_millihz', full_name='motionSensor.ConfigurationGetResponse.sample_rate_millihz', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='full_scale_g', full_name='motionSensor.ConfigurationGetResponse.full_scale_g', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='high_pass_filter_enable', full_name='motionSensor.ConfigurationGetResponse.high_pass_filter_enable', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='band_width_ratio', full_name='motionSensor.ConfigurationGetResponse.band_width_ratio', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=232,
  serialized_end=368,
)


_CONFIGURATIONDESCRIBE = _descriptor.Descriptor(
  name='ConfigurationDescribe',
  full_name='motionSensor.ConfigurationDescribe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=370,
  serialized_end=393,
)


_CONFIGURATIONDESCRIBERESPONSE = _descriptor.Descriptor(
  name='ConfigurationDescribeResponse',
  full_name='motionSensor.ConfigurationDescribeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=395,
  serialized_end=426,
)


_FUNCTIONCONTROLGET = _descriptor.Descriptor(
  name='FunctionControlGet',
  full_name='motionSensor.FunctionControlGet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=428,
  serialized_end=448,
)


_FUNCTIONCONTROLSET = _descriptor.Descriptor(
  name='FunctionControlSet',
  full_name='motionSensor.FunctionControlSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=450,
  serialized_end=470,
)


_FUNCTIONCONTROLGETRESPONSE = _descriptor.Descriptor(
  name='FunctionControlGetResponse',
  full_name='motionSensor.FunctionControlGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=472,
  serialized_end=500,
)


_FUNCTIONCONTROLSETRESPONSE = _descriptor.Descriptor(
  name='FunctionControlSetResponse',
  full_name='motionSensor.FunctionControlSetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=502,
  serialized_end=530,
)


_STREAMCONTROLSTART = _descriptor.Descriptor(
  name='StreamControlStart',
  full_name='motionSensor.StreamControlStart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=532,
  serialized_end=552,
)


_SAMPLE = _descriptor.Descriptor(
  name='Sample',
  full_name='motionSensor.Sample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='motionSensor.Sample.timestamp', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='x', full_name='motionSensor.Sample.x', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='motionSensor.Sample.y', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='motionSensor.Sample.z', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=554,
  serialized_end=614,
)


_STREAMDATA = _descriptor.Descriptor(
  name='StreamData',
  full_name='motionSensor.StreamData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='samples', full_name='motionSensor.StreamData.samples', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=616,
  serialized_end=667,
)

_STREAMDATA.fields_by_name['samples'].message_type = _SAMPLE
DESCRIPTOR.message_types_by_name['ConfigurationSet'] = _CONFIGURATIONSET
DESCRIPTOR.message_types_by_name['ConfigurationSetResponse'] = _CONFIGURATIONSETRESPONSE
DESCRIPTOR.message_types_by_name['ConfigurationGet'] = _CONFIGURATIONGET
DESCRIPTOR.message_types_by_name['ConfigurationGetResponse'] = _CONFIGURATIONGETRESPONSE
DESCRIPTOR.message_types_by_name['ConfigurationDescribe'] = _CONFIGURATIONDESCRIBE
DESCRIPTOR.message_types_by_name['ConfigurationDescribeResponse'] = _CONFIGURATIONDESCRIBERESPONSE
DESCRIPTOR.message_types_by_name['FunctionControlGet'] = _FUNCTIONCONTROLGET
DESCRIPTOR.message_types_by_name['FunctionControlSet'] = _FUNCTIONCONTROLSET
DESCRIPTOR.message_types_by_name['FunctionControlGetResponse'] = _FUNCTIONCONTROLGETRESPONSE
DESCRIPTOR.message_types_by_name['FunctionControlSetResponse'] = _FUNCTIONCONTROLSETRESPONSE
DESCRIPTOR.message_types_by_name['StreamControlStart'] = _STREAMCONTROLSTART
DESCRIPTOR.message_types_by_name['Sample'] = _SAMPLE
DESCRIPTOR.message_types_by_name['StreamData'] = _STREAMDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigurationSet = _reflection.GeneratedProtocolMessageType('ConfigurationSet', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATIONSET,
  '__module__' : 'motionSensor.v1.motionSensor_pb2'
  # @@protoc_insertion_point(class_scope:motionSensor.ConfigurationSet)
  })
_sym_db.RegisterMessage(ConfigurationSet)

ConfigurationSetResponse = _reflection.GeneratedProtocolMessageType('ConfigurationSetResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATIONSETRESPONSE,
  '__module__' : 'motionSensor.v1.motionSensor_pb2'
  # @@protoc_insertion_point(class_scope:motionSensor.ConfigurationSetResponse)
  })
_sym_db.RegisterMessage(ConfigurationSetResponse)

ConfigurationGet = _reflection.GeneratedProtocolMessageType('ConfigurationGet', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATIONGET,
  '__module__' : 'motionSensor.v1.motionSensor_pb2'
  # @@protoc_insertion_point(class_scope:motionSensor.ConfigurationGet)
  })
_sym_db.RegisterMessage(ConfigurationGet)

ConfigurationGetResponse = _reflection.GeneratedProtocolMessageType('ConfigurationGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATIONGETRESPONSE,
  '__module__' : 'motionSensor.v1.motionSensor_pb2'
  # @@protoc_insertion_point(class_scope:motionSensor.ConfigurationGetResponse)
  })
_sym_db.RegisterMessage(ConfigurationGetResponse)

ConfigurationDescribe = _reflection.GeneratedProtocolMessageType('ConfigurationDescribe', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATIONDESCRIBE,
  '__module__' : 'motionSensor.v1.motionSensor_pb2'
  # @@protoc_insertion_point(class_scope:motionSensor.ConfigurationDescribe)
  })
_sym_db.RegisterMessage(ConfigurationDescribe)

ConfigurationDescribeResponse = _reflection.GeneratedProtocolMessageType('ConfigurationDescribeResponse', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGURATIONDESCRIBERESPONSE,
  '__module__' : 'motionSensor.v1.motionSensor_pb2'
  # @@protoc_insertion_point(class_scope:motionSensor.ConfigurationDescribeResponse)
  })
_sym_db.RegisterMessage(ConfigurationDescribeResponse)

FunctionControlGet = _reflection.GeneratedProtocolMessageType('FunctionControlGet', (_message.Message,), {
  'DESCRIPTOR' : _FUNCTIONCONTROLGET,
  '__module__' : 'motionSensor.v1.motionSensor_pb2'
  # @@protoc_insertion_point(class_scope:motionSensor.FunctionControlGet)
  })
_sym_db.RegisterMessage(FunctionControlGet)

FunctionControlSet = _reflection.GeneratedProtocolMessageType('FunctionControlSet', (_message.Message,), {
  'DESCRIPTOR' : _FUNCTIONCONTROLSET,
  '__module__' : 'motionSensor.v1.motionSensor_pb2'
  # @@protoc_insertion_point(class_scope:motionSensor.FunctionControlSet)
  })
_sym_db.RegisterMessage(FunctionControlSet)

FunctionControlGetResponse = _reflection.GeneratedProtocolMessageType('FunctionControlGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _FUNCTIONCONTROLGETRESPONSE,
  '__module__' : 'motionSensor.v1.motionSensor_pb2'
  # @@protoc_insertion_point(class_scope:motionSensor.FunctionControlGetResponse)
  })
_sym_db.RegisterMessage(FunctionControlGetResponse)

FunctionControlSetResponse = _reflection.GeneratedProtocolMessageType('FunctionControlSetResponse', (_message.Message,), {
  'DESCRIPTOR' : _FUNCTIONCONTROLSETRESPONSE,
  '__module__' : 'motionSensor.v1.motionSensor_pb2'
  # @@protoc_insertion_point(class_scope:motionSensor.FunctionControlSetResponse)
  })
_sym_db.RegisterMessage(FunctionControlSetResponse)

StreamControlStart = _reflection.GeneratedProtocolMessageType('StreamControlStart', (_message.Message,), {
  'DESCRIPTOR' : _STREAMCONTROLSTART,
  '__module__' : 'motionSensor.v1.motionSensor_pb2'
  # @@protoc_insertion_point(class_scope:motionSensor.StreamControlStart)
  })
_sym_db.RegisterMessage(StreamControlStart)

Sample = _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), {
  'DESCRIPTOR' : _SAMPLE,
  '__module__' : 'motionSensor.v1.motionSensor_pb2'
  # @@protoc_insertion_point(class_scope:motionSensor.Sample)
  })
_sym_db.RegisterMessage(Sample)

StreamData = _reflection.GeneratedProtocolMessageType('StreamData', (_message.Message,), {
  'DESCRIPTOR' : _STREAMDATA,
  '__module__' : 'motionSensor.v1.motionSensor_pb2'
  # @@protoc_insertion_point(class_scope:motionSensor.StreamData)
  })
_sym_db.RegisterMessage(StreamData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
