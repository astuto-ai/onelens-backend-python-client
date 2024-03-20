# CreateTenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_tenant_request** | [**CreateTenantRequest**](CreateTenantRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.create_tenant import CreateTenant

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenant from a JSON string
create_tenant_instance = CreateTenant.from_json(json)
# print the JSON string representation of the object
print(CreateTenant.to_json())

# convert the object into a dict
create_tenant_dict = create_tenant_instance.to_dict()
# create an instance of CreateTenant from a dict
create_tenant_form_dict = create_tenant.from_dict(create_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


