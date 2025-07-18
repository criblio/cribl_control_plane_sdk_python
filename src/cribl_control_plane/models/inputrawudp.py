"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from cribl_control_plane import utils
from cribl_control_plane.types import BaseModel
from cribl_control_plane.utils import validate_open_enum
from enum import Enum
import pydantic
from pydantic.functional_validators import PlainValidator
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class InputRawUDPType(str, Enum, metaclass=utils.OpenEnumMeta):
    RAW_UDP = "raw_udp"


class InputRawUDPConnectionTypedDict(TypedDict):
    output: str
    pipeline: NotRequired[str]


class InputRawUDPConnection(BaseModel):
    output: str

    pipeline: Optional[str] = None


class InputRawUDPMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""With Smart mode, PQ will write events to the filesystem only when it detects backpressure from the processing engine. With Always On mode, PQ will always write events directly to the queue before forwarding them to the processing engine."""

    SMART = "smart"
    ALWAYS = "always"


class InputRawUDPCompression(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Codec to use to compress the persisted data"""

    NONE = "none"
    GZIP = "gzip"


class InputRawUDPPqTypedDict(TypedDict):
    mode: NotRequired[InputRawUDPMode]
    r"""With Smart mode, PQ will write events to the filesystem only when it detects backpressure from the processing engine. With Always On mode, PQ will always write events directly to the queue before forwarding them to the processing engine."""
    max_buffer_size: NotRequired[float]
    r"""The maximum number of events to hold in memory before writing the events to disk"""
    commit_frequency: NotRequired[float]
    r"""The number of events to send downstream before committing that Stream has read them"""
    max_file_size: NotRequired[str]
    r"""The maximum size to store in each queue file before closing and optionally compressing. Enter a numeral with units of KB, MB, etc."""
    max_size: NotRequired[str]
    r"""The maximum disk space that the queue can consume (as an average per Worker Process) before queueing stops. Enter a numeral with units of KB, MB, etc."""
    path: NotRequired[str]
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/inputs/<input-id>"""
    compress: NotRequired[InputRawUDPCompression]
    r"""Codec to use to compress the persisted data"""


class InputRawUDPPq(BaseModel):
    mode: Annotated[
        Optional[InputRawUDPMode], PlainValidator(validate_open_enum(False))
    ] = InputRawUDPMode.ALWAYS
    r"""With Smart mode, PQ will write events to the filesystem only when it detects backpressure from the processing engine. With Always On mode, PQ will always write events directly to the queue before forwarding them to the processing engine."""

    max_buffer_size: Annotated[
        Optional[float], pydantic.Field(alias="maxBufferSize")
    ] = 1000
    r"""The maximum number of events to hold in memory before writing the events to disk"""

    commit_frequency: Annotated[
        Optional[float], pydantic.Field(alias="commitFrequency")
    ] = 42
    r"""The number of events to send downstream before committing that Stream has read them"""

    max_file_size: Annotated[Optional[str], pydantic.Field(alias="maxFileSize")] = (
        "1 MB"
    )
    r"""The maximum size to store in each queue file before closing and optionally compressing. Enter a numeral with units of KB, MB, etc."""

    max_size: Annotated[Optional[str], pydantic.Field(alias="maxSize")] = "5GB"
    r"""The maximum disk space that the queue can consume (as an average per Worker Process) before queueing stops. Enter a numeral with units of KB, MB, etc."""

    path: Optional[str] = "$CRIBL_HOME/state/queues"
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/inputs/<input-id>"""

    compress: Annotated[
        Optional[InputRawUDPCompression], PlainValidator(validate_open_enum(False))
    ] = InputRawUDPCompression.NONE
    r"""Codec to use to compress the persisted data"""


class InputRawUDPMetadatumTypedDict(TypedDict):
    name: str
    value: str
    r"""JavaScript expression to compute field's value, enclosed in quotes or backticks. (Can evaluate to a constant.)"""


class InputRawUDPMetadatum(BaseModel):
    name: str

    value: str
    r"""JavaScript expression to compute field's value, enclosed in quotes or backticks. (Can evaluate to a constant.)"""


class InputRawUDPTypedDict(TypedDict):
    port: float
    r"""Port to listen on"""
    id: NotRequired[str]
    r"""Unique ID for this input"""
    type: NotRequired[InputRawUDPType]
    disabled: NotRequired[bool]
    pipeline: NotRequired[str]
    r"""Pipeline to process data from this Source before sending it through the Routes"""
    send_to_routes: NotRequired[bool]
    r"""Select whether to send data to Routes, or directly to Destinations."""
    environment: NotRequired[str]
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    pq_enabled: NotRequired[bool]
    r"""Use a disk queue to minimize data loss when connected services block. See [Cribl Docs](https://docs.cribl.io/stream/persistent-queues) for PQ defaults (Cribl-managed Cloud Workers) and configuration options (on-prem and hybrid Workers)."""
    streamtags: NotRequired[List[str]]
    r"""Tags for filtering and grouping in @{product}"""
    connections: NotRequired[List[InputRawUDPConnectionTypedDict]]
    r"""Direct connections to Destinations, and optionally via a Pipeline or a Pack"""
    pq: NotRequired[InputRawUDPPqTypedDict]
    host: NotRequired[str]
    r"""Address to bind on. For IPv4 (all addresses), use the default '0.0.0.0'. For IPv6, enter '::' (all addresses) or specify an IP address."""
    max_buffer_size: NotRequired[float]
    r"""Maximum number of events to buffer when downstream is blocking."""
    ip_whitelist_regex: NotRequired[str]
    r"""Regex matching IP addresses that are allowed to send data"""
    single_msg_udp_packets: NotRequired[bool]
    r"""If true, each UDP packet is assumed to contain a single message. If false, each UDP packet is assumed to contain multiple messages, separated by newlines."""
    ingest_raw_bytes: NotRequired[bool]
    r"""If true, a __rawBytes field will be added to each event containing the raw bytes of the datagram."""
    udp_socket_rx_buf_size: NotRequired[float]
    r"""Optionally, set the SO_RCVBUF socket option for the UDP socket. This value tells the operating system how many bytes can be buffered in the kernel before events are dropped. Leave blank to use the OS default. Caution: Increasing this value will affect OS memory utilization."""
    metadata: NotRequired[List[InputRawUDPMetadatumTypedDict]]
    r"""Fields to add to events from this input"""
    description: NotRequired[str]


class InputRawUDP(BaseModel):
    port: float
    r"""Port to listen on"""

    id: Optional[str] = None
    r"""Unique ID for this input"""

    type: Annotated[
        Optional[InputRawUDPType], PlainValidator(validate_open_enum(False))
    ] = None

    disabled: Optional[bool] = False

    pipeline: Optional[str] = None
    r"""Pipeline to process data from this Source before sending it through the Routes"""

    send_to_routes: Annotated[Optional[bool], pydantic.Field(alias="sendToRoutes")] = (
        True
    )
    r"""Select whether to send data to Routes, or directly to Destinations."""

    environment: Optional[str] = None
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""

    pq_enabled: Annotated[Optional[bool], pydantic.Field(alias="pqEnabled")] = False
    r"""Use a disk queue to minimize data loss when connected services block. See [Cribl Docs](https://docs.cribl.io/stream/persistent-queues) for PQ defaults (Cribl-managed Cloud Workers) and configuration options (on-prem and hybrid Workers)."""

    streamtags: Optional[List[str]] = None
    r"""Tags for filtering and grouping in @{product}"""

    connections: Optional[List[InputRawUDPConnection]] = None
    r"""Direct connections to Destinations, and optionally via a Pipeline or a Pack"""

    pq: Optional[InputRawUDPPq] = None

    host: Optional[str] = "0.0.0.0"
    r"""Address to bind on. For IPv4 (all addresses), use the default '0.0.0.0'. For IPv6, enter '::' (all addresses) or specify an IP address."""

    max_buffer_size: Annotated[
        Optional[float], pydantic.Field(alias="maxBufferSize")
    ] = 1000
    r"""Maximum number of events to buffer when downstream is blocking."""

    ip_whitelist_regex: Annotated[
        Optional[str], pydantic.Field(alias="ipWhitelistRegex")
    ] = "/.*/"
    r"""Regex matching IP addresses that are allowed to send data"""

    single_msg_udp_packets: Annotated[
        Optional[bool], pydantic.Field(alias="singleMsgUdpPackets")
    ] = False
    r"""If true, each UDP packet is assumed to contain a single message. If false, each UDP packet is assumed to contain multiple messages, separated by newlines."""

    ingest_raw_bytes: Annotated[
        Optional[bool], pydantic.Field(alias="ingestRawBytes")
    ] = False
    r"""If true, a __rawBytes field will be added to each event containing the raw bytes of the datagram."""

    udp_socket_rx_buf_size: Annotated[
        Optional[float], pydantic.Field(alias="udpSocketRxBufSize")
    ] = None
    r"""Optionally, set the SO_RCVBUF socket option for the UDP socket. This value tells the operating system how many bytes can be buffered in the kernel before events are dropped. Leave blank to use the OS default. Caution: Increasing this value will affect OS memory utilization."""

    metadata: Optional[List[InputRawUDPMetadatum]] = None
    r"""Fields to add to events from this input"""

    description: Optional[str] = None
