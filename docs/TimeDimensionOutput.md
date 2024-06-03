# TimeDimensionOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | **str** |  | [optional] 
**date_range** | **List[str]** |  | [optional] 
**compare_date_range** | [**List[TimeDimensionOutputCompareDateRangeInner]**](TimeDimensionOutputCompareDateRangeInner.md) |  | [optional] 
**granularity** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.time_dimension_output import TimeDimensionOutput

# TODO update the JSON string below
json = "{}"
# create an instance of TimeDimensionOutput from a JSON string
time_dimension_output_instance = TimeDimensionOutput.from_json(json)
# print the JSON string representation of the object
print(TimeDimensionOutput.to_json())

# convert the object into a dict
time_dimension_output_dict = time_dimension_output_instance.to_dict()
# create an instance of TimeDimensionOutput from a dict
time_dimension_output_form_dict = time_dimension_output.from_dict(time_dimension_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


