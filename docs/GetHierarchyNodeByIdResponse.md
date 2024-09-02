# GetHierarchyNodeByIdResponse

get hierarchy node by id response

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
from onelens_backend_client.models.get_hierarchy_node_by_id_response import GetHierarchyNodeByIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHierarchyNodeByIdResponse from a JSON string
get_hierarchy_node_by_id_response_instance = GetHierarchyNodeByIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetHierarchyNodeByIdResponse.to_json())

# convert the object into a dict
get_hierarchy_node_by_id_response_dict = get_hierarchy_node_by_id_response_instance.to_dict()
# create an instance of GetHierarchyNodeByIdResponse from a dict
get_hierarchy_node_by_id_response_form_dict = get_hierarchy_node_by_id_response.from_dict(get_hierarchy_node_by_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


