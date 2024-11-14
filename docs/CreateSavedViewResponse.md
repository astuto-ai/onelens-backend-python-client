# CreateSavedViewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the saved view | 
**page** | **str** | Page of the saved view | 
**payload** | [**SavedViewItemPayloadOutput**](SavedViewItemPayloadOutput.md) | Payload of the saved view | 
**is_default** | **bool** | Whether the saved view is default | [optional] [default to False]
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**id** | **str** | Unique identifier for the saved view | 

## Example

```python
from onelens_backend_client.models.create_saved_view_response import CreateSavedViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSavedViewResponse from a JSON string
create_saved_view_response_instance = CreateSavedViewResponse.from_json(json)
# print the JSON string representation of the object
print(CreateSavedViewResponse.to_json())

# convert the object into a dict
create_saved_view_response_dict = create_saved_view_response_instance.to_dict()
# create an instance of CreateSavedViewResponse from a dict
create_saved_view_response_form_dict = create_saved_view_response.from_dict(create_saved_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


