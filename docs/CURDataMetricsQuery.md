# CURDataMetricsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**dimension** | **str** |  | [optional] 
**measures** | [**List[CURDataAggregationType]**](CURDataAggregationType.md) |  | 
**filters** | [**List[OnelensModelsServiceInterfacesTenantDataCurServiceFilterCriteria]**](OnelensModelsServiceInterfacesTenantDataCurServiceFilterCriteria.md) |  | 
**time_filter** | [**OnelensModelsServiceInterfacesTenantDataCurServiceTimeDimension**](OnelensModelsServiceInterfacesTenantDataCurServiceTimeDimension.md) |  | 
**timezone** | **str** |  | [optional] [default to 'Asia/Kolkata']

## Example

```python
from onelens_backend_client.models.cur_data_metrics_query import CURDataMetricsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of CURDataMetricsQuery from a JSON string
cur_data_metrics_query_instance = CURDataMetricsQuery.from_json(json)
# print the JSON string representation of the object
print(CURDataMetricsQuery.to_json())

# convert the object into a dict
cur_data_metrics_query_dict = cur_data_metrics_query_instance.to_dict()
# create an instance of CURDataMetricsQuery from a dict
cur_data_metrics_query_form_dict = cur_data_metrics_query.from_dict(cur_data_metrics_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


