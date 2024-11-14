# GetMappedResourcesMetricsAPIRequest

get mapped resources metrics api request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** | The id of the node. | 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 

## Example

```python
from onelens_backend_client.models.get_mapped_resources_metrics_api_request import GetMappedResourcesMetricsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMappedResourcesMetricsAPIRequest from a JSON string
get_mapped_resources_metrics_api_request_instance = GetMappedResourcesMetricsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetMappedResourcesMetricsAPIRequest.to_json())

# convert the object into a dict
get_mapped_resources_metrics_api_request_dict = get_mapped_resources_metrics_api_request_instance.to_dict()
# create an instance of GetMappedResourcesMetricsAPIRequest from a dict
get_mapped_resources_metrics_api_request_form_dict = get_mapped_resources_metrics_api_request.from_dict(get_mapped_resources_metrics_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


