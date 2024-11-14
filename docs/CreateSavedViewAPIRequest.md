# CreateSavedViewAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the saved view | 
**page** | **str** | Page of the saved view | 
**payload** | [**SavedViewItemPayloadInput**](SavedViewItemPayloadInput.md) | Payload of the saved view | 

## Example

```python
from onelens_backend_client.models.create_saved_view_api_request import CreateSavedViewAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSavedViewAPIRequest from a JSON string
create_saved_view_api_request_instance = CreateSavedViewAPIRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSavedViewAPIRequest.to_json())

# convert the object into a dict
create_saved_view_api_request_dict = create_saved_view_api_request_instance.to_dict()
# create an instance of CreateSavedViewAPIRequest from a dict
create_saved_view_api_request_form_dict = create_saved_view_api_request.from_dict(create_saved_view_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


