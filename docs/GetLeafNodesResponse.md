# GetLeafNodesResponse

get leaf nodes response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodes** | [**List[HierarchyNodeEntityDTOOutput]**](HierarchyNodeEntityDTOOutput.md) | List of leaf nodes. | 

## Example

```python
from onelens_backend_client.models.get_leaf_nodes_response import GetLeafNodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetLeafNodesResponse from a JSON string
get_leaf_nodes_response_instance = GetLeafNodesResponse.from_json(json)
# print the JSON string representation of the object
print(GetLeafNodesResponse.to_json())

# convert the object into a dict
get_leaf_nodes_response_dict = get_leaf_nodes_response_instance.to_dict()
# create an instance of GetLeafNodesResponse from a dict
get_leaf_nodes_response_form_dict = get_leaf_nodes_response.from_dict(get_leaf_nodes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


