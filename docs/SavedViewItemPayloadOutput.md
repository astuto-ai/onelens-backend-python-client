# SavedViewItemPayloadOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**Filters**](Filters.md) |  | [optional] 
**sort_criteria** | [**SavedViewItemPayloadInputSortCriteria**](SavedViewItemPayloadInputSortCriteria.md) |  | [optional] 
**pagination** | [**SavedViewItemPayloadInputPagination**](SavedViewItemPayloadInputPagination.md) |  | [optional] 
**selected_fields** | [**SelectedFields**](SelectedFields.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.saved_view_item_payload_output import SavedViewItemPayloadOutput

# TODO update the JSON string below
json = "{}"
# create an instance of SavedViewItemPayloadOutput from a JSON string
saved_view_item_payload_output_instance = SavedViewItemPayloadOutput.from_json(json)
# print the JSON string representation of the object
print(SavedViewItemPayloadOutput.to_json())

# convert the object into a dict
saved_view_item_payload_output_dict = saved_view_item_payload_output_instance.to_dict()
# create an instance of SavedViewItemPayloadOutput from a dict
saved_view_item_payload_output_form_dict = saved_view_item_payload_output.from_dict(saved_view_item_payload_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


