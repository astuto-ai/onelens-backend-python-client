# BulkUpdateTenantTicketsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BulkUpdateTenantTicketsRequestMixin**](BulkUpdateTenantTicketsRequestMixin.md) | Updated tickets data | 
**message** | **str** |  | [optional] 
**error** | [**List[BulkUpdateTenantTicketsErrorMixin]**](BulkUpdateTenantTicketsErrorMixin.md) | Error of the response | [optional] [default to []]
**status_code** | **int** | Status code of the response | 

## Example

```python
from onelens_backend_client.models.bulk_update_tenant_tickets_response import BulkUpdateTenantTicketsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkUpdateTenantTicketsResponse from a JSON string
bulk_update_tenant_tickets_response_instance = BulkUpdateTenantTicketsResponse.from_json(json)
# print the JSON string representation of the object
print(BulkUpdateTenantTicketsResponse.to_json())

# convert the object into a dict
bulk_update_tenant_tickets_response_dict = bulk_update_tenant_tickets_response_instance.to_dict()
# create an instance of BulkUpdateTenantTicketsResponse from a dict
bulk_update_tenant_tickets_response_form_dict = bulk_update_tenant_tickets_response.from_dict(bulk_update_tenant_tickets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


