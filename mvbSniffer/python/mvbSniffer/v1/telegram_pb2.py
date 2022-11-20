# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mvbSniffer/v1/telegram.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mvbSniffer/v1/telegram.proto',
  package='mvbSniffer',
  syntax='proto3',
  serialized_options=_b('Z\rmvbSniffer/v1'),
  serialized_pb=_b('\n\x1cmvbSniffer/v1/telegram.proto\x12\nmvbSniffer\"\xe6\x04\n\x08Telegram\x12\x11\n\ttimestamp\x18\x01 \x01(\x06\x12\r\n\x05state\x18\x02 \x01(\r\x12\'\n\x04type\x18\x03 \x01(\x0e\x32\x19.mvbSniffer.Telegram.Type\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\x12\x13\n\x0btelegram_nr\x18\x06 \x01(\x04\x12\'\n\x04line\x18\x07 \x01(\x0e\x32\x19.mvbSniffer.Telegram.Line\"S\n\x05State\x12\x0f\n\x0bkSuccessful\x10\x00\x12\r\n\tkTimedOut\x10\x01\x12\x14\n\x10kMissedMVBFrames\x10\x02\x12\x14\n\x10kMissedTelegrams\x10\x04\"\xc4\x02\n\x04Type\x12\x15\n\x11kProcessData16Bit\x10\x00\x12\x15\n\x11kProcessData32Bit\x10\x01\x12\x15\n\x11kProcessData64Bit\x10\x02\x12\x16\n\x12kProcessData128Bit\x10\x03\x12\x16\n\x12kProcessData256Bit\x10\x04\x12\x0f\n\x0bkReserved_1\x10\x05\x12\x0f\n\x0bkReserved_2\x10\x06\x12\x0f\n\x0bkReserved_3\x10\x07\x12\x17\n\x13kMastershipTransfer\x10\x08\x12\x11\n\rkGeneralEvent\x10\t\x12\x0f\n\x0bkReserved_4\x10\n\x12\x0f\n\x0bkReserved_5\x10\x0b\x12\x10\n\x0ckMessageData\x10\x0c\x12\x0f\n\x0bkGroupEvent\x10\r\x12\x10\n\x0ckSingleEvent\x10\x0e\x12\x11\n\rkDeviceStatus\x10\x0f\"\x16\n\x04Line\x12\x06\n\x02kA\x10\x00\x12\x06\n\x02kB\x10\x01\"9\n\x12TelegramCollection\x12#\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x14.mvbSniffer.TelegramB\x0fZ\rmvbSniffer/v1b\x06proto3')
)



_TELEGRAM_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='mvbSniffer.Telegram.State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kSuccessful', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kTimedOut', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kMissedMVBFrames', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kMissedTelegrams', index=3, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=225,
  serialized_end=308,
)
_sym_db.RegisterEnumDescriptor(_TELEGRAM_STATE)

_TELEGRAM_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='mvbSniffer.Telegram.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kProcessData16Bit', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kProcessData32Bit', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kProcessData64Bit', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kProcessData128Bit', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kProcessData256Bit', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kReserved_1', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kReserved_2', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kReserved_3', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kMastershipTransfer', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kGeneralEvent', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kReserved_4', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kReserved_5', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kMessageData', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kGroupEvent', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kSingleEvent', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kDeviceStatus', index=15, number=15,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=311,
  serialized_end=635,
)
_sym_db.RegisterEnumDescriptor(_TELEGRAM_TYPE)

_TELEGRAM_LINE = _descriptor.EnumDescriptor(
  name='Line',
  full_name='mvbSniffer.Telegram.Line',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kA', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kB', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=637,
  serialized_end=659,
)
_sym_db.RegisterEnumDescriptor(_TELEGRAM_LINE)


_TELEGRAM = _descriptor.Descriptor(
  name='Telegram',
  full_name='mvbSniffer.Telegram',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='mvbSniffer.Telegram.timestamp', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='mvbSniffer.Telegram.state', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='mvbSniffer.Telegram.type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='mvbSniffer.Telegram.address', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='mvbSniffer.Telegram.data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='telegram_nr', full_name='mvbSniffer.Telegram.telegram_nr', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='line', full_name='mvbSniffer.Telegram.line', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TELEGRAM_STATE,
    _TELEGRAM_TYPE,
    _TELEGRAM_LINE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=659,
)


_TELEGRAMCOLLECTION = _descriptor.Descriptor(
  name='TelegramCollection',
  full_name='mvbSniffer.TelegramCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='mvbSniffer.TelegramCollection.entry', index=0,
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
  serialized_start=661,
  serialized_end=718,
)

_TELEGRAM.fields_by_name['type'].enum_type = _TELEGRAM_TYPE
_TELEGRAM.fields_by_name['line'].enum_type = _TELEGRAM_LINE
_TELEGRAM_STATE.containing_type = _TELEGRAM
_TELEGRAM_TYPE.containing_type = _TELEGRAM
_TELEGRAM_LINE.containing_type = _TELEGRAM
_TELEGRAMCOLLECTION.fields_by_name['entry'].message_type = _TELEGRAM
DESCRIPTOR.message_types_by_name['Telegram'] = _TELEGRAM
DESCRIPTOR.message_types_by_name['TelegramCollection'] = _TELEGRAMCOLLECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Telegram = _reflection.GeneratedProtocolMessageType('Telegram', (_message.Message,), dict(
  DESCRIPTOR = _TELEGRAM,
  __module__ = 'mvbSniffer.v1.telegram_pb2'
  # @@protoc_insertion_point(class_scope:mvbSniffer.Telegram)
  ))
_sym_db.RegisterMessage(Telegram)

TelegramCollection = _reflection.GeneratedProtocolMessageType('TelegramCollection', (_message.Message,), dict(
  DESCRIPTOR = _TELEGRAMCOLLECTION,
  __module__ = 'mvbSniffer.v1.telegram_pb2'
  # @@protoc_insertion_point(class_scope:mvbSniffer.TelegramCollection)
  ))
_sym_db.RegisterMessage(TelegramCollection)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
