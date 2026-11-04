# RecordDataFormat

Format of data inside the Kinesis Stream records. Gzip compression is automatically detected. Cloudwatch Logs records become one event per log event, keeping the event id, message type, log group, log stream, owner, and subscription filters; other fields are dropped.

## Example Usage

```python
from cribl_control_plane.models import RecordDataFormat

value = RecordDataFormat.CRIBL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `CRIBL`      | cribl        |
| `NDJSON`     | ndjson       |
| `CLOUDWATCH` | cloudwatch   |
| `LINE`       | line         |