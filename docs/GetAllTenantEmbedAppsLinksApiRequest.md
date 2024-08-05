# GetAllTenantEmbedAppsLinksApiRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 

## Example

```python
from onelens_backend_client.models.get_all_tenant_embed_apps_links_api_request import GetAllTenantEmbedAppsLinksApiRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllTenantEmbedAppsLinksApiRequest from a JSON string
get_all_tenant_embed_apps_links_api_request_instance = GetAllTenantEmbedAppsLinksApiRequest.from_json(json)
# print the JSON string representation of the object
print(GetAllTenantEmbedAppsLinksApiRequest.to_json())

# convert the object into a dict
get_all_tenant_embed_apps_links_api_request_dict = get_all_tenant_embed_apps_links_api_request_instance.to_dict()
# create an instance of GetAllTenantEmbedAppsLinksApiRequest from a dict
get_all_tenant_embed_apps_links_api_request_form_dict = get_all_tenant_embed_apps_links_api_request.from_dict(get_all_tenant_embed_apps_links_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


