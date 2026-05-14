# OutputWebhookFormat2

How to format events before sending out

## Example Usage

```python
from cribl_control_plane.models import OutputWebhookFormat2

value = OutputWebhookFormat2.NDJSON

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `NDJSON`     | ndjson       |
| `JSON_ARRAY` | json_array   |
| `CUSTOM`     | custom       |
| `ADVANCED`   | advanced     |