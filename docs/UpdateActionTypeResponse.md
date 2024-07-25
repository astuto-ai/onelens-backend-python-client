# UpdateActionTypeResponse


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
from onelens_backend_client.models.update_action_type_response import UpdateActionTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateActionTypeResponse from a JSON string
update_action_type_response_instance = UpdateActionTypeResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateActionTypeResponse.to_json())

# convert the object into a dict
update_action_type_response_dict = update_action_type_response_instance.to_dict()
# create an instance of UpdateActionTypeResponse from a dict
update_action_type_response_form_dict = update_action_type_response.from_dict(update_action_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


