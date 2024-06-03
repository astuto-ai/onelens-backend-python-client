# GetPolicyTicketsByPolicyIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationFields**](PaginationFields.md) | Pagination fields. | 
**policy_tickets** | [**List[GetSinglePolicyTicketByPolicyIdResponse]**](GetSinglePolicyTicketByPolicyIdResponse.md) | List of policy_tickets | 

## Example

```python
from onelens_backend_client.models.get_policy_tickets_by_policy_id_response import GetPolicyTicketsByPolicyIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTicketsByPolicyIdResponse from a JSON string
get_policy_tickets_by_policy_id_response_instance = GetPolicyTicketsByPolicyIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTicketsByPolicyIdResponse.to_json())

# convert the object into a dict
get_policy_tickets_by_policy_id_response_dict = get_policy_tickets_by_policy_id_response_instance.to_dict()
# create an instance of GetPolicyTicketsByPolicyIdResponse from a dict
get_policy_tickets_by_policy_id_response_form_dict = get_policy_tickets_by_policy_id_response.from_dict(get_policy_tickets_by_policy_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


