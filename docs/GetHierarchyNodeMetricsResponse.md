# GetHierarchyNodeMetricsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**Dict[str, HierarchyNodeResourceMetrics]**](HierarchyNodeResourceMetrics.md) | The metrics of the nodes. | 

## Example

```python
from onelens_backend_client.models.get_hierarchy_node_metrics_response import GetHierarchyNodeMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHierarchyNodeMetricsResponse from a JSON string
get_hierarchy_node_metrics_response_instance = GetHierarchyNodeMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(GetHierarchyNodeMetricsResponse.to_json())

# convert the object into a dict
get_hierarchy_node_metrics_response_dict = get_hierarchy_node_metrics_response_instance.to_dict()
# create an instance of GetHierarchyNodeMetricsResponse from a dict
get_hierarchy_node_metrics_response_form_dict = get_hierarchy_node_metrics_response.from_dict(get_hierarchy_node_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


