# ViolationMetricsDetails


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
**filter** | [**List[MetricChartFilters]**](MetricChartFilters.md) |  | [optional] 
**threshold** | [**MetricsThreshold**](MetricsThreshold.md) |  | [optional] 
**query** | [**MetricsQueryOutput**](MetricsQueryOutput.md) | Query for the metric | 

## Example

```python
from onelens_backend_client.models.violation_metrics_details import ViolationMetricsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ViolationMetricsDetails from a JSON string
violation_metrics_details_instance = ViolationMetricsDetails.from_json(json)
# print the JSON string representation of the object
print(ViolationMetricsDetails.to_json())

# convert the object into a dict
violation_metrics_details_dict = violation_metrics_details_instance.to_dict()
# create an instance of ViolationMetricsDetails from a dict
violation_metrics_details_form_dict = violation_metrics_details.from_dict(violation_metrics_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


