# GetHierarchyFlatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HierarchyNodeEntityWithDetails]**](HierarchyNodeEntityWithDetails.md) | The data of the hierarchy. | 

## Example

```python
from onelens_backend_client.models.get_hierarchy_flat_response import GetHierarchyFlatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHierarchyFlatResponse from a JSON string
get_hierarchy_flat_response_instance = GetHierarchyFlatResponse.from_json(json)
# print the JSON string representation of the object
print(GetHierarchyFlatResponse.to_json())

# convert the object into a dict
get_hierarchy_flat_response_dict = get_hierarchy_flat_response_instance.to_dict()
# create an instance of GetHierarchyFlatResponse from a dict
get_hierarchy_flat_response_form_dict = get_hierarchy_flat_response.from_dict(get_hierarchy_flat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


