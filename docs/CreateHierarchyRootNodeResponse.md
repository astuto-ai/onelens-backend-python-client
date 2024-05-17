# CreateHierarchyRootNodeResponse

create a root node request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the hierarchy node. | 
**name** | **str** |  | 

## Example

```python
from onelens_backend_client.models.create_hierarchy_root_node_response import CreateHierarchyRootNodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHierarchyRootNodeResponse from a JSON string
create_hierarchy_root_node_response_instance = CreateHierarchyRootNodeResponse.from_json(json)
# print the JSON string representation of the object
print(CreateHierarchyRootNodeResponse.to_json())

# convert the object into a dict
create_hierarchy_root_node_response_dict = create_hierarchy_root_node_response_instance.to_dict()
# create an instance of CreateHierarchyRootNodeResponse from a dict
create_hierarchy_root_node_response_form_dict = create_hierarchy_root_node_response.from_dict(create_hierarchy_root_node_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


