# GetTenantTicketsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_tickets** | [**List[TenantTicket]**](TenantTicket.md) | List of tickets of the tenant | 

## Example

```python
from onelens_backend_client.models.get_tenant_tickets_response import GetTenantTicketsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTenantTicketsResponse from a JSON string
get_tenant_tickets_response_instance = GetTenantTicketsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTenantTicketsResponse.to_json())

# convert the object into a dict
get_tenant_tickets_response_dict = get_tenant_tickets_response_instance.to_dict()
# create an instance of GetTenantTicketsResponse from a dict
get_tenant_tickets_response_form_dict = get_tenant_tickets_response.from_dict(get_tenant_tickets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


