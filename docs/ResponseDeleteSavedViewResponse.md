# ResponseDeleteSavedViewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_delete_saved_view_response import ResponseDeleteSavedViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseDeleteSavedViewResponse from a JSON string
response_delete_saved_view_response_instance = ResponseDeleteSavedViewResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseDeleteSavedViewResponse.to_json())

# convert the object into a dict
response_delete_saved_view_response_dict = response_delete_saved_view_response_instance.to_dict()
# create an instance of ResponseDeleteSavedViewResponse from a dict
response_delete_saved_view_response_form_dict = response_delete_saved_view_response.from_dict(response_delete_saved_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


