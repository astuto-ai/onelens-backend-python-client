# CreateResourceHierarchyMappingsFromQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 
**query** | **str** |  | [optional] 
**node_id** | **str** | Resource Catalog Ol Id | 

## Example

```python
from onelens_backend_client.models.create_resource_hierarchy_mappings_from_query_request import CreateResourceHierarchyMappingsFromQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateResourceHierarchyMappingsFromQueryRequest from a JSON string
create_resource_hierarchy_mappings_from_query_request_instance = CreateResourceHierarchyMappingsFromQueryRequest.from_json(json)
# print the JSON string representation of the object
print(CreateResourceHierarchyMappingsFromQueryRequest.to_json())

# convert the object into a dict
create_resource_hierarchy_mappings_from_query_request_dict = create_resource_hierarchy_mappings_from_query_request_instance.to_dict()
# create an instance of CreateResourceHierarchyMappingsFromQueryRequest from a dict
create_resource_hierarchy_mappings_from_query_request_form_dict = create_resource_hierarchy_mappings_from_query_request.from_dict(create_resource_hierarchy_mappings_from_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


