# GetTenantById


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**GetTenantByIDRequest**](GetTenantByIDRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.get_tenant_by_id import GetTenantById

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantById from a JSON string
get_tenant_by_id_instance = GetTenantById.from_json(json)
# print the JSON string representation of the object
print(GetTenantById.to_json())

# convert the object into a dict
get_tenant_by_id_dict = get_tenant_by_id_instance.to_dict()
# create an instance of GetTenantById from a dict
get_tenant_by_id_form_dict = get_tenant_by_id.from_dict(get_tenant_by_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


