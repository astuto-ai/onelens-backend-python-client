# Granularity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | [**GranularityUnit**](GranularityUnit.md) |  | 
**value** | **int** |  | 

## Example

```python
from onelens_backend_client.models.granularity import Granularity

# TODO update the JSON string below
json = "{}"
# create an instance of Granularity from a JSON string
granularity_instance = Granularity.from_json(json)
# print the JSON string representation of the object
print(Granularity.to_json())

# convert the object into a dict
granularity_dict = granularity_instance.to_dict()
# create an instance of Granularity from a dict
granularity_form_dict = granularity.from_dict(granularity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


