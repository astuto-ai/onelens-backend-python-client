# TimeDimension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimension** | **str** |  | [optional] 
**date_range** | **List[str]** |  | [optional] 
**compare_date_range** | [**List[TimeDimensionCompareDateRangeInner]**](TimeDimensionCompareDateRangeInner.md) |  | [optional] 
**granularity** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.time_dimension import TimeDimension

# TODO update the JSON string below
json = "{}"
# create an instance of TimeDimension from a JSON string
time_dimension_instance = TimeDimension.from_json(json)
# print the JSON string representation of the object
print(TimeDimension.to_json())

# convert the object into a dict
time_dimension_dict = time_dimension_instance.to_dict()
# create an instance of TimeDimension from a dict
time_dimension_form_dict = time_dimension.from_dict(time_dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


