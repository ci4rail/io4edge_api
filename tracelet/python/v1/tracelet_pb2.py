# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: v1/tracelet.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='v1/tracelet.proto',
  package='tracelet',
  syntax='proto3',
  serialized_options=_b('Z\n./tracelet'),
  serialized_pb=_b('\n\x11v1/tracelet.proto\x12\x08tracelet\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc6\x01\n\x10ServerToTracelet\x12\n\n\x02id\x18\x01 \x01(\x05\x12>\n\x08location\x18\x02 \x01(\x0b\x32*.tracelet.ServerToTracelet.LocationRequestH\x00\x12:\n\x06status\x18\x03 \x01(\x0b\x32(.tracelet.ServerToTracelet.StatusRequestH\x00\x1a\x11\n\x0fLocationRequest\x1a\x0f\n\rStatusRequestB\x06\n\x04type\"\xb9\x07\n\x10TraceletToServer\x12\n\n\x02id\x18\x01 \x01(\x05\x12/\n\x0b\x64\x65livery_ts\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0btracelet_id\x18\x03 \x01(\t\x12\x10\n\x08ignition\x18\x04 \x01(\x08\x12\x37\n\x08location\x18\x05 \x01(\x0b\x32#.tracelet.TraceletToServer.LocationH\x00\x12;\n\x06status\x18\x06 \x01(\x0b\x32).tracelet.TraceletToServer.StatusResponseH\x00\x1a\xa3\x04\n\x08Location\x12\x36\n\x04gnss\x18\x01 \x01(\x0b\x32(.tracelet.TraceletToServer.Location.Gnss\x12\x34\n\x03uwb\x18\x02 \x01(\x0b\x32\'.tracelet.TraceletToServer.Location.Uwb\x12@\n\tdirection\x18\x03 \x01(\x0e\x32-.tracelet.TraceletToServer.Location.Direction\x12\r\n\x05speed\x18\x04 \x01(\x01\x12\x0f\n\x07mileage\x18\x05 \x01(\x05\x12\x13\n\x0btemperature\x18\x06 \x01(\x01\x1ax\n\x04Gnss\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x04 \x01(\x01\x12\x0b\n\x03\x65ph\x18\x05 \x01(\x01\x12\x0b\n\x03\x65pv\x18\x06 \x01(\x01\x12\x10\n\x08\x66ix_type\x18\x07 \x01(\x05\x1ao\n\x03Uwb\x12\r\n\x05valid\x18\x01 \x01(\x08\x12\t\n\x01x\x18\x02 \x01(\x01\x12\t\n\x01y\x18\x03 \x01(\x01\x12\t\n\x01z\x18\x04 \x01(\x01\x12\x0f\n\x07site_id\x18\x05 \x01(\r\x12\x1a\n\x12location_signature\x18\x06 \x01(\x06\x12\x0b\n\x03\x65ph\x18\x07 \x01(\x01\"G\n\tDirection\x12\x10\n\x0cNO_DIRECTION\x10\x00\x12\x13\n\x0f\x43\x41\x42_A_DIRECTION\x10\x01\x12\x13\n\x0f\x43\x41\x42_B_DIRECTION\x10\x02\x1a\x9c\x01\n\x0eStatusResponse\x12\x16\n\x0epower_up_count\x18\x01 \x01(\x05\x12\x10\n\x08has_time\x18\x02 \x01(\x08\x12\x19\n\x11uwb_module_status\x18\x03 \x01(\x05\x12\x1a\n\x12gnss_module_status\x18\x04 \x01(\x05\x12\x13\n\x0bimu1_status\x18\x05 \x01(\x05\x12\x14\n\x0ctacho_status\x18\x06 \x01(\x05\x42\x06\n\x04typeB\x0cZ\n./traceletb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_TRACELETTOSERVER_LOCATION_DIRECTION = _descriptor.EnumDescriptor(
  name='Direction',
  full_name='tracelet.TraceletToServer.Location.Direction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_DIRECTION', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAB_A_DIRECTION', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CAB_B_DIRECTION', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=981,
  serialized_end=1052,
)
_sym_db.RegisterEnumDescriptor(_TRACELETTOSERVER_LOCATION_DIRECTION)


_SERVERTOTRACELET_LOCATIONREQUEST = _descriptor.Descriptor(
  name='LocationRequest',
  full_name='tracelet.ServerToTracelet.LocationRequest',
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
  serialized_start=221,
  serialized_end=238,
)

_SERVERTOTRACELET_STATUSREQUEST = _descriptor.Descriptor(
  name='StatusRequest',
  full_name='tracelet.ServerToTracelet.StatusRequest',
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
  serialized_start=240,
  serialized_end=255,
)

_SERVERTOTRACELET = _descriptor.Descriptor(
  name='ServerToTracelet',
  full_name='tracelet.ServerToTracelet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tracelet.ServerToTracelet.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='tracelet.ServerToTracelet.location', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='tracelet.ServerToTracelet.status', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SERVERTOTRACELET_LOCATIONREQUEST, _SERVERTOTRACELET_STATUSREQUEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='tracelet.ServerToTracelet.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=65,
  serialized_end=263,
)


_TRACELETTOSERVER_LOCATION_GNSS = _descriptor.Descriptor(
  name='Gnss',
  full_name='tracelet.TraceletToServer.Location.Gnss',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valid', full_name='tracelet.TraceletToServer.Location.Gnss.valid', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='tracelet.TraceletToServer.Location.Gnss.latitude', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='tracelet.TraceletToServer.Location.Gnss.longitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='tracelet.TraceletToServer.Location.Gnss.altitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eph', full_name='tracelet.TraceletToServer.Location.Gnss.eph', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='epv', full_name='tracelet.TraceletToServer.Location.Gnss.epv', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fix_type', full_name='tracelet.TraceletToServer.Location.Gnss.fix_type', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=746,
  serialized_end=866,
)

_TRACELETTOSERVER_LOCATION_UWB = _descriptor.Descriptor(
  name='Uwb',
  full_name='tracelet.TraceletToServer.Location.Uwb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valid', full_name='tracelet.TraceletToServer.Location.Uwb.valid', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='x', full_name='tracelet.TraceletToServer.Location.Uwb.x', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='tracelet.TraceletToServer.Location.Uwb.y', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='z', full_name='tracelet.TraceletToServer.Location.Uwb.z', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='site_id', full_name='tracelet.TraceletToServer.Location.Uwb.site_id', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location_signature', full_name='tracelet.TraceletToServer.Location.Uwb.location_signature', index=5,
      number=6, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eph', full_name='tracelet.TraceletToServer.Location.Uwb.eph', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=868,
  serialized_end=979,
)

_TRACELETTOSERVER_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='tracelet.TraceletToServer.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gnss', full_name='tracelet.TraceletToServer.Location.gnss', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uwb', full_name='tracelet.TraceletToServer.Location.uwb', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='direction', full_name='tracelet.TraceletToServer.Location.direction', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='speed', full_name='tracelet.TraceletToServer.Location.speed', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mileage', full_name='tracelet.TraceletToServer.Location.mileage', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='tracelet.TraceletToServer.Location.temperature', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRACELETTOSERVER_LOCATION_GNSS, _TRACELETTOSERVER_LOCATION_UWB, ],
  enum_types=[
    _TRACELETTOSERVER_LOCATION_DIRECTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=505,
  serialized_end=1052,
)

_TRACELETTOSERVER_STATUSRESPONSE = _descriptor.Descriptor(
  name='StatusResponse',
  full_name='tracelet.TraceletToServer.StatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='power_up_count', full_name='tracelet.TraceletToServer.StatusResponse.power_up_count', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_time', full_name='tracelet.TraceletToServer.StatusResponse.has_time', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uwb_module_status', full_name='tracelet.TraceletToServer.StatusResponse.uwb_module_status', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gnss_module_status', full_name='tracelet.TraceletToServer.StatusResponse.gnss_module_status', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imu1_status', full_name='tracelet.TraceletToServer.StatusResponse.imu1_status', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tacho_status', full_name='tracelet.TraceletToServer.StatusResponse.tacho_status', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=1055,
  serialized_end=1211,
)

_TRACELETTOSERVER = _descriptor.Descriptor(
  name='TraceletToServer',
  full_name='tracelet.TraceletToServer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tracelet.TraceletToServer.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='delivery_ts', full_name='tracelet.TraceletToServer.delivery_ts', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tracelet_id', full_name='tracelet.TraceletToServer.tracelet_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ignition', full_name='tracelet.TraceletToServer.ignition', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='tracelet.TraceletToServer.location', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='tracelet.TraceletToServer.status', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRACELETTOSERVER_LOCATION, _TRACELETTOSERVER_STATUSRESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='type', full_name='tracelet.TraceletToServer.type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=266,
  serialized_end=1219,
)

_SERVERTOTRACELET_LOCATIONREQUEST.containing_type = _SERVERTOTRACELET
_SERVERTOTRACELET_STATUSREQUEST.containing_type = _SERVERTOTRACELET
_SERVERTOTRACELET.fields_by_name['location'].message_type = _SERVERTOTRACELET_LOCATIONREQUEST
_SERVERTOTRACELET.fields_by_name['status'].message_type = _SERVERTOTRACELET_STATUSREQUEST
_SERVERTOTRACELET.oneofs_by_name['type'].fields.append(
  _SERVERTOTRACELET.fields_by_name['location'])
_SERVERTOTRACELET.fields_by_name['location'].containing_oneof = _SERVERTOTRACELET.oneofs_by_name['type']
_SERVERTOTRACELET.oneofs_by_name['type'].fields.append(
  _SERVERTOTRACELET.fields_by_name['status'])
_SERVERTOTRACELET.fields_by_name['status'].containing_oneof = _SERVERTOTRACELET.oneofs_by_name['type']
_TRACELETTOSERVER_LOCATION_GNSS.containing_type = _TRACELETTOSERVER_LOCATION
_TRACELETTOSERVER_LOCATION_UWB.containing_type = _TRACELETTOSERVER_LOCATION
_TRACELETTOSERVER_LOCATION.fields_by_name['gnss'].message_type = _TRACELETTOSERVER_LOCATION_GNSS
_TRACELETTOSERVER_LOCATION.fields_by_name['uwb'].message_type = _TRACELETTOSERVER_LOCATION_UWB
_TRACELETTOSERVER_LOCATION.fields_by_name['direction'].enum_type = _TRACELETTOSERVER_LOCATION_DIRECTION
_TRACELETTOSERVER_LOCATION.containing_type = _TRACELETTOSERVER
_TRACELETTOSERVER_LOCATION_DIRECTION.containing_type = _TRACELETTOSERVER_LOCATION
_TRACELETTOSERVER_STATUSRESPONSE.containing_type = _TRACELETTOSERVER
_TRACELETTOSERVER.fields_by_name['delivery_ts'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TRACELETTOSERVER.fields_by_name['location'].message_type = _TRACELETTOSERVER_LOCATION
_TRACELETTOSERVER.fields_by_name['status'].message_type = _TRACELETTOSERVER_STATUSRESPONSE
_TRACELETTOSERVER.oneofs_by_name['type'].fields.append(
  _TRACELETTOSERVER.fields_by_name['location'])
_TRACELETTOSERVER.fields_by_name['location'].containing_oneof = _TRACELETTOSERVER.oneofs_by_name['type']
_TRACELETTOSERVER.oneofs_by_name['type'].fields.append(
  _TRACELETTOSERVER.fields_by_name['status'])
_TRACELETTOSERVER.fields_by_name['status'].containing_oneof = _TRACELETTOSERVER.oneofs_by_name['type']
DESCRIPTOR.message_types_by_name['ServerToTracelet'] = _SERVERTOTRACELET
DESCRIPTOR.message_types_by_name['TraceletToServer'] = _TRACELETTOSERVER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ServerToTracelet = _reflection.GeneratedProtocolMessageType('ServerToTracelet', (_message.Message,), dict(

  LocationRequest = _reflection.GeneratedProtocolMessageType('LocationRequest', (_message.Message,), dict(
    DESCRIPTOR = _SERVERTOTRACELET_LOCATIONREQUEST,
    __module__ = 'v1.tracelet_pb2'
    # @@protoc_insertion_point(class_scope:tracelet.ServerToTracelet.LocationRequest)
    ))
  ,

  StatusRequest = _reflection.GeneratedProtocolMessageType('StatusRequest', (_message.Message,), dict(
    DESCRIPTOR = _SERVERTOTRACELET_STATUSREQUEST,
    __module__ = 'v1.tracelet_pb2'
    # @@protoc_insertion_point(class_scope:tracelet.ServerToTracelet.StatusRequest)
    ))
  ,
  DESCRIPTOR = _SERVERTOTRACELET,
  __module__ = 'v1.tracelet_pb2'
  # @@protoc_insertion_point(class_scope:tracelet.ServerToTracelet)
  ))
_sym_db.RegisterMessage(ServerToTracelet)
_sym_db.RegisterMessage(ServerToTracelet.LocationRequest)
_sym_db.RegisterMessage(ServerToTracelet.StatusRequest)

TraceletToServer = _reflection.GeneratedProtocolMessageType('TraceletToServer', (_message.Message,), dict(

  Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(

    Gnss = _reflection.GeneratedProtocolMessageType('Gnss', (_message.Message,), dict(
      DESCRIPTOR = _TRACELETTOSERVER_LOCATION_GNSS,
      __module__ = 'v1.tracelet_pb2'
      # @@protoc_insertion_point(class_scope:tracelet.TraceletToServer.Location.Gnss)
      ))
    ,

    Uwb = _reflection.GeneratedProtocolMessageType('Uwb', (_message.Message,), dict(
      DESCRIPTOR = _TRACELETTOSERVER_LOCATION_UWB,
      __module__ = 'v1.tracelet_pb2'
      # @@protoc_insertion_point(class_scope:tracelet.TraceletToServer.Location.Uwb)
      ))
    ,
    DESCRIPTOR = _TRACELETTOSERVER_LOCATION,
    __module__ = 'v1.tracelet_pb2'
    # @@protoc_insertion_point(class_scope:tracelet.TraceletToServer.Location)
    ))
  ,

  StatusResponse = _reflection.GeneratedProtocolMessageType('StatusResponse', (_message.Message,), dict(
    DESCRIPTOR = _TRACELETTOSERVER_STATUSRESPONSE,
    __module__ = 'v1.tracelet_pb2'
    # @@protoc_insertion_point(class_scope:tracelet.TraceletToServer.StatusResponse)
    ))
  ,
  DESCRIPTOR = _TRACELETTOSERVER,
  __module__ = 'v1.tracelet_pb2'
  # @@protoc_insertion_point(class_scope:tracelet.TraceletToServer)
  ))
_sym_db.RegisterMessage(TraceletToServer)
_sym_db.RegisterMessage(TraceletToServer.Location)
_sym_db.RegisterMessage(TraceletToServer.Location.Gnss)
_sym_db.RegisterMessage(TraceletToServer.Location.Uwb)
_sym_db.RegisterMessage(TraceletToServer.StatusResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
