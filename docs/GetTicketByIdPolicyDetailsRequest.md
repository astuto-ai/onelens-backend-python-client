# GetTicketByIdPolicyDetailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | The unique identifier of the tenant | 
**ticket_id** | **str** | The unique identifier of the ticket | 

## Example

```python
from onelens_backend_client.models.get_ticket_by_id_policy_details_request import GetTicketByIdPolicyDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetTicketByIdPolicyDetailsRequest from a JSON string
get_ticket_by_id_policy_details_request_instance = GetTicketByIdPolicyDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(GetTicketByIdPolicyDetailsRequest.to_json())

# convert the object into a dict
get_ticket_by_id_policy_details_request_dict = get_ticket_by_id_policy_details_request_instance.to_dict()
# create an instance of GetTicketByIdPolicyDetailsRequest from a dict
get_ticket_by_id_policy_details_request_form_dict = get_ticket_by_id_policy_details_request.from_dict(get_ticket_by_id_policy_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


