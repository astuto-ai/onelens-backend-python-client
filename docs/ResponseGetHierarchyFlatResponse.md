# ResponseGetHierarchyFlatResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetHierarchyFlatResponse**](GetHierarchyFlatResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_hierarchy_flat_response import ResponseGetHierarchyFlatResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetHierarchyFlatResponse from a JSON string
response_get_hierarchy_flat_response_instance = ResponseGetHierarchyFlatResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetHierarchyFlatResponse.to_json())

# convert the object into a dict
response_get_hierarchy_flat_response_dict = response_get_hierarchy_flat_response_instance.to_dict()
# create an instance of ResponseGetHierarchyFlatResponse from a dict
response_get_hierarchy_flat_response_form_dict = response_get_hierarchy_flat_response.from_dict(response_get_hierarchy_flat_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


