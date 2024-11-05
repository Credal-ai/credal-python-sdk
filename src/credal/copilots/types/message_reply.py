# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .policy_trigger import PolicyTrigger
import typing_extensions
import uuid
from ...core.serialization import FieldMetadata
from .response_chunk import ResponseChunk
from .inserted_audit_log import InsertedAuditLog
from .referenced_source import ReferencedSource
from .web_search_result import WebSearchResult
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class MessageReply(UniversalBaseModel):
    policy_triggers: typing.List[PolicyTrigger]
    conversation_id: typing_extensions.Annotated[uuid.UUID, FieldMetadata(alias="conversationId")]
    response: ResponseChunk
    warnings: typing.List[str]
    inserted_audit_log: InsertedAuditLog
    referenced_sources: typing_extensions.Annotated[
        typing.List[ReferencedSource], FieldMetadata(alias="referencedSources")
    ]
    sources_in_data_context: typing_extensions.Annotated[
        typing.List[ReferencedSource], FieldMetadata(alias="sourcesInDataContext")
    ]
    web_search_results: typing_extensions.Annotated[
        typing.List[WebSearchResult], FieldMetadata(alias="webSearchResults")
    ]
    message_id: typing_extensions.Annotated[uuid.UUID, FieldMetadata(alias="messageId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
