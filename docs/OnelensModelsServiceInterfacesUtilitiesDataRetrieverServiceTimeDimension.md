# OnelensModelsServiceInterfacesUtilitiesDataRetrieverServiceTimeDimension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | **str** |  | [optional] 
**date_range** | **List[str]** |  | [optional] 
**compare_date_range** | [**List[TimeDimensionOutputCompareDateRangeInner]**](TimeDimensionOutputCompareDateRangeInner.md) |  | [optional] 
**granularity** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.onelens_models_service_interfaces_utilities_data_retriever_service_time_dimension import OnelensModelsServiceInterfacesUtilitiesDataRetrieverServiceTimeDimension

# TODO update the JSON string below
json = "{}"
# create an instance of OnelensModelsServiceInterfacesUtilitiesDataRetrieverServiceTimeDimension from a JSON string
onelens_models_service_interfaces_utilities_data_retriever_service_time_dimension_instance = OnelensModelsServiceInterfacesUtilitiesDataRetrieverServiceTimeDimension.from_json(json)
# print the JSON string representation of the object
print(OnelensModelsServiceInterfacesUtilitiesDataRetrieverServiceTimeDimension.to_json())

# convert the object into a dict
onelens_models_service_interfaces_utilities_data_retriever_service_time_dimension_dict = onelens_models_service_interfaces_utilities_data_retriever_service_time_dimension_instance.to_dict()
# create an instance of OnelensModelsServiceInterfacesUtilitiesDataRetrieverServiceTimeDimension from a dict
onelens_models_service_interfaces_utilities_data_retriever_service_time_dimension_form_dict = onelens_models_service_interfaces_utilities_data_retriever_service_time_dimension.from_dict(onelens_models_service_interfaces_utilities_data_retriever_service_time_dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


