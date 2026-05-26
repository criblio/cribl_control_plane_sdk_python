# OutputSyslogFacility

Default value for message facility. Will be overwritten by value of __facility if set. Defaults to user.

## Example Usage

```python
from cribl_control_plane.models import OutputSyslogFacility

value = OutputSyslogFacility.KERN

# Open enum: unrecognized values are captured as UnrecognizedInt
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `KERN`         | 0              |
| `USER`         | 1              |
| `MAIL`         | 2              |
| `DAEMON`       | 3              |
| `AUTH`         | 4              |
| `SYSLOG`       | 5              |
| `LPR`          | 6              |
| `NEWS`         | 7              |
| `UUCP`         | 8              |
| `CRON`         | 9              |
| `AUTHPRIV`     | 10             |
| `FTP`          | 11             |
| `NTP`          | 12             |
| `SECURITY`     | 13             |
| `CONSOLE`      | 14             |
| `SOLARIS_CRON` | 15             |
| `LOCAL0`       | 16             |
| `LOCAL1`       | 17             |
| `LOCAL2`       | 18             |
| `LOCAL3`       | 19             |
| `LOCAL4`       | 20             |
| `LOCAL5`       | 21             |