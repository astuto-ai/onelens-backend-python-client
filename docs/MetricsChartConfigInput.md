# MetricsChartConfigInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_title** | **str** | The title of the chart. | 
**chart_type** | **str** | The type of the chart. | 
**chart_data_tooltip** | **str** |  | [optional] 
**table_name** | **str** | The name of the table. | 
**metric_name** | **str** | The name of the metric. | 
**aggregation_type** | [**MetricsAggregationType**](MetricsAggregationType.md) | The aggregation type of the metric. | 
**look_back_period** | [**MetricsLookBackPeriod**](MetricsLookBackPeriod.md) |  | [optional] 
**threshold** | [**MetricsThreshold**](MetricsThreshold.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.metrics_chart_config_input import MetricsChartConfigInput

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsChartConfigInput from a JSON string
metrics_chart_config_input_instance = MetricsChartConfigInput.from_json(json)
# print the JSON string representation of the object
print(MetricsChartConfigInput.to_json())

# convert the object into a dict
metrics_chart_config_input_dict = metrics_chart_config_input_instance.to_dict()
# create an instance of MetricsChartConfigInput from a dict
metrics_chart_config_input_form_dict = metrics_chart_config_input.from_dict(metrics_chart_config_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


