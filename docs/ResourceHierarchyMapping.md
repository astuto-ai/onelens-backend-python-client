# ResourceHierarchyMapping

dto for resource hierarchy mapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hierarchy_node_id** | **str** | List of hierarchy node ids for the resource mapping | 
**resource_id** | **str** | List of resource ids for the resource mapping | 

## Example

```python
from onelens_backend_client.models.resource_hierarchy_mapping import ResourceHierarchyMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceHierarchyMapping from a JSON string
resource_hierarchy_mapping_instance = ResourceHierarchyMapping.from_json(json)
# print the JSON string representation of the object
print(ResourceHierarchyMapping.to_json())

# convert the object into a dict
resource_hierarchy_mapping_dict = resource_hierarchy_mapping_instance.to_dict()
# create an instance of ResourceHierarchyMapping from a dict
resource_hierarchy_mapping_form_dict = resource_hierarchy_mapping.from_dict(resource_hierarchy_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


