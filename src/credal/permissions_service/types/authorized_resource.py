# This file was auto-generated by Fern from our API Definition.

import typing
import uuid

import pydantic
import typing_extensions
from ...common.types.external_resource_id import ExternalResourceId
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class AuthorizedResource(UniversalBaseModel):
    credal_id: typing_extensions.Annotated[uuid.UUID, FieldMetadata(alias="credalId")]
    external_id: typing_extensions.Annotated[ExternalResourceId, FieldMetadata(alias="externalId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
