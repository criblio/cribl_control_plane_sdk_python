"""
On-Prem Authentication Example

This example demonstrates how to configure authentication for an on-prem 
Cribl instance using username and password credentials.

1. Create an SDK client with username and password credentials using the 
bearer_auth security scheme.
2. Automatically handle token exchange and refresh using a callback function.
3. Validate the connection by checking the server health status and listing 
all git branches.

Prerequisites: Replace the placeholder values for ONPREM_SERVER_URL 
ONPREM_USERNAME, and ONPREM_PASSWORD with your server URL and credentials. 
Your credentials are sensitive information and should be kept private. 

NOTE: This example is for on-prem deployments only. It does not require .env 
file configuration.
"""

import asyncio
import base64
import json
from datetime import datetime, timedelta, timezone

from cribl_control_plane import CriblControlPlane
from cribl_control_plane.models import Security

# On-prem configuration: Replace the placeholder values
ONPREM_SERVER_URL = "http://localhost:9000"  # Replace with your server URL
ONPREM_USERNAME = "admin"  # Replace with your username
ONPREM_PASSWORD = "admin"  # Replace with your password

BASE_URL = f"{ONPREM_SERVER_URL}/api/v1"

# Token cache
_cached_token = None
_token_expires_at = None


def _get_jwt_exp(token: str) -> datetime:
    payload_b64 = token.split(".")[1]
    padding = "=" * (-len(payload_b64) % 4)
    payload = json.loads(base64.urlsafe_b64decode(payload_b64 + padding).decode("utf-8"))
    exp = payload.get("exp")
    if exp is None:
        raise ValueError("Token missing 'exp' field")
    return datetime.fromtimestamp(exp, tz=timezone.utc)


async def main():
    # Create client for retrieving Bearer token
    client = CriblControlPlane(server_url=BASE_URL)

    def callback() -> Security:
        global _cached_token, _token_expires_at

        # Check cache
        now = datetime.now(timezone.utc)
        if _cached_token and _token_expires_at and (now + timedelta(seconds=3)) < _token_expires_at:
            return Security(bearer_auth=_cached_token)

        # Retrieve Bearer token initially and refresh automatically when it expires
        response = client.auth.tokens.get(
            username=ONPREM_USERNAME, password=ONPREM_PASSWORD
        )
        token = response.token
        _token_expires_at = _get_jwt_exp(token)
        _cached_token = token
        return Security(bearer_auth=token)

    # Create authenticated SDK client
    client = CriblControlPlane(server_url=BASE_URL, security=callback)
    print(f"✅ Authenticated SDK client created for on-prem server")

    # Validate connection and list all git branches
    response = await client.versions.branches.list_async()
    branches = "\n\t".join([branch.id for branch in (response.items or [])])
    print(f"✅ Client works! Your list of branches:\n\t{branches}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        status_code = getattr(error, "status_code", None)
        if status_code == 401:
            print("⚠️ Authentication failed! Check your USERNAME and PASSWORD.")
        elif status_code == 429:
            print("⚠️ Uh oh, you've reached the rate limit! Try again in a few seconds.")
        else:
            print(f"❌ Something went wrong: {error}")
