# GetActionTypeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_types** | [**List[ActionType]**](ActionType.md) | Action Types | 
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields | 

## Example

```python
from onelens_backend_client.models.get_action_type_response import GetActionTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetActionTypeResponse from a JSON string
get_action_type_response_instance = GetActionTypeResponse.from_json(json)
# print the JSON string representation of the object
print(GetActionTypeResponse.to_json())

# convert the object into a dict
get_action_type_response_dict = get_action_type_response_instance.to_dict()
# create an instance of GetActionTypeResponse from a dict
get_action_type_response_form_dict = get_action_type_response.from_dict(get_action_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


