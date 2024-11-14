# SavedViewItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the saved view | 
**name** | **str** | Name of the saved view | 
**page** | **str** | Page of the saved view | 
**payload** | [**SavedViewItemPayloadOutput**](SavedViewItemPayloadOutput.md) | Payload of the saved view | 
**is_default** | **bool** | Whether the saved view is default | [optional] [default to False]
**created_at** | **datetime** | Created at | 
**updated_at** | **datetime** | Updated at | 

## Example

```python
from onelens_backend_client.models.saved_view_item import SavedViewItem

# TODO update the JSON string below
json = "{}"
# create an instance of SavedViewItem from a JSON string
saved_view_item_instance = SavedViewItem.from_json(json)
# print the JSON string representation of the object
print(SavedViewItem.to_json())

# convert the object into a dict
saved_view_item_dict = saved_view_item_instance.to_dict()
# create an instance of SavedViewItem from a dict
saved_view_item_form_dict = saved_view_item.from_dict(saved_view_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


