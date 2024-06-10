# MetricsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**metric_name** | **str** |  | 
**measures** | [**List[MetricsAggregationType]**](MetricsAggregationType.md) |  | 
**filters** | [**List[OnelensModelsServiceInterfacesTenantDataMetricsServiceFilterCriteria]**](OnelensModelsServiceInterfacesTenantDataMetricsServiceFilterCriteria.md) |  | 
**time_filter** | [**OnelensModelsServiceInterfacesTenantDataMetricsServiceTimeDimension**](OnelensModelsServiceInterfacesTenantDataMetricsServiceTimeDimension.md) |  | 
**timezone** | **str** |  | [optional] [default to 'Asia/Kolkata']

## Example

```python
from onelens_backend_client.models.metrics_query import MetricsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of MetricsQuery from a JSON string
metrics_query_instance = MetricsQuery.from_json(json)
# print the JSON string representation of the object
print(MetricsQuery.to_json())

# convert the object into a dict
metrics_query_dict = metrics_query_instance.to_dict()
# create an instance of MetricsQuery from a dict
metrics_query_form_dict = metrics_query.from_dict(metrics_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


