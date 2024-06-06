# MetricsLookBackPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value_from** | **str** | value from for the look back. | 
**value** | [**MetricsValueUnit**](MetricsValueUnit.md) | The value of the look back. | 

## Example

```python
from onelens_backend_client.models.metrics_look_back_period import MetricsLookBackPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsLookBackPeriod from a JSON string
metrics_look_back_period_instance = MetricsLookBackPeriod.from_json(json)
# print the JSON string representation of the object
print(MetricsLookBackPeriod.to_json())

# convert the object into a dict
metrics_look_back_period_dict = metrics_look_back_period_instance.to_dict()
# create an instance of MetricsLookBackPeriod from a dict
metrics_look_back_period_form_dict = metrics_look_back_period.from_dict(metrics_look_back_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


