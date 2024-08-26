# CURDataQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**dimension** | **str** |  | [optional] 
**measures** | [**List[CurDataAggregationType]**](CurDataAggregationType.md) |  | 
**filters** | [**List[OnelensModelsServiceInterfacesTenantDataCurServiceFilterCriteria]**](OnelensModelsServiceInterfacesTenantDataCurServiceFilterCriteria.md) |  | 
**time_filter** | [**OnelensModelsServiceInterfacesTenantDataCurServiceTimeDimension**](OnelensModelsServiceInterfacesTenantDataCurServiceTimeDimension.md) |  | 
**timezone** | **str** |  | [optional] [default to 'Asia/Kolkata']

## Example

```python
from onelens_backend_client.models.cur_data_query import CURDataQuery

# TODO update the JSON string below
json = "{}"
# create an instance of CURDataQuery from a JSON string
cur_data_query_instance = CURDataQuery.from_json(json)
# print the JSON string representation of the object
print(CURDataQuery.to_json())

# convert the object into a dict
cur_data_query_dict = cur_data_query_instance.to_dict()
# create an instance of CURDataQuery from a dict
cur_data_query_form_dict = cur_data_query.from_dict(cur_data_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


