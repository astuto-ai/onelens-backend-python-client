# ResponseUpdateTenantEmbedAppsLinksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**UpdateTenantEmbedAppsLinksResponse**](UpdateTenantEmbedAppsLinksResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_update_tenant_embed_apps_links_response import ResponseUpdateTenantEmbedAppsLinksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseUpdateTenantEmbedAppsLinksResponse from a JSON string
response_update_tenant_embed_apps_links_response_instance = ResponseUpdateTenantEmbedAppsLinksResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseUpdateTenantEmbedAppsLinksResponse.to_json())

# convert the object into a dict
response_update_tenant_embed_apps_links_response_dict = response_update_tenant_embed_apps_links_response_instance.to_dict()
# create an instance of ResponseUpdateTenantEmbedAppsLinksResponse from a dict
response_update_tenant_embed_apps_links_response_form_dict = response_update_tenant_embed_apps_links_response.from_dict(response_update_tenant_embed_apps_links_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


