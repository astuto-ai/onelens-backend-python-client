# GetAllTenantEmbedAppsLinksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**links** | [**List[TenantEmbedAppsLinksWithUser]**](TenantEmbedAppsLinksWithUser.md) | List of links | 

## Example

```python
from onelens_backend_client.models.get_all_tenant_embed_apps_links_response import GetAllTenantEmbedAppsLinksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllTenantEmbedAppsLinksResponse from a JSON string
get_all_tenant_embed_apps_links_response_instance = GetAllTenantEmbedAppsLinksResponse.from_json(json)
# print the JSON string representation of the object
print(GetAllTenantEmbedAppsLinksResponse.to_json())

# convert the object into a dict
get_all_tenant_embed_apps_links_response_dict = get_all_tenant_embed_apps_links_response_instance.to_dict()
# create an instance of GetAllTenantEmbedAppsLinksResponse from a dict
get_all_tenant_embed_apps_links_response_form_dict = get_all_tenant_embed_apps_links_response.from_dict(get_all_tenant_embed_apps_links_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


