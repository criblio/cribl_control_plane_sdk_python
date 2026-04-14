# CreateInputSystemByPackCheckpointStore

The backing store used to persist consumer checkpoints. Select "None" to disable checkpointing (consumers will restart from the configured start position).

## Example Usage

```python
from cribl_control_plane.models import CreateInputSystemByPackCheckpointStore

value = CreateInputSystemByPackCheckpointStore.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `NONE`       | none         |
| `AZURE_BLOB` | azureBlob    |