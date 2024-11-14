# UpdateHierarchyNodeResponse

update a branch node response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**name** | **str** |  | 
**parent_id** | **str** |  | 
**category** | **str** |  | 
**resource_filters** | [**List[HierarchyNodeResourceFilters]**](HierarchyNodeResourceFilters.md) |  | [optional] 
**resource_filter_expression** | **str** |  | [optional] 
**is_shared** | **bool** | is this node a shared node or not. | [optional] [default to False]
**attribution_details** | [**HierarchyNodeAttributionDetails**](HierarchyNodeAttributionDetails.md) |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **str** | The unique identifier of the hierarchy node. | 
**state** | [**HierarchyNodeState**](HierarchyNodeState.md) | The state of the hierarchy node. | 
**sql_filter** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.update_hierarchy_node_response import UpdateHierarchyNodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHierarchyNodeResponse from a JSON string
update_hierarchy_node_response_instance = UpdateHierarchyNodeResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateHierarchyNodeResponse.to_json())

# convert the object into a dict
update_hierarchy_node_response_dict = update_hierarchy_node_response_instance.to_dict()
# create an instance of UpdateHierarchyNodeResponse from a dict
update_hierarchy_node_response_form_dict = update_hierarchy_node_response.from_dict(update_hierarchy_node_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


