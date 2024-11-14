# GetAllParentNodesRequest

get all parent nodes request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 
**node_ids** | **List[str]** | The id of the node. | 

## Example

```python
from onelens_backend_client.models.get_all_parent_nodes_request import GetAllParentNodesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllParentNodesRequest from a JSON string
get_all_parent_nodes_request_instance = GetAllParentNodesRequest.from_json(json)
# print the JSON string representation of the object
print(GetAllParentNodesRequest.to_json())

# convert the object into a dict
get_all_parent_nodes_request_dict = get_all_parent_nodes_request_instance.to_dict()
# create an instance of GetAllParentNodesRequest from a dict
get_all_parent_nodes_request_form_dict = get_all_parent_nodes_request.from_dict(get_all_parent_nodes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


