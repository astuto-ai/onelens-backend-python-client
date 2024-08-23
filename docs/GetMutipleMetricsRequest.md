# GetMutipleMetricsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | [**List[MetricsQueryInput]**](MetricsQueryInput.md) | The list of queries. | 
**tenant_id** | **str** | The id of the tenant. | 

## Example

```python
from onelens_backend_client.models.get_mutiple_metrics_request import GetMutipleMetricsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetMutipleMetricsRequest from a JSON string
get_mutiple_metrics_request_instance = GetMutipleMetricsRequest.from_json(json)
# print the JSON string representation of the object
print(GetMutipleMetricsRequest.to_json())

# convert the object into a dict
get_mutiple_metrics_request_dict = get_mutiple_metrics_request_instance.to_dict()
# create an instance of GetMutipleMetricsRequest from a dict
get_mutiple_metrics_request_form_dict = get_mutiple_metrics_request.from_dict(get_mutiple_metrics_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


