# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class DocumentCollectionSearchOptions(UniversalBaseModel):
    max_chunks: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="maxChunks")] = pydantic.Field(
        default=None
    )
    """
    The maximum number of chunks to return. Defaults to 10.
    """

    merge_contents: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="mergeContents")] = (
        pydantic.Field(default=None)
    )
    """
    Whether to merge the chunks for a document and just return one result per document. Defaults to false.
    """

    threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    The similarity threshold between 0 and 1 for the search results. A higher number leads to fewer but more relevant results. 
    Defaults to 0.45.
    """

    enable_smart_filtering: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="enableSmartFiltering")
    ] = pydantic.Field(default=None)
    """
    Whether to automatically filter the search results based on the user query and available metadata on the collection. Defaults to false.
    """

    enable_query_extraction: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="enableQueryExtraction")
    ] = pydantic.Field(default=None)
    """
    / Whether to extract search terms from the user query and use them for semantic search. Defaults to false.
    """

    enable_reranking: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="enableReranking")] = (
        pydantic.Field(default=None)
    )
    """
    Whether to rerank the search results after the initial semantic search query. Defaults to false.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
