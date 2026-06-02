# CollectorType

## Example Usage

```python
from cribl_control_plane.models import CollectorType

value = CollectorType.AZURE_BLOB

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                   | Value                  |
| ---------------------- | ---------------------- |
| `AZURE_BLOB`           | azure_blob             |
| `CRIBL_LAKE`           | cribl_lake             |
| `DATABASE`             | database               |
| `FILESYSTEM`           | filesystem             |
| `GOOGLE_CLOUD_STORAGE` | google_cloud_storage   |
| `HEALTH_CHECK`         | health_check           |
| `REST`                 | rest                   |
| `S3`                   | s3                     |
| `SCRIPT`               | script                 |
| `SPLUNK`               | splunk                 |