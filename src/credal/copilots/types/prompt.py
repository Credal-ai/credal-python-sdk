import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class Prompt(UniversalBaseModel):
    """
    Represents a copilot's system prompt configuration.

    The backend requires the prompt to be an object with at least a ``text`` field
    and an ``organizationPromptAdditionEnabled`` flag.  For convenience the SDK also
    accepts a plain string in :class:`Configuration` – it is automatically wrapped
    into a ``Prompt(text=<string>)`` before the request is sent.
    """

    text: str = pydantic.Field()
    """The system prompt text for the copilot."""

    organization_prompt_addition_enabled: typing_extensions.Annotated[
        bool, FieldMetadata(alias="organizationPromptAdditionEnabled")
    ] = pydantic.Field(alias="organizationPromptAdditionEnabled", default=False)
    """
    Whether the organization-wide prompt addition is appended to this
    copilot's prompt.  Defaults to ``False``.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
