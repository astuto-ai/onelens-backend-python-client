# ResponseCreateSavedViewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CreateSavedViewResponse**](CreateSavedViewResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_create_saved_view_response import ResponseCreateSavedViewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseCreateSavedViewResponse from a JSON string
response_create_saved_view_response_instance = ResponseCreateSavedViewResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseCreateSavedViewResponse.to_json())

# convert the object into a dict
response_create_saved_view_response_dict = response_create_saved_view_response_instance.to_dict()
# create an instance of ResponseCreateSavedViewResponse from a dict
response_create_saved_view_response_form_dict = response_create_saved_view_response.from_dict(response_create_saved_view_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


