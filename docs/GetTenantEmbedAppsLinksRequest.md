# GetTenantEmbedAppsLinksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The unique identifier of the tenant | 
**id** | **str** | The unique identifier of the link | 

## Example

```python
from onelens_backend_client.models.get_tenant_embed_apps_links_request import GetTenantEmbedAppsLinksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantEmbedAppsLinksRequest from a JSON string
get_tenant_embed_apps_links_request_instance = GetTenantEmbedAppsLinksRequest.from_json(json)
# print the JSON string representation of the object
print(GetTenantEmbedAppsLinksRequest.to_json())

# convert the object into a dict
get_tenant_embed_apps_links_request_dict = get_tenant_embed_apps_links_request_instance.to_dict()
# create an instance of GetTenantEmbedAppsLinksRequest from a dict
get_tenant_embed_apps_links_request_form_dict = get_tenant_embed_apps_links_request.from_dict(get_tenant_embed_apps_links_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


