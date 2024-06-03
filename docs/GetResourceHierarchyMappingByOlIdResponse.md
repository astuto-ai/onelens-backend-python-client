# GetResourceHierarchyMappingByOlIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_catalog_ol_id** | **str** | Resource Catalog Ol Id | 
**node_id** | **str** | The id of the node. | 

## Example

```python
from onelens_backend_client.models.get_resource_hierarchy_mapping_by_ol_id_response import GetResourceHierarchyMappingByOlIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetResourceHierarchyMappingByOlIdResponse from a JSON string
get_resource_hierarchy_mapping_by_ol_id_response_instance = GetResourceHierarchyMappingByOlIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetResourceHierarchyMappingByOlIdResponse.to_json())

# convert the object into a dict
get_resource_hierarchy_mapping_by_ol_id_response_dict = get_resource_hierarchy_mapping_by_ol_id_response_instance.to_dict()
# create an instance of GetResourceHierarchyMappingByOlIdResponse from a dict
get_resource_hierarchy_mapping_by_ol_id_response_form_dict = get_resource_hierarchy_mapping_by_ol_id_response.from_dict(get_resource_hierarchy_mapping_by_ol_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


