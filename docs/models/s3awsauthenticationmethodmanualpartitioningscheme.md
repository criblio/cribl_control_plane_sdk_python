# S3AwsAuthenticationMethodManualPartitioningScheme

Partitioning scheme used for this dataset. Using a known scheme like DDSS enables more efficient data reading and retrieval.

## Example Usage

```python
from cribl_control_plane.models import S3AwsAuthenticationMethodManualPartitioningScheme

value = S3AwsAuthenticationMethodManualPartitioningScheme.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `NONE` | none   |
| `DDSS` | ddss   |