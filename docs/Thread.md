# Thread

Model representing a conversation thread.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the thread | [optional] 
**created_at** | **datetime** | Timestamp of thread creation | [optional] 
**updated_at** | **datetime** | Timestamp of last thread update | [optional] 
**name** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**agent_type** | [**AgentType**](AgentType.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.thread import Thread

# TODO update the JSON string below
json = "{}"
# create an instance of Thread from a JSON string
thread_instance = Thread.from_json(json)
# print the JSON string representation of the object
print(Thread.to_json())

# convert the object into a dict
thread_dict = thread_instance.to_dict()
# create an instance of Thread from a dict
thread_form_dict = thread.from_dict(thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


