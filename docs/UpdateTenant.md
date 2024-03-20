# UpdateTenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**request** | [**UpdateTenantRequest**](UpdateTenantRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.update_tenant import UpdateTenant

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenant from a JSON string
update_tenant_instance = UpdateTenant.from_json(json)
# print the JSON string representation of the object
print(UpdateTenant.to_json())

# convert the object into a dict
update_tenant_dict = update_tenant_instance.to_dict()
# create an instance of UpdateTenant from a dict
update_tenant_form_dict = update_tenant.from_dict(update_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


