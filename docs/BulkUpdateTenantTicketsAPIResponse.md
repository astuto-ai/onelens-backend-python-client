# BulkUpdateTenantTicketsAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BulkUpdateTenantTicketsRequestMixin**](BulkUpdateTenantTicketsRequestMixin.md) | Updated tickets data | 
**error** | [**List[BulkUpdateTenantTicketsErrorMixin]**](BulkUpdateTenantTicketsErrorMixin.md) | Error of the response | [optional] [default to []]

## Example

```python
from onelens_backend_client.models.bulk_update_tenant_tickets_api_response import BulkUpdateTenantTicketsAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateTenantTicketsAPIResponse from a JSON string
bulk_update_tenant_tickets_api_response_instance = BulkUpdateTenantTicketsAPIResponse.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateTenantTicketsAPIResponse.to_json())

# convert the object into a dict
bulk_update_tenant_tickets_api_response_dict = bulk_update_tenant_tickets_api_response_instance.to_dict()
# create an instance of BulkUpdateTenantTicketsAPIResponse from a dict
bulk_update_tenant_tickets_api_response_form_dict = bulk_update_tenant_tickets_api_response.from_dict(bulk_update_tenant_tickets_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


