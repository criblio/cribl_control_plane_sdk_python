# HealthCheckAuthenticationOauthSecretHealthCheckDiscoveryDiscoverTypeHTTPDiscoverMethodPostDiscoverType

Defines how task discovery will be performed. Use None to skip the discovery. Use HTTP Request to make a REST call to discover tasks. Use Item List to enumerate items for collect to retrieve. Use JSON Response to manually define discover tasks as a JSON array of objects. Each entry returned by the discover operation will result in a collect task.

## Example Usage

```python
from cribl_control_plane.models import HealthCheckAuthenticationOauthSecretHealthCheckDiscoveryDiscoverTypeHTTPDiscoverMethodPostDiscoverType

value = HealthCheckAuthenticationOauthSecretHealthCheckDiscoveryDiscoverTypeHTTPDiscoverMethodPostDiscoverType.HTTP

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `HTTP` | http   |
| `JSON` | json   |
| `LIST` | list   |
| `NONE` | none   |