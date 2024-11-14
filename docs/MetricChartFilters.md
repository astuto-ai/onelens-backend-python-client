# MetricChartFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Dynamic key-value pairs for metric filters | 
**value_from** | **str** |  | [optional] 
**value** | [**Value2**](Value2.md) |  | [optional] 
**operator** | [**OnelensModelsServiceInterfacesPoliciesCommonsOperator**](OnelensModelsServiceInterfacesPoliciesCommonsOperator.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.metric_chart_filters import MetricChartFilters

# TODO update the JSON string below
json = "{}"
# create an instance of MetricChartFilters from a JSON string
metric_chart_filters_instance = MetricChartFilters.from_json(json)
# print the JSON string representation of the object
print(MetricChartFilters.to_json())

# convert the object into a dict
metric_chart_filters_dict = metric_chart_filters_instance.to_dict()
# create an instance of MetricChartFilters from a dict
metric_chart_filters_form_dict = metric_chart_filters.from_dict(metric_chart_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


