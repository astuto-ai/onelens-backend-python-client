# DisableTenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**DisableTenantRequest**](DisableTenantRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.disable_tenant import DisableTenant

# TODO update the JSON string below
json = "{}"
# create an instance of DisableTenant from a JSON string
disable_tenant_instance = DisableTenant.from_json(json)
# print the JSON string representation of the object
print(DisableTenant.to_json())

# convert the object into a dict
disable_tenant_dict = disable_tenant_instance.to_dict()
# create an instance of DisableTenant from a dict
disable_tenant_form_dict = disable_tenant.from_dict(disable_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


