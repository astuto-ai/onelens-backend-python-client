# MetricsQueryOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**metric_name** | **str** |  | 
**measures** | [**List[MetricsAggregationType]**](MetricsAggregationType.md) |  | 
**filters** | [**List[FilterCriteriaOutput]**](FilterCriteriaOutput.md) |  | 
**time_filter** | [**OnelensModelsServiceInterfacesTenantDataMetricsServiceTimeDimension**](OnelensModelsServiceInterfacesTenantDataMetricsServiceTimeDimension.md) |  | 
**timezone** | **str** |  | [optional] [default to 'Asia/Kolkata']

## Example

```python
from onelens_backend_client.models.metrics_query_output import MetricsQueryOutput

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsQueryOutput from a JSON string
metrics_query_output_instance = MetricsQueryOutput.from_json(json)
# print the JSON string representation of the object
print(MetricsQueryOutput.to_json())

# convert the object into a dict
metrics_query_output_dict = metrics_query_output_instance.to_dict()
# create an instance of MetricsQueryOutput from a dict
metrics_query_output_form_dict = metrics_query_output.from_dict(metrics_query_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


