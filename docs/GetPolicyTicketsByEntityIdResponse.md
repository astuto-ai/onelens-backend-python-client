# GetPolicyTicketsByEntityIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**entity_tickets** | [**List[GetSinglePolicyTicketByEntityIdResponse]**](GetSinglePolicyTicketByEntityIdResponse.md) | List of tickets | 

## Example

```python
from onelens_backend_client.models.get_policy_tickets_by_entity_id_response import GetPolicyTicketsByEntityIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTicketsByEntityIdResponse from a JSON string
get_policy_tickets_by_entity_id_response_instance = GetPolicyTicketsByEntityIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTicketsByEntityIdResponse.to_json())

# convert the object into a dict
get_policy_tickets_by_entity_id_response_dict = get_policy_tickets_by_entity_id_response_instance.to_dict()
# create an instance of GetPolicyTicketsByEntityIdResponse from a dict
get_policy_tickets_by_entity_id_response_form_dict = get_policy_tickets_by_entity_id_response.from_dict(get_policy_tickets_by_entity_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


