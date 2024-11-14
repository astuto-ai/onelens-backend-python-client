# GetMetricsCountRequest

get metrics count request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**resource_filters** | [**List[HierarchyNodeResourceFilters]**](HierarchyNodeResourceFilters.md) |  | [optional] 
**resource_filter_expression** | **str** |  | [optional] 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_metrics_count_request import GetMetricsCountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetricsCountRequest from a JSON string
get_metrics_count_request_instance = GetMetricsCountRequest.from_json(json)
# print the JSON string representation of the object
print(GetMetricsCountRequest.to_json())

# convert the object into a dict
get_metrics_count_request_dict = get_metrics_count_request_instance.to_dict()
# create an instance of GetMetricsCountRequest from a dict
get_metrics_count_request_form_dict = get_metrics_count_request.from_dict(get_metrics_count_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


