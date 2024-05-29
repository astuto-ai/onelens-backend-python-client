# DataRetrieverResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**DataRetrieverQuery**](DataRetrieverQuery.md) |  | [optional] 
**data** | **List[object]** |  | [optional] 
**annotation** | **object** |  | [optional] 
**last_refresh_time** | **str** |  | [optional] 
**data_source** | **str** |  | [optional] 
**db_type** | **str** |  | [optional] 
**ext_db_type** | **str** |  | [optional] 
**external** | **bool** |  | [optional] 
**slow_query** | **bool** |  | [optional] 
**total** | **int** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.data_retriever_response import DataRetrieverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataRetrieverResponse from a JSON string
data_retriever_response_instance = DataRetrieverResponse.from_json(json)
# print the JSON string representation of the object
print(DataRetrieverResponse.to_json())

# convert the object into a dict
data_retriever_response_dict = data_retriever_response_instance.to_dict()
# create an instance of DataRetrieverResponse from a dict
data_retriever_response_form_dict = data_retriever_response.from_dict(data_retriever_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


