# SavedViewItemPayloadInputSortCriteria

Sort criteria for the saved views

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**direction** | [**Direction**](Direction.md) |  | 

## Example

```python
from onelens_backend_client.models.saved_view_item_payload_input_sort_criteria import SavedViewItemPayloadInputSortCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of SavedViewItemPayloadInputSortCriteria from a JSON string
saved_view_item_payload_input_sort_criteria_instance = SavedViewItemPayloadInputSortCriteria.from_json(json)
# print the JSON string representation of the object
print(SavedViewItemPayloadInputSortCriteria.to_json())

# convert the object into a dict
saved_view_item_payload_input_sort_criteria_dict = saved_view_item_payload_input_sort_criteria_instance.to_dict()
# create an instance of SavedViewItemPayloadInputSortCriteria from a dict
saved_view_item_payload_input_sort_criteria_form_dict = saved_view_item_payload_input_sort_criteria.from_dict(saved_view_item_payload_input_sort_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


