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


class InputGooglePubsubType(str, Enum, metaclass=utils.OpenEnumMeta):
    GOOGLE_PUBSUB = "google_pubsub"


class InputGooglePubsubConnectionTypedDict(TypedDict):
    output: str
    pipeline: NotRequired[str]


class InputGooglePubsubConnection(BaseModel):
    output: str

    pipeline: Optional[str] = None


class InputGooglePubsubMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""With Smart mode, PQ will write events to the filesystem only when it detects backpressure from the processing engine. With Always On mode, PQ will always write events directly to the queue before forwarding them to the processing engine."""

    SMART = "smart"
    ALWAYS = "always"


class InputGooglePubsubCompression(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Codec to use to compress the persisted data"""

    NONE = "none"
    GZIP = "gzip"


class InputGooglePubsubPqTypedDict(TypedDict):
    mode: NotRequired[InputGooglePubsubMode]
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
    compress: NotRequired[InputGooglePubsubCompression]
    r"""Codec to use to compress the persisted data"""


class InputGooglePubsubPq(BaseModel):
    mode: Annotated[
        Optional[InputGooglePubsubMode], PlainValidator(validate_open_enum(False))
    ] = InputGooglePubsubMode.ALWAYS
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
        Optional[InputGooglePubsubCompression],
        PlainValidator(validate_open_enum(False)),
    ] = InputGooglePubsubCompression.NONE
    r"""Codec to use to compress the persisted data"""


class InputGooglePubsubGoogleAuthenticationMethod(
    str, Enum, metaclass=utils.OpenEnumMeta
):
    r"""Choose Auto to use Google Application Default Credentials (ADC), Manual to enter Google service account credentials directly, or Secret to select or create a stored secret that references Google service account credentials."""

    AUTO = "auto"
    MANUAL = "manual"
    SECRET = "secret"


class InputGooglePubsubMetadatumTypedDict(TypedDict):
    name: str
    value: str
    r"""JavaScript expression to compute field's value, enclosed in quotes or backticks. (Can evaluate to a constant.)"""


class InputGooglePubsubMetadatum(BaseModel):
    name: str

    value: str
    r"""JavaScript expression to compute field's value, enclosed in quotes or backticks. (Can evaluate to a constant.)"""


class InputGooglePubsubTypedDict(TypedDict):
    topic_name: str
    r"""ID of the topic to receive events from"""
    subscription_name: str
    r"""ID of the subscription to use when receiving events"""
    id: NotRequired[str]
    r"""Unique ID for this input"""
    type: NotRequired[InputGooglePubsubType]
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
    connections: NotRequired[List[InputGooglePubsubConnectionTypedDict]]
    r"""Direct connections to Destinations, and optionally via a Pipeline or a Pack"""
    pq: NotRequired[InputGooglePubsubPqTypedDict]
    create_topic: NotRequired[bool]
    r"""Create topic if it does not exist"""
    create_subscription: NotRequired[bool]
    r"""Create subscription if it does not exist"""
    region: NotRequired[str]
    r"""Region to retrieve messages from. Select 'default' to allow Google to auto-select the nearest region. When using ordered delivery, the selected region must be allowed by message storage policy."""
    google_auth_method: NotRequired[InputGooglePubsubGoogleAuthenticationMethod]
    r"""Choose Auto to use Google Application Default Credentials (ADC), Manual to enter Google service account credentials directly, or Secret to select or create a stored secret that references Google service account credentials."""
    service_account_credentials: NotRequired[str]
    r"""Contents of service account credentials (JSON keys) file downloaded from Google Cloud. To upload a file, click the upload button at this field's upper right."""
    secret: NotRequired[str]
    r"""Select or create a stored text secret"""
    max_backlog: NotRequired[float]
    r"""If Destination exerts backpressure, this setting limits how many inbound events Stream will queue for processing before it stops retrieving events"""
    concurrency: NotRequired[float]
    r"""How many streams to pull messages from at one time. Doubling the value doubles the number of messages this Source pulls from the topic (if available), while consuming more CPU and memory. Defaults to 5."""
    request_timeout: NotRequired[float]
    r"""Pull request timeout, in milliseconds"""
    metadata: NotRequired[List[InputGooglePubsubMetadatumTypedDict]]
    r"""Fields to add to events from this input"""
    description: NotRequired[str]
    ordered_delivery: NotRequired[bool]
    r"""Receive events in the order they were added to the queue. The process sending events must have ordering enabled."""


class InputGooglePubsub(BaseModel):
    topic_name: Annotated[str, pydantic.Field(alias="topicName")]
    r"""ID of the topic to receive events from"""

    subscription_name: Annotated[str, pydantic.Field(alias="subscriptionName")]
    r"""ID of the subscription to use when receiving events"""

    id: Optional[str] = None
    r"""Unique ID for this input"""

    type: Annotated[
        Optional[InputGooglePubsubType], PlainValidator(validate_open_enum(False))
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

    connections: Optional[List[InputGooglePubsubConnection]] = None
    r"""Direct connections to Destinations, and optionally via a Pipeline or a Pack"""

    pq: Optional[InputGooglePubsubPq] = None

    create_topic: Annotated[Optional[bool], pydantic.Field(alias="createTopic")] = False
    r"""Create topic if it does not exist"""

    create_subscription: Annotated[
        Optional[bool], pydantic.Field(alias="createSubscription")
    ] = True
    r"""Create subscription if it does not exist"""

    region: Optional[str] = None
    r"""Region to retrieve messages from. Select 'default' to allow Google to auto-select the nearest region. When using ordered delivery, the selected region must be allowed by message storage policy."""

    google_auth_method: Annotated[
        Annotated[
            Optional[InputGooglePubsubGoogleAuthenticationMethod],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="googleAuthMethod"),
    ] = InputGooglePubsubGoogleAuthenticationMethod.MANUAL
    r"""Choose Auto to use Google Application Default Credentials (ADC), Manual to enter Google service account credentials directly, or Secret to select or create a stored secret that references Google service account credentials."""

    service_account_credentials: Annotated[
        Optional[str], pydantic.Field(alias="serviceAccountCredentials")
    ] = None
    r"""Contents of service account credentials (JSON keys) file downloaded from Google Cloud. To upload a file, click the upload button at this field's upper right."""

    secret: Optional[str] = None
    r"""Select or create a stored text secret"""

    max_backlog: Annotated[Optional[float], pydantic.Field(alias="maxBacklog")] = 1000
    r"""If Destination exerts backpressure, this setting limits how many inbound events Stream will queue for processing before it stops retrieving events"""

    concurrency: Optional[float] = 5
    r"""How many streams to pull messages from at one time. Doubling the value doubles the number of messages this Source pulls from the topic (if available), while consuming more CPU and memory. Defaults to 5."""

    request_timeout: Annotated[
        Optional[float], pydantic.Field(alias="requestTimeout")
    ] = 60000
    r"""Pull request timeout, in milliseconds"""

    metadata: Optional[List[InputGooglePubsubMetadatum]] = None
    r"""Fields to add to events from this input"""

    description: Optional[str] = None

    ordered_delivery: Annotated[
        Optional[bool], pydantic.Field(alias="orderedDelivery")
    ] = False
    r"""Receive events in the order they were added to the queue. The process sending events must have ordering enabled."""
