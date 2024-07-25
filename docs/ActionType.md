# ActionType


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
from onelens_backend_client.models.action_type import ActionType

# TODO update the JSON string below
json = "{}"
# create an instance of ActionType from a JSON string
action_type_instance = ActionType.from_json(json)
# print the JSON string representation of the object
print(ActionType.to_json())

# convert the object into a dict
action_type_dict = action_type_instance.to_dict()
# create an instance of ActionType from a dict
action_type_form_dict = action_type.from_dict(action_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


