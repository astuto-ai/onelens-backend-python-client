# MetricsThreshold


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_from** | **str** | value_from for the threshold. | 
**value** | [**MetricsValueUnit**](MetricsValueUnit.md) | The value of the threshold. | 

## Example

```python
from onelens_backend_client.models.metrics_threshold import MetricsThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsThreshold from a JSON string
metrics_threshold_instance = MetricsThreshold.from_json(json)
# print the JSON string representation of the object
print(MetricsThreshold.to_json())

# convert the object into a dict
metrics_threshold_dict = metrics_threshold_instance.to_dict()
# create an instance of MetricsThreshold from a dict
metrics_threshold_form_dict = metrics_threshold.from_dict(metrics_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


