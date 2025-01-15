# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import uuid
from ...core.serialization import FieldMetadata
import typing
from .search_result_chunk import SearchResultChunk
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class DocumentCollectionSearchResult(UniversalBaseModel):
    document_id: typing_extensions.Annotated[uuid.UUID, FieldMetadata(alias="documentId")]
    document_name: typing_extensions.Annotated[str, FieldMetadata(alias="documentName")]
    document_url: typing_extensions.Annotated[str, FieldMetadata(alias="documentUrl")]
    document_external_id: typing_extensions.Annotated[str, FieldMetadata(alias="documentExternalId")]
    document_metadata: typing_extensions.Annotated[typing.Dict[str, str], FieldMetadata(alias="documentMetadata")]
    chunks: typing.List[SearchResultChunk]
    merged_contents: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="mergedContents")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
