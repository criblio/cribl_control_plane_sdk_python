import hashlib
import os
import httpx
import time
from .types import (
    SDKInitHook,
    BeforeRequestContext,
    BeforeRequestHook,
    AfterErrorContext,
    AfterErrorHook,
    HookContext,
)
from typing import Any, Dict, List, Tuple, Union, Optional
from urllib.parse import urlparse, urljoin
from cribl_control_plane.httpclient import HttpClient
from cribl_control_plane.sdkconfiguration import SDKConfiguration


class Credentials:
    client_id: str
    client_secret: str
    token_url: str
    audience: str

    def __init__(self, client_id: str, client_secret: str, token_url: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.token_url = token_url
        self.audience = os.getenv("CRIBLCONTROLPLANE_AUDIENCE", "https://api.cribl.cloud") # Set default audience here


class Session:
    credentials: Credentials
    token: str
    scopes: Optional[List[str]] = None
    expires_at: Optional[int] = None

    def __init__(
        self,
        credentials: Credentials,
        token: str,
        scopes: Optional[List[str]] = None,
        expires_at: Optional[int] = None,
    ):
        self.credentials = credentials
        self.token = token
        self.scopes = scopes
        self.expires_at = expires_at


class ClientCredentialsHook(SDKInitHook, BeforeRequestHook, AfterErrorHook):
    client: HttpClient
    sessions: Dict[str, Session] = {}

    def sdk_init(self, config: SDKConfiguration) -> SDKConfiguration:
        if config.client is None:
            raise Exception("Client is required")

        self.client = config.client
        return config

    def before_request(
        self, hook_ctx: BeforeRequestContext, request: httpx.Request
    ) -> httpx.Request:
        if hook_ctx.oauth2_scopes is None:
            # OAuth2 not in use
            return request

        credentials = self.get_credentials(hook_ctx)
        if credentials is None:
            return request

        session_key = self.get_session_key(
            credentials.client_id, credentials.client_secret
        )

        if (
            session_key not in self.sessions
            or not self.has_required_scopes(
                self.sessions[session_key].scopes, hook_ctx.oauth2_scopes
            )
            or self.has_token_expired(self.sessions[session_key].expires_at)
        ):
            sess = self.do_token_request(
                hook_ctx,
                credentials,
                self.get_scopes(hook_ctx.oauth2_scopes, self.sessions.get(session_key)),
            )

            self.sessions[session_key] = sess

        request.headers["Authorization"] = f"Bearer {self.sessions[session_key].token}"

        return request

    def after_error(
        self,
        hook_ctx: AfterErrorContext,
        response: Optional[httpx.Response],
        error: Optional[Exception],
    ) -> Union[Tuple[Optional[httpx.Response], Optional[Exception]], Exception]:
        if hook_ctx.oauth2_scopes is None:
            # OAuth2 not in use
            return (response, error)

        # We don't want to refresh the token if the error is not related to the token
        if error is not None:
            return (response, error)

        credentials = self.get_credentials(hook_ctx)
        if credentials is None:
            return (response, error)

        if response is not None and response.status_code == 401:
            session_key = self.get_session_key(
                credentials.client_id, credentials.client_secret
            )

            if session_key in self.sessions:
                del self.sessions[session_key]

        return (response, error)

    def get_credentials(self, hook_ctx: HookContext) -> Optional[Credentials]:
        source = hook_ctx.security_source

        if source is None:
            return None

        security = source() if callable(source) else source

        return self.get_credentials_global(security)

    def get_credentials_global(self, security: Any) -> Optional[Credentials]:
        if security is None or security.client_oauth is None:
            return None

        return Credentials(
            client_id=security.client_oauth.client_id,
            client_secret=security.client_oauth.client_secret,
            token_url=security.client_oauth.token_url,
        )

    def do_token_request(
        self,
        hook_ctx: HookContext,
        credentials: Credentials,
        scopes: Optional[List[str]],
    ) -> Session:
        payload = {
            "grant_type": "client_credentials",
            "client_id": credentials.client_id,
            "client_secret": credentials.client_secret,
        }

        if credentials.audience is not None:
            payload["audience"] = credentials.audience

        if scopes is not None and len(scopes) > 0:
            payload["scope"] = " ".join(scopes)

        token_url = credentials.token_url
        if not bool(urlparse(credentials.token_url).netloc):
            token_url = urljoin(hook_ctx.base_url, credentials.token_url)
        response = self.client.send(
            self.client.build_request(method="POST", url=token_url, data=payload)
        )

        if response.status_code < 200 or response.status_code >= 300:
            raise Exception(
                f"Unexpected status code {response.status_code} from token endpoint"
            )

        response_data = response.json()

        if response_data.get("token_type") != "Bearer":
            raise Exception("Unexpected token type from token endpoint")

        expires_at = None
        if "expires_in" in response_data:
            expires_at = int(time.time()) + response_data.get("expires_in")

        return Session(
            credentials=credentials,
            token=response_data.get("access_token"),
            scopes=scopes,
            expires_at=expires_at,
        )

    def get_session_key(self, client_id: str, client_secret: str) -> str:
        return hashlib.md5(f"{client_id}:{client_secret}".encode()).hexdigest()

    def has_required_scopes(
        self, scopes: Optional[List[str]], required_scopes: List[str]
    ) -> bool:
        if scopes is None:
            return False

        return all(scope in scopes for scope in required_scopes)

    def get_scopes(
        self, required_scopes: List[str], sess: Optional[Session]
    ) -> List[str]:
        scopes = required_scopes.copy()
        if sess is not None and sess.scopes is not None:
            scopes.extend(sess.scopes)
            scopes = list(set(scopes))
        return scopes

    def has_token_expired(self, expires_at: Optional[int]) -> bool:
        return expires_at is None or time.time() + 60 >= expires_at
