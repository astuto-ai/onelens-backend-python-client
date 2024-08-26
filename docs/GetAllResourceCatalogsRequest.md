# GetAllResourceCatalogsRequest

Get All Resource Catalogs Request with navira

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**tenant_id** | **str** | The id of the tenant. | 
**user_id** | **str** |  | [optional] 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**navira_log_id** | **str** |  | [optional] 
**request** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.get_all_resource_catalogs_request import GetAllResourceCatalogsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllResourceCatalogsRequest from a JSON string
get_all_resource_catalogs_request_instance = GetAllResourceCatalogsRequest.from_json(json)
# print the JSON string representation of the object
print(GetAllResourceCatalogsRequest.to_json())

# convert the object into a dict
get_all_resource_catalogs_request_dict = get_all_resource_catalogs_request_instance.to_dict()
# create an instance of GetAllResourceCatalogsRequest from a dict
get_all_resource_catalogs_request_form_dict = get_all_resource_catalogs_request.from_dict(get_all_resource_catalogs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


