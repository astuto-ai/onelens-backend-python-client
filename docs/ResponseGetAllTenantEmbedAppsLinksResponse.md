# ResponseGetAllTenantEmbedAppsLinksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetAllTenantEmbedAppsLinksResponse**](GetAllTenantEmbedAppsLinksResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_all_tenant_embed_apps_links_response import ResponseGetAllTenantEmbedAppsLinksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetAllTenantEmbedAppsLinksResponse from a JSON string
response_get_all_tenant_embed_apps_links_response_instance = ResponseGetAllTenantEmbedAppsLinksResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetAllTenantEmbedAppsLinksResponse.to_json())

# convert the object into a dict
response_get_all_tenant_embed_apps_links_response_dict = response_get_all_tenant_embed_apps_links_response_instance.to_dict()
# create an instance of ResponseGetAllTenantEmbedAppsLinksResponse from a dict
response_get_all_tenant_embed_apps_links_response_form_dict = response_get_all_tenant_embed_apps_links_response.from_dict(response_get_all_tenant_embed_apps_links_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


