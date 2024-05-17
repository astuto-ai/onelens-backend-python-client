# CreateHierarchyRootNodeAPIRequest

create root node api request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from onelens_backend_client.models.create_hierarchy_root_node_api_request import CreateHierarchyRootNodeAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHierarchyRootNodeAPIRequest from a JSON string
create_hierarchy_root_node_api_request_instance = CreateHierarchyRootNodeAPIRequest.from_json(json)
# print the JSON string representation of the object
print(CreateHierarchyRootNodeAPIRequest.to_json())

# convert the object into a dict
create_hierarchy_root_node_api_request_dict = create_hierarchy_root_node_api_request_instance.to_dict()
# create an instance of CreateHierarchyRootNodeAPIRequest from a dict
create_hierarchy_root_node_api_request_form_dict = create_hierarchy_root_node_api_request.from_dict(create_hierarchy_root_node_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


