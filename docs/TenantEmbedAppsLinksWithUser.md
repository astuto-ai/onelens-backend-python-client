# TenantEmbedAppsLinksWithUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | The unique identifier of the user who created the link | 
**created_at** | **datetime** | The date and time when the link was created | 
**updated_at** | **datetime** | The date and time when the link was updated | 
**updated_by** | **str** |  | [optional] 
**tab_name** | **str** | Name of the tab | 
**link** | **str** | Link of the tab | 
**system_created** | **bool** |  | [optional] 
**state** | [**TenantEmbedAppsLinkState**](TenantEmbedAppsLinkState.md) | State of the link | 
**id** | **str** | The unique identifier of the link | 
**created_by_email** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.tenant_embed_apps_links_with_user import TenantEmbedAppsLinksWithUser

# TODO update the JSON string below
json = "{}"
# create an instance of TenantEmbedAppsLinksWithUser from a JSON string
tenant_embed_apps_links_with_user_instance = TenantEmbedAppsLinksWithUser.from_json(json)
# print the JSON string representation of the object
print(TenantEmbedAppsLinksWithUser.to_json())

# convert the object into a dict
tenant_embed_apps_links_with_user_dict = tenant_embed_apps_links_with_user_instance.to_dict()
# create an instance of TenantEmbedAppsLinksWithUser from a dict
tenant_embed_apps_links_with_user_form_dict = tenant_embed_apps_links_with_user.from_dict(tenant_embed_apps_links_with_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


