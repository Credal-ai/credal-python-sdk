# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.query_encoder import encode_query
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from .types.user_metadata_patch import UserMetadataPatch

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def metadata(
        self, *, request: typing.Sequence[UserMetadataPatch], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Bulk patch metadata for users

        Parameters
        ----------
        request : typing.Sequence[UserMetadataPatch]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from credal import UserMetadataPatch
        from credal.client import CredalApi

        client = CredalApi(
            api_key="YOUR_API_KEY",
        )
        client.users.metadata(
            request=[
                UserMetadataPatch(
                    metadata={"State": "NY", "Job Role": "CEO"},
                    user_email="ravin@credal.ai",
                ),
                UserMetadataPatch(
                    metadata={"State": "NY", "Department": "Engineering"},
                    user_email="jack@credal.ai",
                ),
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="PATCH",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v0/users/metadata"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def metadata(
        self, *, request: typing.Sequence[UserMetadataPatch], request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Bulk patch metadata for users

        Parameters
        ----------
        request : typing.Sequence[UserMetadataPatch]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from credal import UserMetadataPatch
        from credal.client import AsyncCredalApi

        client = AsyncCredalApi(
            api_key="YOUR_API_KEY",
        )
        await client.users.metadata(
            request=[
                UserMetadataPatch(
                    metadata={"State": "NY", "Job Role": "CEO"},
                    user_email="ravin@credal.ai",
                ),
                UserMetadataPatch(
                    metadata={"State": "NY", "Department": "Engineering"},
                    user_email="jack@credal.ai",
                ),
            ],
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="PATCH",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "v0/users/metadata"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
