# CreateOutputSystemByPackAISIEMEndpointPath

Endpoint to send events to. Use /services/collector/event for structured JSON payloads with standard HEC top-level fields. Use /services/collector/raw for unstructured log lines (plain text).

## Example Usage

```python
from cribl_control_plane.models import CreateOutputSystemByPackAISIEMEndpointPath

value = CreateOutputSystemByPackAISIEMEndpointPath.ROOT_SERVICES_COLLECTOR_EVENT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                            | Value                           |
| ------------------------------- | ------------------------------- |
| `ROOT_SERVICES_COLLECTOR_EVENT` | /services/collector/event       |
| `ROOT_SERVICES_COLLECTOR_RAW`   | /services/collector/raw         |