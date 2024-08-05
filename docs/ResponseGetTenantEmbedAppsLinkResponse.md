# ResponseGetTenantEmbedAppsLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetTenantEmbedAppsLinkResponse**](GetTenantEmbedAppsLinkResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_tenant_embed_apps_link_response import ResponseGetTenantEmbedAppsLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetTenantEmbedAppsLinkResponse from a JSON string
response_get_tenant_embed_apps_link_response_instance = ResponseGetTenantEmbedAppsLinkResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetTenantEmbedAppsLinkResponse.to_json())

# convert the object into a dict
response_get_tenant_embed_apps_link_response_dict = response_get_tenant_embed_apps_link_response_instance.to_dict()
# create an instance of ResponseGetTenantEmbedAppsLinkResponse from a dict
response_get_tenant_embed_apps_link_response_form_dict = response_get_tenant_embed_apps_link_response.from_dict(response_get_tenant_embed_apps_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


