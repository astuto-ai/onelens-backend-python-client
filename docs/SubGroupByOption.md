# SubGroupByOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GroupByType**](GroupByType.md) | Type of the group (e.g., NODE, GENERAL) | 
**value** | [**Value3**](Value3.md) |  | 

## Example

```python
from onelens_backend_client.models.sub_group_by_option import SubGroupByOption

# TODO update the JSON string below
json = "{}"
# create an instance of SubGroupByOption from a JSON string
sub_group_by_option_instance = SubGroupByOption.from_json(json)
# print the JSON string representation of the object
print(SubGroupByOption.to_json())

# convert the object into a dict
sub_group_by_option_dict = sub_group_by_option_instance.to_dict()
# create an instance of SubGroupByOption from a dict
sub_group_by_option_form_dict = sub_group_by_option.from_dict(sub_group_by_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


