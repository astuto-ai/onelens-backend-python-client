# GetActionTypeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**ActionTypeFilters**](ActionTypeFilters.md) | Filters to apply to the Action Types. | [optional] 

## Example

```python
from onelens_backend_client.models.get_action_type_request import GetActionTypeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetActionTypeRequest from a JSON string
get_action_type_request_instance = GetActionTypeRequest.from_json(json)
# print the JSON string representation of the object
print(GetActionTypeRequest.to_json())

# convert the object into a dict
get_action_type_request_dict = get_action_type_request_instance.to_dict()
# create an instance of GetActionTypeRequest from a dict
get_action_type_request_form_dict = get_action_type_request.from_dict(get_action_type_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


