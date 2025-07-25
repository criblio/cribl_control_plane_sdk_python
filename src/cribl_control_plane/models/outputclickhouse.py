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


class OutputClickHouseType(str, Enum, metaclass=utils.OpenEnumMeta):
    CLICK_HOUSE = "click_house"


class OutputClickHouseAuthenticationType(str, Enum, metaclass=utils.OpenEnumMeta):
    NONE = "none"
    BASIC = "basic"
    CREDENTIALS_SECRET = "credentialsSecret"
    SSL_USER_CERTIFICATE = "sslUserCertificate"
    TOKEN = "token"
    TEXT_SECRET = "textSecret"
    OAUTH = "oauth"


class OutputClickHouseFormat(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Data format to use when sending data to ClickHouse. Defaults to JSON Compact."""

    JSON_COMPACT_EACH_ROW_WITH_NAMES = "json-compact-each-row-with-names"
    JSON_EACH_ROW = "json-each-row"


class MappingType(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""How event fields are mapped to ClickHouse columns."""

    AUTOMATIC = "automatic"
    CUSTOM = "custom"


class OutputClickHouseMinimumTLSVersion(str, Enum, metaclass=utils.OpenEnumMeta):
    TL_SV1 = "TLSv1"
    TL_SV1_1 = "TLSv1.1"
    TL_SV1_2 = "TLSv1.2"
    TL_SV1_3 = "TLSv1.3"


class OutputClickHouseMaximumTLSVersion(str, Enum, metaclass=utils.OpenEnumMeta):
    TL_SV1 = "TLSv1"
    TL_SV1_1 = "TLSv1.1"
    TL_SV1_2 = "TLSv1.2"
    TL_SV1_3 = "TLSv1.3"


class OutputClickHouseTLSSettingsClientSideTypedDict(TypedDict):
    disabled: NotRequired[bool]
    servername: NotRequired[str]
    r"""Server name for the SNI (Server Name Indication) TLS extension. It must be a host name, and not an IP address."""
    certificate_name: NotRequired[str]
    r"""The name of the predefined certificate"""
    ca_path: NotRequired[str]
    r"""Path on client in which to find CA certificates to verify the server's cert. PEM format. Can reference $ENV_VARS."""
    priv_key_path: NotRequired[str]
    r"""Path on client in which to find the private key to use. PEM format. Can reference $ENV_VARS."""
    cert_path: NotRequired[str]
    r"""Path on client in which to find certificates to use. PEM format. Can reference $ENV_VARS."""
    passphrase: NotRequired[str]
    r"""Passphrase to use to decrypt private key"""
    min_version: NotRequired[OutputClickHouseMinimumTLSVersion]
    max_version: NotRequired[OutputClickHouseMaximumTLSVersion]


class OutputClickHouseTLSSettingsClientSide(BaseModel):
    disabled: Optional[bool] = True

    servername: Optional[str] = None
    r"""Server name for the SNI (Server Name Indication) TLS extension. It must be a host name, and not an IP address."""

    certificate_name: Annotated[
        Optional[str], pydantic.Field(alias="certificateName")
    ] = None
    r"""The name of the predefined certificate"""

    ca_path: Annotated[Optional[str], pydantic.Field(alias="caPath")] = None
    r"""Path on client in which to find CA certificates to verify the server's cert. PEM format. Can reference $ENV_VARS."""

    priv_key_path: Annotated[Optional[str], pydantic.Field(alias="privKeyPath")] = None
    r"""Path on client in which to find the private key to use. PEM format. Can reference $ENV_VARS."""

    cert_path: Annotated[Optional[str], pydantic.Field(alias="certPath")] = None
    r"""Path on client in which to find certificates to use. PEM format. Can reference $ENV_VARS."""

    passphrase: Optional[str] = None
    r"""Passphrase to use to decrypt private key"""

    min_version: Annotated[
        Annotated[
            Optional[OutputClickHouseMinimumTLSVersion],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="minVersion"),
    ] = None

    max_version: Annotated[
        Annotated[
            Optional[OutputClickHouseMaximumTLSVersion],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="maxVersion"),
    ] = None


class OutputClickHouseExtraHTTPHeaderTypedDict(TypedDict):
    value: str
    name: NotRequired[str]


class OutputClickHouseExtraHTTPHeader(BaseModel):
    value: str

    name: Optional[str] = None


class OutputClickHouseFailedRequestLoggingMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Data to log when a request fails. All headers are redacted by default, unless listed as safe headers below."""

    PAYLOAD = "payload"
    PAYLOAD_AND_HEADERS = "payloadAndHeaders"
    NONE = "none"


class OutputClickHouseResponseRetrySettingTypedDict(TypedDict):
    http_status: float
    r"""The HTTP response status code that will trigger retries"""
    initial_backoff: NotRequired[float]
    r"""How long, in milliseconds, Cribl Stream should wait before initiating backoff. Maximum interval is 600,000 ms (10 minutes)."""
    backoff_rate: NotRequired[float]
    r"""Base for exponential backoff. A value of 2 (default) means Cribl Stream will retry after 2 seconds, then 4 seconds, then 8 seconds, etc."""
    max_backoff: NotRequired[float]
    r"""The maximum backoff interval, in milliseconds, Cribl Stream should apply. Default (and minimum) is 10,000 ms (10 seconds); maximum is 180,000 ms (180 seconds)."""


class OutputClickHouseResponseRetrySetting(BaseModel):
    http_status: Annotated[float, pydantic.Field(alias="httpStatus")]
    r"""The HTTP response status code that will trigger retries"""

    initial_backoff: Annotated[
        Optional[float], pydantic.Field(alias="initialBackoff")
    ] = 1000
    r"""How long, in milliseconds, Cribl Stream should wait before initiating backoff. Maximum interval is 600,000 ms (10 minutes)."""

    backoff_rate: Annotated[Optional[float], pydantic.Field(alias="backoffRate")] = 2
    r"""Base for exponential backoff. A value of 2 (default) means Cribl Stream will retry after 2 seconds, then 4 seconds, then 8 seconds, etc."""

    max_backoff: Annotated[Optional[float], pydantic.Field(alias="maxBackoff")] = 10000
    r"""The maximum backoff interval, in milliseconds, Cribl Stream should apply. Default (and minimum) is 10,000 ms (10 seconds); maximum is 180,000 ms (180 seconds)."""


class OutputClickHouseTimeoutRetrySettingsTypedDict(TypedDict):
    timeout_retry: NotRequired[bool]
    initial_backoff: NotRequired[float]
    r"""How long, in milliseconds, Cribl Stream should wait before initiating backoff. Maximum interval is 600,000 ms (10 minutes)."""
    backoff_rate: NotRequired[float]
    r"""Base for exponential backoff. A value of 2 (default) means Cribl Stream will retry after 2 seconds, then 4 seconds, then 8 seconds, etc."""
    max_backoff: NotRequired[float]
    r"""The maximum backoff interval, in milliseconds, Cribl Stream should apply. Default (and minimum) is 10,000 ms (10 seconds); maximum is 180,000 ms (180 seconds)."""


class OutputClickHouseTimeoutRetrySettings(BaseModel):
    timeout_retry: Annotated[Optional[bool], pydantic.Field(alias="timeoutRetry")] = (
        False
    )

    initial_backoff: Annotated[
        Optional[float], pydantic.Field(alias="initialBackoff")
    ] = 1000
    r"""How long, in milliseconds, Cribl Stream should wait before initiating backoff. Maximum interval is 600,000 ms (10 minutes)."""

    backoff_rate: Annotated[Optional[float], pydantic.Field(alias="backoffRate")] = 2
    r"""Base for exponential backoff. A value of 2 (default) means Cribl Stream will retry after 2 seconds, then 4 seconds, then 8 seconds, etc."""

    max_backoff: Annotated[Optional[float], pydantic.Field(alias="maxBackoff")] = 10000
    r"""The maximum backoff interval, in milliseconds, Cribl Stream should apply. Default (and minimum) is 10,000 ms (10 seconds); maximum is 180,000 ms (180 seconds)."""


class OutputClickHouseBackpressureBehavior(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""How to handle events when all receivers are exerting backpressure"""

    BLOCK = "block"
    DROP = "drop"
    QUEUE = "queue"


class OutputClickHouseOauthParamTypedDict(TypedDict):
    name: str
    r"""OAuth parameter name"""
    value: str
    r"""OAuth parameter value"""


class OutputClickHouseOauthParam(BaseModel):
    name: str
    r"""OAuth parameter name"""

    value: str
    r"""OAuth parameter value"""


class OutputClickHouseOauthHeaderTypedDict(TypedDict):
    name: str
    r"""OAuth header name"""
    value: str
    r"""OAuth header value"""


class OutputClickHouseOauthHeader(BaseModel):
    name: str
    r"""OAuth header name"""

    value: str
    r"""OAuth header value"""


class ColumnMappingTypedDict(TypedDict):
    column_name: str
    r"""Name of the column in ClickHouse that will store field value"""
    column_value_expression: str
    r"""JavaScript expression to compute value to be inserted into ClickHouse table"""
    column_type: NotRequired[str]
    r"""Type of the column in the ClickHouse database"""


class ColumnMapping(BaseModel):
    column_name: Annotated[str, pydantic.Field(alias="columnName")]
    r"""Name of the column in ClickHouse that will store field value"""

    column_value_expression: Annotated[
        str, pydantic.Field(alias="columnValueExpression")
    ]
    r"""JavaScript expression to compute value to be inserted into ClickHouse table"""

    column_type: Annotated[Optional[str], pydantic.Field(alias="columnType")] = None
    r"""Type of the column in the ClickHouse database"""


class OutputClickHouseCompression(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Codec to use to compress the persisted data"""

    NONE = "none"
    GZIP = "gzip"


class OutputClickHouseQueueFullBehavior(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""How to handle events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""

    BLOCK = "block"
    DROP = "drop"


class OutputClickHouseMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""In Error mode, PQ writes events to the filesystem if the Destination is unavailable. In Backpressure mode, PQ writes events to the filesystem when it detects backpressure from the Destination. In Always On mode, PQ always writes events to the filesystem."""

    ERROR = "error"
    BACKPRESSURE = "backpressure"
    ALWAYS = "always"


class OutputClickHousePqControlsTypedDict(TypedDict):
    pass


class OutputClickHousePqControls(BaseModel):
    pass


class OutputClickHouseTypedDict(TypedDict):
    url: str
    r"""URL of the ClickHouse instance. Example: http://localhost:8123/"""
    database: str
    table_name: str
    r"""Name of the ClickHouse table where data will be inserted. Name can contain letters (A-Z, a-z), numbers (0-9), and the character \"_\", and must start with either a letter or the character \"_\"."""
    id: NotRequired[str]
    r"""Unique ID for this output"""
    type: NotRequired[OutputClickHouseType]
    pipeline: NotRequired[str]
    r"""Pipeline to process data before sending out to this output"""
    system_fields: NotRequired[List[str]]
    r"""Fields to automatically add to events, such as cribl_pipe. Supports wildcards."""
    environment: NotRequired[str]
    r"""Optionally, enable this config only on a specified Git branch. If empty, will be enabled everywhere."""
    streamtags: NotRequired[List[str]]
    r"""Tags for filtering and grouping in @{product}"""
    auth_type: NotRequired[OutputClickHouseAuthenticationType]
    format_: NotRequired[OutputClickHouseFormat]
    r"""Data format to use when sending data to ClickHouse. Defaults to JSON Compact."""
    mapping_type: NotRequired[MappingType]
    r"""How event fields are mapped to ClickHouse columns."""
    async_inserts: NotRequired[bool]
    r"""Collect data into batches for later processing. Disable to write to a ClickHouse table immediately."""
    tls: NotRequired[OutputClickHouseTLSSettingsClientSideTypedDict]
    concurrency: NotRequired[float]
    r"""Maximum number of ongoing requests before blocking"""
    max_payload_size_kb: NotRequired[float]
    r"""Maximum size, in KB, of the request body"""
    max_payload_events: NotRequired[float]
    r"""Maximum number of events to include in the request body. Default is 0 (unlimited)."""
    compress: NotRequired[bool]
    r"""Compress the payload body before sending"""
    reject_unauthorized: NotRequired[bool]
    r"""Reject certificates not authorized by a CA in the CA certificate path or by another trusted CA (such as the system's).
    Enabled by default. When this setting is also present in TLS Settings (Client Side),
    that value will take precedence.
    """
    timeout_sec: NotRequired[float]
    r"""Amount of time, in seconds, to wait for a request to complete before canceling it"""
    flush_period_sec: NotRequired[float]
    r"""Maximum time between requests. Small values could cause the payload size to be smaller than the configured Body size limit."""
    extra_http_headers: NotRequired[List[OutputClickHouseExtraHTTPHeaderTypedDict]]
    r"""Headers to add to all events"""
    use_round_robin_dns: NotRequired[bool]
    r"""Enable round-robin DNS lookup. When a DNS server returns multiple addresses, @{product} will cycle through them in the order returned. For optimal performance, consider enabling this setting for non-load balanced destinations."""
    failed_request_logging_mode: NotRequired[OutputClickHouseFailedRequestLoggingMode]
    r"""Data to log when a request fails. All headers are redacted by default, unless listed as safe headers below."""
    safe_headers: NotRequired[List[str]]
    r"""List of headers that are safe to log in plain text"""
    response_retry_settings: NotRequired[
        List[OutputClickHouseResponseRetrySettingTypedDict]
    ]
    r"""Automatically retry after unsuccessful response status codes, such as 429 (Too Many Requests) or 503 (Service Unavailable)"""
    timeout_retry_settings: NotRequired[OutputClickHouseTimeoutRetrySettingsTypedDict]
    response_honor_retry_after_header: NotRequired[bool]
    r"""Honor any Retry-After header that specifies a delay (in seconds) no longer than 180 seconds after the retry request. @{product} limits the delay to 180 seconds, even if the Retry-After header specifies a longer delay. When enabled, takes precedence over user-configured retry options. When disabled, all Retry-After headers are ignored."""
    dump_format_errors_to_disk: NotRequired[bool]
    r"""Log the most recent event that fails to match the table schema"""
    on_backpressure: NotRequired[OutputClickHouseBackpressureBehavior]
    r"""How to handle events when all receivers are exerting backpressure"""
    description: NotRequired[str]
    username: NotRequired[str]
    password: NotRequired[str]
    token: NotRequired[str]
    r"""Bearer token to include in the authorization header"""
    credentials_secret: NotRequired[str]
    r"""Select or create a secret that references your credentials"""
    text_secret: NotRequired[str]
    r"""Select or create a stored text secret"""
    login_url: NotRequired[str]
    r"""URL for OAuth"""
    secret_param_name: NotRequired[str]
    r"""Secret parameter name to pass in request body"""
    secret: NotRequired[str]
    r"""Secret parameter value to pass in request body"""
    token_attribute_name: NotRequired[str]
    r"""Name of the auth token attribute in the OAuth response. Can be top-level (e.g., 'token'); or nested, using a period (e.g., 'data.token')."""
    auth_header_expr: NotRequired[str]
    r"""JavaScript expression to compute the Authorization header value to pass in requests. The value `${token}` is used to reference the token obtained from authentication, e.g.: `Bearer ${token}`."""
    token_timeout_secs: NotRequired[float]
    r"""How often the OAuth token should be refreshed."""
    oauth_params: NotRequired[List[OutputClickHouseOauthParamTypedDict]]
    r"""Additional parameters to send in the OAuth login request. @{product} will combine the secret with these parameters, and will send the URL-encoded result in a POST request to the endpoint specified in the 'Login URL'. We'll automatically add the content-type header 'application/x-www-form-urlencoded' when sending this request."""
    oauth_headers: NotRequired[List[OutputClickHouseOauthHeaderTypedDict]]
    r"""Additional headers to send in the OAuth login request. @{product} will automatically add the content-type header 'application/x-www-form-urlencoded' when sending this request."""
    sql_username: NotRequired[str]
    r"""Username for certificate authentication"""
    wait_for_async_inserts: NotRequired[bool]
    r"""Cribl will wait for confirmation that data has been fully inserted into the ClickHouse database before proceeding. Disabling this option can increase throughput, but Cribl won’t be able to verify data has been completely inserted."""
    exclude_mapping_fields: NotRequired[List[str]]
    r"""Fields to exclude from sending to ClickHouse"""
    describe_table: NotRequired[str]
    r"""Retrieves the table schema from ClickHouse and populates the Column Mapping table"""
    column_mappings: NotRequired[List[ColumnMappingTypedDict]]
    pq_max_file_size: NotRequired[str]
    r"""The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.)"""
    pq_max_size: NotRequired[str]
    r"""The maximum disk space that the queue can consume (as an average per Worker Process) before queueing stops. Enter a numeral with units of KB, MB, etc."""
    pq_path: NotRequired[str]
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>."""
    pq_compress: NotRequired[OutputClickHouseCompression]
    r"""Codec to use to compress the persisted data"""
    pq_on_backpressure: NotRequired[OutputClickHouseQueueFullBehavior]
    r"""How to handle events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""
    pq_mode: NotRequired[OutputClickHouseMode]
    r"""In Error mode, PQ writes events to the filesystem if the Destination is unavailable. In Backpressure mode, PQ writes events to the filesystem when it detects backpressure from the Destination. In Always On mode, PQ always writes events to the filesystem."""
    pq_controls: NotRequired[OutputClickHousePqControlsTypedDict]


class OutputClickHouse(BaseModel):
    url: str
    r"""URL of the ClickHouse instance. Example: http://localhost:8123/"""

    database: str

    table_name: Annotated[str, pydantic.Field(alias="tableName")]
    r"""Name of the ClickHouse table where data will be inserted. Name can contain letters (A-Z, a-z), numbers (0-9), and the character \"_\", and must start with either a letter or the character \"_\"."""

    id: Optional[str] = None
    r"""Unique ID for this output"""

    type: Annotated[
        Optional[OutputClickHouseType], PlainValidator(validate_open_enum(False))
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

    auth_type: Annotated[
        Annotated[
            Optional[OutputClickHouseAuthenticationType],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="authType"),
    ] = OutputClickHouseAuthenticationType.NONE

    format_: Annotated[
        Annotated[
            Optional[OutputClickHouseFormat], PlainValidator(validate_open_enum(False))
        ],
        pydantic.Field(alias="format"),
    ] = OutputClickHouseFormat.JSON_COMPACT_EACH_ROW_WITH_NAMES
    r"""Data format to use when sending data to ClickHouse. Defaults to JSON Compact."""

    mapping_type: Annotated[
        Annotated[Optional[MappingType], PlainValidator(validate_open_enum(False))],
        pydantic.Field(alias="mappingType"),
    ] = MappingType.AUTOMATIC
    r"""How event fields are mapped to ClickHouse columns."""

    async_inserts: Annotated[Optional[bool], pydantic.Field(alias="asyncInserts")] = (
        False
    )
    r"""Collect data into batches for later processing. Disable to write to a ClickHouse table immediately."""

    tls: Optional[OutputClickHouseTLSSettingsClientSide] = None

    concurrency: Optional[float] = 5
    r"""Maximum number of ongoing requests before blocking"""

    max_payload_size_kb: Annotated[
        Optional[float], pydantic.Field(alias="maxPayloadSizeKB")
    ] = 4096
    r"""Maximum size, in KB, of the request body"""

    max_payload_events: Annotated[
        Optional[float], pydantic.Field(alias="maxPayloadEvents")
    ] = 0
    r"""Maximum number of events to include in the request body. Default is 0 (unlimited)."""

    compress: Optional[bool] = True
    r"""Compress the payload body before sending"""

    reject_unauthorized: Annotated[
        Optional[bool], pydantic.Field(alias="rejectUnauthorized")
    ] = True
    r"""Reject certificates not authorized by a CA in the CA certificate path or by another trusted CA (such as the system's).
    Enabled by default. When this setting is also present in TLS Settings (Client Side),
    that value will take precedence.
    """

    timeout_sec: Annotated[Optional[float], pydantic.Field(alias="timeoutSec")] = 30
    r"""Amount of time, in seconds, to wait for a request to complete before canceling it"""

    flush_period_sec: Annotated[
        Optional[float], pydantic.Field(alias="flushPeriodSec")
    ] = 1
    r"""Maximum time between requests. Small values could cause the payload size to be smaller than the configured Body size limit."""

    extra_http_headers: Annotated[
        Optional[List[OutputClickHouseExtraHTTPHeader]],
        pydantic.Field(alias="extraHttpHeaders"),
    ] = None
    r"""Headers to add to all events"""

    use_round_robin_dns: Annotated[
        Optional[bool], pydantic.Field(alias="useRoundRobinDns")
    ] = False
    r"""Enable round-robin DNS lookup. When a DNS server returns multiple addresses, @{product} will cycle through them in the order returned. For optimal performance, consider enabling this setting for non-load balanced destinations."""

    failed_request_logging_mode: Annotated[
        Annotated[
            Optional[OutputClickHouseFailedRequestLoggingMode],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="failedRequestLoggingMode"),
    ] = OutputClickHouseFailedRequestLoggingMode.NONE
    r"""Data to log when a request fails. All headers are redacted by default, unless listed as safe headers below."""

    safe_headers: Annotated[
        Optional[List[str]], pydantic.Field(alias="safeHeaders")
    ] = None
    r"""List of headers that are safe to log in plain text"""

    response_retry_settings: Annotated[
        Optional[List[OutputClickHouseResponseRetrySetting]],
        pydantic.Field(alias="responseRetrySettings"),
    ] = None
    r"""Automatically retry after unsuccessful response status codes, such as 429 (Too Many Requests) or 503 (Service Unavailable)"""

    timeout_retry_settings: Annotated[
        Optional[OutputClickHouseTimeoutRetrySettings],
        pydantic.Field(alias="timeoutRetrySettings"),
    ] = None

    response_honor_retry_after_header: Annotated[
        Optional[bool], pydantic.Field(alias="responseHonorRetryAfterHeader")
    ] = False
    r"""Honor any Retry-After header that specifies a delay (in seconds) no longer than 180 seconds after the retry request. @{product} limits the delay to 180 seconds, even if the Retry-After header specifies a longer delay. When enabled, takes precedence over user-configured retry options. When disabled, all Retry-After headers are ignored."""

    dump_format_errors_to_disk: Annotated[
        Optional[bool], pydantic.Field(alias="dumpFormatErrorsToDisk")
    ] = False
    r"""Log the most recent event that fails to match the table schema"""

    on_backpressure: Annotated[
        Annotated[
            Optional[OutputClickHouseBackpressureBehavior],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="onBackpressure"),
    ] = OutputClickHouseBackpressureBehavior.BLOCK
    r"""How to handle events when all receivers are exerting backpressure"""

    description: Optional[str] = None

    username: Optional[str] = None

    password: Optional[str] = None

    token: Optional[str] = None
    r"""Bearer token to include in the authorization header"""

    credentials_secret: Annotated[
        Optional[str], pydantic.Field(alias="credentialsSecret")
    ] = None
    r"""Select or create a secret that references your credentials"""

    text_secret: Annotated[Optional[str], pydantic.Field(alias="textSecret")] = None
    r"""Select or create a stored text secret"""

    login_url: Annotated[Optional[str], pydantic.Field(alias="loginUrl")] = None
    r"""URL for OAuth"""

    secret_param_name: Annotated[
        Optional[str], pydantic.Field(alias="secretParamName")
    ] = None
    r"""Secret parameter name to pass in request body"""

    secret: Optional[str] = None
    r"""Secret parameter value to pass in request body"""

    token_attribute_name: Annotated[
        Optional[str], pydantic.Field(alias="tokenAttributeName")
    ] = None
    r"""Name of the auth token attribute in the OAuth response. Can be top-level (e.g., 'token'); or nested, using a period (e.g., 'data.token')."""

    auth_header_expr: Annotated[
        Optional[str], pydantic.Field(alias="authHeaderExpr")
    ] = "`Bearer ${token}`"
    r"""JavaScript expression to compute the Authorization header value to pass in requests. The value `${token}` is used to reference the token obtained from authentication, e.g.: `Bearer ${token}`."""

    token_timeout_secs: Annotated[
        Optional[float], pydantic.Field(alias="tokenTimeoutSecs")
    ] = 3600
    r"""How often the OAuth token should be refreshed."""

    oauth_params: Annotated[
        Optional[List[OutputClickHouseOauthParam]], pydantic.Field(alias="oauthParams")
    ] = None
    r"""Additional parameters to send in the OAuth login request. @{product} will combine the secret with these parameters, and will send the URL-encoded result in a POST request to the endpoint specified in the 'Login URL'. We'll automatically add the content-type header 'application/x-www-form-urlencoded' when sending this request."""

    oauth_headers: Annotated[
        Optional[List[OutputClickHouseOauthHeader]],
        pydantic.Field(alias="oauthHeaders"),
    ] = None
    r"""Additional headers to send in the OAuth login request. @{product} will automatically add the content-type header 'application/x-www-form-urlencoded' when sending this request."""

    sql_username: Annotated[Optional[str], pydantic.Field(alias="sqlUsername")] = None
    r"""Username for certificate authentication"""

    wait_for_async_inserts: Annotated[
        Optional[bool], pydantic.Field(alias="waitForAsyncInserts")
    ] = True
    r"""Cribl will wait for confirmation that data has been fully inserted into the ClickHouse database before proceeding. Disabling this option can increase throughput, but Cribl won’t be able to verify data has been completely inserted."""

    exclude_mapping_fields: Annotated[
        Optional[List[str]], pydantic.Field(alias="excludeMappingFields")
    ] = None
    r"""Fields to exclude from sending to ClickHouse"""

    describe_table: Annotated[Optional[str], pydantic.Field(alias="describeTable")] = (
        None
    )
    r"""Retrieves the table schema from ClickHouse and populates the Column Mapping table"""

    column_mappings: Annotated[
        Optional[List[ColumnMapping]], pydantic.Field(alias="columnMappings")
    ] = None

    pq_max_file_size: Annotated[
        Optional[str], pydantic.Field(alias="pqMaxFileSize")
    ] = "1 MB"
    r"""The maximum size to store in each queue file before closing and optionally compressing (KB, MB, etc.)"""

    pq_max_size: Annotated[Optional[str], pydantic.Field(alias="pqMaxSize")] = "5GB"
    r"""The maximum disk space that the queue can consume (as an average per Worker Process) before queueing stops. Enter a numeral with units of KB, MB, etc."""

    pq_path: Annotated[Optional[str], pydantic.Field(alias="pqPath")] = (
        "$CRIBL_HOME/state/queues"
    )
    r"""The location for the persistent queue files. To this field's value, the system will append: /<worker-id>/<output-id>."""

    pq_compress: Annotated[
        Annotated[
            Optional[OutputClickHouseCompression],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="pqCompress"),
    ] = OutputClickHouseCompression.NONE
    r"""Codec to use to compress the persisted data"""

    pq_on_backpressure: Annotated[
        Annotated[
            Optional[OutputClickHouseQueueFullBehavior],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="pqOnBackpressure"),
    ] = OutputClickHouseQueueFullBehavior.BLOCK
    r"""How to handle events when the queue is exerting backpressure (full capacity or low disk). 'Block' is the same behavior as non-PQ blocking. 'Drop new data' throws away incoming data, while leaving the contents of the PQ unchanged."""

    pq_mode: Annotated[
        Annotated[
            Optional[OutputClickHouseMode], PlainValidator(validate_open_enum(False))
        ],
        pydantic.Field(alias="pqMode"),
    ] = OutputClickHouseMode.ERROR
    r"""In Error mode, PQ writes events to the filesystem if the Destination is unavailable. In Backpressure mode, PQ writes events to the filesystem when it detects backpressure from the Destination. In Always On mode, PQ always writes events to the filesystem."""

    pq_controls: Annotated[
        Optional[OutputClickHousePqControls], pydantic.Field(alias="pqControls")
    ] = None
