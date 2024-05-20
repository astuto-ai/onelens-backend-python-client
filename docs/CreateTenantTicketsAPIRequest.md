# CreateTenantTicketsAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_ticket_details** | [**List[CreateTenantTicketRequestMixin]**](CreateTenantTicketRequestMixin.md) | Request payload for ticket creation | 

## Example

```python
from onelens_backend_client.models.create_tenant_tickets_api_request import CreateTenantTicketsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantTicketsAPIRequest from a JSON string
create_tenant_tickets_api_request_instance = CreateTenantTicketsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTenantTicketsAPIRequest.to_json())

# convert the object into a dict
create_tenant_tickets_api_request_dict = create_tenant_tickets_api_request_instance.to_dict()
# create an instance of CreateTenantTicketsAPIRequest from a dict
create_tenant_tickets_api_request_form_dict = create_tenant_tickets_api_request.from_dict(create_tenant_tickets_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


