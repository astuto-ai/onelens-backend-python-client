# GetMutipleMetricsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[GetMutipleMetricsResponseMixin]**](GetMutipleMetricsResponseMixin.md) |  | 

## Example

```python
from onelens_backend_client.models.get_mutiple_metrics_response import GetMutipleMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMutipleMetricsResponse from a JSON string
get_mutiple_metrics_response_instance = GetMutipleMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(GetMutipleMetricsResponse.to_json())

# convert the object into a dict
get_mutiple_metrics_response_dict = get_mutiple_metrics_response_instance.to_dict()
# create an instance of GetMutipleMetricsResponse from a dict
get_mutiple_metrics_response_form_dict = get_mutiple_metrics_response.from_dict(get_mutiple_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


