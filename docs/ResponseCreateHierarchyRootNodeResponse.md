# ResponseCreateHierarchyRootNodeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateHierarchyRootNodeResponse**](CreateHierarchyRootNodeResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_create_hierarchy_root_node_response import ResponseCreateHierarchyRootNodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCreateHierarchyRootNodeResponse from a JSON string
response_create_hierarchy_root_node_response_instance = ResponseCreateHierarchyRootNodeResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseCreateHierarchyRootNodeResponse.to_json())

# convert the object into a dict
response_create_hierarchy_root_node_response_dict = response_create_hierarchy_root_node_response_instance.to_dict()
# create an instance of ResponseCreateHierarchyRootNodeResponse from a dict
response_create_hierarchy_root_node_response_form_dict = response_create_hierarchy_root_node_response.from_dict(response_create_hierarchy_root_node_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


