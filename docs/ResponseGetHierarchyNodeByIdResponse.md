# ResponseGetHierarchyNodeByIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetHierarchyNodeByIdResponse**](GetHierarchyNodeByIdResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_hierarchy_node_by_id_response import ResponseGetHierarchyNodeByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetHierarchyNodeByIdResponse from a JSON string
response_get_hierarchy_node_by_id_response_instance = ResponseGetHierarchyNodeByIdResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetHierarchyNodeByIdResponse.to_json())

# convert the object into a dict
response_get_hierarchy_node_by_id_response_dict = response_get_hierarchy_node_by_id_response_instance.to_dict()
# create an instance of ResponseGetHierarchyNodeByIdResponse from a dict
response_get_hierarchy_node_by_id_response_form_dict = response_get_hierarchy_node_by_id_response.from_dict(response_get_hierarchy_node_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


