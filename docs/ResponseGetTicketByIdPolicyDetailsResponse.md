# ResponseGetTicketByIdPolicyDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetTicketByIdPolicyDetailsResponse**](GetTicketByIdPolicyDetailsResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_get_ticket_by_id_policy_details_response import ResponseGetTicketByIdPolicyDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseGetTicketByIdPolicyDetailsResponse from a JSON string
response_get_ticket_by_id_policy_details_response_instance = ResponseGetTicketByIdPolicyDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseGetTicketByIdPolicyDetailsResponse.to_json())

# convert the object into a dict
response_get_ticket_by_id_policy_details_response_dict = response_get_ticket_by_id_policy_details_response_instance.to_dict()
# create an instance of ResponseGetTicketByIdPolicyDetailsResponse from a dict
response_get_ticket_by_id_policy_details_response_form_dict = response_get_ticket_by_id_policy_details_response.from_dict(response_get_ticket_by_id_policy_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


