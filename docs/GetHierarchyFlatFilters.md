# GetHierarchyFlatFilters

get hierarchy flat filters request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_leaf** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**parent_names** | **List[str]** |  | [optional] 
**has_conflict** | **List[bool]** |  | [optional] 
**node_category** | [**List[OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory2]**](OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory2.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_hierarchy_flat_filters import GetHierarchyFlatFilters

# TODO update the JSON string below
json = "{}"
# create an instance of GetHierarchyFlatFilters from a JSON string
get_hierarchy_flat_filters_instance = GetHierarchyFlatFilters.from_json(json)
# print the JSON string representation of the object
print(GetHierarchyFlatFilters.to_json())

# convert the object into a dict
get_hierarchy_flat_filters_dict = get_hierarchy_flat_filters_instance.to_dict()
# create an instance of GetHierarchyFlatFilters from a dict
get_hierarchy_flat_filters_form_dict = get_hierarchy_flat_filters.from_dict(get_hierarchy_flat_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


