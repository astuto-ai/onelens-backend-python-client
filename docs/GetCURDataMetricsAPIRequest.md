# GetCURDataMetricsAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**CURDataMetricsQuery**](CURDataMetricsQuery.md) |  | 

## Example

```python
from onelens_backend_client.models.get_cur_data_metrics_api_request import GetCURDataMetricsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetCURDataMetricsAPIRequest from a JSON string
get_cur_data_metrics_api_request_instance = GetCURDataMetricsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(GetCURDataMetricsAPIRequest.to_json())

# convert the object into a dict
get_cur_data_metrics_api_request_dict = get_cur_data_metrics_api_request_instance.to_dict()
# create an instance of GetCURDataMetricsAPIRequest from a dict
get_cur_data_metrics_api_request_form_dict = get_cur_data_metrics_api_request.from_dict(get_cur_data_metrics_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


