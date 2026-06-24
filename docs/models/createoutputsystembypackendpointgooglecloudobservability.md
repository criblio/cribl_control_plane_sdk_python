# CreateOutputSystemByPackEndpointGoogleCloudObservability

Fixed Google Cloud Observability gRPC endpoint. All three signals share this transport; the OTLP service path determines whether the call lands on traces, metrics, or logs.

## Example Usage

```python
from cribl_control_plane.models import CreateOutputSystemByPackEndpointGoogleCloudObservability

value = CreateOutputSystemByPackEndpointGoogleCloudObservability.TELEMETRY_GOOGLEAPIS_COM_443

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                           | Value                          |
| ------------------------------ | ------------------------------ |
| `TELEMETRY_GOOGLEAPIS_COM_443` | telemetry.googleapis.com:443   |