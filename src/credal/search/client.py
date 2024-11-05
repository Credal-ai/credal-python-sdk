# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
import uuid
from .types.single_field_filter import SingleFieldFilter
from .types.document_collection_search_options import DocumentCollectionSearchOptions
from ..core.request_options import RequestOptions
from .types.search_document_collection_response import SearchDocumentCollectionResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SearchClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def search_document_collection(
        self,
        *,
        collection_id: uuid.UUID,
        search_query: str,
        user_email: str,
        structured_query_filters: typing.Optional[typing.Sequence[SingleFieldFilter]] = OMIT,
        search_options: typing.Optional[DocumentCollectionSearchOptions] = OMIT,
        metadata_filter_expression: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchDocumentCollectionResponse:
        """
        Search across all documents in a document collection using the document metadata and contents.

        Parameters
        ----------
        collection_id : uuid.UUID

        search_query : str

        user_email : str
            The email of the user making the search request for permissions reduction.


        structured_query_filters : typing.Optional[typing.Sequence[SingleFieldFilter]]
            The structured query filters to apply to the search query.


        search_options : typing.Optional[DocumentCollectionSearchOptions]

        metadata_filter_expression : typing.Optional[str]
            Legacy metadata filter expression to apply to the search query. Use structuredQueryFilters instead.


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchDocumentCollectionResponse

        Examples
        --------
        import uuid

        from credal import CredalApi
        from credal.search import DocumentCollectionSearchOptions, SingleFieldFilter

        client = CredalApi(
            api_key="YOUR_API_KEY",
        )
        client.search.search_document_collection(
            collection_id=uuid.UUID(
                "82e4b12a-6990-45d4-8ebd-85c00e030c24",
            ),
            search_query="ABC Corp",
            structured_query_filters=[
                SingleFieldFilter(
                    field="status",
                    operator="==",
                    value="Open",
                )
            ],
            user_email="jack@credal.ai",
            search_options=DocumentCollectionSearchOptions(
                max_chunks=10,
                merge_contents=True,
                threshold=0.8,
                enable_smart_filtering=True,
                enable_query_extraction=True,
                enable_reranking=True,
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/search/searchDocumentCollection",
            method="POST",
            json={
                "collectionId": collection_id,
                "searchQuery": search_query,
                "userEmail": user_email,
                "structuredQueryFilters": convert_and_respect_annotation_metadata(
                    object_=structured_query_filters, annotation=typing.Sequence[SingleFieldFilter], direction="write"
                ),
                "searchOptions": convert_and_respect_annotation_metadata(
                    object_=search_options, annotation=DocumentCollectionSearchOptions, direction="write"
                ),
                "metadataFilterExpression": metadata_filter_expression,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SearchDocumentCollectionResponse,
                    parse_obj_as(
                        type_=SearchDocumentCollectionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSearchClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def search_document_collection(
        self,
        *,
        collection_id: uuid.UUID,
        search_query: str,
        user_email: str,
        structured_query_filters: typing.Optional[typing.Sequence[SingleFieldFilter]] = OMIT,
        search_options: typing.Optional[DocumentCollectionSearchOptions] = OMIT,
        metadata_filter_expression: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchDocumentCollectionResponse:
        """
        Search across all documents in a document collection using the document metadata and contents.

        Parameters
        ----------
        collection_id : uuid.UUID

        search_query : str

        user_email : str
            The email of the user making the search request for permissions reduction.


        structured_query_filters : typing.Optional[typing.Sequence[SingleFieldFilter]]
            The structured query filters to apply to the search query.


        search_options : typing.Optional[DocumentCollectionSearchOptions]

        metadata_filter_expression : typing.Optional[str]
            Legacy metadata filter expression to apply to the search query. Use structuredQueryFilters instead.


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchDocumentCollectionResponse

        Examples
        --------
        import asyncio
        import uuid

        from credal import AsyncCredalApi
        from credal.search import DocumentCollectionSearchOptions, SingleFieldFilter

        client = AsyncCredalApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.search.search_document_collection(
                collection_id=uuid.UUID(
                    "82e4b12a-6990-45d4-8ebd-85c00e030c24",
                ),
                search_query="ABC Corp",
                structured_query_filters=[
                    SingleFieldFilter(
                        field="status",
                        operator="==",
                        value="Open",
                    )
                ],
                user_email="jack@credal.ai",
                search_options=DocumentCollectionSearchOptions(
                    max_chunks=10,
                    merge_contents=True,
                    threshold=0.8,
                    enable_smart_filtering=True,
                    enable_query_extraction=True,
                    enable_reranking=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/search/searchDocumentCollection",
            method="POST",
            json={
                "collectionId": collection_id,
                "searchQuery": search_query,
                "userEmail": user_email,
                "structuredQueryFilters": convert_and_respect_annotation_metadata(
                    object_=structured_query_filters, annotation=typing.Sequence[SingleFieldFilter], direction="write"
                ),
                "searchOptions": convert_and_respect_annotation_metadata(
                    object_=search_options, annotation=DocumentCollectionSearchOptions, direction="write"
                ),
                "metadataFilterExpression": metadata_filter_expression,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    SearchDocumentCollectionResponse,
                    parse_obj_as(
                        type_=SearchDocumentCollectionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
