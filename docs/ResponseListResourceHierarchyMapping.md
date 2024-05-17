# ResponseListResourceHierarchyMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ResourceHierarchyMapping]**](ResourceHierarchyMapping.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_list_resource_hierarchy_mapping import ResponseListResourceHierarchyMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseListResourceHierarchyMapping from a JSON string
response_list_resource_hierarchy_mapping_instance = ResponseListResourceHierarchyMapping.from_json(json)
# print the JSON string representation of the object
print(ResponseListResourceHierarchyMapping.to_json())

# convert the object into a dict
response_list_resource_hierarchy_mapping_dict = response_list_resource_hierarchy_mapping_instance.to_dict()
# create an instance of ResponseListResourceHierarchyMapping from a dict
response_list_resource_hierarchy_mapping_form_dict = response_list_resource_hierarchy_mapping.from_dict(response_list_resource_hierarchy_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


