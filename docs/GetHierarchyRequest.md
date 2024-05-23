# GetHierarchyRequest

get hierarchy request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**GetHierarchyFilters**](GetHierarchyFilters.md) | Filters for the hierarchy nodes. | [optional] 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_hierarchy_request import GetHierarchyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetHierarchyRequest from a JSON string
get_hierarchy_request_instance = GetHierarchyRequest.from_json(json)
# print the JSON string representation of the object
print(GetHierarchyRequest.to_json())

# convert the object into a dict
get_hierarchy_request_dict = get_hierarchy_request_instance.to_dict()
# create an instance of GetHierarchyRequest from a dict
get_hierarchy_request_form_dict = get_hierarchy_request.from_dict(get_hierarchy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


