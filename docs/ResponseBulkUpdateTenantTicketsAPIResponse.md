# ResponseBulkUpdateTenantTicketsAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BulkUpdateTenantTicketsAPIResponse**](BulkUpdateTenantTicketsAPIResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_bulk_update_tenant_tickets_api_response import ResponseBulkUpdateTenantTicketsAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseBulkUpdateTenantTicketsAPIResponse from a JSON string
response_bulk_update_tenant_tickets_api_response_instance = ResponseBulkUpdateTenantTicketsAPIResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseBulkUpdateTenantTicketsAPIResponse.to_json())

# convert the object into a dict
response_bulk_update_tenant_tickets_api_response_dict = response_bulk_update_tenant_tickets_api_response_instance.to_dict()
# create an instance of ResponseBulkUpdateTenantTicketsAPIResponse from a dict
response_bulk_update_tenant_tickets_api_response_form_dict = response_bulk_update_tenant_tickets_api_response.from_dict(response_bulk_update_tenant_tickets_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


