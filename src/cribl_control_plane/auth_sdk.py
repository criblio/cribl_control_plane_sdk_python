"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .basesdk import BaseSDK
from cribl_control_plane import errors, models, utils
from cribl_control_plane._hooks import HookContext
from cribl_control_plane.types import OptionalNullable, UNSET
from cribl_control_plane.utils.unmarshal_json_response import unmarshal_json_response
from typing import Mapping, Optional


class AuthSDK(BaseSDK):
    r"""Actions related to authentication. Do not use the /auth endpoints in Cribl.Cloud deployments. Instead, follow the instructions at https://docs.cribl.io/stream/api-tutorials/#criblcloud to authenticate for Cribl.Cloud."""

    def login(
        self,
        *,
        username: str,
        password: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.AuthToken:
        r"""Log in and obtain Auth token

        This endpoint is unavailable on Cribl.Cloud. Instead, follow the instructions at https://docs.cribl.io/stream/api-tutorials/#criblcloud to get an Auth token for Cribl.Cloud.

        :param username:
        :param password:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.LoginInfo(
            username=username,
            password=password,
        )

        req = self._build_request(
            method="POST",
            path="/auth/login",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=False,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.LoginInfo
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = self.do_request(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="login",
                oauth2_scopes=[],
                security_source=None,
            ),
            request=req,
            error_status_codes=["401", "403", "429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(models.AuthToken, http_res)
        if utils.match_response(http_res, ["401", "403", "429", "4XX"], "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = utils.stream_to_text(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)

        raise errors.APIError("Unexpected response received", http_res)

    async def login_async(
        self,
        *,
        username: str,
        password: str,
        retries: OptionalNullable[utils.RetryConfig] = UNSET,
        server_url: Optional[str] = None,
        timeout_ms: Optional[int] = None,
        http_headers: Optional[Mapping[str, str]] = None,
    ) -> models.AuthToken:
        r"""Log in and obtain Auth token

        This endpoint is unavailable on Cribl.Cloud. Instead, follow the instructions at https://docs.cribl.io/stream/api-tutorials/#criblcloud to get an Auth token for Cribl.Cloud.

        :param username:
        :param password:
        :param retries: Override the default retry configuration for this method
        :param server_url: Override the default server URL for this method
        :param timeout_ms: Override the default request timeout configuration for this method in milliseconds
        :param http_headers: Additional headers to set or replace on requests.
        """
        base_url = None
        url_variables = None
        if timeout_ms is None:
            timeout_ms = self.sdk_configuration.timeout_ms

        if server_url is not None:
            base_url = server_url
        else:
            base_url = self._get_url(base_url, url_variables)

        request = models.LoginInfo(
            username=username,
            password=password,
        )

        req = self._build_request_async(
            method="POST",
            path="/auth/login",
            base_url=base_url,
            url_variables=url_variables,
            request=request,
            request_body_required=True,
            request_has_path_params=False,
            request_has_query_params=False,
            user_agent_header="user-agent",
            accept_header_value="application/json",
            http_headers=http_headers,
            get_serialized_body=lambda: utils.serialize_request_body(
                request, False, False, "json", models.LoginInfo
            ),
            timeout_ms=timeout_ms,
        )

        if retries == UNSET:
            if self.sdk_configuration.retry_config is not UNSET:
                retries = self.sdk_configuration.retry_config

        retry_config = None
        if isinstance(retries, utils.RetryConfig):
            retry_config = (retries, ["429", "500", "502", "503", "504"])

        http_res = await self.do_request_async(
            hook_ctx=HookContext(
                config=self.sdk_configuration,
                base_url=base_url or "",
                operation_id="login",
                oauth2_scopes=[],
                security_source=None,
            ),
            request=req,
            error_status_codes=["401", "403", "429", "4XX", "5XX"],
            retry_config=retry_config,
        )

        if utils.match_response(http_res, "200", "application/json"):
            return unmarshal_json_response(models.AuthToken, http_res)
        if utils.match_response(http_res, ["401", "403", "429", "4XX"], "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)
        if utils.match_response(http_res, "5XX", "*"):
            http_res_text = await utils.stream_to_text_async(http_res)
            raise errors.APIError("API error occurred", http_res, http_res_text)

        raise errors.APIError("Unexpected response received", http_res)
