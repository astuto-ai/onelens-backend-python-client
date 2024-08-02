# CreateTenantEmbedAppsLinksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tab_name** | **str** | Name of the tab | 
**link** | **str** | Link of the tab | 

## Example

```python
from onelens_backend_client.models.create_tenant_embed_apps_links_request import CreateTenantEmbedAppsLinksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantEmbedAppsLinksRequest from a JSON string
create_tenant_embed_apps_links_request_instance = CreateTenantEmbedAppsLinksRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTenantEmbedAppsLinksRequest.to_json())

# convert the object into a dict
create_tenant_embed_apps_links_request_dict = create_tenant_embed_apps_links_request_instance.to_dict()
# create an instance of CreateTenantEmbedAppsLinksRequest from a dict
create_tenant_embed_apps_links_request_form_dict = create_tenant_embed_apps_links_request.from_dict(create_tenant_embed_apps_links_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


