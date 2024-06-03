# ResourceHierarchyMappingRequest

dto for resource hierarchy mapping request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.resource_hierarchy_mapping_request import ResourceHierarchyMappingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceHierarchyMappingRequest from a JSON string
resource_hierarchy_mapping_request_instance = ResourceHierarchyMappingRequest.from_json(json)
# print the JSON string representation of the object
print(ResourceHierarchyMappingRequest.to_json())

# convert the object into a dict
resource_hierarchy_mapping_request_dict = resource_hierarchy_mapping_request_instance.to_dict()
# create an instance of ResourceHierarchyMappingRequest from a dict
resource_hierarchy_mapping_request_form_dict = resource_hierarchy_mapping_request.from_dict(resource_hierarchy_mapping_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


