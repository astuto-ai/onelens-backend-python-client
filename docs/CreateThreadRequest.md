# CreateThreadRequest

Request model for creating a thread.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**agent_type** | [**AgentType**](AgentType.md) | Type of the workflow | 
**user_id** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.create_thread_request import CreateThreadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateThreadRequest from a JSON string
create_thread_request_instance = CreateThreadRequest.from_json(json)
# print the JSON string representation of the object
print(CreateThreadRequest.to_json())

# convert the object into a dict
create_thread_request_dict = create_thread_request_instance.to_dict()
# create an instance of CreateThreadRequest from a dict
create_thread_request_form_dict = create_thread_request.from_dict(create_thread_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


