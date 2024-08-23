# GetMutipleMetricsAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | [**List[MetricsQueryInput]**](MetricsQueryInput.md) | The list of queries. | 

## Example

```python
from onelens_backend_client.models.get_mutiple_metrics_api_request import GetMutipleMetricsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMutipleMetricsAPIRequest from a JSON string
get_mutiple_metrics_api_request_instance = GetMutipleMetricsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetMutipleMetricsAPIRequest.to_json())

# convert the object into a dict
get_mutiple_metrics_api_request_dict = get_mutiple_metrics_api_request_instance.to_dict()
# create an instance of GetMutipleMetricsAPIRequest from a dict
get_mutiple_metrics_api_request_form_dict = get_mutiple_metrics_api_request.from_dict(get_mutiple_metrics_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


