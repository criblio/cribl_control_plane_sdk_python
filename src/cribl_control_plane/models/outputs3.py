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


class OutputS3Type(str, Enum, metaclass=utils.OpenEnumMeta):
    S3 = "s3"


class OutputS3AuthenticationMethod(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""AWS authentication method. Choose Auto to use IAM roles."""

    AUTO = "auto"
    MANUAL = "manual"
    SECRET = "secret"


class OutputS3SignatureVersion(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Signature version to use for signing S3 requests"""

    V2 = "v2"
    V4 = "v4"


class OutputS3ObjectACL(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Object ACL to assign to uploaded objects"""

    PRIVATE = "private"
    PUBLIC_READ = "public-read"
    PUBLIC_READ_WRITE = "public-read-write"
    AUTHENTICATED_READ = "authenticated-read"
    AWS_EXEC_READ = "aws-exec-read"
    BUCKET_OWNER_READ = "bucket-owner-read"
    BUCKET_OWNER_FULL_CONTROL = "bucket-owner-full-control"


class OutputS3StorageClass(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Storage class to select for uploaded objects"""

    STANDARD = "STANDARD"
    REDUCED_REDUNDANCY = "REDUCED_REDUNDANCY"
    STANDARD_IA = "STANDARD_IA"
    ONEZONE_IA = "ONEZONE_IA"
    INTELLIGENT_TIERING = "INTELLIGENT_TIERING"
    GLACIER = "GLACIER"
    GLACIER_IR = "GLACIER_IR"
    DEEP_ARCHIVE = "DEEP_ARCHIVE"


class OutputS3ServerSideEncryptionForUploadedObjects(
    str, Enum, metaclass=utils.OpenEnumMeta
):
    AES256 = "AES256"
    AWS_KMS = "aws:kms"


class OutputS3DataFormat(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Format of the output data"""

    JSON = "json"
    RAW = "raw"
    PARQUET = "parquet"


class OutputS3BackpressureBehavior(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""How to handle events when all receivers are exerting backpressure"""

    BLOCK = "block"
    DROP = "drop"


class OutputS3DiskSpaceProtection(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""How to handle events when disk space is below the global 'Min free disk space' limit"""

    BLOCK = "block"
    DROP = "drop"


class OutputS3Compression(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Data compression format to apply to HTTP content before it is delivered"""

    NONE = "none"
    GZIP = "gzip"


class OutputS3CompressionLevel(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Compression level to apply before moving files to final destination"""

    BEST_SPEED = "best_speed"
    NORMAL = "normal"
    BEST_COMPRESSION = "best_compression"


class OutputS3ParquetVersion(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Determines which data types are supported and how they are represented"""

    PARQUET_1_0 = "PARQUET_1_0"
    PARQUET_2_4 = "PARQUET_2_4"
    PARQUET_2_6 = "PARQUET_2_6"


class OutputS3DataPageVersion(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Serialization format of data pages. Note that some reader implementations use Data page V2's attributes to work more efficiently, while others ignore it."""

    DATA_PAGE_V1 = "DATA_PAGE_V1"
    DATA_PAGE_V2 = "DATA_PAGE_V2"


class OutputS3KeyValueMetadatumTypedDict(TypedDict):
    value: str
    key: NotRequired[str]


class OutputS3KeyValueMetadatum(BaseModel):
    value: str

    key: Optional[str] = ""


class OutputS3TypedDict(TypedDict):
    bucket: str
    r"""Name of the destination S3 bucket. Must be a JavaScript expression (which can evaluate to a constant value), enclosed in quotes or backticks. Can be evaluated only at initialization time. Example referencing a Global Variable: `myBucket-${C.vars.myVar}`"""
    id: NotRequired[str]
    r"""Unique ID for this output"""
    type: NotRequired[OutputS3Type]
    pipeline: NotRequired[str]
    r"""Pipeline to process data before sending out to this output"""
    system_fields: NotRequired[List[str]]
    r"""Fields to automatically add to events, such as cribl_pipe. Supports wildcards."""
    environment: NotRequired[str]
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    streamtags: NotRequired[List[str]]
    r"""Tags for filtering and grouping in @{product}"""
    region: NotRequired[str]
    r"""Region where the S3 bucket is located"""
    aws_secret_key: NotRequired[str]
    r"""Secret key. This value can be a constant or a JavaScript expression. Example: `${C.env.SOME_SECRET}`)"""
    aws_authentication_method: NotRequired[OutputS3AuthenticationMethod]
    r"""AWS authentication method. Choose Auto to use IAM roles."""
    endpoint: NotRequired[str]
    r"""S3 service endpoint. If empty, defaults to the AWS Region-specific endpoint. Otherwise, it must point to S3-compatible endpoint."""
    signature_version: NotRequired[OutputS3SignatureVersion]
    r"""Signature version to use for signing S3 requests"""
    reuse_connections: NotRequired[bool]
    r"""Reuse connections between requests, which can improve performance"""
    reject_unauthorized: NotRequired[bool]
    r"""Reject certificates that cannot be verified against a valid CA, such as self-signed certificates"""
    enable_assume_role: NotRequired[bool]
    r"""Use Assume Role credentials to access S3"""
    assume_role_arn: NotRequired[str]
    r"""Amazon Resource Name (ARN) of the role to assume"""
    assume_role_external_id: NotRequired[str]
    r"""External ID to use when assuming role"""
    duration_seconds: NotRequired[float]
    r"""Duration of the assumed role's session, in seconds. Minimum is 900 (15 minutes), default is 3600 (1 hour), and maximum is 43200 (12 hours)."""
    stage_path: NotRequired[str]
    r"""Filesystem location in which to buffer files, before compressing and moving to final destination. Use performant and stable storage."""
    add_id_to_stage_path: NotRequired[bool]
    r"""Add the Output ID value to staging location"""
    dest_path: NotRequired[str]
    r"""Prefix to append to files before uploading. Must be a JavaScript expression (which can evaluate to a constant value), enclosed in quotes or backticks. Can be evaluated only at init time. Example referencing a Global Variable: `myKeyPrefix-${C.vars.myVar}`"""
    object_acl: NotRequired[OutputS3ObjectACL]
    r"""Object ACL to assign to uploaded objects"""
    storage_class: NotRequired[OutputS3StorageClass]
    r"""Storage class to select for uploaded objects"""
    server_side_encryption: NotRequired[OutputS3ServerSideEncryptionForUploadedObjects]
    kms_key_id: NotRequired[str]
    r"""ID or ARN of the KMS customer-managed key to use for encryption"""
    remove_empty_dirs: NotRequired[bool]
    r"""Remove empty staging directories after moving files"""
    partition_expr: NotRequired[str]
    r"""JavaScript expression defining how files are partitioned and organized. Default is date-based. If blank, Stream will fall back to the event's __partition field value – if present – otherwise to each location's root directory."""
    format_: NotRequired[OutputS3DataFormat]
    r"""Format of the output data"""
    base_file_name: NotRequired[str]
    r"""JavaScript expression to define the output filename prefix (can be constant)"""
    file_name_suffix: NotRequired[str]
    r"""JavaScript expression to define the output filename suffix (can be constant).  The `__format` variable refers to the value of the `Data format` field (`json` or `raw`).  The `__compression` field refers to the kind of compression being used (`none` or `gzip`)."""
    max_file_size_mb: NotRequired[float]
    r"""Maximum uncompressed output file size. Files of this size will be closed and moved to final output location."""
    max_open_files: NotRequired[float]
    r"""Maximum number of files to keep open concurrently. When exceeded, @{product} will close the oldest open files and move them to the final output location."""
    header_line: NotRequired[str]
    r"""If set, this line will be written to the beginning of each output file"""
    write_high_water_mark: NotRequired[float]
    r"""Buffer size used to write to a file"""
    on_backpressure: NotRequired[OutputS3BackpressureBehavior]
    r"""How to handle events when all receivers are exerting backpressure"""
    deadletter_enabled: NotRequired[bool]
    r"""If a file fails to move to its final destination after the maximum number of retries, move it to a designated directory to prevent further errors"""
    on_disk_full_backpressure: NotRequired[OutputS3DiskSpaceProtection]
    r"""How to handle events when disk space is below the global 'Min free disk space' limit"""
    max_file_open_time_sec: NotRequired[float]
    r"""Maximum amount of time to write to a file. Files open for longer than this will be closed and moved to final output location."""
    max_file_idle_time_sec: NotRequired[float]
    r"""Maximum amount of time to keep inactive files open. Files open for longer than this will be closed and moved to final output location."""
    max_concurrent_file_parts: NotRequired[float]
    r"""Maximum number of parts to upload in parallel per file. Minimum part size is 5MB."""
    verify_permissions: NotRequired[bool]
    r"""Disable if you can access files within the bucket but not the bucket itself"""
    max_closing_files_to_backpressure: NotRequired[float]
    r"""Maximum number of files that can be waiting for upload before backpressure is applied"""
    description: NotRequired[str]
    aws_api_key: NotRequired[str]
    r"""This value can be a constant or a JavaScript expression (`${C.env.SOME_ACCESS_KEY}`)"""
    aws_secret: NotRequired[str]
    r"""Select or create a stored secret that references your access key and secret key"""
    compress: NotRequired[OutputS3Compression]
    r"""Data compression format to apply to HTTP content before it is delivered"""
    compression_level: NotRequired[OutputS3CompressionLevel]
    r"""Compression level to apply before moving files to final destination"""
    automatic_schema: NotRequired[bool]
    r"""Automatically calculate the schema based on the events of each Parquet file generated"""
    parquet_version: NotRequired[OutputS3ParquetVersion]
    r"""Determines which data types are supported and how they are represented"""
    parquet_data_page_version: NotRequired[OutputS3DataPageVersion]
    r"""Serialization format of data pages. Note that some reader implementations use Data page V2's attributes to work more efficiently, while others ignore it."""
    parquet_row_group_length: NotRequired[float]
    r"""The number of rows that every group will contain. The final group can contain a smaller number of rows."""
    parquet_page_size: NotRequired[str]
    r"""Target memory size for page segments, such as 1MB or 128MB. Generally, lower values improve reading speed, while higher values improve compression."""
    should_log_invalid_rows: NotRequired[bool]
    r"""Log up to 3 rows that @{product} skips due to data mismatch"""
    key_value_metadata: NotRequired[List[OutputS3KeyValueMetadatumTypedDict]]
    r"""The metadata of files the Destination writes will include the properties you add here as key-value pairs. Useful for tagging. Examples: \"key\":\"OCSF Event Class\", \"value\":\"9001\" """
    enable_statistics: NotRequired[bool]
    r"""Statistics profile an entire file in terms of minimum/maximum values within data, numbers of nulls, etc. You can use Parquet tools to view statistics."""
    enable_write_page_index: NotRequired[bool]
    r"""One page index contains statistics for one data page. Parquet readers use statistics to enable page skipping."""
    enable_page_checksum: NotRequired[bool]
    r"""Parquet tools can use the checksum of a Parquet page to verify data integrity"""
    empty_dir_cleanup_sec: NotRequired[float]
    r"""How frequently, in seconds, to clean up empty directories"""
    deadletter_path: NotRequired[str]
    r"""Storage location for files that fail to reach their final destination after maximum retries are exceeded"""
    max_retry_num: NotRequired[float]
    r"""The maximum number of times a file will attempt to move to its final destination before being dead-lettered"""


class OutputS3(BaseModel):
    bucket: str
    r"""Name of the destination S3 bucket. Must be a JavaScript expression (which can evaluate to a constant value), enclosed in quotes or backticks. Can be evaluated only at initialization time. Example referencing a Global Variable: `myBucket-${C.vars.myVar}`"""

    id: Optional[str] = None
    r"""Unique ID for this output"""

    type: Annotated[
        Optional[OutputS3Type], PlainValidator(validate_open_enum(False))
    ] = None

    pipeline: Optional[str] = None
    r"""Pipeline to process data before sending out to this output"""

    system_fields: Annotated[
        Optional[List[str]], pydantic.Field(alias="systemFields")
    ] = None
    r"""Fields to automatically add to events, such as cribl_pipe. Supports wildcards."""

    environment: Optional[str] = None
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""

    streamtags: Optional[List[str]] = None
    r"""Tags for filtering and grouping in @{product}"""

    region: Optional[str] = None
    r"""Region where the S3 bucket is located"""

    aws_secret_key: Annotated[Optional[str], pydantic.Field(alias="awsSecretKey")] = (
        None
    )
    r"""Secret key. This value can be a constant or a JavaScript expression. Example: `${C.env.SOME_SECRET}`)"""

    aws_authentication_method: Annotated[
        Annotated[
            Optional[OutputS3AuthenticationMethod],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="awsAuthenticationMethod"),
    ] = OutputS3AuthenticationMethod.AUTO
    r"""AWS authentication method. Choose Auto to use IAM roles."""

    endpoint: Optional[str] = None
    r"""S3 service endpoint. If empty, defaults to the AWS Region-specific endpoint. Otherwise, it must point to S3-compatible endpoint."""

    signature_version: Annotated[
        Annotated[
            Optional[OutputS3SignatureVersion],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="signatureVersion"),
    ] = OutputS3SignatureVersion.V4
    r"""Signature version to use for signing S3 requests"""

    reuse_connections: Annotated[
        Optional[bool], pydantic.Field(alias="reuseConnections")
    ] = True
    r"""Reuse connections between requests, which can improve performance"""

    reject_unauthorized: Annotated[
        Optional[bool], pydantic.Field(alias="rejectUnauthorized")
    ] = True
    r"""Reject certificates that cannot be verified against a valid CA, such as self-signed certificates"""

    enable_assume_role: Annotated[
        Optional[bool], pydantic.Field(alias="enableAssumeRole")
    ] = False
    r"""Use Assume Role credentials to access S3"""

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

    stage_path: Annotated[Optional[str], pydantic.Field(alias="stagePath")] = (
        "$CRIBL_HOME/state/outputs/staging"
    )
    r"""Filesystem location in which to buffer files, before compressing and moving to final destination. Use performant and stable storage."""

    add_id_to_stage_path: Annotated[
        Optional[bool], pydantic.Field(alias="addIdToStagePath")
    ] = True
    r"""Add the Output ID value to staging location"""

    dest_path: Annotated[Optional[str], pydantic.Field(alias="destPath")] = ""
    r"""Prefix to append to files before uploading. Must be a JavaScript expression (which can evaluate to a constant value), enclosed in quotes or backticks. Can be evaluated only at init time. Example referencing a Global Variable: `myKeyPrefix-${C.vars.myVar}`"""

    object_acl: Annotated[
        Annotated[
            Optional[OutputS3ObjectACL], PlainValidator(validate_open_enum(False))
        ],
        pydantic.Field(alias="objectACL"),
    ] = OutputS3ObjectACL.PRIVATE
    r"""Object ACL to assign to uploaded objects"""

    storage_class: Annotated[
        Annotated[
            Optional[OutputS3StorageClass], PlainValidator(validate_open_enum(False))
        ],
        pydantic.Field(alias="storageClass"),
    ] = None
    r"""Storage class to select for uploaded objects"""

    server_side_encryption: Annotated[
        Annotated[
            Optional[OutputS3ServerSideEncryptionForUploadedObjects],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="serverSideEncryption"),
    ] = None

    kms_key_id: Annotated[Optional[str], pydantic.Field(alias="kmsKeyId")] = None
    r"""ID or ARN of the KMS customer-managed key to use for encryption"""

    remove_empty_dirs: Annotated[
        Optional[bool], pydantic.Field(alias="removeEmptyDirs")
    ] = True
    r"""Remove empty staging directories after moving files"""

    partition_expr: Annotated[Optional[str], pydantic.Field(alias="partitionExpr")] = (
        "C.Time.strftime(_time ? _time : Date.now()/1000, '%Y/%m/%d')"
    )
    r"""JavaScript expression defining how files are partitioned and organized. Default is date-based. If blank, Stream will fall back to the event's __partition field value – if present – otherwise to each location's root directory."""

    format_: Annotated[
        Annotated[
            Optional[OutputS3DataFormat], PlainValidator(validate_open_enum(False))
        ],
        pydantic.Field(alias="format"),
    ] = OutputS3DataFormat.JSON
    r"""Format of the output data"""

    base_file_name: Annotated[Optional[str], pydantic.Field(alias="baseFileName")] = (
        "`CriblOut`"
    )
    r"""JavaScript expression to define the output filename prefix (can be constant)"""

    file_name_suffix: Annotated[
        Optional[str], pydantic.Field(alias="fileNameSuffix")
    ] = '`.${C.env["CRIBL_WORKER_ID"]}.${__format}${__compression === "gzip" ? ".gz" : ""}`'
    r"""JavaScript expression to define the output filename suffix (can be constant).  The `__format` variable refers to the value of the `Data format` field (`json` or `raw`).  The `__compression` field refers to the kind of compression being used (`none` or `gzip`)."""

    max_file_size_mb: Annotated[
        Optional[float], pydantic.Field(alias="maxFileSizeMB")
    ] = 32
    r"""Maximum uncompressed output file size. Files of this size will be closed and moved to final output location."""

    max_open_files: Annotated[Optional[float], pydantic.Field(alias="maxOpenFiles")] = (
        100
    )
    r"""Maximum number of files to keep open concurrently. When exceeded, @{product} will close the oldest open files and move them to the final output location."""

    header_line: Annotated[Optional[str], pydantic.Field(alias="headerLine")] = ""
    r"""If set, this line will be written to the beginning of each output file"""

    write_high_water_mark: Annotated[
        Optional[float], pydantic.Field(alias="writeHighWaterMark")
    ] = 64
    r"""Buffer size used to write to a file"""

    on_backpressure: Annotated[
        Annotated[
            Optional[OutputS3BackpressureBehavior],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="onBackpressure"),
    ] = OutputS3BackpressureBehavior.BLOCK
    r"""How to handle events when all receivers are exerting backpressure"""

    deadletter_enabled: Annotated[
        Optional[bool], pydantic.Field(alias="deadletterEnabled")
    ] = False
    r"""If a file fails to move to its final destination after the maximum number of retries, move it to a designated directory to prevent further errors"""

    on_disk_full_backpressure: Annotated[
        Annotated[
            Optional[OutputS3DiskSpaceProtection],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="onDiskFullBackpressure"),
    ] = OutputS3DiskSpaceProtection.BLOCK
    r"""How to handle events when disk space is below the global 'Min free disk space' limit"""

    max_file_open_time_sec: Annotated[
        Optional[float], pydantic.Field(alias="maxFileOpenTimeSec")
    ] = 300
    r"""Maximum amount of time to write to a file. Files open for longer than this will be closed and moved to final output location."""

    max_file_idle_time_sec: Annotated[
        Optional[float], pydantic.Field(alias="maxFileIdleTimeSec")
    ] = 30
    r"""Maximum amount of time to keep inactive files open. Files open for longer than this will be closed and moved to final output location."""

    max_concurrent_file_parts: Annotated[
        Optional[float], pydantic.Field(alias="maxConcurrentFileParts")
    ] = 4
    r"""Maximum number of parts to upload in parallel per file. Minimum part size is 5MB."""

    verify_permissions: Annotated[
        Optional[bool], pydantic.Field(alias="verifyPermissions")
    ] = True
    r"""Disable if you can access files within the bucket but not the bucket itself"""

    max_closing_files_to_backpressure: Annotated[
        Optional[float], pydantic.Field(alias="maxClosingFilesToBackpressure")
    ] = 100
    r"""Maximum number of files that can be waiting for upload before backpressure is applied"""

    description: Optional[str] = None

    aws_api_key: Annotated[Optional[str], pydantic.Field(alias="awsApiKey")] = None
    r"""This value can be a constant or a JavaScript expression (`${C.env.SOME_ACCESS_KEY}`)"""

    aws_secret: Annotated[Optional[str], pydantic.Field(alias="awsSecret")] = None
    r"""Select or create a stored secret that references your access key and secret key"""

    compress: Annotated[
        Optional[OutputS3Compression], PlainValidator(validate_open_enum(False))
    ] = OutputS3Compression.GZIP
    r"""Data compression format to apply to HTTP content before it is delivered"""

    compression_level: Annotated[
        Annotated[
            Optional[OutputS3CompressionLevel],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="compressionLevel"),
    ] = OutputS3CompressionLevel.BEST_SPEED
    r"""Compression level to apply before moving files to final destination"""

    automatic_schema: Annotated[
        Optional[bool], pydantic.Field(alias="automaticSchema")
    ] = False
    r"""Automatically calculate the schema based on the events of each Parquet file generated"""

    parquet_version: Annotated[
        Annotated[
            Optional[OutputS3ParquetVersion], PlainValidator(validate_open_enum(False))
        ],
        pydantic.Field(alias="parquetVersion"),
    ] = OutputS3ParquetVersion.PARQUET_2_6
    r"""Determines which data types are supported and how they are represented"""

    parquet_data_page_version: Annotated[
        Annotated[
            Optional[OutputS3DataPageVersion], PlainValidator(validate_open_enum(False))
        ],
        pydantic.Field(alias="parquetDataPageVersion"),
    ] = OutputS3DataPageVersion.DATA_PAGE_V2
    r"""Serialization format of data pages. Note that some reader implementations use Data page V2's attributes to work more efficiently, while others ignore it."""

    parquet_row_group_length: Annotated[
        Optional[float], pydantic.Field(alias="parquetRowGroupLength")
    ] = 10000
    r"""The number of rows that every group will contain. The final group can contain a smaller number of rows."""

    parquet_page_size: Annotated[
        Optional[str], pydantic.Field(alias="parquetPageSize")
    ] = "1MB"
    r"""Target memory size for page segments, such as 1MB or 128MB. Generally, lower values improve reading speed, while higher values improve compression."""

    should_log_invalid_rows: Annotated[
        Optional[bool], pydantic.Field(alias="shouldLogInvalidRows")
    ] = None
    r"""Log up to 3 rows that @{product} skips due to data mismatch"""

    key_value_metadata: Annotated[
        Optional[List[OutputS3KeyValueMetadatum]],
        pydantic.Field(alias="keyValueMetadata"),
    ] = None
    r"""The metadata of files the Destination writes will include the properties you add here as key-value pairs. Useful for tagging. Examples: \"key\":\"OCSF Event Class\", \"value\":\"9001\" """

    enable_statistics: Annotated[
        Optional[bool], pydantic.Field(alias="enableStatistics")
    ] = True
    r"""Statistics profile an entire file in terms of minimum/maximum values within data, numbers of nulls, etc. You can use Parquet tools to view statistics."""

    enable_write_page_index: Annotated[
        Optional[bool], pydantic.Field(alias="enableWritePageIndex")
    ] = True
    r"""One page index contains statistics for one data page. Parquet readers use statistics to enable page skipping."""

    enable_page_checksum: Annotated[
        Optional[bool], pydantic.Field(alias="enablePageChecksum")
    ] = False
    r"""Parquet tools can use the checksum of a Parquet page to verify data integrity"""

    empty_dir_cleanup_sec: Annotated[
        Optional[float], pydantic.Field(alias="emptyDirCleanupSec")
    ] = 300
    r"""How frequently, in seconds, to clean up empty directories"""

    deadletter_path: Annotated[
        Optional[str], pydantic.Field(alias="deadletterPath")
    ] = "$CRIBL_HOME/state/outputs/dead-letter"
    r"""Storage location for files that fail to reach their final destination after maximum retries are exceeded"""

    max_retry_num: Annotated[Optional[float], pydantic.Field(alias="maxRetryNum")] = 20
    r"""The maximum number of times a file will attempt to move to its final destination before being dead-lettered"""
