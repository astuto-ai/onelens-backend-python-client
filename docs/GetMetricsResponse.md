# GetMetricsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[OnelensModelsServiceInterfacesTenantDataMetricsServiceMetric]**](OnelensModelsServiceInterfacesTenantDataMetricsServiceMetric.md) |  | 
**unit** | **str** |  | 

## Example

```python
from onelens_backend_client.models.get_metrics_response import GetMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetricsResponse from a JSON string
get_metrics_response_instance = GetMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(GetMetricsResponse.to_json())

# convert the object into a dict
get_metrics_response_dict = get_metrics_response_instance.to_dict()
# create an instance of GetMetricsResponse from a dict
get_metrics_response_form_dict = get_metrics_response.from_dict(get_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


