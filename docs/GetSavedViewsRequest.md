# GetSavedViewsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) |  | [optional] 
**sort_criteria** | [**SortCriteria**](SortCriteria.md) |  | [optional] 
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.get_saved_views_request import GetSavedViewsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetSavedViewsRequest from a JSON string
get_saved_views_request_instance = GetSavedViewsRequest.from_json(json)
# print the JSON string representation of the object
print(GetSavedViewsRequest.to_json())

# convert the object into a dict
get_saved_views_request_dict = get_saved_views_request_instance.to_dict()
# create an instance of GetSavedViewsRequest from a dict
get_saved_views_request_form_dict = get_saved_views_request.from_dict(get_saved_views_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


