# GetSinglePolicyTicketByPolicyIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **object** | The unique identifier of the ticket | 
**status** | [**PolicyTicketStatus**](PolicyTicketStatus.md) | Status of the ticket | 
**state** | [**GetSinglePolicyTicketByPolicyIdResponseState**](GetSinglePolicyTicketByPolicyIdResponseState.md) |  | [optional] 
**violation_attributes** | [**ViolationAttributes**](ViolationAttributes.md) |  | [optional] 
**entity_id** | [**EntityId**](EntityId.md) |  | [optional] 
**entity_name** | [**EntityName**](EntityName.md) |  | [optional] 
**region** | [**Region**](Region.md) |  | [optional] 
**service** | [**Service1**](Service1.md) |  | [optional] 
**service_display_name** | [**ServiceDisplayName**](ServiceDisplayName.md) |  | [optional] 
**account_id** | [**AccountId**](AccountId.md) |  | [optional] 
**recommendation_unit_title** | [**RecommendationUnitTitle**](RecommendationUnitTitle.md) |  | [optional] 
**potential_savings** | [**PotentialSavings**](PotentialSavings.md) |  | [optional] 
**resource_id** | [**ResourceId**](ResourceId.md) |  | [optional] 
**account_name** | [**AccountName**](AccountName.md) |  | [optional] 
**policy_id** | [**PolicyId**](PolicyId.md) |  | [optional] 
**policy_title** | [**PolicyTitle**](PolicyTitle.md) |  | [optional] 
**policy_display_alias** | [**PolicyDisplayAlias**](PolicyDisplayAlias.md) |  | [optional] 
**policy_labels** | [**PolicyLabels**](PolicyLabels.md) |  | [optional] 
**effort** | [**GetSinglePolicyTicketByPolicyIdResponseEffort**](GetSinglePolicyTicketByPolicyIdResponseEffort.md) |  | [optional] 
**ticket_alias** | [**TicketAlias**](TicketAlias.md) |  | [optional] 
**first_run_at** | [**FirstRunAt**](FirstRunAt.md) |  | [optional] 
**node_ids** | [**NodeIds**](NodeIds.md) |  | [optional] 

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


