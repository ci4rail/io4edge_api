from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SlaveMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    not_configured: _ClassVar[SlaveMode]
    ndm: _ClassVar[SlaveMode]
    nrm: _ClassVar[SlaveMode]
not_configured: SlaveMode
ndm: SlaveMode
nrm: SlaveMode

class ConfigurationSet(_message.Message):
    __slots__ = ("slave_address", "max_frame_length", "app_wd_timeout_ms", "idle_response", "baud_62500")
    SLAVE_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    MAX_FRAME_LENGTH_FIELD_NUMBER: _ClassVar[int]
    APP_WD_TIMEOUT_MS_FIELD_NUMBER: _ClassVar[int]
    IDLE_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    BAUD_62500_FIELD_NUMBER: _ClassVar[int]
    slave_address: int
    max_frame_length: int
    app_wd_timeout_ms: int
    idle_response: bytes
    baud_62500: bool
    def __init__(self, slave_address: _Optional[int] = ..., max_frame_length: _Optional[int] = ..., app_wd_timeout_ms: _Optional[int] = ..., idle_response: _Optional[bytes] = ..., baud_62500: _Optional[bool] = ...) -> None: ...

class ConfigurationSetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfigurationGet(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfigurationGetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfigurationDescribe(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ConfigurationDescribeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FunctionControlGet(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PreparedTxMsg(_message.Message):
    __slots__ = ("bitbus_information",)
    BITBUS_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    bitbus_information: bytes
    def __init__(self, bitbus_information: _Optional[bytes] = ...) -> None: ...

class FunctionControlSet(_message.Message):
    __slots__ = ("tx_msg",)
    TX_MSG_FIELD_NUMBER: _ClassVar[int]
    tx_msg: PreparedTxMsg
    def __init__(self, tx_msg: _Optional[_Union[PreparedTxMsg, _Mapping]] = ...) -> None: ...

class FunctionControlGetResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class FunctionControlSetResponse(_message.Message):
    __slots__ = ("mode", "have_pending_tx_msg")
    MODE_FIELD_NUMBER: _ClassVar[int]
    HAVE_PENDING_TX_MSG_FIELD_NUMBER: _ClassVar[int]
    mode: SlaveMode
    have_pending_tx_msg: bool
    def __init__(self, mode: _Optional[_Union[SlaveMode, str]] = ..., have_pending_tx_msg: _Optional[bool] = ...) -> None: ...

class StreamControlStart(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Sample(_message.Message):
    __slots__ = ("timestamp", "bitbus_information")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    BITBUS_INFORMATION_FIELD_NUMBER: _ClassVar[int]
    timestamp: int
    bitbus_information: bytes
    def __init__(self, timestamp: _Optional[int] = ..., bitbus_information: _Optional[bytes] = ...) -> None: ...

class StreamData(_message.Message):
    __slots__ = ("samples",)
    SAMPLES_FIELD_NUMBER: _ClassVar[int]
    samples: _containers.RepeatedCompositeFieldContainer[Sample]
    def __init__(self, samples: _Optional[_Iterable[_Union[Sample, _Mapping]]] = ...) -> None: ...
