# BulkUpdateTenantTicketsRequestMixin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_ids** | **List[str]** | List of ticket ids | [optional] [default to []]
**status** | [**PolicyTicketStatus**](PolicyTicketStatus.md) |  | [optional] 
**assignment** | **str** |  | [optional] 
**assigned_to** | **str** |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.bulk_update_tenant_tickets_request_mixin import BulkUpdateTenantTicketsRequestMixin

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateTenantTicketsRequestMixin from a JSON string
bulk_update_tenant_tickets_request_mixin_instance = BulkUpdateTenantTicketsRequestMixin.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateTenantTicketsRequestMixin.to_json())

# convert the object into a dict
bulk_update_tenant_tickets_request_mixin_dict = bulk_update_tenant_tickets_request_mixin_instance.to_dict()
# create an instance of BulkUpdateTenantTicketsRequestMixin from a dict
bulk_update_tenant_tickets_request_mixin_form_dict = bulk_update_tenant_tickets_request_mixin.from_dict(bulk_update_tenant_tickets_request_mixin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


