# Reference
## Copilots
<details><summary><code>client.copilots.<a href="src/credal/copilots/client.py">create_copilot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new agent. The API key used will be added to the agent for future Requests
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
from credal.common import Collaborator
client = CredalApi(api_key="YOUR_API_KEY", )
client.copilots.create_copilot(name='Customer Agent', description='This agent is used to answer customer requests based on internal documentation.', collaborators=[Collaborator(email='test@gmail.com', role="editor", )], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — A descriptive name for the agent.
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — An in depth name for the agent's function. Useful for routing requests to the right agent.
    
</dd>
</dl>

<dl>
<dd>

**collaborators:** `typing.Sequence[Collaborator]` — A list of collaborator emails and roles that will have access to the agent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copilots.<a href="src/credal/copilots/client.py">create_conversation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

OPTIONAL. Create a new conversation with the Agent. The conversation ID can be used in the `sendMessage` endpoint. The `sendMessage` endpoint automatically creates new conversations upon first request, but calling this endpoint can simplify certain use cases where it is helpful for the application to have the conversation ID before the first message is sent.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
import uuid
client = CredalApi(api_key="YOUR_API_KEY", )
client.copilots.create_conversation(agent_id=uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c24", ), user_email='ravin@credal.ai', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `uuid.UUID` — Credal-generated Agent ID to specify which agent to route the request to.
    
</dd>
</dl>

<dl>
<dd>

**user_email:** `str` — End-user for the conversation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copilots.<a href="src/credal/copilots/client.py">provide_message_feedback</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
import uuid
from credal.copilots import MessageFeedback
client = CredalApi(api_key="YOUR_API_KEY", )
client.copilots.provide_message_feedback(user_email='ravin@credal.ai', message_id=uuid.UUID("dd721cd8-4bf2-4b94-9869-258df3dab9dc", ), agent_id=uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c24", ), message_feedback=MessageFeedback(feedback="NEGATIVE", suggested_answer='Yes, Credal is SOC 2 compliant.', descriptive_feedback='The response should be extremely clear and concise.', ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `uuid.UUID` — Credal-generated Agent ID to specify which agent to route the request to.
    
</dd>
</dl>

<dl>
<dd>

**user_email:** `str` — The user profile you want to use when providing feedback.
    
</dd>
</dl>

<dl>
<dd>

**message_id:** `uuid.UUID` — The message ID for which feedback is being provided.
    
</dd>
</dl>

<dl>
<dd>

**message_feedback:** `MessageFeedback` — The feedback provided by the user.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copilots.<a href="src/credal/copilots/client.py">send_message</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
import uuid
from credal.copilots import InputVariable
client = CredalApi(api_key="YOUR_API_KEY", )
client.copilots.send_message(agent_id=uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c24", ), message='Is Credal SOC 2 compliant?', user_email='ravin@credal.ai', input_variables=[InputVariable(name='input1', ids=[uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c24", )], ), InputVariable(name='input2', ids=[uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c25", ), uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c26", )], )], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**agent_id:** `uuid.UUID` — Credal-generated Agent ID to specify which agent to route the request to.
    
</dd>
</dl>

<dl>
<dd>

**message:** `str` — The message you want to send to your agent.
    
</dd>
</dl>

<dl>
<dd>

**user_email:** `str` — The user profile you want to use when sending the message.
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[uuid.UUID]` — Credal-generated conversation ID for sending follow up messages. Conversation ID is returned after initial message. Optional, to be left off for first messages on new conversations.
    
</dd>
</dl>

<dl>
<dd>

**input_variables:** `typing.Optional[typing.Sequence[InputVariable]]` — Optional input variables to be used in the message. Map the name of the variable to a list of urls.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copilots.<a href="src/credal/copilots/client.py">stream_message</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint allows you to send a message to a specific agent and get the response back as a streamed set of Server-Sent Events.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
import uuid
from credal.copilots import InputVariable
client = CredalApi(api_key="YOUR_API_KEY", )
response = client.copilots.stream_message(copilot_id=uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c25", ), message='Is Credal SOC 2 compliant?', email='ravin@credal.ai', input_variables=[InputVariable(name='input1', ids=[uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c24", )], ), InputVariable(name='input2', ids=[uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c25", ), uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c26", )], )], )
for chunk in response.data:
    yield chunk

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**copilot_id:** `uuid.UUID` — Credal-generated Agent ID to specify which agent to route the request to.
    
</dd>
</dl>

<dl>
<dd>

**message:** `str` — The message you want to send to your agent.
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — The user profile you want to use when sending the message.
    
</dd>
</dl>

<dl>
<dd>

**conversation_id:** `typing.Optional[uuid.UUID]` — Credal-generated conversation ID for sending follow up messages. Conversation ID is returned after initial message. Optional, to be left off for first messages on new conversations.
    
</dd>
</dl>

<dl>
<dd>

**input_variables:** `typing.Optional[typing.Sequence[InputVariable]]` — Optional input variables to be used in the message. Map the name of the variable to a list of urls.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copilots.<a href="src/credal/copilots/client.py">add_collection_to_copilot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Link a collection with a agent. The API Key used must be added to both the collection and the agent beforehand.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
import uuid
client = CredalApi(api_key="YOUR_API_KEY", )
client.copilots.add_collection_to_copilot(copilot_id=uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c24", ), collection_id=uuid.UUID("def1055f-83c5-43d6-b558-f7a38e7b299e", ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**copilot_id:** `uuid.UUID` — Credal-generated Agent ID to add the collection to.
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `uuid.UUID` — Credal-generated collection ID to add.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copilots.<a href="src/credal/copilots/client.py">remove_collection_from_copilot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Unlink a collection with a agent. The API Key used must be added to both the collection and the agent beforehand.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
import uuid
client = CredalApi(api_key="YOUR_API_KEY", )
client.copilots.remove_collection_from_copilot(copilot_id=uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c24", ), collection_id=uuid.UUID("def1055f-83c5-43d6-b558-f7a38e7b299e", ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**copilot_id:** `uuid.UUID` — Credal-generated agent ID to add the collection to.
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `uuid.UUID` — Credal-generated collection ID to add.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copilots.<a href="src/credal/copilots/client.py">update_configuration</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the configuration for a agent
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
import uuid
from credal.copilots import Configuration
from credal.copilots import AiEndpointConfiguration
client = CredalApi(api_key="YOUR_API_KEY", )
client.copilots.update_configuration(copilot_id=uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c24", ), configuration=Configuration(name='Customer Agent', description='This agent is used to answer customer requests based on internal documentation.', prompt='You are a polite, helpful assistant used to answer customer requests.', ai_endpoint_configuration=AiEndpointConfiguration(base_url='https://api.openai.com/v1/', api_key='<YOUR_API_KEY_HERE>', ), ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**copilot_id:** `uuid.UUID` — Credal-generated agent ID to add the collection to.
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `Configuration` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.copilots.<a href="src/credal/copilots/client.py">delete_copilot</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
import uuid
client = CredalApi(api_key="YOUR_API_KEY", )
client.copilots.delete_copilot(id=uuid.UUID("ac20e6ba-0bae-11ef-b25a-efca73df4c3a", ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `uuid.UUID` — Copilot ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DocumentCatalog
<details><summary><code>client.document_catalog.<a href="src/credal/document_catalog/client.py">upload_document_contents</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
client = CredalApi(api_key="YOUR_API_KEY", )
client.document_catalog.upload_document_contents(document_name='My Document', document_contents='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', document_external_id='73eead26-d124-4940-b329-5f068a0a8db9', allowed_users_email_addresses=['jack@credal.ai', 'ravin@credal.ai'], upload_as_user_email='jack@credal.ai', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**document_name:** `str` — The name of the document you want to upload.
    
</dd>
</dl>

<dl>
<dd>

**document_contents:** `str` — The full LLM-formatted text contents of the document you want to upload.
    
</dd>
</dl>

<dl>
<dd>

**allowed_users_email_addresses:** `typing.Sequence[str]` — Users allowed to access the document. Unlike Credal's out of the box connectors which reconcile various permissions models from 3rd party software, for custom uploads the caller is responsible for specifying who can access the document and currently flattening groups if applicable. Documents can also be marked as internal public.
    
</dd>
</dl>

<dl>
<dd>

**upload_as_user_email:** `str` — [Legacy] The user on behalf of whom the document should be uploaded. In most cases, this can simply be the email of the developer making the API call. This field will be removed in the future in favor of purely specifying permissions via allowedUsersEmailAddresses.
    
</dd>
</dl>

<dl>
<dd>

**document_external_id:** `str` — The external ID of the document. This is typically the ID as it exists in its original external system. Uploads to the same external ID will update the document in Credal.
    
</dd>
</dl>

<dl>
<dd>

**document_external_url:** `typing.Optional[str]` — The external URL of the document you want to upload. If provided Credal will link to this URL.
    
</dd>
</dl>

<dl>
<dd>

**custom_metadata:** `typing.Optional[typing.Optional[typing.Any]]` — Optional JSON representing any custom metdata for this document
    
</dd>
</dl>

<dl>
<dd>

**collection_id:** `typing.Optional[str]` — If specified, document will also be added to a particular document collection
    
</dd>
</dl>

<dl>
<dd>

**force_update:** `typing.Optional[bool]` — If specified, document contents will be re-uploaded and re-embedded even if the document already exists in Credal
    
</dd>
</dl>

<dl>
<dd>

**internal_public:** `typing.Optional[bool]` — If specified, document will be accessible to everyone within the organization of the uploader
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document_catalog.<a href="src/credal/document_catalog/client.py">sync_source_by_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sync a document from a source URL. Does not support recursive web search. Reach out to a Credal representative for access.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
client = CredalApi(api_key="YOUR_API_KEY", )
client.document_catalog.sync_source_by_url(source_url='https://drive.google.com/file/d/123456/view', upload_as_user_email='ria@credal.ai', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**upload_as_user_email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document_catalog.<a href="src/credal/document_catalog/client.py">metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk patch metadata for documents, synced natively by Credal or manual API uploads
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
from credal.document_catalog import DocumentMetadataPatch
from credal.common import ResourceIdentifier_ExternalResourceId
client = CredalApi(api_key="YOUR_API_KEY", )
client.document_catalog.metadata(sources=[DocumentMetadataPatch(metadata={'Department': 'HR', 'Country': 'United States'}
, resource_identifier=ResourceIdentifier_ExternalResourceId(external_resource_id='170NrBm0Do7gdzvr54UvyslPVWkQFOA0lgNycFmdZJQr', resource_type="GOOGLE_DRIVE_ITEM", ), ), DocumentMetadataPatch(metadata={'Department': 'Sales', 'Vertical': 'Healthcare'}
, resource_identifier=ResourceIdentifier_ExternalResourceId(external_resource_id='123456', resource_type="ZENDESK_TICKET", ), )], upload_as_user_email='ben@credal.ai', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sources:** `typing.Sequence[DocumentMetadataPatch]` 
    
</dd>
</dl>

<dl>
<dd>

**upload_as_user_email:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## DocumentCollections
<details><summary><code>client.document_collections.<a href="src/credal/document_collections/client.py">add_documents_to_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add documents to a document collection. Note that the documents must already exist in the document catalog to use this endpoint. If you want to upload a new document to a collection, use the `uploadDocumentContents` endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
import uuid
from credal.common import ResourceIdentifier_ExternalResourceId
client = CredalApi(api_key="YOUR_API_KEY", )
client.document_collections.add_documents_to_collection(collection_id=uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c24", ), resource_identifiers=[ResourceIdentifier_ExternalResourceId(external_resource_id='170NrBm0Do7gdzvr54UvyslPVWkQFOA0lgNycFmdZJQr', resource_type="GOOGLE_DRIVE_ITEM", ), ResourceIdentifier_ExternalResourceId(external_resource_id='398KAHdfkjsdf09r54UvyslPVWkQFOA0lOiu34in923', resource_type="GOOGLE_DRIVE_ITEM", )], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `uuid.UUID` — The ID of the document collection you want to add to.
    
</dd>
</dl>

<dl>
<dd>

**resource_identifiers:** `typing.Sequence[ResourceIdentifier]` — The set of resource identifier for which you want to add to the collection.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document_collections.<a href="src/credal/document_collections/client.py">remove_documents_from_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove documents from a collection
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
import uuid
from credal.common import ResourceIdentifier_ExternalResourceId
client = CredalApi(api_key="YOUR_API_KEY", )
client.document_collections.remove_documents_from_collection(collection_id=uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c24", ), resource_identifiers=[ResourceIdentifier_ExternalResourceId(external_resource_id='170NrBm0Do7gdzvr54UvyslPVWkQFOA0lgNycFmdZJQr', resource_type="GOOGLE_DRIVE_ITEM", ), ResourceIdentifier_ExternalResourceId(external_resource_id='398KAHdfkjsdf09r54UvyslPVWkQFOA0lOiu34in923', resource_type="GOOGLE_DRIVE_ITEM", )], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `uuid.UUID` — The ID of the document collection you want to add to.
    
</dd>
</dl>

<dl>
<dd>

**resource_identifiers:** `typing.Sequence[ResourceIdentifier]` — The set of resource identifier for which you want to remove from the collection
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document_collections.<a href="src/credal/document_collections/client.py">create_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new collection. The API key used will be added to the collection for future Requests
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
from credal.common import Collaborator
client = CredalApi(api_key="YOUR_API_KEY", )
client.document_collections.create_collection(name='Customer Collection', description='This collection is used to answer customer requests based on internal documentation.', collaborators=[Collaborator(email='test@gmail.com', role="editor", )], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — A descriptive name for the collection.
    
</dd>
</dl>

<dl>
<dd>

**description:** `str` — An in depth name for the agent's function. Useful for routing requests to the right agent.
    
</dd>
</dl>

<dl>
<dd>

**collaborators:** `typing.Sequence[Collaborator]` — A list of collaborator emails and roles that will have access to the agent.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document_collections.<a href="src/credal/document_collections/client.py">delete_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete the collection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
import uuid
client = CredalApi(api_key="YOUR_API_KEY", )
client.document_collections.delete_collection(collection_id=uuid.UUID("ac20e6ba-0bae-11ef-b25a-efca73df4c3a", ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `uuid.UUID` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document_collections.<a href="src/credal/document_collections/client.py">create_mongo_collection_sync</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Credal lets you easily sync your MongoDB data for use in Collections and Agents. Create a new sync from a MongoDB collection to a Credal collection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
import uuid
from credal.document_collections import MongoCollectionSyncConfig
from credal.document_collections import MongoSourceFieldsConfig
client = CredalApi(api_key="YOUR_API_KEY", )
client.document_collections.create_mongo_collection_sync(mongo_uri='mongodb+srv://cluster0.hzwklqn.mongodb.net/Cluster0?retryWrites=true&w=majority', collection_id=uuid.UUID("ac20e6ba-0bae-11ef-b25a-efca73df4c3a", ), config=MongoCollectionSyncConfig(sync_name='My sales transcripts', collection_name='myCollection', filter_expression={'status': {'$ne': 'disabled'}}
, source_fields=MongoSourceFieldsConfig(body='body', source_name='meetingName', source_system_updated='transcriptDatetime', source_url='link', ), ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `uuid.UUID` 
    
</dd>
</dl>

<dl>
<dd>

**mongo_uri:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `MongoCollectionSyncConfig` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.document_collections.<a href="src/credal/document_collections/client.py">update_mongo_collection_sync</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Credal lets you easily sync your MongoDB data for use in Collections and Agents. Update an existing sync from a MongoDB collection to a Credal collection via the `mongoCredentialId`, to disambiguate between multiple potential syncs to a given collection.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
import uuid
from credal.document_collections import MongoCollectionSyncConfig
from credal.document_collections import MongoSourceFieldsConfig
client = CredalApi(api_key="YOUR_API_KEY", )
client.document_collections.update_mongo_collection_sync(mongo_uri='mongodb+srv://cluster0.hzwklqn.mongodb.net/Cluster0?retryWrites=true&w=majority', mongo_credential_id=uuid.UUID("5988ed76-6ee1-11ef-97dd-1fca54b7c4bc", ), config=MongoCollectionSyncConfig(sync_name='My recent summarized sales transcripts', collection_name='myCollection', filter_expression={'transcriptDatetime': {'$gt': '2023-01-01T00:00:00.000Z'}}
, source_fields=MongoSourceFieldsConfig(body='transcriptSummary', source_name='meetingName', source_system_updated='transcriptDatetime', source_url='link', ), ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**mongo_credential_id:** `uuid.UUID` 
    
</dd>
</dl>

<dl>
<dd>

**mongo_uri:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `MongoCollectionSyncConfig` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PermissionsService
<details><summary><code>client.permissions_service.<a href="src/credal/permissions_service/client.py">check_resource_authorization_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Admin endpoint to check whether the specified user is authorized to read the specified resource.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
from credal.common import ResourceIdentifier_ExternalResourceId
client = CredalApi(api_key="YOUR_API_KEY", )
client.permissions_service.check_resource_authorization_for_user(resource_identifier=ResourceIdentifier_ExternalResourceId(external_resource_id='170NrBm0Do7gdzvr54UvyslPVWkQFOA0lgNycFmdZJQr', resource_type="GOOGLE_DRIVE_ITEM", ), user_email='john.smith@foo.com', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**resource_identifier:** `ResourceIdentifier` — The resource identifier for which you want to check authorization.
    
</dd>
</dl>

<dl>
<dd>

**user_email:** `str` — The user email to check authorization for.
    
</dd>
</dl>

<dl>
<dd>

**disable_cache:** `typing.Optional[bool]` — If specified, Credal will bypass the permissions cache and check current permissions for this resource
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.permissions_service.<a href="src/credal/permissions_service/client.py">check_bulk_resources_authorization_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Admin endpoint to check whether the specified user is authorized to read the specified set of resources.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
from credal.common import ResourceIdentifier_Url
from credal.common import ResourceIdentifier_ExternalResourceId
client = CredalApi(api_key="YOUR_API_KEY", )
client.permissions_service.check_bulk_resources_authorization_for_user(resource_identifiers=[ResourceIdentifier_Url(url='https://docs.google.com/document/d/170NrBm0Do7gdzvr54UvyslPVWkQFOA0lgNycFmdZJQr/edit', ), ResourceIdentifier_ExternalResourceId(external_resource_id='sfsdfvr54UvyslPVWkQFOA0dfsdfsdflgNycFmdZJQr', resource_type="ZENDESK_TICKET", )], user_email='john.smith@foo.com', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**resource_identifiers:** `typing.Sequence[ResourceIdentifier]` — The set of resource identifier for which you want to check authorization. Currently limited to 20 resources.
    
</dd>
</dl>

<dl>
<dd>

**user_email:** `str` — The user email to check authorization for.
    
</dd>
</dl>

<dl>
<dd>

**disable_cache:** `typing.Optional[bool]` — If specified, Credal will bypass the permissions cache and check current permissions for all resources specified.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.permissions_service.<a href="src/credal/permissions_service/client.py">list_cached_authorized_resources_for_user</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Admin endpoint to list all resources that the specified user is authorized to read. Note this endpoint returns cached results and may not be up-to-date. You can use the checkResourceAuthorizationForUser endpoint with disableCache set to true to get the most up-to-date results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
client = CredalApi(api_key="YOUR_API_KEY", )
client.permissions_service.list_cached_authorized_resources_for_user(user_email='john.smith@foo.com', )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**user_email:** `str` — The user email to list authorized resources for.
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `typing.Optional[ResourceType]` — The type of resource you want to list. If not specified, all resource types will be listed.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of resources to return. Defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — The offset to use for pagination. If not specified, the first page of results will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Search
<details><summary><code>client.search.<a href="src/credal/search/client.py">search_document_collection</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search across all documents in a document collection using the document metadata and contents.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
import uuid
from credal.search import SingleFieldFilter
from credal.search import DocumentCollectionSearchOptions
client = CredalApi(api_key="YOUR_API_KEY", )
client.search.search_document_collection(collection_id=uuid.UUID("82e4b12a-6990-45d4-8ebd-85c00e030c24", ), search_query='ABC Corp', structured_query_filters=[SingleFieldFilter(field='status', operator="==", value='Open', )], user_email='jack@credal.ai', search_options=DocumentCollectionSearchOptions(max_chunks=10, merge_contents=True, threshold=0.8, enable_smart_filtering=True, enable_query_extraction=True, enable_reranking=True, ), )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**collection_id:** `uuid.UUID` 
    
</dd>
</dl>

<dl>
<dd>

**search_query:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**user_email:** `str` — The email of the user making the search request for permissions reduction.
    
</dd>
</dl>

<dl>
<dd>

**structured_query_filters:** `typing.Optional[typing.Sequence[SingleFieldFilter]]` — The structured query filters to apply to the search query.
    
</dd>
</dl>

<dl>
<dd>

**search_options:** `typing.Optional[DocumentCollectionSearchOptions]` 
    
</dd>
</dl>

<dl>
<dd>

**metadata_filter_expression:** `typing.Optional[str]` — Legacy metadata filter expression to apply to the search query. Use structuredQueryFilters instead.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/credal/users/client.py">metadata</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Bulk patch metadata for users
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from credal import CredalApi
from credal.users import UserMetadataPatch
client = CredalApi(api_key="YOUR_API_KEY", )
client.users.metadata(request=[UserMetadataPatch(metadata={'State': 'NY', 'Job Role': 'CEO'}
, user_email='ravin@credal.ai', ), UserMetadataPatch(metadata={'State': 'NY', 'Department': 'Engineering'}
, user_email='jack@credal.ai', )], )

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Sequence[UserMetadataPatch]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

