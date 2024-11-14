# GetHierarchyNodeByIdRequest

get hierarchy node by id request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the hierarchy node. | 
**tenant_id** | **str** | The id of the tenant. | 
**with_info** | **bool** | Whether to include additional info in the response. | [optional] [default to True]

## Example

```python
from onelens_backend_client.models.get_hierarchy_node_by_id_request import GetHierarchyNodeByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetHierarchyNodeByIdRequest from a JSON string
get_hierarchy_node_by_id_request_instance = GetHierarchyNodeByIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetHierarchyNodeByIdRequest.to_json())

# convert the object into a dict
get_hierarchy_node_by_id_request_dict = get_hierarchy_node_by_id_request_instance.to_dict()
# create an instance of GetHierarchyNodeByIdRequest from a dict
get_hierarchy_node_by_id_request_form_dict = get_hierarchy_node_by_id_request.from_dict(get_hierarchy_node_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


