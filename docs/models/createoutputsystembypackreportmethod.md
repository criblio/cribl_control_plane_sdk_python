# CreateOutputSystemByPackReportMethod

Target of the ingestion status reporting. Defaults to Queue.

## Example Usage

```python
from cribl_control_plane.models import CreateOutputSystemByPackReportMethod

value = CreateOutputSystemByPackReportMethod.QUEUE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name              | Value             |
| ----------------- | ----------------- |
| `QUEUE`           | queue             |
| `TABLE`           | table             |
| `QUEUE_AND_TABLE` | queueAndTable     |