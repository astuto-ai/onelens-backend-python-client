# GetMetricsAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**MetricsQuery**](MetricsQuery.md) |  | 

## Example

```python
from onelens_backend_client.models.get_metrics_api_request import GetMetricsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetricsAPIRequest from a JSON string
get_metrics_api_request_instance = GetMetricsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetMetricsAPIRequest.to_json())

# convert the object into a dict
get_metrics_api_request_dict = get_metrics_api_request_instance.to_dict()
# create an instance of GetMetricsAPIRequest from a dict
get_metrics_api_request_form_dict = get_metrics_api_request.from_dict(get_metrics_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


