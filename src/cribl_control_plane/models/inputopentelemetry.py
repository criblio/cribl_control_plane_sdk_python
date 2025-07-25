"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from cribl_control_plane import utils
from cribl_control_plane.types import BaseModel
from cribl_control_plane.utils import validate_open_enum
from enum import Enum
import pydantic
from pydantic.functional_validators import PlainValidator
from typing import Any, List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class InputOpenTelemetryType(str, Enum, metaclass=utils.OpenEnumMeta):
    OPEN_TELEMETRY = "open_telemetry"


class InputOpenTelemetryConnectionTypedDict(TypedDict):
    output: str
    pipeline: NotRequired[str]


class InputOpenTelemetryConnection(BaseModel):
    output: str

    pipeline: Optional[str] = None


class InputOpenTelemetryMode(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""With Smart mode, PQ will write events to the filesystem only when it detects backpressure from the processing engine. With Always On mode, PQ will always write events directly to the queue before forwarding them to the processing engine."""

    SMART = "smart"
    ALWAYS = "always"


class InputOpenTelemetryCompression(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Codec to use to compress the persisted data"""

    NONE = "none"
    GZIP = "gzip"


class InputOpenTelemetryPqTypedDict(TypedDict):
    mode: NotRequired[InputOpenTelemetryMode]
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
    compress: NotRequired[InputOpenTelemetryCompression]
    r"""Codec to use to compress the persisted data"""


class InputOpenTelemetryPq(BaseModel):
    mode: Annotated[
        Optional[InputOpenTelemetryMode], PlainValidator(validate_open_enum(False))
    ] = InputOpenTelemetryMode.ALWAYS
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
        Optional[InputOpenTelemetryCompression],
        PlainValidator(validate_open_enum(False)),
    ] = InputOpenTelemetryCompression.NONE
    r"""Codec to use to compress the persisted data"""


class InputOpenTelemetryMinimumTLSVersion(str, Enum, metaclass=utils.OpenEnumMeta):
    TL_SV1 = "TLSv1"
    TL_SV1_1 = "TLSv1.1"
    TL_SV1_2 = "TLSv1.2"
    TL_SV1_3 = "TLSv1.3"


class InputOpenTelemetryMaximumTLSVersion(str, Enum, metaclass=utils.OpenEnumMeta):
    TL_SV1 = "TLSv1"
    TL_SV1_1 = "TLSv1.1"
    TL_SV1_2 = "TLSv1.2"
    TL_SV1_3 = "TLSv1.3"


class InputOpenTelemetryTLSSettingsServerSideTypedDict(TypedDict):
    disabled: NotRequired[bool]
    certificate_name: NotRequired[str]
    r"""The name of the predefined certificate"""
    priv_key_path: NotRequired[str]
    r"""Path on server containing the private key to use. PEM format. Can reference $ENV_VARS."""
    passphrase: NotRequired[str]
    r"""Passphrase to use to decrypt private key"""
    cert_path: NotRequired[str]
    r"""Path on server containing certificates to use. PEM format. Can reference $ENV_VARS."""
    ca_path: NotRequired[str]
    r"""Path on server containing CA certificates to use. PEM format. Can reference $ENV_VARS."""
    request_cert: NotRequired[bool]
    r"""Require clients to present their certificates. Used to perform client authentication using SSL certs."""
    reject_unauthorized: NotRequired[Any]
    common_name_regex: NotRequired[Any]
    min_version: NotRequired[InputOpenTelemetryMinimumTLSVersion]
    max_version: NotRequired[InputOpenTelemetryMaximumTLSVersion]


class InputOpenTelemetryTLSSettingsServerSide(BaseModel):
    disabled: Optional[bool] = True

    certificate_name: Annotated[
        Optional[str], pydantic.Field(alias="certificateName")
    ] = None
    r"""The name of the predefined certificate"""

    priv_key_path: Annotated[Optional[str], pydantic.Field(alias="privKeyPath")] = None
    r"""Path on server containing the private key to use. PEM format. Can reference $ENV_VARS."""

    passphrase: Optional[str] = None
    r"""Passphrase to use to decrypt private key"""

    cert_path: Annotated[Optional[str], pydantic.Field(alias="certPath")] = None
    r"""Path on server containing certificates to use. PEM format. Can reference $ENV_VARS."""

    ca_path: Annotated[Optional[str], pydantic.Field(alias="caPath")] = None
    r"""Path on server containing CA certificates to use. PEM format. Can reference $ENV_VARS."""

    request_cert: Annotated[Optional[bool], pydantic.Field(alias="requestCert")] = False
    r"""Require clients to present their certificates. Used to perform client authentication using SSL certs."""

    reject_unauthorized: Annotated[
        Optional[Any], pydantic.Field(alias="rejectUnauthorized")
    ] = None

    common_name_regex: Annotated[
        Optional[Any], pydantic.Field(alias="commonNameRegex")
    ] = None

    min_version: Annotated[
        Annotated[
            Optional[InputOpenTelemetryMinimumTLSVersion],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="minVersion"),
    ] = None

    max_version: Annotated[
        Annotated[
            Optional[InputOpenTelemetryMaximumTLSVersion],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="maxVersion"),
    ] = None


class InputOpenTelemetryProtocol(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""Select whether to leverage gRPC or HTTP for OpenTelemetry"""

    GRPC = "grpc"
    HTTP = "http"


class InputOpenTelemetryOTLPVersion(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""The version of OTLP Protobuf definitions to use when interpreting received data"""

    ZERO_DOT_10_DOT_0 = "0.10.0"
    ONE_DOT_3_DOT_1 = "1.3.1"


class InputOpenTelemetryAuthenticationType(str, Enum, metaclass=utils.OpenEnumMeta):
    r"""OpenTelemetry authentication type"""

    NONE = "none"
    BASIC = "basic"
    CREDENTIALS_SECRET = "credentialsSecret"
    TOKEN = "token"
    TEXT_SECRET = "textSecret"
    OAUTH = "oauth"


class InputOpenTelemetryMetadatumTypedDict(TypedDict):
    name: str
    value: str
    r"""JavaScript expression to compute field's value, enclosed in quotes or backticks. (Can evaluate to a constant.)"""


class InputOpenTelemetryMetadatum(BaseModel):
    name: str

    value: str
    r"""JavaScript expression to compute field's value, enclosed in quotes or backticks. (Can evaluate to a constant.)"""


class InputOpenTelemetryOauthParamTypedDict(TypedDict):
    name: str
    r"""OAuth parameter name"""
    value: str
    r"""OAuth parameter value"""


class InputOpenTelemetryOauthParam(BaseModel):
    name: str
    r"""OAuth parameter name"""

    value: str
    r"""OAuth parameter value"""


class InputOpenTelemetryOauthHeaderTypedDict(TypedDict):
    name: str
    r"""OAuth header name"""
    value: str
    r"""OAuth header value"""


class InputOpenTelemetryOauthHeader(BaseModel):
    name: str
    r"""OAuth header name"""

    value: str
    r"""OAuth header value"""


class InputOpenTelemetryTypedDict(TypedDict):
    id: NotRequired[str]
    r"""Unique ID for this input"""
    type: NotRequired[InputOpenTelemetryType]
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
    connections: NotRequired[List[InputOpenTelemetryConnectionTypedDict]]
    r"""Direct connections to Destinations, and optionally via a Pipeline or a Pack"""
    pq: NotRequired[InputOpenTelemetryPqTypedDict]
    host: NotRequired[str]
    r"""Address to bind on. Defaults to 0.0.0.0 (all addresses)."""
    port: NotRequired[float]
    r"""Port to listen on"""
    tls: NotRequired[InputOpenTelemetryTLSSettingsServerSideTypedDict]
    max_active_req: NotRequired[float]
    r"""Maximum number of active requests allowed per Worker Process. Set to 0 for unlimited. Caution: Increasing the limit above the default value, or setting it to unlimited, may degrade performance and reduce throughput."""
    max_requests_per_socket: NotRequired[int]
    r"""Maximum number of requests per socket before @{product} instructs the client to close the connection. Default is 0 (unlimited)."""
    enable_proxy_header: NotRequired[Any]
    capture_headers: NotRequired[Any]
    activity_log_sample_rate: NotRequired[Any]
    request_timeout: NotRequired[float]
    r"""How long to wait for an incoming request to complete before aborting it. Use 0 to disable."""
    socket_timeout: NotRequired[float]
    r"""How long @{product} should wait before assuming that an inactive socket has timed out. To wait forever, set to 0."""
    keep_alive_timeout: NotRequired[float]
    r"""After the last response is sent, @{product} will wait this long for additional data before closing the socket connection. Minimum 1 sec.; maximum 600 sec. (10 min.)."""
    enable_health_check: NotRequired[bool]
    r"""Enable to expose the /cribl_health endpoint, which returns 200 OK when this Source is healthy"""
    ip_allowlist_regex: NotRequired[str]
    r"""Messages from matched IP addresses will be processed, unless also matched by the denylist."""
    ip_denylist_regex: NotRequired[str]
    r"""Messages from matched IP addresses will be ignored. This takes precedence over the allowlist."""
    protocol: NotRequired[InputOpenTelemetryProtocol]
    r"""Select whether to leverage gRPC or HTTP for OpenTelemetry"""
    extract_spans: NotRequired[bool]
    r"""Enable to extract each incoming span to a separate event"""
    extract_metrics: NotRequired[bool]
    r"""Enable to extract each incoming Gauge or IntGauge metric to multiple events, one per data point"""
    otlp_version: NotRequired[InputOpenTelemetryOTLPVersion]
    r"""The version of OTLP Protobuf definitions to use when interpreting received data"""
    auth_type: NotRequired[InputOpenTelemetryAuthenticationType]
    r"""OpenTelemetry authentication type"""
    metadata: NotRequired[List[InputOpenTelemetryMetadatumTypedDict]]
    r"""Fields to add to events from this input"""
    max_active_cxn: NotRequired[float]
    r"""Maximum number of active connections allowed per Worker Process. Use 0 for unlimited."""
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
    oauth_params: NotRequired[List[InputOpenTelemetryOauthParamTypedDict]]
    r"""Additional parameters to send in the OAuth login request. @{product} will combine the secret with these parameters, and will send the URL-encoded result in a POST request to the endpoint specified in the 'Login URL'. We'll automatically add the content-type header 'application/x-www-form-urlencoded' when sending this request."""
    oauth_headers: NotRequired[List[InputOpenTelemetryOauthHeaderTypedDict]]
    r"""Additional headers to send in the OAuth login request. @{product} will automatically add the content-type header 'application/x-www-form-urlencoded' when sending this request."""
    extract_logs: NotRequired[bool]
    r"""Enable to extract each incoming log record to a separate event"""


class InputOpenTelemetry(BaseModel):
    id: Optional[str] = None
    r"""Unique ID for this input"""

    type: Annotated[
        Optional[InputOpenTelemetryType], PlainValidator(validate_open_enum(False))
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

    connections: Optional[List[InputOpenTelemetryConnection]] = None
    r"""Direct connections to Destinations, and optionally via a Pipeline or a Pack"""

    pq: Optional[InputOpenTelemetryPq] = None

    host: Optional[str] = "0.0.0.0"
    r"""Address to bind on. Defaults to 0.0.0.0 (all addresses)."""

    port: Optional[float] = 4317
    r"""Port to listen on"""

    tls: Optional[InputOpenTelemetryTLSSettingsServerSide] = None

    max_active_req: Annotated[Optional[float], pydantic.Field(alias="maxActiveReq")] = (
        256
    )
    r"""Maximum number of active requests allowed per Worker Process. Set to 0 for unlimited. Caution: Increasing the limit above the default value, or setting it to unlimited, may degrade performance and reduce throughput."""

    max_requests_per_socket: Annotated[
        Optional[int], pydantic.Field(alias="maxRequestsPerSocket")
    ] = 0
    r"""Maximum number of requests per socket before @{product} instructs the client to close the connection. Default is 0 (unlimited)."""

    enable_proxy_header: Annotated[
        Optional[Any], pydantic.Field(alias="enableProxyHeader")
    ] = None

    capture_headers: Annotated[
        Optional[Any], pydantic.Field(alias="captureHeaders")
    ] = None

    activity_log_sample_rate: Annotated[
        Optional[Any], pydantic.Field(alias="activityLogSampleRate")
    ] = None

    request_timeout: Annotated[
        Optional[float], pydantic.Field(alias="requestTimeout")
    ] = 0
    r"""How long to wait for an incoming request to complete before aborting it. Use 0 to disable."""

    socket_timeout: Annotated[
        Optional[float], pydantic.Field(alias="socketTimeout")
    ] = 0
    r"""How long @{product} should wait before assuming that an inactive socket has timed out. To wait forever, set to 0."""

    keep_alive_timeout: Annotated[
        Optional[float], pydantic.Field(alias="keepAliveTimeout")
    ] = 15
    r"""After the last response is sent, @{product} will wait this long for additional data before closing the socket connection. Minimum 1 sec.; maximum 600 sec. (10 min.)."""

    enable_health_check: Annotated[
        Optional[bool], pydantic.Field(alias="enableHealthCheck")
    ] = False
    r"""Enable to expose the /cribl_health endpoint, which returns 200 OK when this Source is healthy"""

    ip_allowlist_regex: Annotated[
        Optional[str], pydantic.Field(alias="ipAllowlistRegex")
    ] = "/.*/"
    r"""Messages from matched IP addresses will be processed, unless also matched by the denylist."""

    ip_denylist_regex: Annotated[
        Optional[str], pydantic.Field(alias="ipDenylistRegex")
    ] = "/^$/"
    r"""Messages from matched IP addresses will be ignored. This takes precedence over the allowlist."""

    protocol: Annotated[
        Optional[InputOpenTelemetryProtocol], PlainValidator(validate_open_enum(False))
    ] = InputOpenTelemetryProtocol.GRPC
    r"""Select whether to leverage gRPC or HTTP for OpenTelemetry"""

    extract_spans: Annotated[Optional[bool], pydantic.Field(alias="extractSpans")] = (
        False
    )
    r"""Enable to extract each incoming span to a separate event"""

    extract_metrics: Annotated[
        Optional[bool], pydantic.Field(alias="extractMetrics")
    ] = False
    r"""Enable to extract each incoming Gauge or IntGauge metric to multiple events, one per data point"""

    otlp_version: Annotated[
        Annotated[
            Optional[InputOpenTelemetryOTLPVersion],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="otlpVersion"),
    ] = InputOpenTelemetryOTLPVersion.ZERO_DOT_10_DOT_0
    r"""The version of OTLP Protobuf definitions to use when interpreting received data"""

    auth_type: Annotated[
        Annotated[
            Optional[InputOpenTelemetryAuthenticationType],
            PlainValidator(validate_open_enum(False)),
        ],
        pydantic.Field(alias="authType"),
    ] = InputOpenTelemetryAuthenticationType.NONE
    r"""OpenTelemetry authentication type"""

    metadata: Optional[List[InputOpenTelemetryMetadatum]] = None
    r"""Fields to add to events from this input"""

    max_active_cxn: Annotated[Optional[float], pydantic.Field(alias="maxActiveCxn")] = (
        1000
    )
    r"""Maximum number of active connections allowed per Worker Process. Use 0 for unlimited."""

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
        Optional[List[InputOpenTelemetryOauthParam]],
        pydantic.Field(alias="oauthParams"),
    ] = None
    r"""Additional parameters to send in the OAuth login request. @{product} will combine the secret with these parameters, and will send the URL-encoded result in a POST request to the endpoint specified in the 'Login URL'. We'll automatically add the content-type header 'application/x-www-form-urlencoded' when sending this request."""

    oauth_headers: Annotated[
        Optional[List[InputOpenTelemetryOauthHeader]],
        pydantic.Field(alias="oauthHeaders"),
    ] = None
    r"""Additional headers to send in the OAuth login request. @{product} will automatically add the content-type header 'application/x-www-form-urlencoded' when sending this request."""

    extract_logs: Annotated[Optional[bool], pydantic.Field(alias="extractLogs")] = False
    r"""Enable to extract each incoming log record to a separate event"""
