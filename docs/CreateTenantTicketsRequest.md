# CreateTenantTicketsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_ticket_details** | [**List[CreateTenantTicketRequestMixin]**](CreateTenantTicketRequestMixin.md) | Request payload for ticket creation | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.create_tenant_tickets_request import CreateTenantTicketsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenantTicketsRequest from a JSON string
create_tenant_tickets_request_instance = CreateTenantTicketsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTenantTicketsRequest.to_json())

# convert the object into a dict
create_tenant_tickets_request_dict = create_tenant_tickets_request_instance.to_dict()
# create an instance of CreateTenantTicketsRequest from a dict
create_tenant_tickets_request_form_dict = create_tenant_tickets_request.from_dict(create_tenant_tickets_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


