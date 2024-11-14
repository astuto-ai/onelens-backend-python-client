# GetResourceIdsListForNodeIdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 
**node_ids** | **List[str]** | The ids of the nodes. | 

## Example

```python
from onelens_backend_client.models.get_resource_ids_list_for_node_ids_request import GetResourceIdsListForNodeIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceIdsListForNodeIdsRequest from a JSON string
get_resource_ids_list_for_node_ids_request_instance = GetResourceIdsListForNodeIdsRequest.from_json(json)
# print the JSON string representation of the object
print(GetResourceIdsListForNodeIdsRequest.to_json())

# convert the object into a dict
get_resource_ids_list_for_node_ids_request_dict = get_resource_ids_list_for_node_ids_request_instance.to_dict()
# create an instance of GetResourceIdsListForNodeIdsRequest from a dict
get_resource_ids_list_for_node_ids_request_form_dict = get_resource_ids_list_for_node_ids_request.from_dict(get_resource_ids_list_for_node_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


