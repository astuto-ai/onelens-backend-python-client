# HierarchyNodeEntityWithDetails

hierarchy node entity with path

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**category** | **str** |  | 
**resource_filters** | [**List[HierarchyNodeResourceFilters]**](HierarchyNodeResourceFilters.md) |  | [optional] 
**resource_filter_expression** | **str** |  | [optional] 
**is_shared** | **bool** | is this node a shared node or not. | [optional] [default to False]
**attribution_details** | [**HierarchyNodeAttributionDetails**](HierarchyNodeAttributionDetails.md) |  | [optional] 
**state** | [**HierarchyNodeState**](HierarchyNodeState.md) | The state of the hierarchy node. | 
**sql_filter** | **str** |  | [optional] 
**path** | [**List[HierarchyNodePathItem]**](HierarchyNodePathItem.md) | The path of the node from root. | 
**parent** | [**HierarchyNodeParentItem**](HierarchyNodeParentItem.md) |  | [optional] 
**resources_metrics** | [**HierarchyNodeResourceMetrics**](HierarchyNodeResourceMetrics.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.hierarchy_node_entity_with_details import HierarchyNodeEntityWithDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HierarchyNodeEntityWithDetails from a JSON string
hierarchy_node_entity_with_details_instance = HierarchyNodeEntityWithDetails.from_json(json)
# print the JSON string representation of the object
print(HierarchyNodeEntityWithDetails.to_json())

# convert the object into a dict
hierarchy_node_entity_with_details_dict = hierarchy_node_entity_with_details_instance.to_dict()
# create an instance of HierarchyNodeEntityWithDetails from a dict
hierarchy_node_entity_with_details_form_dict = hierarchy_node_entity_with_details.from_dict(hierarchy_node_entity_with_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


