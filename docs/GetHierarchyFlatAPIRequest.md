# GetHierarchyFlatAPIRequest

get hierarchy flat api request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**GetHierarchyFlatFilters**](GetHierarchyFlatFilters.md) | Filters for flat hierarchy nodes. | [optional] 

## Example

```python
from onelens_backend_client.models.get_hierarchy_flat_api_request import GetHierarchyFlatAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetHierarchyFlatAPIRequest from a JSON string
get_hierarchy_flat_api_request_instance = GetHierarchyFlatAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetHierarchyFlatAPIRequest.to_json())

# convert the object into a dict
get_hierarchy_flat_api_request_dict = get_hierarchy_flat_api_request_instance.to_dict()
# create an instance of GetHierarchyFlatAPIRequest from a dict
get_hierarchy_flat_api_request_form_dict = get_hierarchy_flat_api_request.from_dict(get_hierarchy_flat_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


