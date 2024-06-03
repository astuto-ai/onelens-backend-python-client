# ResponseGetMetricsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetMetricsResponse**](GetMetricsResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_metrics_response import ResponseGetMetricsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetMetricsResponse from a JSON string
response_get_metrics_response_instance = ResponseGetMetricsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetMetricsResponse.to_json())

# convert the object into a dict
response_get_metrics_response_dict = response_get_metrics_response_instance.to_dict()
# create an instance of ResponseGetMetricsResponse from a dict
response_get_metrics_response_form_dict = response_get_metrics_response.from_dict(response_get_metrics_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


