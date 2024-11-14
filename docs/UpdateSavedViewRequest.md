# UpdateSavedViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**payload** | [**SavedViewItemPayloadInput**](SavedViewItemPayloadInput.md) |  | [optional] 
**id** | **str** | Unique identifier for the saved view | 
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.update_saved_view_request import UpdateSavedViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSavedViewRequest from a JSON string
update_saved_view_request_instance = UpdateSavedViewRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSavedViewRequest.to_json())

# convert the object into a dict
update_saved_view_request_dict = update_saved_view_request_instance.to_dict()
# create an instance of UpdateSavedViewRequest from a dict
update_saved_view_request_form_dict = update_saved_view_request.from_dict(update_saved_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


