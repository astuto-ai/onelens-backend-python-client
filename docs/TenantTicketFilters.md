# TenantTicketFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**monitor_ids** | **List[str]** | List of violation monitor ids/anomaly node ids for which tickets are to be fetched. | [optional] [default to []]
**ticket_categories** | [**List[TicketCategory]**](TicketCategory.md) | List of ticket categories for which tickets are to be fetched. | [optional] [default to []]
**states** | [**List[TicketState]**](TicketState.md) | List of ticket State for which tickets are to be fetched. | [optional] [default to []]
**statuses** | [**Statuses**](Statuses.md) |  | [optional] 
**policy_ids** | **List[str]** | List of policy ids for which tickets are to be fetched. | [optional] [default to []]

## Example

```python
from onelens_backend_client.models.tenant_ticket_filters import TenantTicketFilters

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTicketFilters from a JSON string
tenant_ticket_filters_instance = TenantTicketFilters.from_json(json)
# print the JSON string representation of the object
print(TenantTicketFilters.to_json())

# convert the object into a dict
tenant_ticket_filters_dict = tenant_ticket_filters_instance.to_dict()
# create an instance of TenantTicketFilters from a dict
tenant_ticket_filters_form_dict = tenant_ticket_filters.from_dict(tenant_ticket_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


