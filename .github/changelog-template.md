<!--
Template for Cribl SDKs for the control and management planes.
Usage:
- Omit any section that has no entries for this release.
- Text inside angle brackets < > represents example changelog notes
  and varying details like version numbers and dates. Replace each < > 
  and its contents with the relevant information for the SDK version 
  that the changelog describes.
-->

# Changelog: <Language> SDK for the <Control or Management> Plane
Version <X.Y.Z> - <YYYY-MM-DD>

This version of the SDK is generated for Cribl version <X.Y.Z>.

## New Features

<!--
Enhancements that add new functionality, such as new methods 
or new parameters in existing methods.
-->

- <Added the following methods for creating and managing Collectors>:
   - <`collectors.create`>
   - <`collectors.list`>
   - <`collectors.delete`>
   - <`collectors.get`>
   - <`collectors.update`>
- <Added the following methods for retrieving and clearing persistent queues for Destinations>:
   - <`destinations.pq.clear`>
   - <`destinations.pq.get`>
- <Added the `retry_connection_errors` body parameter to the `destinations.samples.create` method to specify whether to retry a request after a connection error.>
- <Added the `limit` and `offset` query parameters to the `lake_datasets.list` method to support results pagination.>

## Improvements

<!--
Refinements to existing functionality that improve 
performance, usability, security, or efficiency.
-->

- <Optimized the caching strategy to reduce redundant API calls.>
- <Added details and fix suggestions to error messages in the XYZ class.>
- <Updated XYZ dependency to version X.Y.Z.>

## Bug Fixes

<!--
Changes that address problems with functionality, 
reliability, security, or performance.
-->

- <Fixed a logic error that could produce incorrect output and unexpected behavior when using the `groups.acl.get` method.>
- <Special characters in query parameters are now properly URL-encoded, which prevents certain failed requests.>
- <Fixed a problem that prevented proper memory release during data processing, which was causing increased memory usage over time.>

## Breaking Changes

<!--
Changes that make this version of the SDK incompatible 
with previous versions and require users to update their code.
-->

- <Removed the following methods>:
   - <`functions.create`>
   - <`nodes.create`>
- <Rate limit is now 60 requests per minute instead of 100. Adjust your request logic to avoid throttling.>
- <Modified the output structure of the `nodes.list` method to include nested objects.>
- <Changed to version X.Y.Z of the ABC library, which may require you to adjust error handling and response parsing logic.>

## Deprecated Features

<!--
Features that will be removed but are still available 
to give users time to transition to the specified alternative.
-->

- <Deprecated methods>:
   - <`system.get` (use `project.get` instead)>
- <Deprecated the legacy login credentials authentication method. Use the OAuth 2.0 method instead.>
- <Deprecated support for Python 2. Upgrade to Python 3.x.>

## Known Issues

<!--
Problems that can affect the user experience with the SDK 
that are not yet resolved, along with any recommended mitigations.
-->

- <You may experience unexpected behavior when using the SDK with Python 3.5. Upgrade to Python 3.6 or later for proper functionality.>
- <The DatabaseConnection object may not properly close connections in some cases, leading to resource exhaustion. Implement explicit connection closing until a fix is available.>
- <Performance may degrade when processing datasets larger than 100,000 rows. Consider chunking data to improve handling as needed.>
