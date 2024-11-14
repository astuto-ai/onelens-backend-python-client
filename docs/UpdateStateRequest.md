# UpdateStateRequest

Request model for updating the agent state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**thread_id** | **str** | Unique identifier of the thread | 
**agent_type** | [**AgentType**](AgentType.md) | Type of the workflow | 
**input_state** | **object** | New state of the agent | 

## Example

```python
from onelens_backend_client.models.update_state_request import UpdateStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStateRequest from a JSON string
update_state_request_instance = UpdateStateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateStateRequest.to_json())

# convert the object into a dict
update_state_request_dict = update_state_request_instance.to_dict()
# create an instance of UpdateStateRequest from a dict
update_state_request_form_dict = update_state_request.from_dict(update_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


