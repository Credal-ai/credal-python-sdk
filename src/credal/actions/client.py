# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
import uuid
from .types.human_confirmation_channel import HumanConfirmationChannel
from ..core.request_options import RequestOptions
from .types.invoke_action_response import InvokeActionResponse
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ActionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def invoke_action(
        self,
        *,
        action_id: uuid.UUID,
        user_email: str,
        human_confirmation_channel: HumanConfirmationChannel,
        justification: str,
        audit_log_id: uuid.UUID,
        action_inputs: typing.Optional[typing.Any] = OMIT,
        require_human_confirmation: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InvokeActionResponse:
        """
        Invoke an action, asking for human confirmation if necessary

        Parameters
        ----------
        action_id : uuid.UUID

        user_email : str
            The user who we should take the action on behalf of


        human_confirmation_channel : HumanConfirmationChannel
            Where we should ask for human confirmation if necessary


        justification : str
            The justification for requesting this action.  This is likely generated by the LLM that requested the action.


        audit_log_id : uuid.UUID
            Audit log for the message that called for this action


        action_inputs : typing.Optional[typing.Any]
            The inputs needed to execute the action


        require_human_confirmation : typing.Optional[bool]
            If true, then before executing the action we will ask for a human confirmation in Slack.  If false, we may still ask for human confirmation if it's required by your organization admin.


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InvokeActionResponse

        Examples
        --------
        import uuid

        from credal import CredalApi
        from credal.actions import HumanConfirmationChannel_SlackThread

        client = CredalApi(
            api_key="YOUR_API_KEY",
        )
        client.actions.invoke_action(
            action_id=uuid.UUID(
                "2b5cf2b8-3df3-11ef-9a96-332d4470d189",
            ),
            action_inputs={
                "textToAppend": "If you need more help, please contact your direct manager."
            },
            user_email="ben@credal.ai",
            require_human_confirmation=True,
            human_confirmation_channel=HumanConfirmationChannel_SlackThread(
                channel_id="ABC123",
                thread_timestamp="123456789",
            ),
            justification="The user directly asked to update the Relocations Confluence document with this text.",
            audit_log_id=uuid.UUID(
                "3df3f2b8-3df3-11ef-9a96-332d447011ef",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/actions/invokeAction",
            method="POST",
            json={
                "actionId": action_id,
                "actionInputs": action_inputs,
                "userEmail": user_email,
                "requireHumanConfirmation": require_human_confirmation,
                "humanConfirmationChannel": convert_and_respect_annotation_metadata(
                    object_=human_confirmation_channel, annotation=HumanConfirmationChannel, direction="write"
                ),
                "justification": justification,
                "auditLogId": audit_log_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    InvokeActionResponse,
                    parse_obj_as(
                        type_=InvokeActionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncActionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def invoke_action(
        self,
        *,
        action_id: uuid.UUID,
        user_email: str,
        human_confirmation_channel: HumanConfirmationChannel,
        justification: str,
        audit_log_id: uuid.UUID,
        action_inputs: typing.Optional[typing.Any] = OMIT,
        require_human_confirmation: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InvokeActionResponse:
        """
        Invoke an action, asking for human confirmation if necessary

        Parameters
        ----------
        action_id : uuid.UUID

        user_email : str
            The user who we should take the action on behalf of


        human_confirmation_channel : HumanConfirmationChannel
            Where we should ask for human confirmation if necessary


        justification : str
            The justification for requesting this action.  This is likely generated by the LLM that requested the action.


        audit_log_id : uuid.UUID
            Audit log for the message that called for this action


        action_inputs : typing.Optional[typing.Any]
            The inputs needed to execute the action


        require_human_confirmation : typing.Optional[bool]
            If true, then before executing the action we will ask for a human confirmation in Slack.  If false, we may still ask for human confirmation if it's required by your organization admin.


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InvokeActionResponse

        Examples
        --------
        import asyncio
        import uuid

        from credal import AsyncCredalApi
        from credal.actions import HumanConfirmationChannel_SlackThread

        client = AsyncCredalApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.actions.invoke_action(
                action_id=uuid.UUID(
                    "2b5cf2b8-3df3-11ef-9a96-332d4470d189",
                ),
                action_inputs={
                    "textToAppend": "If you need more help, please contact your direct manager."
                },
                user_email="ben@credal.ai",
                require_human_confirmation=True,
                human_confirmation_channel=HumanConfirmationChannel_SlackThread(
                    channel_id="ABC123",
                    thread_timestamp="123456789",
                ),
                justification="The user directly asked to update the Relocations Confluence document with this text.",
                audit_log_id=uuid.UUID(
                    "3df3f2b8-3df3-11ef-9a96-332d447011ef",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/actions/invokeAction",
            method="POST",
            json={
                "actionId": action_id,
                "actionInputs": action_inputs,
                "userEmail": user_email,
                "requireHumanConfirmation": require_human_confirmation,
                "humanConfirmationChannel": convert_and_respect_annotation_metadata(
                    object_=human_confirmation_channel, annotation=HumanConfirmationChannel, direction="write"
                ),
                "justification": justification,
                "auditLogId": audit_log_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    InvokeActionResponse,
                    parse_obj_as(
                        type_=InvokeActionResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
