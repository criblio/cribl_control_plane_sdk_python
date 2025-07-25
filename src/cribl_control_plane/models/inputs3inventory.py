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


class InputS3InventoryType(str, Enum, metaclass=utils.OpenEnumMeta):
    S3_INVENTORY = "s3_inventory"


class InputS3InventoryConnectionTypedDict(TypedDict):
    output: str
    pipeline: NotRequired[str]


class InputS3InventoryConnection(BaseModel):
    output: str

    pipeline: Optional[str] = None


class InputS3InventoryMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""With Smart mode, PQ will write events to the filesystem only when it detects backpressure from the processing engine. With Always On mode, PQ will always write events directly to the queue before forwarding them to the processing engine."""

    SMART = "smart"
    ALWAYS = "always"


class InputS3InventoryCompression(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Codec to use to compress the persisted data"""

    NONE = "none"
    GZIP = "gzip"


class InputS3InventoryPqTypedDict(TypedDict):
    mode: NotRequired[InputS3InventoryMode]
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
    compress: NotRequired[InputS3InventoryCompression]
    r"""Codec to use to compress the persisted data"""


class InputS3InventoryPq(BaseModel):
    mode: Annotated[
        Optional[InputS3InventoryMode], PlainValidator(validate_open_enum(False))
    ] = InputS3InventoryMode.ALWAYS
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
        Optional[InputS3InventoryCompression], PlainValidator(validate_open_enum(False))
    ] = InputS3InventoryCompression.NONE
    r"""Codec to use to compress the persisted data"""


class InputS3InventoryAuthenticationMethod(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""AWS authentication method. Choose Auto to use IAM roles."""

    AUTO = "auto"
    MANUAL = "manual"
    SECRET = "secret"


class InputS3InventorySignatureVersion(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Signature version to use for signing S3 requests"""

    V2 = "v2"
    V4 = "v4"


class InputS3InventoryPreprocessTypedDict(TypedDict):
    disabled: NotRequired[bool]
    command: NotRequired[str]
    r"""Command to feed the data through (via stdin) and process its output (stdout)"""
    args: NotRequired[List[str]]
    r"""Arguments to be added to the custom command"""


class InputS3InventoryPreprocess(BaseModel):
    disabled: Optional[bool] = True

    command: Optional[str] = None
    r"""Command to feed the data through (via stdin) and process its output (stdout)"""

    args: Optional[List[str]] = None
    r"""Arguments to be added to the custom command"""


class InputS3InventoryMetadatumTypedDict(TypedDict):
    name: str
    value: str
    r"""JavaScript expression to compute field's value, enclosed in quotes or backticks. (Can evaluate to a constant.)"""


class InputS3InventoryMetadatum(BaseModel):
    name: str

    value: str
    r"""JavaScript expression to compute field's value, enclosed in quotes or backticks. (Can evaluate to a constant.)"""


class InputS3InventoryCheckpointingTypedDict(TypedDict):
    enabled: NotRequired[bool]
    r"""Resume processing files after an interruption"""
    retries: NotRequired[float]
    r"""The number of times to retry processing when a processing error occurs. If Skip file on error is enabled, this setting is ignored."""


class InputS3InventoryCheckpointing(BaseModel):
    enabled: Optional[bool] = False
    r"""Resume processing files after an interruption"""

    retries: Optional[float] = 5
    r"""The number of times to retry processing when a processing error occurs. If Skip file on error is enabled, this setting is ignored."""


class InputS3InventoryTagAfterProcessing(str, Enum, metaclass=utils.OpenEnumMeta):
    FALSE = "false"
    TRUE = "true"


class InputS3InventoryTypedDict(TypedDict):
    type: InputS3InventoryType
    queue_name: str
    r"""The name, URL, or ARN of the SQS queue to read notifications from. When a non-AWS URL is specified, format must be: '{url}/myQueueName'. Example: 'https://host:port/myQueueName'. Value must be a JavaScript expression (which can evaluate to a constant value), enclosed in quotes or backticks. Can be evaluated only at init time. Example referencing a Global Variable: `https://host:port/myQueue-${C.vars.myVar}`."""
    id: NotRequired[str]
    r"""Unique ID for this input"""
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
    connections: NotRequired[List[InputS3InventoryConnectionTypedDict]]
    r"""Direct connections to Destinations, and optionally via a Pipeline or a Pack"""
    pq: NotRequired[InputS3InventoryPqTypedDict]
    file_filter: NotRequired[str]
    r"""Regex matching file names to download and process. Defaults to: .*"""
    aws_account_id: NotRequired[str]
    r"""SQS queue owner's AWS account ID. Leave empty if SQS queue is in same AWS account."""
    aws_authentication_method: NotRequired[InputS3InventoryAuthenticationMethod]
    r"""AWS authentication method. Choose Auto to use IAM roles."""
    aws_secret_key: NotRequired[str]
    region: NotRequired[str]
    r"""AWS Region where the S3 bucket and SQS queue are located. Required, unless the Queue entry is a URL or ARN that includes a Region."""
    endpoint: NotRequired[str]
    r"""S3 service endpoint. If empty, defaults to the AWS Region-specific endpoint. Otherwise, it must point to S3-compatible endpoint."""
    signature_version: NotRequired[InputS3InventorySignatureVersion]
    r"""Signature version to use for signing S3 requests"""
    reuse_connections: NotRequired[bool]
    r"""Reuse connections between requests, which can improve performance"""
    reject_unauthorized: NotRequired[bool]
    r"""Reject certificates that cannot be verified against a valid CA, such as self-signed certificates"""
    breaker_rulesets: NotRequired[List[str]]
    r"""A list of event-breaking rulesets that will be applied, in order, to the input data stream"""
    stale_channel_flush_ms: NotRequired[float]
    r"""How long (in milliseconds) the Event Breaker will wait for new data to be sent to a specific channel before flushing the data stream out, as is, to the Pipelines"""
    max_messages: NotRequired[float]
    r"""The maximum number of messages SQS should return in a poll request. Amazon SQS never returns more messages than this value (however, fewer messages might be returned). Valid values: 1 to 10."""
    visibility_timeout: NotRequired[float]
    r"""After messages are retrieved by a ReceiveMessage request, @{product} will hide them from subsequent retrieve requests for at least this duration. You can set this as high as 43200 sec. (12 hours)."""
    num_receivers: NotRequired[float]
    r"""How many receiver processes to run. The higher the number, the better the throughput - at the expense of CPU overhead."""
    socket_timeout: NotRequired[float]
    r"""Socket inactivity timeout (in seconds). Increase this value if timeouts occur due to backpressure."""
    skip_on_error: NotRequired[bool]
    r"""Skip files that trigger a processing error. Disabled by default, which allows retries after processing errors."""
    enable_assume_role: NotRequired[bool]
    r"""Use Assume Role credentials to access Amazon S3"""
    assume_role_arn: NotRequired[str]
    r"""Amazon Resource Name (ARN) of the role to assume"""
    assume_role_external_id: NotRequired[str]
    r"""External ID to use when assuming role"""
    duration_seconds: NotRequired[float]
    r"""Duration of the assumed role's session, in seconds. Minimum is 900 (15 minutes), default is 3600 (1 hour), and maximum is 43200 (12 hours)."""
    enable_sqs_assume_role: NotRequired[bool]
    r"""Use Assume Role credentials when accessing Amazon SQS"""
    preprocess: NotRequired[InputS3InventoryPreprocessTypedDict]
    metadata: NotRequired[List[InputS3InventoryMetadatumTypedDict]]
    r"""Fields to add to events from this input"""
    parquet_chunk_size_mb: NotRequired[float]
    r"""Maximum file size for each Parquet chunk"""
    parquet_chunk_download_timeout: NotRequired[float]
    r"""The maximum time allowed for downloading a Parquet chunk. Processing will stop if a chunk cannot be downloaded within the time specified."""
    checkpointing: NotRequired[InputS3InventoryCheckpointingTypedDict]
    poll_timeout: NotRequired[float]
    r"""How long to wait for events before trying polling again. The lower the number the higher the AWS bill. The higher the number the longer it will take for the source to react to configuration changes and system restarts."""
    checksum_suffix: NotRequired[str]
    r"""Filename suffix of the manifest checksum file. If a filename matching this suffix is received        in the queue, the matching manifest file will be downloaded and validated against its value. Defaults to \"checksum\" """
    max_manifest_size_kb: NotRequired[int]
    r"""Maximum download size (KB) of each manifest or checksum file. Manifest files larger than this size will not be read.        Defaults to 4096."""
    validate_inventory_files: NotRequired[bool]
    r"""If set to Yes, each inventory file in the manifest will be validated against its checksum. Defaults to false"""
    description: NotRequired[str]
    aws_api_key: NotRequired[str]
    aws_secret: NotRequired[str]
    r"""Select or create a stored secret that references your access key and secret key"""
    tag_after_processing: NotRequired[InputS3InventoryTagAfterProcessing]
    processed_tag_key: NotRequired[str]
    r"""The key for the S3 object tag applied after processing. This field accepts an expression for dynamic generation."""
    processed_tag_value: NotRequired[str]
    r"""The value for the S3 object tag applied after processing. This field accepts an expression for dynamic generation."""


class InputS3Inventory(BaseModel):
    type: Annotated[InputS3InventoryType, PlainValidator(validate_open_enum(False))]

    queue_name: Annotated[str, pydantic.Field(alias="queueName")]
    r"""The name, URL, or ARN of the SQS queue to read notifications from. When a non-AWS URL is specified, format must be: '{url}/myQueueName'. Example: 'https://host:port/myQueueName'. Value must be a JavaScript expression (which can evaluate to a constant value), enclosed in quotes or backticks. Can be evaluated only at init time. Example referencing a Global Variable: `https://host:port/myQueue-${C.vars.myVar}`."""

    id: Optional[str] = None
    r"""Unique ID for this input"""

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

    connections: Optional[List[InputS3InventoryConnection]] = None
    r"""Direct connections to Destinations, and optionally via a Pipeline or a Pack"""

    pq: Optional[InputS3InventoryPq] = None

    file_filter: Annotated[Optional[str], pydantic.Field(alias="fileFilter")] = "/.*/"
    r"""Regex matching file names to download and process. Defaults to: .*"""

    aws_account_id: Annotated[Optional[str], pydantic.Field(alias="awsAccountId")] = (
        None
    )
    r"""SQS queue owner's AWS account ID. Leave empty if SQS queue is in same AWS account."""

    aws_authentication_method: Annotated[
        Annotated[
            Optional[InputS3InventoryAuthenticationMethod],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="awsAuthenticationMethod"),
    ] = InputS3InventoryAuthenticationMethod.AUTO
    r"""AWS authentication method. Choose Auto to use IAM roles."""

    aws_secret_key: Annotated[Optional[str], pydantic.Field(alias="awsSecretKey")] = (
        None
    )

    region: Optional[str] = None
    r"""AWS Region where the S3 bucket and SQS queue are located. Required, unless the Queue entry is a URL or ARN that includes a Region."""

    endpoint: Optional[str] = None
    r"""S3 service endpoint. If empty, defaults to the AWS Region-specific endpoint. Otherwise, it must point to S3-compatible endpoint."""

    signature_version: Annotated[
        Annotated[
            Optional[InputS3InventorySignatureVersion],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="signatureVersion"),
    ] = InputS3InventorySignatureVersion.V4
    r"""Signature version to use for signing S3 requests"""

    reuse_connections: Annotated[
        Optional[bool], pydantic.Field(alias="reuseConnections")
    ] = True
    r"""Reuse connections between requests, which can improve performance"""

    reject_unauthorized: Annotated[
        Optional[bool], pydantic.Field(alias="rejectUnauthorized")
    ] = True
    r"""Reject certificates that cannot be verified against a valid CA, such as self-signed certificates"""

    breaker_rulesets: Annotated[
        Optional[List[str]], pydantic.Field(alias="breakerRulesets")
    ] = None
    r"""A list of event-breaking rulesets that will be applied, in order, to the input data stream"""

    stale_channel_flush_ms: Annotated[
        Optional[float], pydantic.Field(alias="staleChannelFlushMs")
    ] = 10000
    r"""How long (in milliseconds) the Event Breaker will wait for new data to be sent to a specific channel before flushing the data stream out, as is, to the Pipelines"""

    max_messages: Annotated[Optional[float], pydantic.Field(alias="maxMessages")] = 1
    r"""The maximum number of messages SQS should return in a poll request. Amazon SQS never returns more messages than this value (however, fewer messages might be returned). Valid values: 1 to 10."""

    visibility_timeout: Annotated[
        Optional[float], pydantic.Field(alias="visibilityTimeout")
    ] = 600
    r"""After messages are retrieved by a ReceiveMessage request, @{product} will hide them from subsequent retrieve requests for at least this duration. You can set this as high as 43200 sec. (12 hours)."""

    num_receivers: Annotated[Optional[float], pydantic.Field(alias="numReceivers")] = 1
    r"""How many receiver processes to run. The higher the number, the better the throughput - at the expense of CPU overhead."""

    socket_timeout: Annotated[
        Optional[float], pydantic.Field(alias="socketTimeout")
    ] = 300
    r"""Socket inactivity timeout (in seconds). Increase this value if timeouts occur due to backpressure."""

    skip_on_error: Annotated[Optional[bool], pydantic.Field(alias="skipOnError")] = (
        False
    )
    r"""Skip files that trigger a processing error. Disabled by default, which allows retries after processing errors."""

    enable_assume_role: Annotated[
        Optional[bool], pydantic.Field(alias="enableAssumeRole")
    ] = True
    r"""Use Assume Role credentials to access Amazon S3"""

    assume_role_arn: Annotated[Optional[str], pydantic.Field(alias="assumeRoleArn")] = (
        None
    )
    r"""Amazon Resource Name (ARN) of the role to assume"""

    assume_role_external_id: Annotated[
        Optional[str], pydantic.Field(alias="assumeRoleExternalId")
    ] = None
    r"""External ID to use when assuming role"""

    duration_seconds: Annotated[
        Optional[float], pydantic.Field(alias="durationSeconds")
    ] = 3600
    r"""Duration of the assumed role's session, in seconds. Minimum is 900 (15 minutes), default is 3600 (1 hour), and maximum is 43200 (12 hours)."""

    enable_sqs_assume_role: Annotated[
        Optional[bool], pydantic.Field(alias="enableSQSAssumeRole")
    ] = False
    r"""Use Assume Role credentials when accessing Amazon SQS"""

    preprocess: Optional[InputS3InventoryPreprocess] = None

    metadata: Optional[List[InputS3InventoryMetadatum]] = None
    r"""Fields to add to events from this input"""

    parquet_chunk_size_mb: Annotated[
        Optional[float], pydantic.Field(alias="parquetChunkSizeMB")
    ] = 5
    r"""Maximum file size for each Parquet chunk"""

    parquet_chunk_download_timeout: Annotated[
        Optional[float], pydantic.Field(alias="parquetChunkDownloadTimeout")
    ] = 600
    r"""The maximum time allowed for downloading a Parquet chunk. Processing will stop if a chunk cannot be downloaded within the time specified."""

    checkpointing: Optional[InputS3InventoryCheckpointing] = None

    poll_timeout: Annotated[Optional[float], pydantic.Field(alias="pollTimeout")] = 10
    r"""How long to wait for events before trying polling again. The lower the number the higher the AWS bill. The higher the number the longer it will take for the source to react to configuration changes and system restarts."""

    checksum_suffix: Annotated[
        Optional[str], pydantic.Field(alias="checksumSuffix")
    ] = "checksum"
    r"""Filename suffix of the manifest checksum file. If a filename matching this suffix is received        in the queue, the matching manifest file will be downloaded and validated against its value. Defaults to \"checksum\" """

    max_manifest_size_kb: Annotated[
        Optional[int], pydantic.Field(alias="maxManifestSizeKB")
    ] = 4096
    r"""Maximum download size (KB) of each manifest or checksum file. Manifest files larger than this size will not be read.        Defaults to 4096."""

    validate_inventory_files: Annotated[
        Optional[bool], pydantic.Field(alias="validateInventoryFiles")
    ] = False
    r"""If set to Yes, each inventory file in the manifest will be validated against its checksum. Defaults to false"""

    description: Optional[str] = None

    aws_api_key: Annotated[Optional[str], pydantic.Field(alias="awsApiKey")] = None

    aws_secret: Annotated[Optional[str], pydantic.Field(alias="awsSecret")] = None
    r"""Select or create a stored secret that references your access key and secret key"""

    tag_after_processing: Annotated[
        Annotated[
            Optional[InputS3InventoryTagAfterProcessing],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="tagAfterProcessing"),
    ] = None

    processed_tag_key: Annotated[
        Optional[str], pydantic.Field(alias="processedTagKey")
    ] = None
    r"""The key for the S3 object tag applied after processing. This field accepts an expression for dynamic generation."""

    processed_tag_value: Annotated[
        Optional[str], pydantic.Field(alias="processedTagValue")
    ] = None
    r"""The value for the S3 object tag applied after processing. This field accepts an expression for dynamic generation."""
