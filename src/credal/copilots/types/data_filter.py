# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ...core.serialization import FieldMetadata
from .collection_filtered_data import CollectionFilteredData
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class DataFilter(UniversalBaseModel):
    semantic_search_terms: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="semanticSearchTerms")]
    web_search_term: typing_extensions.Annotated[typing.List[str], FieldMetadata(alias="webSearchTerm")]
    filtered_data_sources_per_collection: typing_extensions.Annotated[
        typing.List[CollectionFilteredData], FieldMetadata(alias="filteredDataSourcesPerCollection")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
