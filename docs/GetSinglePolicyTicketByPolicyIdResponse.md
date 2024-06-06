# GetSinglePolicyTicketByPolicyIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **str** | The unique identifier of the ticket | 
**status** | [**PolicyTicketStatus**](PolicyTicketStatus.md) | Status of the ticket | 
**state** | [**TicketState**](TicketState.md) | State of the ticket | 
**violation_attributes** | **object** | Attributes of the violation | 
**entity_id** | **str** | The id of the resource experiencing policy violation. | 
**entity_name** | **str** | Name of the resource | 
**region** | **str** | Region of the resource | 
**service** | **str** | Service of the resource | 
**service_display_name** | **str** | Service name in UI | 
**account_id** | **str** | Account Id managing the resource | 
**recommendation_unit_title** | **str** |  | [optional] 
**potential_savings** | **float** | Potential savings of the ticket | 

## Example

```python
from onelens_backend_client.models.get_single_policy_ticket_by_policy_id_response import GetSinglePolicyTicketByPolicyIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetSinglePolicyTicketByPolicyIdResponse from a JSON string
get_single_policy_ticket_by_policy_id_response_instance = GetSinglePolicyTicketByPolicyIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetSinglePolicyTicketByPolicyIdResponse.to_json())

# convert the object into a dict
get_single_policy_ticket_by_policy_id_response_dict = get_single_policy_ticket_by_policy_id_response_instance.to_dict()
# create an instance of GetSinglePolicyTicketByPolicyIdResponse from a dict
get_single_policy_ticket_by_policy_id_response_form_dict = get_single_policy_ticket_by_policy_id_response.from_dict(get_single_policy_ticket_by_policy_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


