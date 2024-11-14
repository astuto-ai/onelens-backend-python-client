# HierarchyNodeResourceFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **int** |  | 
**var_field** | **str** |  | 
**operator** | **str** |  | 
**value** | [**Value1**](Value1.md) |  | 
**json_key** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.hierarchy_node_resource_filters import HierarchyNodeResourceFilters

# TODO update the JSON string below
json = "{}"
# create an instance of HierarchyNodeResourceFilters from a JSON string
hierarchy_node_resource_filters_instance = HierarchyNodeResourceFilters.from_json(json)
# print the JSON string representation of the object
print(HierarchyNodeResourceFilters.to_json())

# convert the object into a dict
hierarchy_node_resource_filters_dict = hierarchy_node_resource_filters_instance.to_dict()
# create an instance of HierarchyNodeResourceFilters from a dict
hierarchy_node_resource_filters_form_dict = hierarchy_node_resource_filters.from_dict(hierarchy_node_resource_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


