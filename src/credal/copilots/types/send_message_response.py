# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing
import uuid

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .inserted_audit_log import InsertedAuditLog
from .policy_trigger import PolicyTrigger
from .referenced_source import ReferencedSource
from .response_chunk import ResponseChunk


class SendMessageResponse_AiResponseResult(pydantic_v1.BaseModel):
    policy_triggers: typing.List[PolicyTrigger]
    conversation_id: uuid.UUID = pydantic_v1.Field(alias="conversationId")
    response: ResponseChunk
    warnings: typing.List[str]
    inserted_audit_log: InsertedAuditLog
    referenced_sources: typing.List[ReferencedSource] = pydantic_v1.Field(alias="referencedSources")
    sources_in_data_context: typing.List[ReferencedSource] = pydantic_v1.Field(alias="sourcesInDataContext")
    message_id: uuid.UUID = pydantic_v1.Field(alias="messageId")
    type: typing.Literal["ai_response_result"] = "ai_response_result"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


class SendMessageResponse_BlockedResult(pydantic_v1.BaseModel):
    policy_triggers: typing.List[PolicyTrigger]
    conversation_id: uuid.UUID = pydantic_v1.Field(alias="conversationId")
    blocks: typing.List[str]
    warnings: typing.List[str]
    inserted_audit_log: InsertedAuditLog
    type: typing.Literal["blocked_result"] = "blocked_result"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


SendMessageResponse = typing.Union[SendMessageResponse_AiResponseResult, SendMessageResponse_BlockedResult]
