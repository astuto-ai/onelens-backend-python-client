# HierarchyNodeResourceMetrics

hierarchy node resource metrics like unique count and conflict count of resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The total count of the resource. | 
**unique** | **int** |  | [optional] 
**conflicting** | **int** |  | [optional] 

## Example

```python
from onelens_backend_client.models.hierarchy_node_resource_metrics import HierarchyNodeResourceMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of HierarchyNodeResourceMetrics from a JSON string
hierarchy_node_resource_metrics_instance = HierarchyNodeResourceMetrics.from_json(json)
# print the JSON string representation of the object
print(HierarchyNodeResourceMetrics.to_json())

# convert the object into a dict
hierarchy_node_resource_metrics_dict = hierarchy_node_resource_metrics_instance.to_dict()
# create an instance of HierarchyNodeResourceMetrics from a dict
hierarchy_node_resource_metrics_form_dict = hierarchy_node_resource_metrics.from_dict(hierarchy_node_resource_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


