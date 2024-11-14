# ReCreateResourceHierarchyMappingsRequest

re create resource hierarchy mappings request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.re_create_resource_hierarchy_mappings_request import ReCreateResourceHierarchyMappingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReCreateResourceHierarchyMappingsRequest from a JSON string
re_create_resource_hierarchy_mappings_request_instance = ReCreateResourceHierarchyMappingsRequest.from_json(json)
# print the JSON string representation of the object
print(ReCreateResourceHierarchyMappingsRequest.to_json())

# convert the object into a dict
re_create_resource_hierarchy_mappings_request_dict = re_create_resource_hierarchy_mappings_request_instance.to_dict()
# create an instance of ReCreateResourceHierarchyMappingsRequest from a dict
re_create_resource_hierarchy_mappings_request_form_dict = re_create_resource_hierarchy_mappings_request.from_dict(re_create_resource_hierarchy_mappings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


