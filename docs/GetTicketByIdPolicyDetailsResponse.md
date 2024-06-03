# GetTicketByIdPolicyDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_ticket** | [**TenantTicket**](TenantTicket.md) | Tenant ticket details | 
**policy_details** | [**TenantPolicy**](TenantPolicy.md) | Policy details | 
**recommendation_units** | **List[str]** | List of recommendation units | 
**hierarchy_details** | **object** | The resource hierarchy details | 
**resource_details** | **object** | The resource details | 

## Example

```python
from onelens_backend_client.models.get_ticket_by_id_policy_details_response import GetTicketByIdPolicyDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTicketByIdPolicyDetailsResponse from a JSON string
get_ticket_by_id_policy_details_response_instance = GetTicketByIdPolicyDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(GetTicketByIdPolicyDetailsResponse.to_json())

# convert the object into a dict
get_ticket_by_id_policy_details_response_dict = get_ticket_by_id_policy_details_response_instance.to_dict()
# create an instance of GetTicketByIdPolicyDetailsResponse from a dict
get_ticket_by_id_policy_details_response_form_dict = get_ticket_by_id_policy_details_response.from_dict(get_ticket_by_id_policy_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


