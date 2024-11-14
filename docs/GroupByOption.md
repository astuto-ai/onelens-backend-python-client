# GroupByOption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**GroupByType**](GroupByType.md) | Type of the group (e.g., NODE, GENERAL) | 
**value** | [**Value**](Value.md) |  | 

## Example

```python
from onelens_backend_client.models.group_by_option import GroupByOption

# TODO update the JSON string below
json = "{}"
# create an instance of GroupByOption from a JSON string
group_by_option_instance = GroupByOption.from_json(json)
# print the JSON string representation of the object
print(GroupByOption.to_json())

# convert the object into a dict
group_by_option_dict = group_by_option_instance.to_dict()
# create an instance of GroupByOption from a dict
group_by_option_form_dict = group_by_option.from_dict(group_by_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


