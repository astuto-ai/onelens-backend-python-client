# GetHierarchyResponse

get hierarchy response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the hierarchy. | 
**data** | **object** | The data of the hierarchy. | 
**version** | **int** | The version of the hierarchy. | 
**state** | [**HierarchyState**](HierarchyState.md) | The state of the hierarchy. | 
**type** | [**HierarchyType**](HierarchyType.md) | The type of the hierarchy. | 

## Example

```python
from onelens_backend_client.models.get_hierarchy_response import GetHierarchyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHierarchyResponse from a JSON string
get_hierarchy_response_instance = GetHierarchyResponse.from_json(json)
# print the JSON string representation of the object
print(GetHierarchyResponse.to_json())

# convert the object into a dict
get_hierarchy_response_dict = get_hierarchy_response_instance.to_dict()
# create an instance of GetHierarchyResponse from a dict
get_hierarchy_response_form_dict = get_hierarchy_response.from_dict(get_hierarchy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


