# ActionTypeFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_query** | **str** |  | [optional] 
**ids** | **List[int]** | Filter by recommendation unit id/alias. | [optional] [default to []]
**services** | [**List[ActionTypeFiltersServicesInner]**](ActionTypeFiltersServicesInner.md) | Filter by Services | [optional] [default to []]

## Example

```python
from onelens_backend_client.models.action_type_filters import ActionTypeFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ActionTypeFilters from a JSON string
action_type_filters_instance = ActionTypeFilters.from_json(json)
# print the JSON string representation of the object
print(ActionTypeFilters.to_json())

# convert the object into a dict
action_type_filters_dict = action_type_filters_instance.to_dict()
# create an instance of ActionTypeFilters from a dict
action_type_filters_form_dict = action_type_filters.from_dict(action_type_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


