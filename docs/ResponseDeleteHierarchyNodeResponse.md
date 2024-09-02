# ResponseDeleteHierarchyNodeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | delete hierarchy node response | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_delete_hierarchy_node_response import ResponseDeleteHierarchyNodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseDeleteHierarchyNodeResponse from a JSON string
response_delete_hierarchy_node_response_instance = ResponseDeleteHierarchyNodeResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseDeleteHierarchyNodeResponse.to_json())

# convert the object into a dict
response_delete_hierarchy_node_response_dict = response_delete_hierarchy_node_response_instance.to_dict()
# create an instance of ResponseDeleteHierarchyNodeResponse from a dict
response_delete_hierarchy_node_response_form_dict = response_delete_hierarchy_node_response.from_dict(response_delete_hierarchy_node_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


