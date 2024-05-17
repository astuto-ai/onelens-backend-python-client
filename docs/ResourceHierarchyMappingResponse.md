# ResourceHierarchyMappingResponse

dto for resource hierarchy mapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hierarchy_node_id** | **str** | List of hierarchy node ids for the resource mapping | 
**resource_id** | **str** | List of resource ids for the resource mapping | 

## Example

```python
from onelens_backend_client.models.resource_hierarchy_mapping_response import ResourceHierarchyMappingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceHierarchyMappingResponse from a JSON string
resource_hierarchy_mapping_response_instance = ResourceHierarchyMappingResponse.from_json(json)
# print the JSON string representation of the object
print(ResourceHierarchyMappingResponse.to_json())

# convert the object into a dict
resource_hierarchy_mapping_response_dict = resource_hierarchy_mapping_response_instance.to_dict()
# create an instance of ResourceHierarchyMappingResponse from a dict
resource_hierarchy_mapping_response_form_dict = resource_hierarchy_mapping_response.from_dict(resource_hierarchy_mapping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


