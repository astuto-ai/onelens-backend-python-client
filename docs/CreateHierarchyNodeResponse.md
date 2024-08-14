# CreateHierarchyNodeResponse

create a branch node response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**parent_id** | **str** |  | 
**category** | **str** |  | 
**resource_filters** | [**List[HierarchyNodeResourceFilters]**](HierarchyNodeResourceFilters.md) |  | [optional] 
**resource_filter_expression** | **str** |  | [optional] 
**is_shared** | **bool** | is this node a shared node or not. | [optional] [default to False]
**attribution_details** | [**HierarchyNodeAttributionDetails**](HierarchyNodeAttributionDetails.md) |  | [optional] 
**id** | **str** | The unique identifier of the hierarchy node. | 
**state** | [**HierarchyNodeState**](HierarchyNodeState.md) | The state of the hierarchy node. | 
**sql_filter** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.create_hierarchy_node_response import CreateHierarchyNodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHierarchyNodeResponse from a JSON string
create_hierarchy_node_response_instance = CreateHierarchyNodeResponse.from_json(json)
# print the JSON string representation of the object
print(CreateHierarchyNodeResponse.to_json())

# convert the object into a dict
create_hierarchy_node_response_dict = create_hierarchy_node_response_instance.to_dict()
# create an instance of CreateHierarchyNodeResponse from a dict
create_hierarchy_node_response_form_dict = create_hierarchy_node_response.from_dict(create_hierarchy_node_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


