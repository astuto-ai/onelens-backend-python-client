# GetAllResourceCatalogsApiRequest

Get All Resource Catalogs API Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**navira_log_id** | **str** |  | [optional] 
**prompt** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_all_resource_catalogs_api_request import GetAllResourceCatalogsApiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllResourceCatalogsApiRequest from a JSON string
get_all_resource_catalogs_api_request_instance = GetAllResourceCatalogsApiRequest.from_json(json)
# print the JSON string representation of the object
print(GetAllResourceCatalogsApiRequest.to_json())

# convert the object into a dict
get_all_resource_catalogs_api_request_dict = get_all_resource_catalogs_api_request_instance.to_dict()
# create an instance of GetAllResourceCatalogsApiRequest from a dict
get_all_resource_catalogs_api_request_form_dict = get_all_resource_catalogs_api_request.from_dict(get_all_resource_catalogs_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


