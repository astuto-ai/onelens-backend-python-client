# GetMetricsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**MetricsQuery**](MetricsQuery.md) |  | 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_metrics_request import GetMetricsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetricsRequest from a JSON string
get_metrics_request_instance = GetMetricsRequest.from_json(json)
# print the JSON string representation of the object
print(GetMetricsRequest.to_json())

# convert the object into a dict
get_metrics_request_dict = get_metrics_request_instance.to_dict()
# create an instance of GetMetricsRequest from a dict
get_metrics_request_form_dict = get_metrics_request.from_dict(get_metrics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


