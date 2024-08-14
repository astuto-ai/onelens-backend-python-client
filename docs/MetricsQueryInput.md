# MetricsQueryInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**metric_name** | **str** |  | 
**measures** | [**List[MetricsAggregationType]**](MetricsAggregationType.md) |  | 
**filters** | [**List[OnelensModelsServiceInterfacesTenantDataMetricsServiceFilterCriteriaInput]**](OnelensModelsServiceInterfacesTenantDataMetricsServiceFilterCriteriaInput.md) |  | 
**time_filter** | [**OnelensModelsServiceInterfacesTenantDataMetricsServiceTimeDimensionInput**](OnelensModelsServiceInterfacesTenantDataMetricsServiceTimeDimensionInput.md) |  | 
**timezone** | **str** |  | [optional] [default to 'Asia/Kolkata']

## Example

```python
from onelens_backend_client.models.metrics_query_input import MetricsQueryInput

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsQueryInput from a JSON string
metrics_query_input_instance = MetricsQueryInput.from_json(json)
# print the JSON string representation of the object
print(MetricsQueryInput.to_json())

# convert the object into a dict
metrics_query_input_dict = metrics_query_input_instance.to_dict()
# create an instance of MetricsQueryInput from a dict
metrics_query_input_form_dict = metrics_query_input.from_dict(metrics_query_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


