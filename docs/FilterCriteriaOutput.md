# FilterCriteriaOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**operator** | [**OperatorOutput**](OperatorOutput.md) |  | 
**values** | [**Values**](Values.md) |  | 

## Example

```python
from onelens_backend_client.models.filter_criteria_output import FilterCriteriaOutput

# TODO update the JSON string below
json = "{}"
# create an instance of FilterCriteriaOutput from a JSON string
filter_criteria_output_instance = FilterCriteriaOutput.from_json(json)
# print the JSON string representation of the object
print(FilterCriteriaOutput.to_json())

# convert the object into a dict
filter_criteria_output_dict = filter_criteria_output_instance.to_dict()
# create an instance of FilterCriteriaOutput from a dict
filter_criteria_output_form_dict = filter_criteria_output.from_dict(filter_criteria_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


