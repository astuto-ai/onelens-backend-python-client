# GetResourceHierarchyMappingByOlIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_catalog_ol_id** | **str** | Resource Catalog Ol Id | 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_resource_hierarchy_mapping_by_ol_id_request import GetResourceHierarchyMappingByOlIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceHierarchyMappingByOlIdRequest from a JSON string
get_resource_hierarchy_mapping_by_ol_id_request_instance = GetResourceHierarchyMappingByOlIdRequest.from_json(json)
# print the JSON string representation of the object
print(GetResourceHierarchyMappingByOlIdRequest.to_json())

# convert the object into a dict
get_resource_hierarchy_mapping_by_ol_id_request_dict = get_resource_hierarchy_mapping_by_ol_id_request_instance.to_dict()
# create an instance of GetResourceHierarchyMappingByOlIdRequest from a dict
get_resource_hierarchy_mapping_by_ol_id_request_form_dict = get_resource_hierarchy_mapping_by_ol_id_request.from_dict(get_resource_hierarchy_mapping_by_ol_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


