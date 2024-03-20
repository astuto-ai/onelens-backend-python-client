# CreateTenantRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_tenant_request** | [**CreateTenantRequest**](CreateTenantRequest.md) |  | 

## Example

```python
from onelens_backend_client.models.create_tenant_request import CreateTenantRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantRequest from a JSON string
create_tenant_request_instance = CreateTenantRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTenantRequest.to_json())

# convert the object into a dict
create_tenant_request_dict = create_tenant_request_instance.to_dict()
# create an instance of CreateTenantRequest from a dict
create_tenant_request_form_dict = create_tenant_request.from_dict(create_tenant_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


