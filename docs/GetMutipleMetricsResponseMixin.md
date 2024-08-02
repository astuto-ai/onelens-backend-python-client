# GetMutipleMetricsResponseMixin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**MetricsQueryOutput**](MetricsQueryOutput.md) | Query for the metric | 
**metrics** | [**List[Metric]**](Metric.md) |  | 
**unit** | **str** |  | 

## Example

```python
from onelens_backend_client.models.get_mutiple_metrics_response_mixin import GetMutipleMetricsResponseMixin

# TODO update the JSON string below
json = "{}"
# create an instance of GetMutipleMetricsResponseMixin from a JSON string
get_mutiple_metrics_response_mixin_instance = GetMutipleMetricsResponseMixin.from_json(json)
# print the JSON string representation of the object
print(GetMutipleMetricsResponseMixin.to_json())

# convert the object into a dict
get_mutiple_metrics_response_mixin_dict = get_mutiple_metrics_response_mixin_instance.to_dict()
# create an instance of GetMutipleMetricsResponseMixin from a dict
get_mutiple_metrics_response_mixin_form_dict = get_mutiple_metrics_response_mixin.from_dict(get_mutiple_metrics_response_mixin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


