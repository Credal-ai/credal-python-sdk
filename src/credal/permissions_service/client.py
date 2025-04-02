# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
from ..common.types.resource_identifier import ResourceIdentifier
from ..core.request_options import RequestOptions
from .types.check_resource_authorization_response import CheckResourceAuthorizationResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from .types.check_bulk_resources_authorization_response import CheckBulkResourcesAuthorizationResponse
from ..common.types.resource_type import ResourceType
from .types.authorized_resource_list_page import AuthorizedResourceListPage
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class PermissionsServiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def check_resource_authorization_for_user(
        self,
        *,
        resource_identifier: ResourceIdentifier,
        user_email: str,
        disable_cache: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckResourceAuthorizationResponse:
        """
        Admin endpoint to check whether the specified user is authorized to read the specified resource.

        Parameters
        ----------
        resource_identifier : ResourceIdentifier
            The resource identifier for which you want to check authorization.

        user_email : str
            The user email to check authorization for.

        disable_cache : typing.Optional[bool]
            If specified, Credal will bypass the permissions cache and check current permissions for this resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckResourceAuthorizationResponse

        Examples
        --------
        from credal import CredalApi
        from credal.common import ResourceIdentifier_ExternalResourceId

        client = CredalApi(
            api_key="YOUR_API_KEY",
        )
        client.permissions_service.check_resource_authorization_for_user(
            resource_identifier=ResourceIdentifier_ExternalResourceId(
                external_resource_id="170NrBm0Do7gdzvr54UvyslPVWkQFOA0lgNycFmdZJQr",
                resource_type="GOOGLE_DRIVE_ITEM",
            ),
            user_email="john.smith@foo.com",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/permissions/checkResourceAuthorizationForUser",
            method="POST",
            json={
                "resourceIdentifier": convert_and_respect_annotation_metadata(
                    object_=resource_identifier, annotation=ResourceIdentifier, direction="write"
                ),
                "userEmail": user_email,
                "disableCache": disable_cache,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CheckResourceAuthorizationResponse,
                    parse_obj_as(
                        type_=CheckResourceAuthorizationResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def check_bulk_resources_authorization_for_user(
        self,
        *,
        resource_identifiers: typing.Sequence[ResourceIdentifier],
        user_email: str,
        disable_cache: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckBulkResourcesAuthorizationResponse:
        """
        Admin endpoint to check whether the specified user is authorized to read the specified set of resources.

        Parameters
        ----------
        resource_identifiers : typing.Sequence[ResourceIdentifier]
            The set of resource identifier for which you want to check authorization. Currently limited to 20 resources.

        user_email : str
            The user email to check authorization for.

        disable_cache : typing.Optional[bool]
            If specified, Credal will bypass the permissions cache and check current permissions for all resources specified.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckBulkResourcesAuthorizationResponse

        Examples
        --------
        from credal import CredalApi
        from credal.common import (
            ResourceIdentifier_ExternalResourceId,
            ResourceIdentifier_Url,
        )

        client = CredalApi(
            api_key="YOUR_API_KEY",
        )
        client.permissions_service.check_bulk_resources_authorization_for_user(
            resource_identifiers=[
                ResourceIdentifier_Url(
                    url="https://docs.google.com/document/d/170NrBm0Do7gdzvr54UvyslPVWkQFOA0lgNycFmdZJQr/edit",
                ),
                ResourceIdentifier_ExternalResourceId(
                    external_resource_id="sfsdfvr54UvyslPVWkQFOA0dfsdfsdflgNycFmdZJQr",
                    resource_type="ZENDESK_TICKET",
                ),
            ],
            user_email="john.smith@foo.com",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/permissions/checkBulkResourcesAuthorizationForUser",
            method="POST",
            json={
                "resourceIdentifiers": convert_and_respect_annotation_metadata(
                    object_=resource_identifiers, annotation=typing.Sequence[ResourceIdentifier], direction="write"
                ),
                "userEmail": user_email,
                "disableCache": disable_cache,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CheckBulkResourcesAuthorizationResponse,
                    parse_obj_as(
                        type_=CheckBulkResourcesAuthorizationResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_cached_authorized_resources_for_user(
        self,
        *,
        user_email: str,
        resource_type: typing.Optional[ResourceType] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorizedResourceListPage:
        """
        Admin endpoint to list all resources that the specified user is authorized to read. Note this endpoint returns cached results and may not be up-to-date. You can use the checkResourceAuthorizationForUser endpoint with disableCache set to true to get the most up-to-date results.

        Parameters
        ----------
        user_email : str
            The user email to list authorized resources for.

        resource_type : typing.Optional[ResourceType]
            The type of resource you want to list. If not specified, all resource types will be listed.

        limit : typing.Optional[int]
            The maximum number of resources to return. Defaults to 100.

        offset : typing.Optional[int]
            The offset to use for pagination. If not specified, the first page of results will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizedResourceListPage

        Examples
        --------
        from credal import CredalApi

        client = CredalApi(
            api_key="YOUR_API_KEY",
        )
        client.permissions_service.list_cached_authorized_resources_for_user(
            user_email="john.smith@foo.com",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/permissions/listCachedAuthorizedResourcesForUser",
            method="POST",
            json={
                "userEmail": user_email,
                "resourceType": resource_type,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AuthorizedResourceListPage,
                    parse_obj_as(
                        type_=AuthorizedResourceListPage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncPermissionsServiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def check_resource_authorization_for_user(
        self,
        *,
        resource_identifier: ResourceIdentifier,
        user_email: str,
        disable_cache: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckResourceAuthorizationResponse:
        """
        Admin endpoint to check whether the specified user is authorized to read the specified resource.

        Parameters
        ----------
        resource_identifier : ResourceIdentifier
            The resource identifier for which you want to check authorization.

        user_email : str
            The user email to check authorization for.

        disable_cache : typing.Optional[bool]
            If specified, Credal will bypass the permissions cache and check current permissions for this resource

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckResourceAuthorizationResponse

        Examples
        --------
        import asyncio

        from credal import AsyncCredalApi
        from credal.common import ResourceIdentifier_ExternalResourceId

        client = AsyncCredalApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.permissions_service.check_resource_authorization_for_user(
                resource_identifier=ResourceIdentifier_ExternalResourceId(
                    external_resource_id="170NrBm0Do7gdzvr54UvyslPVWkQFOA0lgNycFmdZJQr",
                    resource_type="GOOGLE_DRIVE_ITEM",
                ),
                user_email="john.smith@foo.com",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/permissions/checkResourceAuthorizationForUser",
            method="POST",
            json={
                "resourceIdentifier": convert_and_respect_annotation_metadata(
                    object_=resource_identifier, annotation=ResourceIdentifier, direction="write"
                ),
                "userEmail": user_email,
                "disableCache": disable_cache,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CheckResourceAuthorizationResponse,
                    parse_obj_as(
                        type_=CheckResourceAuthorizationResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def check_bulk_resources_authorization_for_user(
        self,
        *,
        resource_identifiers: typing.Sequence[ResourceIdentifier],
        user_email: str,
        disable_cache: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CheckBulkResourcesAuthorizationResponse:
        """
        Admin endpoint to check whether the specified user is authorized to read the specified set of resources.

        Parameters
        ----------
        resource_identifiers : typing.Sequence[ResourceIdentifier]
            The set of resource identifier for which you want to check authorization. Currently limited to 20 resources.

        user_email : str
            The user email to check authorization for.

        disable_cache : typing.Optional[bool]
            If specified, Credal will bypass the permissions cache and check current permissions for all resources specified.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckBulkResourcesAuthorizationResponse

        Examples
        --------
        import asyncio

        from credal import AsyncCredalApi
        from credal.common import (
            ResourceIdentifier_ExternalResourceId,
            ResourceIdentifier_Url,
        )

        client = AsyncCredalApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.permissions_service.check_bulk_resources_authorization_for_user(
                resource_identifiers=[
                    ResourceIdentifier_Url(
                        url="https://docs.google.com/document/d/170NrBm0Do7gdzvr54UvyslPVWkQFOA0lgNycFmdZJQr/edit",
                    ),
                    ResourceIdentifier_ExternalResourceId(
                        external_resource_id="sfsdfvr54UvyslPVWkQFOA0dfsdfsdflgNycFmdZJQr",
                        resource_type="ZENDESK_TICKET",
                    ),
                ],
                user_email="john.smith@foo.com",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/permissions/checkBulkResourcesAuthorizationForUser",
            method="POST",
            json={
                "resourceIdentifiers": convert_and_respect_annotation_metadata(
                    object_=resource_identifiers, annotation=typing.Sequence[ResourceIdentifier], direction="write"
                ),
                "userEmail": user_email,
                "disableCache": disable_cache,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    CheckBulkResourcesAuthorizationResponse,
                    parse_obj_as(
                        type_=CheckBulkResourcesAuthorizationResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_cached_authorized_resources_for_user(
        self,
        *,
        user_email: str,
        resource_type: typing.Optional[ResourceType] = OMIT,
        limit: typing.Optional[int] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AuthorizedResourceListPage:
        """
        Admin endpoint to list all resources that the specified user is authorized to read. Note this endpoint returns cached results and may not be up-to-date. You can use the checkResourceAuthorizationForUser endpoint with disableCache set to true to get the most up-to-date results.

        Parameters
        ----------
        user_email : str
            The user email to list authorized resources for.

        resource_type : typing.Optional[ResourceType]
            The type of resource you want to list. If not specified, all resource types will be listed.

        limit : typing.Optional[int]
            The maximum number of resources to return. Defaults to 100.

        offset : typing.Optional[int]
            The offset to use for pagination. If not specified, the first page of results will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuthorizedResourceListPage

        Examples
        --------
        import asyncio

        from credal import AsyncCredalApi

        client = AsyncCredalApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.permissions_service.list_cached_authorized_resources_for_user(
                user_email="john.smith@foo.com",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/permissions/listCachedAuthorizedResourcesForUser",
            method="POST",
            json={
                "userEmail": user_email,
                "resourceType": resource_type,
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    AuthorizedResourceListPage,
                    parse_obj_as(
                        type_=AuthorizedResourceListPage,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
