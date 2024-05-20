# UpdateTenantTicketsAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**updated_ticket_details** | [**List[UpdateTenantTicketRequestMixin]**](UpdateTenantTicketRequestMixin.md) | Request payload for ticket updation | 

## Example

```python
from onelens_backend_client.models.update_tenant_tickets_api_request import UpdateTenantTicketsAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTenantTicketsAPIRequest from a JSON string
update_tenant_tickets_api_request_instance = UpdateTenantTicketsAPIRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateTenantTicketsAPIRequest.to_json())

# convert the object into a dict
update_tenant_tickets_api_request_dict = update_tenant_tickets_api_request_instance.to_dict()
# create an instance of UpdateTenantTicketsAPIRequest from a dict
update_tenant_tickets_api_request_form_dict = update_tenant_tickets_api_request.from_dict(update_tenant_tickets_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


