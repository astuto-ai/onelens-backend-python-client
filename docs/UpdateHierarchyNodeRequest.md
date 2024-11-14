# UpdateHierarchyNodeRequest

update a branch node request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**resource_filters** | [**List[HierarchyNodeResourceFilters]**](HierarchyNodeResourceFilters.md) |  | [optional] 
**resource_filter_expression** | **str** |  | [optional] 
**is_shared** | **bool** |  | [optional] 
**attribution_details** | [**HierarchyNodeAttributionDetails**](HierarchyNodeAttributionDetails.md) |  | [optional] 
**description** | **str** |  | [optional] 
**node_id** | **str** | The id of the node. | 
**tenant_id** | **str** | The id of the tenant. | 
**updated_by** | **str** | The id of the user updating the node. | 

## Example

```python
from onelens_backend_client.models.update_hierarchy_node_request import UpdateHierarchyNodeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHierarchyNodeRequest from a JSON string
update_hierarchy_node_request_instance = UpdateHierarchyNodeRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateHierarchyNodeRequest.to_json())

# convert the object into a dict
update_hierarchy_node_request_dict = update_hierarchy_node_request_instance.to_dict()
# create an instance of UpdateHierarchyNodeRequest from a dict
update_hierarchy_node_request_form_dict = update_hierarchy_node_request.from_dict(update_hierarchy_node_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


