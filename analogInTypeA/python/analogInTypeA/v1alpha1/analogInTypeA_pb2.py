# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analogInTypeA/v1alpha1/analogInTypeA.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*analogInTypeA/v1alpha1/analogInTypeA.proto\x12\ranalogInTypeA\"\'\n\x10\x43onfigurationSet\x12\x13\n\x0bsample_rate\x18\x01 \x01(\x07\"\x1a\n\x18\x43onfigurationSetResponse\"\x12\n\x10\x43onfigurationGet\"/\n\x18\x43onfigurationGetResponse\x12\x13\n\x0bsample_rate\x18\x01 \x01(\x07\"\x17\n\x15\x43onfigurationDescribe\"\x1f\n\x1d\x43onfigurationDescribeResponse\"\x14\n\x12\x46unctionControlGet\"\x14\n\x12\x46unctionControlSet\"+\n\x1a\x46unctionControlGetResponse\x12\r\n\x05value\x18\x01 \x01(\x02\"\x1c\n\x1a\x46unctionControlSetResponse\"\x14\n\x12StreamControlStart\"*\n\x06Sample\x12\x11\n\ttimestamp\x18\x01 \x01(\x06\x12\r\n\x05value\x18\x02 \x01(\x02\"4\n\nStreamData\x12&\n\x07samples\x18\x01 \x03(\x0b\x32\x15.analogInTypeA.SampleB\x18Z\x16\x61nalogInTypeA/v1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'analogInTypeA.v1alpha1.analogInTypeA_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\026analogInTypeA/v1alpha1'
  _globals['_CONFIGURATIONSET']._serialized_start=61
  _globals['_CONFIGURATIONSET']._serialized_end=100
  _globals['_CONFIGURATIONSETRESPONSE']._serialized_start=102
  _globals['_CONFIGURATIONSETRESPONSE']._serialized_end=128
  _globals['_CONFIGURATIONGET']._serialized_start=130
  _globals['_CONFIGURATIONGET']._serialized_end=148
  _globals['_CONFIGURATIONGETRESPONSE']._serialized_start=150
  _globals['_CONFIGURATIONGETRESPONSE']._serialized_end=197
  _globals['_CONFIGURATIONDESCRIBE']._serialized_start=199
  _globals['_CONFIGURATIONDESCRIBE']._serialized_end=222
  _globals['_CONFIGURATIONDESCRIBERESPONSE']._serialized_start=224
  _globals['_CONFIGURATIONDESCRIBERESPONSE']._serialized_end=255
  _globals['_FUNCTIONCONTROLGET']._serialized_start=257
  _globals['_FUNCTIONCONTROLGET']._serialized_end=277
  _globals['_FUNCTIONCONTROLSET']._serialized_start=279
  _globals['_FUNCTIONCONTROLSET']._serialized_end=299
  _globals['_FUNCTIONCONTROLGETRESPONSE']._serialized_start=301
  _globals['_FUNCTIONCONTROLGETRESPONSE']._serialized_end=344
  _globals['_FUNCTIONCONTROLSETRESPONSE']._serialized_start=346
  _globals['_FUNCTIONCONTROLSETRESPONSE']._serialized_end=374
  _globals['_STREAMCONTROLSTART']._serialized_start=376
  _globals['_STREAMCONTROLSTART']._serialized_end=396
  _globals['_SAMPLE']._serialized_start=398
  _globals['_SAMPLE']._serialized_end=440
  _globals['_STREAMDATA']._serialized_start=442
  _globals['_STREAMDATA']._serialized_end=494
# @@protoc_insertion_point(module_scope)
