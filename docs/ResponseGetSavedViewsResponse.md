# ResponseGetSavedViewsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetSavedViewsResponse**](GetSavedViewsResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_saved_views_response import ResponseGetSavedViewsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetSavedViewsResponse from a JSON string
response_get_saved_views_response_instance = ResponseGetSavedViewsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetSavedViewsResponse.to_json())

# convert the object into a dict
response_get_saved_views_response_dict = response_get_saved_views_response_instance.to_dict()
# create an instance of ResponseGetSavedViewsResponse from a dict
response_get_saved_views_response_form_dict = response_get_saved_views_response.from_dict(response_get_saved_views_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


