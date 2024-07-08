# SortCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**direction** | [**Direction**](Direction.md) |  | 

## Example

```python
from onelens_backend_client.models.sort_criteria import SortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of SortCriteria from a JSON string
sort_criteria_instance = SortCriteria.from_json(json)
# print the JSON string representation of the object
print(SortCriteria.to_json())

# convert the object into a dict
sort_criteria_dict = sort_criteria_instance.to_dict()
# create an instance of SortCriteria from a dict
sort_criteria_form_dict = sort_criteria.from_dict(sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


