# GetTenantEmbedAppsLinkResponse


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

## Example

```python
from onelens_backend_client.models.get_tenant_embed_apps_link_response import GetTenantEmbedAppsLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantEmbedAppsLinkResponse from a JSON string
get_tenant_embed_apps_link_response_instance = GetTenantEmbedAppsLinkResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantEmbedAppsLinkResponse.to_json())

# convert the object into a dict
get_tenant_embed_apps_link_response_dict = get_tenant_embed_apps_link_response_instance.to_dict()
# create an instance of GetTenantEmbedAppsLinkResponse from a dict
get_tenant_embed_apps_link_response_form_dict = get_tenant_embed_apps_link_response.from_dict(get_tenant_embed_apps_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


