# UpdateTenantEmbedAppsLinksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tab_name** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**system_created** | **bool** |  | [optional] 

## Example

```python
from onelens_backend_client.models.update_tenant_embed_apps_links_request import UpdateTenantEmbedAppsLinksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantEmbedAppsLinksRequest from a JSON string
update_tenant_embed_apps_links_request_instance = UpdateTenantEmbedAppsLinksRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantEmbedAppsLinksRequest.to_json())

# convert the object into a dict
update_tenant_embed_apps_links_request_dict = update_tenant_embed_apps_links_request_instance.to_dict()
# create an instance of UpdateTenantEmbedAppsLinksRequest from a dict
update_tenant_embed_apps_links_request_form_dict = update_tenant_embed_apps_links_request.from_dict(update_tenant_embed_apps_links_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


