# ResponseResourceHierarchyMappingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | dto for resource hierarchy mapping | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_resource_hierarchy_mapping_response import ResponseResourceHierarchyMappingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseResourceHierarchyMappingResponse from a JSON string
response_resource_hierarchy_mapping_response_instance = ResponseResourceHierarchyMappingResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseResourceHierarchyMappingResponse.to_json())

# convert the object into a dict
response_resource_hierarchy_mapping_response_dict = response_resource_hierarchy_mapping_response_instance.to_dict()
# create an instance of ResponseResourceHierarchyMappingResponse from a dict
response_resource_hierarchy_mapping_response_form_dict = response_resource_hierarchy_mapping_response.from_dict(response_resource_hierarchy_mapping_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


