"""
Authentication Helper Module

This helper module handles authentication for all SDK examples, supporting both
cloud (OAuth2) and on-premises (username/password) deployments. It automatically
detects the deployment type, loads environment variables, validates credentials,
and provides authenticated SDK client instances.

Used by: Example files that that can run on cloud or on-premises
"""

import asyncio
import os
from pathlib import Path
from typing import Optional, Dict, Any, Union
from dataclasses import dataclass

from dotenv import load_dotenv
from cribl_control_plane import CriblControlPlane
from cribl_control_plane.models import Security, SchemeClientOauth


async def sleep(ms: float) -> None:
    """Sleep for the given number of milliseconds."""
    await asyncio.sleep(ms / 1000)


DOMAIN = "cribl.cloud"


@dataclass
class OnpremConfiguration:
    server_url: str
    username: str
    password: str


@dataclass 
class CloudConfiguration:
    org_id: str
    client_id: str
    client_secret: str
    workspace_name: str


def get_configuration_cloud() -> CloudConfiguration:
    """
    Validates and returns configuration for cloud deployment

    Returns:
        CloudConfiguration: Configuration object with required credentials
    """
    org_id = os.getenv("ORG_ID")
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    workspace_name = os.getenv("WORKSPACE_NAME")

    if not org_id:
        raise ValueError("ORG_ID is required for cloud deployment")
    if not client_id:
        raise ValueError("CLIENT_ID is required for cloud deployment")
    if not client_secret:
        raise ValueError("CLIENT_SECRET is required for cloud deployment")
    if not workspace_name:
        raise ValueError("WORKSPACE_NAME is required for cloud deployment")

    return CloudConfiguration(
        org_id=org_id,
        client_id=client_id,
        client_secret=client_secret,
        workspace_name=workspace_name
    )

def get_configuration_onprem() -> OnpremConfiguration:
    """
    Validates and returns configuration for on-premises deployment
    
    Returns:
        OnpremConfiguration: Configuration object with required credentials
    """
    server_url = os.getenv("ONPREM_SERVER_URL")
    username = os.getenv("ONPREM_USERNAME") 
    password = os.getenv("ONPREM_PASSWORD")
    
    if not server_url:
        raise ValueError("ONPREM_SERVER_URL is required for on-premises deployment")
    if not username:
        raise ValueError("ONPREM_USERNAME is required for on-premises deployment")
    if not password:
        raise ValueError("ONPREM_PASSWORD is required for on-premises deployment")
        
    return OnpremConfiguration(
        server_url=server_url,
        username=username,
        password=password
    )

# Resolve .env path
env_path = Path.cwd() / ".env"
if not env_path.exists():
    raise FileNotFoundError(f"No .env file found in current directory: {env_path}")

# Load .env file
load_dotenv(env_path, override=False)  # System env vars take precedence

is_onprem = os.getenv("DEPLOYMENT_ENV") == "onprem"

# Load configuration and determine base URL based on deployment type
onprem_config: Optional[OnpremConfiguration] = None
cloud_config: Optional[CloudConfiguration] = None

if is_onprem:
    onprem_config = get_configuration_onprem()
    base_url = f"{onprem_config.server_url}/api/v1"
else:
    cloud_config = get_configuration_cloud()
    base_url = f"https://{cloud_config.workspace_name}-{cloud_config.org_id}.{DOMAIN}/api/v1"


async def create_cribl_client() -> CriblControlPlane:
    """
    Factory function that creates an authenticated Cribl Control Plane client
    Automatically detects deployment type and uses appropriate authentication method

    Returns:
        CriblControlPlane: Authenticated SDK client instance
    """
    cribl_auth: Union[AuthOnprem, AuthCloud]
    
    if is_onprem and onprem_config:
        cribl_auth = AuthOnprem(onprem_config)
    elif cloud_config:
        cribl_auth = AuthCloud(cloud_config)
    else:
        raise RuntimeError("No valid configuration found")

    return await cribl_auth.get_client()


class ICriblAuth:
    """Common interface for authentication providers"""
    
    async def get_client(self) -> CriblControlPlane:
        """Returns an authenticated CriblControlPlane client instance"""
        raise NotImplementedError


class AuthOnprem(ICriblAuth):
    """
    On-premises authentication provider using username/password credentials
    Handles token retrieval and client creation with retry logic for rate limits
    """

    def __init__(self, config: OnpremConfiguration):
        self.username = config.username
        self.password = config.password
        self.base_url = f"{config.server_url}/api/v1"
        self.client: Optional[CriblControlPlane] = None
        self.attempts = 0

    async def get_client(self) -> CriblControlPlane:
        if self.client:
            return self.client
            
        token_getter = CriblControlPlane(server_url=self.base_url)

        try:
            response = await token_getter.auth.tokens.get_async(
                username=self.username,
                password=self.password
            )
            token = response.token

            security = Security(bearer_auth=token)
            self.client = CriblControlPlane(
                server_url=self.base_url,
                security=security
            )
            return self.client

        except Exception as error:
            # Check if it's a rate limit error (status code 429)
            status_code = getattr(error, 'status_code', None)
            if status_code == 429 and self.attempts < 10:
                print("⚠️ Rate limit exceeded, retrying...")
                self.attempts += 1
                await sleep(1000)
                return await self.get_client()

            if status_code == 401:
                raise Exception(f"Failed to authenticate with on-premises server: {error}")

            raise Exception(f"Failed to authenticate with on-premises server: {error}")


class AuthCloud(ICriblAuth):
    """
    Cloud authentication provider using OAuth2 client credentials flow
    Automatically handles token exchange and refresh
    """

    def __init__(self, config: CloudConfiguration):
        self.client_id = config.client_id
        self.client_secret = config.client_secret
        self.base_url = f"https://{config.workspace_name}-{config.org_id}.{DOMAIN}/api/v1"
        self.token_url = f"https://login.{DOMAIN}/oauth/token"
        self.audience = f"https://api.{DOMAIN}"
        self.client: Optional[CriblControlPlane] = None
        self.attempts = 0

    def get_search_group_url(self) -> str:
        """Get the server URL for the default search group"""
        return f"{self.base_url}/m/default_search"

    async def get_client(self) -> CriblControlPlane:
        if self.client:
            return self.client

        try:
            client_oauth = SchemeClientOauth(
                client_id=self.client_id,
                client_secret=self.client_secret,
                token_url=self.token_url,
                audience=self.audience
            )

            security = Security(client_oauth=client_oauth)
            self.client = CriblControlPlane(
                server_url=self.base_url,
                security=security
            )
            return self.client

        except Exception as error:
            # Check if it's a rate limit error (status code 429)
            status_code = getattr(error, 'status_code', None)
            if status_code == 429 and self.attempts < 10:
                print("⚠️ Rate limit exceeded, retrying...")
                self.attempts += 1
                await sleep(1000)
                return await self.get_client()

            if status_code == 401:
                raise Exception(f"Failed to authenticate with cloud server: {error}")

            raise Exception(f"Failed to authenticate with cloud server: {error}; attempts: {self.attempts}")
