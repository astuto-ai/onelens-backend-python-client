# UpdateActionTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**Service**](Service.md) |  | 
**title** | **str** | Title | 
**subtitle** | **str** |  | [optional] 
**description** | **str** | Description | 
**id** | **int** | Action Type ID | 

## Example

```python
from onelens_backend_client.models.update_action_type_request import UpdateActionTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateActionTypeRequest from a JSON string
update_action_type_request_instance = UpdateActionTypeRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateActionTypeRequest.to_json())

# convert the object into a dict
update_action_type_request_dict = update_action_type_request_instance.to_dict()
# create an instance of UpdateActionTypeRequest from a dict
update_action_type_request_form_dict = update_action_type_request.from_dict(update_action_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


