# GetAllParentNodesResponse

get all parent nodes response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_nodes** | **Dict[str, List[HierarchyNodeEntityDTOOutput]]** | List of parent nodes. | 

## Example

```python
from onelens_backend_client.models.get_all_parent_nodes_response import GetAllParentNodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllParentNodesResponse from a JSON string
get_all_parent_nodes_response_instance = GetAllParentNodesResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllParentNodesResponse.to_json())

# convert the object into a dict
get_all_parent_nodes_response_dict = get_all_parent_nodes_response_instance.to_dict()
# create an instance of GetAllParentNodesResponse from a dict
get_all_parent_nodes_response_form_dict = get_all_parent_nodes_response.from_dict(get_all_parent_nodes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


