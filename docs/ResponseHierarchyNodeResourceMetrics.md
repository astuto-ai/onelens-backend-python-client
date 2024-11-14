# ResponseHierarchyNodeResourceMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**HierarchyNodeResourceMetrics**](HierarchyNodeResourceMetrics.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_hierarchy_node_resource_metrics import ResponseHierarchyNodeResourceMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseHierarchyNodeResourceMetrics from a JSON string
response_hierarchy_node_resource_metrics_instance = ResponseHierarchyNodeResourceMetrics.from_json(json)
# print the JSON string representation of the object
print(ResponseHierarchyNodeResourceMetrics.to_json())

# convert the object into a dict
response_hierarchy_node_resource_metrics_dict = response_hierarchy_node_resource_metrics_instance.to_dict()
# create an instance of ResponseHierarchyNodeResourceMetrics from a dict
response_hierarchy_node_resource_metrics_form_dict = response_hierarchy_node_resource_metrics.from_dict(response_hierarchy_node_resource_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


