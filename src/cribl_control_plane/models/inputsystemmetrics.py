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


class InputSystemMetricsType(str, Enum, metaclass=utils.OpenEnumMeta):
    SYSTEM_METRICS = "system_metrics"


class InputSystemMetricsConnectionTypedDict(TypedDict):
    output: str
    pipeline: NotRequired[str]


class InputSystemMetricsConnection(BaseModel):
    output: str

    pipeline: Optional[str] = None


class InputSystemMetricsPqMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""With Smart mode, PQ will write events to the filesystem only when it detects backpressure from the processing engine. With Always On mode, PQ will always write events directly to the queue before forwarding them to the processing engine."""

    SMART = "smart"
    ALWAYS = "always"


class InputSystemMetricsCompression(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Codec to use to compress the persisted data"""

    NONE = "none"
    GZIP = "gzip"


class InputSystemMetricsPqTypedDict(TypedDict):
    mode: NotRequired[InputSystemMetricsPqMode]
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
    compress: NotRequired[InputSystemMetricsCompression]
    r"""Codec to use to compress the persisted data"""


class InputSystemMetricsPq(BaseModel):
    mode: Annotated[
        Optional[InputSystemMetricsPqMode], PlainValidator(validate_open_enum(False))
    ] = InputSystemMetricsPqMode.ALWAYS
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
        Optional[InputSystemMetricsCompression],
        PlainValidator(validate_open_enum(False)),
    ] = InputSystemMetricsCompression.NONE
    r"""Codec to use to compress the persisted data"""


class InputSystemMetricsHostMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Select level of detail for host metrics"""

    BASIC = "basic"
    ALL = "all"
    CUSTOM = "custom"
    DISABLED = "disabled"


class InputSystemMetricsSystemMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Select the level of detail for system metrics"""

    BASIC = "basic"
    ALL = "all"
    CUSTOM = "custom"
    DISABLED = "disabled"


class InputSystemMetricsSystemTypedDict(TypedDict):
    mode: NotRequired[InputSystemMetricsSystemMode]
    r"""Select the level of detail for system metrics"""
    processes: NotRequired[bool]
    r"""Generate metrics for the numbers of processes in various states"""


class InputSystemMetricsSystem(BaseModel):
    mode: Annotated[
        Optional[InputSystemMetricsSystemMode],
        PlainValidator(validate_open_enum(False)),
    ] = InputSystemMetricsSystemMode.BASIC
    r"""Select the level of detail for system metrics"""

    processes: Optional[bool] = False
    r"""Generate metrics for the numbers of processes in various states"""


class InputSystemMetricsCPUMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Select the level of detail for CPU metrics"""

    BASIC = "basic"
    ALL = "all"
    CUSTOM = "custom"
    DISABLED = "disabled"


class InputSystemMetricsCPUTypedDict(TypedDict):
    mode: NotRequired[InputSystemMetricsCPUMode]
    r"""Select the level of detail for CPU metrics"""
    per_cpu: NotRequired[bool]
    r"""Generate metrics for each CPU"""
    detail: NotRequired[bool]
    r"""Generate metrics for all CPU states"""
    time: NotRequired[bool]
    r"""Generate raw, monotonic CPU time counters"""


class InputSystemMetricsCPU(BaseModel):
    mode: Annotated[
        Optional[InputSystemMetricsCPUMode], PlainValidator(validate_open_enum(False))
    ] = InputSystemMetricsCPUMode.BASIC
    r"""Select the level of detail for CPU metrics"""

    per_cpu: Annotated[Optional[bool], pydantic.Field(alias="perCpu")] = False
    r"""Generate metrics for each CPU"""

    detail: Optional[bool] = False
    r"""Generate metrics for all CPU states"""

    time: Optional[bool] = False
    r"""Generate raw, monotonic CPU time counters"""


class InputSystemMetricsMemoryMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Select the level of detail for memory metrics"""

    BASIC = "basic"
    ALL = "all"
    CUSTOM = "custom"
    DISABLED = "disabled"


class InputSystemMetricsMemoryTypedDict(TypedDict):
    mode: NotRequired[InputSystemMetricsMemoryMode]
    r"""Select the level of detail for memory metrics"""
    detail: NotRequired[bool]
    r"""Generate metrics for all memory states"""


class InputSystemMetricsMemory(BaseModel):
    mode: Annotated[
        Optional[InputSystemMetricsMemoryMode],
        PlainValidator(validate_open_enum(False)),
    ] = InputSystemMetricsMemoryMode.BASIC
    r"""Select the level of detail for memory metrics"""

    detail: Optional[bool] = False
    r"""Generate metrics for all memory states"""


class InputSystemMetricsNetworkMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Select the level of detail for network metrics"""

    BASIC = "basic"
    ALL = "all"
    CUSTOM = "custom"
    DISABLED = "disabled"


class InputSystemMetricsNetworkTypedDict(TypedDict):
    mode: NotRequired[InputSystemMetricsNetworkMode]
    r"""Select the level of detail for network metrics"""
    devices: NotRequired[List[str]]
    r"""Network interfaces to include/exclude. Examples: eth0, !lo. All interfaces are included if this list is empty."""
    per_interface: NotRequired[bool]
    r"""Generate separate metrics for each interface"""
    detail: NotRequired[bool]
    r"""Generate full network metrics"""


class InputSystemMetricsNetwork(BaseModel):
    mode: Annotated[
        Optional[InputSystemMetricsNetworkMode],
        PlainValidator(validate_open_enum(False)),
    ] = InputSystemMetricsNetworkMode.BASIC
    r"""Select the level of detail for network metrics"""

    devices: Optional[List[str]] = None
    r"""Network interfaces to include/exclude. Examples: eth0, !lo. All interfaces are included if this list is empty."""

    per_interface: Annotated[Optional[bool], pydantic.Field(alias="perInterface")] = (
        False
    )
    r"""Generate separate metrics for each interface"""

    detail: Optional[bool] = False
    r"""Generate full network metrics"""


class InputSystemMetricsDiskMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Select the level of detail for disk metrics"""

    BASIC = "basic"
    ALL = "all"
    CUSTOM = "custom"
    DISABLED = "disabled"


class InputSystemMetricsDiskTypedDict(TypedDict):
    mode: NotRequired[InputSystemMetricsDiskMode]
    r"""Select the level of detail for disk metrics"""
    devices: NotRequired[List[str]]
    r"""Block devices to include/exclude. Examples: sda*, !loop*. Wildcards and ! (not) operators are supported. All devices are included if this list is empty."""
    mountpoints: NotRequired[List[str]]
    r"""Filesystem mountpoints to include/exclude. Examples: /, /home, !/proc*, !/tmp. Wildcards and ! (not) operators are supported. All mountpoints are included if this list is empty."""
    fstypes: NotRequired[List[str]]
    r"""Filesystem types to include/exclude. Examples: ext4, !*tmpfs, !squashfs. Wildcards and ! (not) operators are supported. All types are included if this list is empty."""
    per_device: NotRequired[bool]
    r"""Generate separate metrics for each device"""
    detail: NotRequired[bool]
    r"""Generate full disk metrics"""


class InputSystemMetricsDisk(BaseModel):
    mode: Annotated[
        Optional[InputSystemMetricsDiskMode], PlainValidator(validate_open_enum(False))
    ] = InputSystemMetricsDiskMode.BASIC
    r"""Select the level of detail for disk metrics"""

    devices: Optional[List[str]] = None
    r"""Block devices to include/exclude. Examples: sda*, !loop*. Wildcards and ! (not) operators are supported. All devices are included if this list is empty."""

    mountpoints: Optional[List[str]] = None
    r"""Filesystem mountpoints to include/exclude. Examples: /, /home, !/proc*, !/tmp. Wildcards and ! (not) operators are supported. All mountpoints are included if this list is empty."""

    fstypes: Optional[List[str]] = None
    r"""Filesystem types to include/exclude. Examples: ext4, !*tmpfs, !squashfs. Wildcards and ! (not) operators are supported. All types are included if this list is empty."""

    per_device: Annotated[Optional[bool], pydantic.Field(alias="perDevice")] = False
    r"""Generate separate metrics for each device"""

    detail: Optional[bool] = False
    r"""Generate full disk metrics"""


class InputSystemMetricsCustomTypedDict(TypedDict):
    system: NotRequired[InputSystemMetricsSystemTypedDict]
    cpu: NotRequired[InputSystemMetricsCPUTypedDict]
    memory: NotRequired[InputSystemMetricsMemoryTypedDict]
    network: NotRequired[InputSystemMetricsNetworkTypedDict]
    disk: NotRequired[InputSystemMetricsDiskTypedDict]


class InputSystemMetricsCustom(BaseModel):
    system: Optional[InputSystemMetricsSystem] = None

    cpu: Optional[InputSystemMetricsCPU] = None

    memory: Optional[InputSystemMetricsMemory] = None

    network: Optional[InputSystemMetricsNetwork] = None

    disk: Optional[InputSystemMetricsDisk] = None


class InputSystemMetricsHostTypedDict(TypedDict):
    mode: NotRequired[InputSystemMetricsHostMode]
    r"""Select level of detail for host metrics"""
    custom: NotRequired[InputSystemMetricsCustomTypedDict]


class InputSystemMetricsHost(BaseModel):
    mode: Annotated[
        Optional[InputSystemMetricsHostMode], PlainValidator(validate_open_enum(False))
    ] = InputSystemMetricsHostMode.BASIC
    r"""Select level of detail for host metrics"""

    custom: Optional[InputSystemMetricsCustom] = None


class InputSystemMetricsSetTypedDict(TypedDict):
    name: str
    filter_: str
    include_children: NotRequired[bool]


class InputSystemMetricsSet(BaseModel):
    name: str

    filter_: Annotated[str, pydantic.Field(alias="filter")]

    include_children: Annotated[
        Optional[bool], pydantic.Field(alias="includeChildren")
    ] = False


class InputSystemMetricsProcessTypedDict(TypedDict):
    sets: NotRequired[List[InputSystemMetricsSetTypedDict]]
    r"""Configure sets to collect process metrics"""


class InputSystemMetricsProcess(BaseModel):
    sets: Optional[List[InputSystemMetricsSet]] = None
    r"""Configure sets to collect process metrics"""


class ContainerMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Select the level of detail for container metrics"""

    BASIC = "basic"
    ALL = "all"
    CUSTOM = "custom"
    DISABLED = "disabled"


class InputSystemMetricsFilterTypedDict(TypedDict):
    expr: str


class InputSystemMetricsFilter(BaseModel):
    expr: str


class ContainerTypedDict(TypedDict):
    mode: NotRequired[ContainerMode]
    r"""Select the level of detail for container metrics"""
    docker_socket: NotRequired[List[str]]
    r"""Full paths for Docker's UNIX-domain socket"""
    docker_timeout: NotRequired[float]
    r"""Timeout, in seconds, for the Docker API"""
    filters: NotRequired[List[InputSystemMetricsFilterTypedDict]]
    r"""Containers matching any of these will be included. All are included if no filters are added."""
    all_containers: NotRequired[bool]
    r"""Include stopped and paused containers"""
    per_device: NotRequired[bool]
    r"""Generate separate metrics for each device"""
    detail: NotRequired[bool]
    r"""Generate full container metrics"""


class Container(BaseModel):
    mode: Annotated[
        Optional[ContainerMode], PlainValidator(validate_open_enum(False))
    ] = ContainerMode.BASIC
    r"""Select the level of detail for container metrics"""

    docker_socket: Annotated[
        Optional[List[str]], pydantic.Field(alias="dockerSocket")
    ] = None
    r"""Full paths for Docker's UNIX-domain socket"""

    docker_timeout: Annotated[
        Optional[float], pydantic.Field(alias="dockerTimeout")
    ] = 5
    r"""Timeout, in seconds, for the Docker API"""

    filters: Optional[List[InputSystemMetricsFilter]] = None
    r"""Containers matching any of these will be included. All are included if no filters are added."""

    all_containers: Annotated[Optional[bool], pydantic.Field(alias="allContainers")] = (
        False
    )
    r"""Include stopped and paused containers"""

    per_device: Annotated[Optional[bool], pydantic.Field(alias="perDevice")] = False
    r"""Generate separate metrics for each device"""

    detail: Optional[bool] = False
    r"""Generate full container metrics"""


class InputSystemMetricsMetadatumTypedDict(TypedDict):
    name: str
    value: str
    r"""JavaScript expression to compute field's value, enclosed in quotes or backticks. (Can evaluate to a constant.)"""


class InputSystemMetricsMetadatum(BaseModel):
    name: str

    value: str
    r"""JavaScript expression to compute field's value, enclosed in quotes or backticks. (Can evaluate to a constant.)"""


class InputSystemMetricsDataCompressionFormat(str, Enum, metaclass=utils.OpenEnumMeta):
    NONE = "none"
    GZIP = "gzip"


class InputSystemMetricsPersistenceTypedDict(TypedDict):
    enable: NotRequired[bool]
    r"""Spool metrics to disk for Cribl Edge and Search"""
    time_window: NotRequired[str]
    r"""Time span for each file bucket"""
    max_data_size: NotRequired[str]
    r"""Maximum disk space allowed to be consumed (examples: 420MB, 4GB). When limit is reached, older data will be deleted."""
    max_data_time: NotRequired[str]
    r"""Maximum amount of time to retain data (examples: 2h, 4d). When limit is reached, older data will be deleted."""
    compress: NotRequired[InputSystemMetricsDataCompressionFormat]
    dest_path: NotRequired[str]
    r"""Path to use to write metrics. Defaults to $CRIBL_HOME/state/system_metrics"""


class InputSystemMetricsPersistence(BaseModel):
    enable: Optional[bool] = False
    r"""Spool metrics to disk for Cribl Edge and Search"""

    time_window: Annotated[Optional[str], pydantic.Field(alias="timeWindow")] = "10m"
    r"""Time span for each file bucket"""

    max_data_size: Annotated[Optional[str], pydantic.Field(alias="maxDataSize")] = "1GB"
    r"""Maximum disk space allowed to be consumed (examples: 420MB, 4GB). When limit is reached, older data will be deleted."""

    max_data_time: Annotated[Optional[str], pydantic.Field(alias="maxDataTime")] = "24h"
    r"""Maximum amount of time to retain data (examples: 2h, 4d). When limit is reached, older data will be deleted."""

    compress: Annotated[
        Optional[InputSystemMetricsDataCompressionFormat],
        PlainValidator(validate_open_enum(False)),
    ] = InputSystemMetricsDataCompressionFormat.GZIP

    dest_path: Annotated[Optional[str], pydantic.Field(alias="destPath")] = (
        "$CRIBL_HOME/state/system_metrics"
    )
    r"""Path to use to write metrics. Defaults to $CRIBL_HOME/state/system_metrics"""


class InputSystemMetricsTypedDict(TypedDict):
    id: str
    r"""Unique ID for this input"""
    type: InputSystemMetricsType
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
    connections: NotRequired[List[InputSystemMetricsConnectionTypedDict]]
    r"""Direct connections to Destinations, and optionally via a Pipeline or a Pack"""
    pq: NotRequired[InputSystemMetricsPqTypedDict]
    interval: NotRequired[float]
    r"""Time, in seconds, between consecutive metric collections. Default is 10 seconds."""
    host: NotRequired[InputSystemMetricsHostTypedDict]
    process: NotRequired[InputSystemMetricsProcessTypedDict]
    container: NotRequired[ContainerTypedDict]
    metadata: NotRequired[List[InputSystemMetricsMetadatumTypedDict]]
    r"""Fields to add to events from this input"""
    persistence: NotRequired[InputSystemMetricsPersistenceTypedDict]
    description: NotRequired[str]


class InputSystemMetrics(BaseModel):
    id: str
    r"""Unique ID for this input"""

    type: Annotated[InputSystemMetricsType, PlainValidator(validate_open_enum(False))]

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

    connections: Optional[List[InputSystemMetricsConnection]] = None
    r"""Direct connections to Destinations, and optionally via a Pipeline or a Pack"""

    pq: Optional[InputSystemMetricsPq] = None

    interval: Optional[float] = 10
    r"""Time, in seconds, between consecutive metric collections. Default is 10 seconds."""

    host: Optional[InputSystemMetricsHost] = None

    process: Optional[InputSystemMetricsProcess] = None

    container: Optional[Container] = None

    metadata: Optional[List[InputSystemMetricsMetadatum]] = None
    r"""Fields to add to events from this input"""

    persistence: Optional[InputSystemMetricsPersistence] = None

    description: Optional[str] = None
