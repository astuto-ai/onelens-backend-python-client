# DataRetrieverQueryOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**measures** | **List[str]** |  | [optional] 
**dimensions** | **List[str]** |  | [optional] 
**filters** | [**List[QueryFilters]**](QueryFilters.md) |  | [optional] 
**time_dimensions** | [**List[TimeDimensionOutput]**](TimeDimensionOutput.md) |  | [optional] 
**segments** | **List[str]** |  | [optional] 
**limit** | **int** |  | [optional] 
**total** | **bool** |  | [optional] 
**offset** | **int** |  | [optional] 
**order** | [**List[QueryOrder]**](QueryOrder.md) |  | [optional] 
**timezone** | **str** |  | [optional] 
**renew_query** | **bool** |  | [optional] 
**ungrouped** | **bool** |  | [optional] 

## Example

```python
from onelens_backend_client.models.data_retriever_query_output import DataRetrieverQueryOutput

# TODO update the JSON string below
json = "{}"
# create an instance of DataRetrieverQueryOutput from a JSON string
data_retriever_query_output_instance = DataRetrieverQueryOutput.from_json(json)
# print the JSON string representation of the object
print(DataRetrieverQueryOutput.to_json())

# convert the object into a dict
data_retriever_query_output_dict = data_retriever_query_output_instance.to_dict()
# create an instance of DataRetrieverQueryOutput from a dict
data_retriever_query_output_form_dict = data_retriever_query_output.from_dict(data_retriever_query_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


