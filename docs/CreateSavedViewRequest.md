# CreateSavedViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the saved view | 
**page** | **str** | Page of the saved view | 
**payload** | [**SavedViewItemPayloadInput**](SavedViewItemPayloadInput.md) | Payload of the saved view | 
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.create_saved_view_request import CreateSavedViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSavedViewRequest from a JSON string
create_saved_view_request_instance = CreateSavedViewRequest.from_json(json)
# print the JSON string representation of the object
print(CreateSavedViewRequest.to_json())

# convert the object into a dict
create_saved_view_request_dict = create_saved_view_request_instance.to_dict()
# create an instance of CreateSavedViewRequest from a dict
create_saved_view_request_form_dict = create_saved_view_request.from_dict(create_saved_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


