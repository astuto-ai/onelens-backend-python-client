# SavedViewItemPayloadInputPagination

Pagination parameters for the saved views

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | Page number (1-indexed). | [optional] [default to 1]
**page_size** | **int** | Number of items per page. | [optional] [default to 10]

## Example

```python
from onelens_backend_client.models.saved_view_item_payload_input_pagination import SavedViewItemPayloadInputPagination

# TODO update the JSON string below
json = "{}"
# create an instance of SavedViewItemPayloadInputPagination from a JSON string
saved_view_item_payload_input_pagination_instance = SavedViewItemPayloadInputPagination.from_json(json)
# print the JSON string representation of the object
print(SavedViewItemPayloadInputPagination.to_json())

# convert the object into a dict
saved_view_item_payload_input_pagination_dict = saved_view_item_payload_input_pagination_instance.to_dict()
# create an instance of SavedViewItemPayloadInputPagination from a dict
saved_view_item_payload_input_pagination_form_dict = saved_view_item_payload_input_pagination.from_dict(saved_view_item_payload_input_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


