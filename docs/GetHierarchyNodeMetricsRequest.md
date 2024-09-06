# GetHierarchyNodeMetricsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The id of the tenant. | 
**node_ids** | **List[str]** | The ids of the nodes. | 
**breakdown** | **bool** | Whether to breakdown the metrics. | [optional] [default to False]

## Example

```python
from onelens_backend_client.models.get_hierarchy_node_metrics_request import GetHierarchyNodeMetricsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetHierarchyNodeMetricsRequest from a JSON string
get_hierarchy_node_metrics_request_instance = GetHierarchyNodeMetricsRequest.from_json(json)
# print the JSON string representation of the object
print(GetHierarchyNodeMetricsRequest.to_json())

# convert the object into a dict
get_hierarchy_node_metrics_request_dict = get_hierarchy_node_metrics_request_instance.to_dict()
# create an instance of GetHierarchyNodeMetricsRequest from a dict
get_hierarchy_node_metrics_request_form_dict = get_hierarchy_node_metrics_request.from_dict(get_hierarchy_node_metrics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


