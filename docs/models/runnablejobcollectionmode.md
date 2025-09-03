# RunnableJobCollectionMode

Job run mode. Preview will either return up to N matching results, or will run until capture time T is reached. Discovery will gather the list of files to turn into streaming tasks, without running the data collection job. Full Run will run the collection job.


## Values

| Name      | Value     |
| --------- | --------- |
| `LIST`    | list      |
| `PREVIEW` | preview   |
| `RUN`     | run       |