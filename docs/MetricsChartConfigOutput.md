# MetricsChartConfigOutput


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
from onelens_backend_client.models.metrics_chart_config_output import MetricsChartConfigOutput

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsChartConfigOutput from a JSON string
metrics_chart_config_output_instance = MetricsChartConfigOutput.from_json(json)
# print the JSON string representation of the object
print(MetricsChartConfigOutput.to_json())

# convert the object into a dict
metrics_chart_config_output_dict = metrics_chart_config_output_instance.to_dict()
# create an instance of MetricsChartConfigOutput from a dict
metrics_chart_config_output_form_dict = metrics_chart_config_output.from_dict(metrics_chart_config_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


