# GetLeafNodesRequest

get leaf nodes request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 
**filters** | [**GetHierarchyFilters**](GetHierarchyFilters.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_leaf_nodes_request import GetLeafNodesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetLeafNodesRequest from a JSON string
get_leaf_nodes_request_instance = GetLeafNodesRequest.from_json(json)
# print the JSON string representation of the object
print(GetLeafNodesRequest.to_json())

# convert the object into a dict
get_leaf_nodes_request_dict = get_leaf_nodes_request_instance.to_dict()
# create an instance of GetLeafNodesRequest from a dict
get_leaf_nodes_request_form_dict = get_leaf_nodes_request.from_dict(get_leaf_nodes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


