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


class InputCriblmetricsType(str, Enum, metaclass=utils.OpenEnumMeta):
    CRIBLMETRICS = "criblmetrics"


class InputCriblmetricsConnectionTypedDict(TypedDict):
    output: str
    pipeline: NotRequired[str]


class InputCriblmetricsConnection(BaseModel):
    output: str

    pipeline: Optional[str] = None


class InputCriblmetricsMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""With Smart mode, PQ will write events to the filesystem only when it detects backpressure from the processing engine. With Always On mode, PQ will always write events directly to the queue before forwarding them to the processing engine."""

    SMART = "smart"
    ALWAYS = "always"


class InputCriblmetricsCompression(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Codec to use to compress the persisted data"""

    NONE = "none"
    GZIP = "gzip"


class InputCriblmetricsPqTypedDict(TypedDict):
    mode: NotRequired[InputCriblmetricsMode]
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
    compress: NotRequired[InputCriblmetricsCompression]
    r"""Codec to use to compress the persisted data"""


class InputCriblmetricsPq(BaseModel):
    mode: Annotated[
        Optional[InputCriblmetricsMode], PlainValidator(validate_open_enum(False))
    ] = InputCriblmetricsMode.ALWAYS
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
        Optional[InputCriblmetricsCompression],
        PlainValidator(validate_open_enum(False)),
    ] = InputCriblmetricsCompression.NONE
    r"""Codec to use to compress the persisted data"""


class InputCriblmetricsMetadatumTypedDict(TypedDict):
    name: str
    value: str
    r"""JavaScript expression to compute field's value, enclosed in quotes or backticks. (Can evaluate to a constant.)"""


class InputCriblmetricsMetadatum(BaseModel):
    name: str

    value: str
    r"""JavaScript expression to compute field's value, enclosed in quotes or backticks. (Can evaluate to a constant.)"""


class InputCriblmetricsTypedDict(TypedDict):
    id: str
    r"""Unique ID for this input"""
    type: InputCriblmetricsType
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
    connections: NotRequired[List[InputCriblmetricsConnectionTypedDict]]
    r"""Direct connections to Destinations, and optionally via a Pipeline or a Pack"""
    pq: NotRequired[InputCriblmetricsPqTypedDict]
    prefix: NotRequired[str]
    r"""A prefix that is applied to the metrics provided by Cribl Stream"""
    full_fidelity: NotRequired[bool]
    r"""Include granular metrics. Disabling this will drop the following metrics events: `cribl.logstream.host.(in_bytes,in_events,out_bytes,out_events)`, `cribl.logstream.index.(in_bytes,in_events,out_bytes,out_events)`, `cribl.logstream.source.(in_bytes,in_events,out_bytes,out_events)`, `cribl.logstream.sourcetype.(in_bytes,in_events,out_bytes,out_events)`."""
    metadata: NotRequired[List[InputCriblmetricsMetadatumTypedDict]]
    r"""Fields to add to events from this input"""
    description: NotRequired[str]


class InputCriblmetrics(BaseModel):
    id: str
    r"""Unique ID for this input"""

    type: Annotated[InputCriblmetricsType, PlainValidator(validate_open_enum(False))]

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

    connections: Optional[List[InputCriblmetricsConnection]] = None
    r"""Direct connections to Destinations, and optionally via a Pipeline or a Pack"""

    pq: Optional[InputCriblmetricsPq] = None

    prefix: Optional[str] = "cribl.logstream."
    r"""A prefix that is applied to the metrics provided by Cribl Stream"""

    full_fidelity: Annotated[Optional[bool], pydantic.Field(alias="fullFidelity")] = (
        True
    )
    r"""Include granular metrics. Disabling this will drop the following metrics events: `cribl.logstream.host.(in_bytes,in_events,out_bytes,out_events)`, `cribl.logstream.index.(in_bytes,in_events,out_bytes,out_events)`, `cribl.logstream.source.(in_bytes,in_events,out_bytes,out_events)`, `cribl.logstream.sourcetype.(in_bytes,in_events,out_bytes,out_events)`."""

    metadata: Optional[List[InputCriblmetricsMetadatum]] = None
    r"""Fields to add to events from this input"""

    description: Optional[str] = None
