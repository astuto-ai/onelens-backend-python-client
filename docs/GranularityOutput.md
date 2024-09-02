# GranularityOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | [**GranularityUnitOutput**](GranularityUnitOutput.md) |  | 
**value** | **int** |  | 

## Example

```python
from onelens_backend_client.models.granularity_output import GranularityOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GranularityOutput from a JSON string
granularity_output_instance = GranularityOutput.from_json(json)
# print the JSON string representation of the object
print(GranularityOutput.to_json())

# convert the object into a dict
granularity_output_dict = granularity_output_instance.to_dict()
# create an instance of GranularityOutput from a dict
granularity_output_form_dict = granularity_output.from_dict(granularity_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


