# CreateHierarchyNodeAPIRequest

create a branch node api request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**parent_id** | **str** |  | 
**category** | [**OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory1**](OnelensModelsServiceInterfacesTenantMetadataCommonsHierarchyNodeCategory1.md) |  | 
**resource_filters** | [**List[HierarchyNodeResourceFilters]**](HierarchyNodeResourceFilters.md) |  | [optional] 
**resource_filter_expression** | **str** |  | [optional] 
**is_shared** | **bool** | is this node a shared node or not. | [optional] [default to False]
**attribution_details** | [**HierarchyNodeAttributionDetails**](HierarchyNodeAttributionDetails.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.create_hierarchy_node_api_request import CreateHierarchyNodeAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHierarchyNodeAPIRequest from a JSON string
create_hierarchy_node_api_request_instance = CreateHierarchyNodeAPIRequest.from_json(json)
# print the JSON string representation of the object
print(CreateHierarchyNodeAPIRequest.to_json())

# convert the object into a dict
create_hierarchy_node_api_request_dict = create_hierarchy_node_api_request_instance.to_dict()
# create an instance of CreateHierarchyNodeAPIRequest from a dict
create_hierarchy_node_api_request_form_dict = create_hierarchy_node_api_request.from_dict(create_hierarchy_node_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


