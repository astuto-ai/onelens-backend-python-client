# SendMessageRequest

Request model for sending a message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**thread_id** | **str** |  | [optional] 
**agent_type** | [**AgentType**](AgentType.md) | Type of the workflow, required if thread_id is not provided to create a new thread for the workflow | [optional] 
**message** | [**MessageInput**](MessageInput.md) | Message to be sent | 
**input_state** | **object** |  | [optional] 

## Example

```python
from onelens_backend_client.models.send_message_request import SendMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendMessageRequest from a JSON string
send_message_request_instance = SendMessageRequest.from_json(json)
# print the JSON string representation of the object
print(SendMessageRequest.to_json())

# convert the object into a dict
send_message_request_dict = send_message_request_instance.to_dict()
# create an instance of SendMessageRequest from a dict
send_message_request_form_dict = send_message_request.from_dict(send_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


