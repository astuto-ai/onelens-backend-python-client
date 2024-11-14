# GetSavedViewsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**saved_views** | [**List[SavedViewItem]**](SavedViewItem.md) | List of saved views | 

## Example

```python
from onelens_backend_client.models.get_saved_views_response import GetSavedViewsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavedViewsResponse from a JSON string
get_saved_views_response_instance = GetSavedViewsResponse.from_json(json)
# print the JSON string representation of the object
print(GetSavedViewsResponse.to_json())

# convert the object into a dict
get_saved_views_response_dict = get_saved_views_response_instance.to_dict()
# create an instance of GetSavedViewsResponse from a dict
get_saved_views_response_form_dict = get_saved_views_response.from_dict(get_saved_views_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


