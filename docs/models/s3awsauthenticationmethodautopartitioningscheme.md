# S3AwsAuthenticationMethodAutoPartitioningScheme

Partitioning scheme used for this dataset. Using a known scheme like DDSS enables more efficient data reading and retrieval.

## Example Usage

```python
from cribl_control_plane.models import S3AwsAuthenticationMethodAutoPartitioningScheme

value = S3AwsAuthenticationMethodAutoPartitioningScheme.NONE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `NONE` | none   |
| `DDSS` | ddss   |