# GetPolicyTicketsExportToResponseType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | downloadable url | 
**extenstion** | **str** | The file extension of the file | 

## Example

```python
from onelens_backend_client.models.get_policy_tickets_export_to_response_type import GetPolicyTicketsExportToResponseType

# TODO update the JSON string below
json = "{}"
# create an instance of GetPolicyTicketsExportToResponseType from a JSON string
get_policy_tickets_export_to_response_type_instance = GetPolicyTicketsExportToResponseType.from_json(json)
# print the JSON string representation of the object
print(GetPolicyTicketsExportToResponseType.to_json())

# convert the object into a dict
get_policy_tickets_export_to_response_type_dict = get_policy_tickets_export_to_response_type_instance.to_dict()
# create an instance of GetPolicyTicketsExportToResponseType from a dict
get_policy_tickets_export_to_response_type_form_dict = get_policy_tickets_export_to_response_type.from_dict(get_policy_tickets_export_to_response_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


