# BulkUpdateTenantTicketsErrorMixin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **str** | The unique identifier of the ticket | 
**description** | **str** | Description of the error | 
**code** | **int** | Status code of the error | 

## Example

```python
from onelens_backend_client.models.bulk_update_tenant_tickets_error_mixin import BulkUpdateTenantTicketsErrorMixin

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateTenantTicketsErrorMixin from a JSON string
bulk_update_tenant_tickets_error_mixin_instance = BulkUpdateTenantTicketsErrorMixin.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateTenantTicketsErrorMixin.to_json())

# convert the object into a dict
bulk_update_tenant_tickets_error_mixin_dict = bulk_update_tenant_tickets_error_mixin_instance.to_dict()
# create an instance of BulkUpdateTenantTicketsErrorMixin from a dict
bulk_update_tenant_tickets_error_mixin_form_dict = bulk_update_tenant_tickets_error_mixin.from_dict(bulk_update_tenant_tickets_error_mixin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


