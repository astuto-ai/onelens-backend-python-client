# DeleteHierarchyNodeRequest

delete hierarchy node request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the hierarchy node. | 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.delete_hierarchy_node_request import DeleteHierarchyNodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteHierarchyNodeRequest from a JSON string
delete_hierarchy_node_request_instance = DeleteHierarchyNodeRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteHierarchyNodeRequest.to_json())

# convert the object into a dict
delete_hierarchy_node_request_dict = delete_hierarchy_node_request_instance.to_dict()
# create an instance of DeleteHierarchyNodeRequest from a dict
delete_hierarchy_node_request_form_dict = delete_hierarchy_node_request.from_dict(delete_hierarchy_node_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


