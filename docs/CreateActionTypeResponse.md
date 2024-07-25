# CreateActionTypeResponse


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
from onelens_backend_client.models.create_action_type_response import CreateActionTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateActionTypeResponse from a JSON string
create_action_type_response_instance = CreateActionTypeResponse.from_json(json)
# print the JSON string representation of the object
print(CreateActionTypeResponse.to_json())

# convert the object into a dict
create_action_type_response_dict = create_action_type_response_instance.to_dict()
# create an instance of CreateActionTypeResponse from a dict
create_action_type_response_form_dict = create_action_type_response.from_dict(create_action_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


