# GetHierarchyFilters

get hierarchy filters request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | [**HierarchyState**](HierarchyState.md) |  | [optional] 
**type** | [**HierarchyType**](HierarchyType.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_hierarchy_filters import GetHierarchyFilters

# TODO update the JSON string below
json = "{}"
# create an instance of GetHierarchyFilters from a JSON string
get_hierarchy_filters_instance = GetHierarchyFilters.from_json(json)
# print the JSON string representation of the object
print(GetHierarchyFilters.to_json())

# convert the object into a dict
get_hierarchy_filters_dict = get_hierarchy_filters_instance.to_dict()
# create an instance of GetHierarchyFilters from a dict
get_hierarchy_filters_form_dict = get_hierarchy_filters.from_dict(get_hierarchy_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


