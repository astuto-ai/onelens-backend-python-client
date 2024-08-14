# HierarchyNodeEntityDTO

Hierarchy Node Entity in the JSON data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**category** | [**OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory1**](OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory1.md) |  | 
**resource_filters** | [**List[HierarchyNodeResourceFilters]**](HierarchyNodeResourceFilters.md) |  | [optional] 
**resource_filter_expression** | **str** |  | [optional] 
**is_shared** | **bool** | is this node a shared node or not. | [optional] [default to False]
**attribution_details** | [**HierarchyNodeAttributionDetails**](HierarchyNodeAttributionDetails.md) |  | [optional] 
**state** | [**HierarchyNodeState**](HierarchyNodeState.md) | The state of the hierarchy node. | 
**sql_filter** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.hierarchy_node_entity_dto import HierarchyNodeEntityDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HierarchyNodeEntityDTO from a JSON string
hierarchy_node_entity_dto_instance = HierarchyNodeEntityDTO.from_json(json)
# print the JSON string representation of the object
print(HierarchyNodeEntityDTO.to_json())

# convert the object into a dict
hierarchy_node_entity_dto_dict = hierarchy_node_entity_dto_instance.to_dict()
# create an instance of HierarchyNodeEntityDTO from a dict
hierarchy_node_entity_dto_form_dict = hierarchy_node_entity_dto.from_dict(hierarchy_node_entity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


