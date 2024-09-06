# DeleteResourceHierarchyMappingsByNodeIdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 
**node_ids** | **List[str]** | The ids of the nodes. | 

## Example

```python
from onelens_backend_client.models.delete_resource_hierarchy_mappings_by_node_ids_request import DeleteResourceHierarchyMappingsByNodeIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteResourceHierarchyMappingsByNodeIdsRequest from a JSON string
delete_resource_hierarchy_mappings_by_node_ids_request_instance = DeleteResourceHierarchyMappingsByNodeIdsRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteResourceHierarchyMappingsByNodeIdsRequest.to_json())

# convert the object into a dict
delete_resource_hierarchy_mappings_by_node_ids_request_dict = delete_resource_hierarchy_mappings_by_node_ids_request_instance.to_dict()
# create an instance of DeleteResourceHierarchyMappingsByNodeIdsRequest from a dict
delete_resource_hierarchy_mappings_by_node_ids_request_form_dict = delete_resource_hierarchy_mappings_by_node_ids_request.from_dict(delete_resource_hierarchy_mappings_by_node_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


