# GetStateRequest

Request model for getting the agent state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**thread_id** | **str** | Unique identifier of the thread | 
**agent_type** | [**AgentType**](AgentType.md) | Type of the workflow | 

## Example

```python
from onelens_backend_client.models.get_state_request import GetStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetStateRequest from a JSON string
get_state_request_instance = GetStateRequest.from_json(json)
# print the JSON string representation of the object
print(GetStateRequest.to_json())

# convert the object into a dict
get_state_request_dict = get_state_request_instance.to_dict()
# create an instance of GetStateRequest from a dict
get_state_request_form_dict = get_state_request.from_dict(get_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


