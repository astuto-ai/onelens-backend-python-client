# CreateHierarchyRootNodeRequest

create a root node request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.create_hierarchy_root_node_request import CreateHierarchyRootNodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHierarchyRootNodeRequest from a JSON string
create_hierarchy_root_node_request_instance = CreateHierarchyRootNodeRequest.from_json(json)
# print the JSON string representation of the object
print(CreateHierarchyRootNodeRequest.to_json())

# convert the object into a dict
create_hierarchy_root_node_request_dict = create_hierarchy_root_node_request_instance.to_dict()
# create an instance of CreateHierarchyRootNodeRequest from a dict
create_hierarchy_root_node_request_form_dict = create_hierarchy_root_node_request.from_dict(create_hierarchy_root_node_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


