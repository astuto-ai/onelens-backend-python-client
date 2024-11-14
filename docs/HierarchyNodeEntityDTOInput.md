# HierarchyNodeEntityDTOInput

Hierarchy Node Entity in the JSON data

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
**description** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_by** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.hierarchy_node_entity_dto_input import HierarchyNodeEntityDTOInput

# TODO update the JSON string below
json = "{}"
# create an instance of HierarchyNodeEntityDTOInput from a JSON string
hierarchy_node_entity_dto_input_instance = HierarchyNodeEntityDTOInput.from_json(json)
# print the JSON string representation of the object
print(HierarchyNodeEntityDTOInput.to_json())

# convert the object into a dict
hierarchy_node_entity_dto_input_dict = hierarchy_node_entity_dto_input_instance.to_dict()
# create an instance of HierarchyNodeEntityDTOInput from a dict
hierarchy_node_entity_dto_input_form_dict = hierarchy_node_entity_dto_input.from_dict(hierarchy_node_entity_dto_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


