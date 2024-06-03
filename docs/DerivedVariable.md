# DerivedVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**value_type** | **str** |  | 
**source_key** | **str** |  | 

## Example

```python
from onelens_backend_client.models.derived_variable import DerivedVariable

# TODO update the JSON string below
json = "{}"
# create an instance of DerivedVariable from a JSON string
derived_variable_instance = DerivedVariable.from_json(json)
# print the JSON string representation of the object
print(DerivedVariable.to_json())

# convert the object into a dict
derived_variable_dict = derived_variable_instance.to_dict()
# create an instance of DerivedVariable from a dict
derived_variable_form_dict = derived_variable.from_dict(derived_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


