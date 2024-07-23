# UpdateTenantEmbedAppsLinksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**tenant_id** | **str** | The unique identifier of the tenant | 
**tab_name** | **str** | Name of the tab | 
**link** | **str** | Link of the tab | 
**system_created** | **bool** |  | [optional] 

## Example

```python
from onelens_backend_client.models.update_tenant_embed_apps_links_response import UpdateTenantEmbedAppsLinksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantEmbedAppsLinksResponse from a JSON string
update_tenant_embed_apps_links_response_instance = UpdateTenantEmbedAppsLinksResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantEmbedAppsLinksResponse.to_json())

# convert the object into a dict
update_tenant_embed_apps_links_response_dict = update_tenant_embed_apps_links_response_instance.to_dict()
# create an instance of UpdateTenantEmbedAppsLinksResponse from a dict
update_tenant_embed_apps_links_response_form_dict = update_tenant_embed_apps_links_response.from_dict(update_tenant_embed_apps_links_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


