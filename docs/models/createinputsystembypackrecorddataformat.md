# CreateInputSystemByPackRecordDataFormat

Format of data inside the Kinesis Stream records. Gzip compression is automatically detected.

## Example Usage

```python
from cribl_control_plane.models import CreateInputSystemByPackRecordDataFormat

value = CreateInputSystemByPackRecordDataFormat.CRIBL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `CRIBL`      | cribl        |
| `NDJSON`     | ndjson       |
| `CLOUDWATCH` | cloudwatch   |
| `LINE`       | line         |