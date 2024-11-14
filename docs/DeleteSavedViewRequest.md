# DeleteSavedViewRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the saved view | 
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.delete_saved_view_request import DeleteSavedViewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteSavedViewRequest from a JSON string
delete_saved_view_request_instance = DeleteSavedViewRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteSavedViewRequest.to_json())

# convert the object into a dict
delete_saved_view_request_dict = delete_saved_view_request_instance.to_dict()
# create an instance of DeleteSavedViewRequest from a dict
delete_saved_view_request_form_dict = delete_saved_view_request.from_dict(delete_saved_view_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


