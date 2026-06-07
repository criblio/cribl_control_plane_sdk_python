"""
Configure Resources

- Creates a new Worker Group in Cribl Stream.
- Creates several resources in the new Worker Group:
   - Syslog Source to receive data on port 9021.
   - S3 Destination to store processed data.
   - Pipeline that filters events and keeps only data in the eventSource and
     eventID fields.
- Updates the Routing table with a Route that sends matching events from the
  Source through the Pipeline to the Destination.
- Commits and deploys the configuration to make it active.

NOTE: This example is for Cribl.Cloud deployments only.

Required to use this example:
- A Cribl.Cloud Enterprise account.
- A Cribl.Cloud Organization ID and Workspace name, which are used to build the 
base URL for the SDK calls.
- The Client ID and Secret for a Cribl.Cloud API Credential, which are used to 
authenticate the SDK calls. To get the Client ID and Secret, follow 
https://docs.cribl.io/cribl-as-code/sdks-auth/#sdks-auth-cloud. The Client ID 
and Secret are sensitive information and should be kept private.
- AWS S3 values for AWS_API_KEY, AWS_SECRET_KEY, AWS_BUCKET_NAME, and 
AWS_REGION, which are used to configure an S3 Destination.
"""

# Import block
# Imports asyncio so that the file can run an asynchronous control plane 
# sequence for authentication and creating and deploying resources.
#
# Imports CriblControlPlane as the API client from the cribl_control_plane 
# SDK package.
#
# Imports model classes that provide the Python types used for Cribl Stream 
# resource configurations and API payloads in this file from the 
# cribl_control_plane.models subpackage.
#
# Imports List (for list annotations) and the cast static typing helper from 
# the standard library typing module.
import asyncio

from cribl_control_plane import CriblControlPlane

from cribl_control_plane.models import (
    ProductsCore,
    CreateInputInputSyslogSyslog2,
    CreateInputInputSyslogType2,
    CreateOutputOutputS3,
    CreateOutputTypeS3,
    CompressionOptions2,
    CompressionLevelOptions,
    Pipeline,
    RouteConf,
    RouteConfInput,
    PipelineConf,
    ConfInput,
    PipelineFunctionEval,
    PipelineFunctionEvalID,
    PipelineFunctionConf,
    FunctionConfSchemaEval,
    TLSSettingsServerSideType,
    Security,
    SchemeClientOauth,
    ConfigGroupCloud,
    CloudProvider,
    EstimatedIngestRateOptionsConfigGroup
)
from typing import List, cast

# User-supplied parameters block
# Values to use in the URL block, Authentication block, and resource 
# configuration blocks. Replace the placeholder values before executing 
# this file.
ORG_ID = "your-org-id"  # Replace with the Organization ID
WORKSPACE_NAME = "your-workspace-name"  # Replace with the Workspace name
WORKER_GROUP_ID = "your-group"  # Replace with the ID to use for the new Worker Group

CLIENT_ID = "your-client-id"  # Replace with the Client ID for the API Credential
CLIENT_SECRET = "your-client-secret"  # Replace with the Client Secret for the API Credential

SYSLOG_PORT = 9021  # Replace with a different port number if desired

AWS_API_KEY = "your-aws-access-key-id"  # Replace with your AWS Access Key ID
AWS_SECRET_KEY = "your-aws-secret-access-key"  # Replace with your AWS Secret Access Key
AWS_BUCKET_NAME = "your-s3-bucket-name"  # Replace with your S3 bucket name
AWS_REGION = "your-s3-bucket-region"  # Replace with your S3 bucket region, such as us-east-2

# URL block
# Builds the base URL and Worker Group-specific URL to use for the 
# API requests that this file makes using the ORG_ID, WORKSPACE_NAME, 
# and WORKER_GROUP_ID provided in the user-supplied parameters block.
base_url = f"https://{WORKSPACE_NAME}-{ORG_ID}.cribl.cloud/api/v1"
group_url = f"{base_url}/m/{WORKER_GROUP_ID}"

# Source definition block
# The configuration for a new Syslog Source that listens on all interfaces, 
# has TLS disabled, and uses the SYSLOG_PORT value provided in the 
# user-supplied parameters block. This configuration is passed to the API 
# in the Create Source block.
syslog_source = CreateInputInputSyslogSyslog2(
    id="in-syslog-9021",
    type=CreateInputInputSyslogType2.SYSLOG,
    host="0.0.0.0",
    tcp_port=SYSLOG_PORT,
    tls=TLSSettingsServerSideType(disabled=True),
)

# Destination definition block
# The configuration for a new S3 Destination that uses gzip + fast 
# compression, stages under /tmp/cribl_stage, and uses the AWS_BUCKET_NAME, 
# AWS_REGION, AWS_SECRET_KEY, and AWS_API_KEY from the user-supplied 
# parameters block. This configuration is passed to the API in the 
# Create Destination block. 
s3_destination = CreateOutputOutputS3(
    id="out_s3",
    type=CreateOutputTypeS3.S3,
    bucket=AWS_BUCKET_NAME,
    stage_path="/tmp/cribl_stage",
    region=AWS_REGION,
    aws_secret_key=AWS_SECRET_KEY,
    aws_api_key=AWS_API_KEY,
    compress=CompressionOptions2.GZIP,
    compression_level=CompressionLevelOptions.BEST_SPEED,
    empty_dir_cleanup_sec=300,
)

# Pipeline definition block
# The configuration for a new Pipeline with one Eval function that keeps only 
# eventSource and eventID. This configuration is passed to the API in the 
# Create Pipeline block.
pipeline = Pipeline(
    id="my_pipeline",
    conf=PipelineConf(
        async_func_timeout=1000,
        functions=cast(
            List[PipelineFunctionConf],
            [
                PipelineFunctionEval(
                    filter_="true",
                    conf=FunctionConfSchemaEval(
                        remove=["*"],
                        keep=["eventSource", "eventID"],
                    ),
                    id=PipelineFunctionEvalID.EVAL,
                    final=True,
                )
            ],
        ),
    ),
)

# Route definition block
# The configuration for a Route that matches only events from the Syslog Source and sends them through the Pipeline to the S3 Destination. Allows other Routes to run after it (final=False).
route = RouteConf(
    final=False,
    id="default",  # Routing table ID (do not change; the supported value is default)
    name="your_route",  # Replace with the name of the Route
    pipeline=pipeline.id,
    output=s3_destination.id,
    filter_=f"__inputId=='{syslog_source.id}'",
    description="This is my new Route",  # Replace with the desired description for the Route
)

# Workflow block
# The async function that contains the full automation and runs when you 
# execute this file. Authenticates using your Cribl.Cloud API Credentials, 
# creates the Worker Group and Stream resources, updates the Routing table, 
# and commits and deploys the configuration.
async def main():
    # Authentication block
    # Creates an OAuth client (SchemeClientOauth) that exchanges CLIENT_ID and 
    # CLIENT_SECRET from the user-supplied parameters block for a Bearer 
    # token and wraps the client in Security.
    # Constructs the SDK client CriblControlPlane to make authenticated API 
    # requests using the base_url from the URL block and Security, which holds 
    # the Bearer token.
    client_oauth = SchemeClientOauth(
      client_id=CLIENT_ID,
      client_secret=CLIENT_SECRET,
      token_url="https://login.cribl.cloud/oauth/token",
      audience="https://api.cribl.cloud",
    )

    security = Security(client_oauth=client_oauth)
    cribl = CriblControlPlane(server_url=base_url, security=security)

    # Create Worker Group block
    # Checks for a Worker Group with the WORKER_GROUP_ID provided in the 
    # user-supplied parameters block and exits if it already exists. 
    # Otherwise, creates the Worker Group and prints a confirmation message.
    worker_group_response = cribl.groups.get(id=WORKER_GROUP_ID, product=ProductsCore.STREAM)
    if worker_group_response.items and len(worker_group_response.items) > 0:
        print(
            f"❌ Worker Group already exists: {WORKER_GROUP_ID}. Try a different Worker Group ID."
        )
        return

    cribl.groups.create(
        product=ProductsCore.STREAM,
        id=WORKER_GROUP_ID,
        on_prem=False,
        worker_remote_access=True,
        is_fleet=False,
        is_search=False,
        name=WORKER_GROUP_ID,
        estimated_ingest_rate=EstimatedIngestRateOptionsConfigGroup.RATE12_MB_PER_SEC,
        cloud=ConfigGroupCloud(
            provider=CloudProvider.AWS,
            region="us-east-1"
        ),
    )
    print(f"✅ Worker Group created: {WORKER_GROUP_ID}")

    # Create Source block
    # Creates a Syslog Source (based on the Source definition block) in the 
    # new Worker Group and prints a confirmation message.
    cribl.sources.create(request=syslog_source, server_url=group_url)
    print(f"✅ Syslog source created: {syslog_source.id}")

    # Create Destination block
    # Creates an S3 Destination (based on the Destination definition block) 
    # in the new Worker Group and prints a confirmation message.
    cribl.destinations.create(request=s3_destination, server_url=group_url)
    print(f"✅ S3 Destination created: {s3_destination.id}")

    # Create Pipeline block
    # Creates a Pipeline (based on the Pipeline definition block) in the new 
    # Worker Group and prints a confirmation message.
    cribl.pipelines.create(id=pipeline.id, conf=ConfInput.model_validate(pipeline.conf.model_dump()), server_url=group_url)
    print(f"✅ Pipeline created: {pipeline.id}")

    # Update Routing table block
    # Fetches the current list of Routes and raises an exception if the API 
    # returns nothing or the first Routes entry has no ID. Otherwise, prepends 
    # the new Route (based on the Route definition block), saves the updated 
    # Routing table, and prints a confirmation message.
    routes_list_response = cribl.routes.list(server_url=group_url)
    if not routes_list_response.items or len(routes_list_response.items) == 0:
        raise Exception("No Routes found")

    routes = routes_list_response.items[0]
    if not routes or not routes.id:
        raise Exception("No Routes found")

    routes.routes = [route] + (routes.routes or [])
    routes_input = [
        RouteConfInput.model_validate(r.model_dump()) for r in routes.routes
    ]
    cribl.routes.update(
        id_param=routes.id, id=routes.id, routes=routes_input, server_url=group_url
    )
    print(f"✅ Route added: {route.id}")

    # Commit block
    # Records a new version of the Worker Group configuration, marks that 
    # version as effective, and captures the commit ID to use in the 
    # Deploy block. Raises an exception if the API returns no commit. 
    # Otherwise, prints a confirmation message.
    commit_response = cribl.versions.commits.create(
        message="Commit for Cribl Stream example",
        effective=True,
        files=["."],
        server_url=group_url
    )
    
    if not commit_response.items or len(commit_response.items) == 0:
        raise Exception("Failed to commit configuration changes")
    
    version = commit_response.items[0].commit
    print(f"✅ Committed configuration changes to the group: {WORKER_GROUP_ID}, commit ID: {version}")

    # Deploy block
    # Pushes the committed configuration version (using the commit ID from 
    # the Commit block) to the Cribl Stream Worker Group so that Workers load 
    # and run that version, then prints a confirmation message.
    cribl.groups.deploy(
        product=ProductsCore.STREAM,
        id=WORKER_GROUP_ID,
        version=version
    )
    print(f"✅ Worker Group changes deployed: {WORKER_GROUP_ID}")

# Script entry block
# Starts the async function main() with the standard library helper 
# asyncio.run and prints an error message if the run fails. Runs only when you 
# execute this file as the main script (not when another file imports it).
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        print(f"❌ Something went wrong: {error}")

