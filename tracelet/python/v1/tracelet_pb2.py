# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/tracelet.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11v1/tracelet.proto\x12\x08tracelet\x1a\x1fgoogle/protobuf/timestamp.proto\"\xe7\n\n\x10TraceletToServer\x12\n\n\x02id\x18\x01 \x01(\x05\x12/\n\x0b\x64\x65livery_ts\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0btracelet_id\x18\x03 \x01(\t\x12\x10\n\x08ignition\x18\x04 \x01(\x08\x12\x37\n\x08location\x18\x05 \x01(\x0b\x32#.tracelet.TraceletToServer.LocationH\x00\x1a\xad\t\n\x08Location\x12\x36\n\x04gnss\x18\x01 \x01(\x0b\x32(.tracelet.TraceletToServer.Location.Gnss\x12\x34\n\x03uwb\x18\x02 \x01(\x0b\x32\'.tracelet.TraceletToServer.Location.Uwb\x12\x38\n\x05\x66used\x18\x07 \x01(\x0b\x32).tracelet.TraceletToServer.Location.Fused\x12@\n\tdirection\x18\x03 \x01(\x0e\x32-.tracelet.TraceletToServer.Location.Direction\x12\r\n\x05speed\x18\x04 \x01(\x01\x12\x0f\n\x07mileage\x18\x05 \x01(\x05\x12\x13\n\x0btemperature\x18\x06 \x01(\x01\x12\x46\n\x0c\x61\x63\x63\x65leration\x18\x08 \x01(\x0b\x32\x30.tracelet.TraceletToServer.Location.Acceleration\x1a\xcd\x01\n\x04Gnss\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x04 \x01(\x01\x12\x0b\n\x03\x65ph\x18\x05 \x01(\x01\x12\x0b\n\x03\x65pv\x18\x06 \x01(\x01\x12\x10\n\x08\x66ix_type\x18\x07 \x01(\x05\x12\x13\n\x0bhead_motion\x18\x08 \x01(\x01\x12\x14\n\x0chead_vehicle\x18\t \x01(\x01\x12\x12\n\nhead_valid\x18\n \x01(\r\x12\x14\n\x0cground_speed\x18\x0b \x01(\x01\x1a\xd6\x01\n\x03Uwb\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\t\n\x01x\x18\x02 \x01(\x01\x12\t\n\x01y\x18\x03 \x01(\x01\x12\t\n\x01z\x18\x04 \x01(\x01\x12\x0f\n\x07site_id\x18\x05 \x01(\r\x12\x1a\n\x12location_signature\x18\x06 \x01(\x06\x12\x0b\n\x03\x65ph\x18\x07 \x01(\x01\x12\x10\n\x08\x66ix_type\x18\x08 \x01(\x05\x12\x13\n\x0bhead_motion\x18\t \x01(\x01\x12\x14\n\x0chead_vehicle\x18\n \x01(\x01\x12\x12\n\nhead_valid\x18\x0b \x01(\r\x12\x14\n\x0cground_speed\x18\x0c \x01(\x01\x1a\xaf\x01\n\x05\x46used\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x04 \x01(\x01\x12\x0b\n\x03\x65ph\x18\x05 \x01(\x01\x12\x13\n\x0bhead_motion\x18\x06 \x01(\x01\x12\x14\n\x0chead_vehicle\x18\x07 \x01(\x01\x12\x12\n\nhead_valid\x18\x08 \x01(\r\x12\x14\n\x0cground_speed\x18\t \x01(\x01\x1a\x95\x01\n\x0c\x41\x63\x63\x65leration\x12\r\n\x05x_max\x18\x01 \x01(\x01\x12\r\n\x05y_max\x18\x02 \x01(\x01\x12\r\n\x05z_max\x18\x03 \x01(\x01\x12\r\n\x05x_min\x18\x04 \x01(\x01\x12\r\n\x05y_min\x18\x05 \x01(\x01\x12\r\n\x05z_min\x18\x06 \x01(\x01\x12\r\n\x05x_avg\x18\x07 \x01(\x01\x12\r\n\x05y_avg\x18\x08 \x01(\x01\x12\r\n\x05z_avg\x18\t \x01(\x01\"G\n\tDirection\x12\x10\n\x0cNO_DIRECTION\x10\x00\x12\x13\n\x0f\x43\x41\x42_A_DIRECTION\x10\x01\x12\x13\n\x0f\x43\x41\x42_B_DIRECTION\x10\x02\x42\x06\n\x04typeB\x0cZ\n./traceletb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'v1.tracelet_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\n./tracelet'
  _globals['_TRACELETTOSERVER']._serialized_start=65
  _globals['_TRACELETTOSERVER']._serialized_end=1448
  _globals['_TRACELETTOSERVER_LOCATION']._serialized_start=243
  _globals['_TRACELETTOSERVER_LOCATION']._serialized_end=1440
  _globals['_TRACELETTOSERVER_LOCATION_GNSS']._serialized_start=615
  _globals['_TRACELETTOSERVER_LOCATION_GNSS']._serialized_end=820
  _globals['_TRACELETTOSERVER_LOCATION_UWB']._serialized_start=823
  _globals['_TRACELETTOSERVER_LOCATION_UWB']._serialized_end=1037
  _globals['_TRACELETTOSERVER_LOCATION_FUSED']._serialized_start=1040
  _globals['_TRACELETTOSERVER_LOCATION_FUSED']._serialized_end=1215
  _globals['_TRACELETTOSERVER_LOCATION_ACCELERATION']._serialized_start=1218
  _globals['_TRACELETTOSERVER_LOCATION_ACCELERATION']._serialized_end=1367
  _globals['_TRACELETTOSERVER_LOCATION_DIRECTION']._serialized_start=1369
  _globals['_TRACELETTOSERVER_LOCATION_DIRECTION']._serialized_end=1440
# @@protoc_insertion_point(module_scope)
