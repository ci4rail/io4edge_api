# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: binaryIoTypeD/v1/binaryIoTypeD.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$binaryIoTypeD/v1/binaryIoTypeD.proto\x12\rbinaryIoTypeD\"\xb6\x01\n\rChannelConfig\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\x05\x12(\n\x04mode\x18\x02 \x01(\x0e\x32\x1a.binaryIoTypeD.ChannelMode\x12\x14\n\x0cinitialValue\x18\x03 \x01(\x08\x12!\n\x19overloadRecoveryTimeoutMs\x18\x04 \x01(\x05\x12\x19\n\x11watchdogTimeoutMs\x18\x05 \x01(\x05\x12\x16\n\x0e\x66rittingEnable\x18\x06 \x01(\x08\"G\n\x10\x43onfigurationSet\x12\x33\n\rchannelConfig\x18\x01 \x03(\x0b\x32\x1c.binaryIoTypeD.ChannelConfig\"\x1a\n\x18\x43onfigurationSetResponse\"\x12\n\x10\x43onfigurationGet\"O\n\x18\x43onfigurationGetResponse\x12\x33\n\rchannelConfig\x18\x01 \x03(\x0b\x32\x1c.binaryIoTypeD.ChannelConfig\"\x17\n\x15\x43onfigurationDescribe\"9\n\x1d\x43onfigurationDescribeResponse\x12\x18\n\x10numberOfChannels\x18\x01 \x01(\x07\"\x14\n\x12\x46unctionControlGet\"+\n\tSetSingle\x12\x0f\n\x07\x63hannel\x18\x01 \x01(\x07\x12\r\n\x05state\x18\x02 \x01(\x08\"&\n\x06SetAll\x12\x0e\n\x06values\x18\x01 \x01(\x07\x12\x0c\n\x04mask\x18\x02 \x01(\x07\"\x1c\n\x0cSetExitError\x12\x0c\n\x04mask\x18\x01 \x01(\x07\"\xa1\x01\n\x12\x46unctionControlSet\x12*\n\x06single\x18\x01 \x01(\x0b\x32\x18.binaryIoTypeD.SetSingleH\x00\x12$\n\x03\x61ll\x18\x02 \x01(\x0b\x32\x15.binaryIoTypeD.SetAllH\x00\x12\x31\n\nexit_error\x18\x03 \x01(\x0b\x32\x1b.binaryIoTypeD.SetExitErrorH\x00\x42\x06\n\x04type\":\n\x1a\x46unctionControlGetResponse\x12\x0e\n\x06inputs\x18\x01 \x01(\x07\x12\x0c\n\x04\x64iag\x18\x02 \x03(\r\"\x10\n\x0eSetAllResponse\"\x13\n\x11SetSingleResponse\"\x16\n\x14SetExitErrorResponse\"\xc1\x01\n\x1a\x46unctionControlSetResponse\x12\x32\n\x06single\x18\x01 \x01(\x0b\x32 .binaryIoTypeD.SetSingleResponseH\x00\x12,\n\x03\x61ll\x18\x02 \x01(\x0b\x32\x1d.binaryIoTypeD.SetAllResponseH\x00\x12\x39\n\nexit_error\x18\x03 \x01(\x0b\x32#.binaryIoTypeD.SetExitErrorResponseH\x00\x42\x06\n\x04type\"\x14\n\x12StreamControlStart\"\x08\n\x06Sample\"\x0c\n\nStreamData*\xa1\x01\n\x0b\x43hannelMode\x12\"\n\x1e\x42INARYIOTYPED_INPUT_LOW_ACTIVE\x10\x00\x12#\n\x1f\x42INARYIOTYPED_INPUT_HIGH_ACTIVE\x10\x01\x12#\n\x1f\x42INARYIOTYPED_OUTPUT_LOW_ACTIVE\x10\x02\x12$\n BINARYIOTYPED_OUTPUT_HIGH_ACTIVE\x10\x03*<\n\x0b\x43hannelDiag\x12\n\n\x06NoDiag\x10\x00\x12\x13\n\x0fNoSupplyVoltage\x10\x01\x12\x0c\n\x08Overload\x10\x02\x42\x12Z\x10\x62inaryIoTypeD/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'binaryIoTypeD.v1.binaryIoTypeD_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\020binaryIoTypeD/v1'
  _globals['_CHANNELMODE']._serialized_start=1193
  _globals['_CHANNELMODE']._serialized_end=1354
  _globals['_CHANNELDIAG']._serialized_start=1356
  _globals['_CHANNELDIAG']._serialized_end=1416
  _globals['_CHANNELCONFIG']._serialized_start=56
  _globals['_CHANNELCONFIG']._serialized_end=238
  _globals['_CONFIGURATIONSET']._serialized_start=240
  _globals['_CONFIGURATIONSET']._serialized_end=311
  _globals['_CONFIGURATIONSETRESPONSE']._serialized_start=313
  _globals['_CONFIGURATIONSETRESPONSE']._serialized_end=339
  _globals['_CONFIGURATIONGET']._serialized_start=341
  _globals['_CONFIGURATIONGET']._serialized_end=359
  _globals['_CONFIGURATIONGETRESPONSE']._serialized_start=361
  _globals['_CONFIGURATIONGETRESPONSE']._serialized_end=440
  _globals['_CONFIGURATIONDESCRIBE']._serialized_start=442
  _globals['_CONFIGURATIONDESCRIBE']._serialized_end=465
  _globals['_CONFIGURATIONDESCRIBERESPONSE']._serialized_start=467
  _globals['_CONFIGURATIONDESCRIBERESPONSE']._serialized_end=524
  _globals['_FUNCTIONCONTROLGET']._serialized_start=526
  _globals['_FUNCTIONCONTROLGET']._serialized_end=546
  _globals['_SETSINGLE']._serialized_start=548
  _globals['_SETSINGLE']._serialized_end=591
  _globals['_SETALL']._serialized_start=593
  _globals['_SETALL']._serialized_end=631
  _globals['_SETEXITERROR']._serialized_start=633
  _globals['_SETEXITERROR']._serialized_end=661
  _globals['_FUNCTIONCONTROLSET']._serialized_start=664
  _globals['_FUNCTIONCONTROLSET']._serialized_end=825
  _globals['_FUNCTIONCONTROLGETRESPONSE']._serialized_start=827
  _globals['_FUNCTIONCONTROLGETRESPONSE']._serialized_end=885
  _globals['_SETALLRESPONSE']._serialized_start=887
  _globals['_SETALLRESPONSE']._serialized_end=903
  _globals['_SETSINGLERESPONSE']._serialized_start=905
  _globals['_SETSINGLERESPONSE']._serialized_end=924
  _globals['_SETEXITERRORRESPONSE']._serialized_start=926
  _globals['_SETEXITERRORRESPONSE']._serialized_end=948
  _globals['_FUNCTIONCONTROLSETRESPONSE']._serialized_start=951
  _globals['_FUNCTIONCONTROLSETRESPONSE']._serialized_end=1144
  _globals['_STREAMCONTROLSTART']._serialized_start=1146
  _globals['_STREAMCONTROLSTART']._serialized_end=1166
  _globals['_SAMPLE']._serialized_start=1168
  _globals['_SAMPLE']._serialized_end=1176
  _globals['_STREAMDATA']._serialized_start=1178
  _globals['_STREAMDATA']._serialized_end=1190
# @@protoc_insertion_point(module_scope)
