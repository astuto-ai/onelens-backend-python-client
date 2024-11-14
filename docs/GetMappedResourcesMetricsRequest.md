# GetMappedResourcesMetricsRequest

get mapped resources metrics request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | The id of the node. | 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_mapped_resources_metrics_request import GetMappedResourcesMetricsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMappedResourcesMetricsRequest from a JSON string
get_mapped_resources_metrics_request_instance = GetMappedResourcesMetricsRequest.from_json(json)
# print the JSON string representation of the object
print(GetMappedResourcesMetricsRequest.to_json())

# convert the object into a dict
get_mapped_resources_metrics_request_dict = get_mapped_resources_metrics_request_instance.to_dict()
# create an instance of GetMappedResourcesMetricsRequest from a dict
get_mapped_resources_metrics_request_form_dict = get_mapped_resources_metrics_request.from_dict(get_mapped_resources_metrics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


