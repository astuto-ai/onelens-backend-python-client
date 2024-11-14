# UpdateSavedViewAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**payload** | [**SavedViewItemPayloadInput**](SavedViewItemPayloadInput.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.update_saved_view_api_request import UpdateSavedViewAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSavedViewAPIRequest from a JSON string
update_saved_view_api_request_instance = UpdateSavedViewAPIRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateSavedViewAPIRequest.to_json())

# convert the object into a dict
update_saved_view_api_request_dict = update_saved_view_api_request_instance.to_dict()
# create an instance of UpdateSavedViewAPIRequest from a dict
update_saved_view_api_request_form_dict = update_saved_view_api_request.from_dict(update_saved_view_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


