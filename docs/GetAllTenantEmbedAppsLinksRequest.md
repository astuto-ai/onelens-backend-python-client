# GetAllTenantEmbedAppsLinksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationParams**](PaginationParams.md) | Pagination parameters for the request. | [optional] 
**filters** | [**List[OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria]**](OnelensDomainUtilitiesRepositoriesDynamicFiltersFilterCriteria.md) | Filters to be applied | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.get_all_tenant_embed_apps_links_request import GetAllTenantEmbedAppsLinksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllTenantEmbedAppsLinksRequest from a JSON string
get_all_tenant_embed_apps_links_request_instance = GetAllTenantEmbedAppsLinksRequest.from_json(json)
# print the JSON string representation of the object
print(GetAllTenantEmbedAppsLinksRequest.to_json())

# convert the object into a dict
get_all_tenant_embed_apps_links_request_dict = get_all_tenant_embed_apps_links_request_instance.to_dict()
# create an instance of GetAllTenantEmbedAppsLinksRequest from a dict
get_all_tenant_embed_apps_links_request_form_dict = get_all_tenant_embed_apps_links_request.from_dict(get_all_tenant_embed_apps_links_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


