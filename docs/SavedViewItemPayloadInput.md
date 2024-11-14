# SavedViewItemPayloadInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**Filters**](Filters.md) |  | [optional] 
**sort_criteria** | [**SavedViewItemPayloadInputSortCriteria**](SavedViewItemPayloadInputSortCriteria.md) |  | [optional] 
**pagination** | [**SavedViewItemPayloadInputPagination**](SavedViewItemPayloadInputPagination.md) |  | [optional] 
**selected_fields** | [**SelectedFields**](SelectedFields.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.saved_view_item_payload_input import SavedViewItemPayloadInput

# TODO update the JSON string below
json = "{}"
# create an instance of SavedViewItemPayloadInput from a JSON string
saved_view_item_payload_input_instance = SavedViewItemPayloadInput.from_json(json)
# print the JSON string representation of the object
print(SavedViewItemPayloadInput.to_json())

# convert the object into a dict
saved_view_item_payload_input_dict = saved_view_item_payload_input_instance.to_dict()
# create an instance of SavedViewItemPayloadInput from a dict
saved_view_item_payload_input_form_dict = saved_view_item_payload_input.from_dict(saved_view_item_payload_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


