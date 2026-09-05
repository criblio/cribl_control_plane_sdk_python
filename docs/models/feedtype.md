# FeedType

Proofpoint on Demand feed to ingest.

## Example Usage

```python
from cribl_control_plane.models import FeedType

value = FeedType.MESSAGE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `MESSAGE` | message   |
| `MAILLOG` | maillog   |
| `AUDIT`   | audit     |