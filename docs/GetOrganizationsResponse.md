# GetOrganizationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | [**List[Organization]**](Organization.md) |  | 

## Example

```python
from onelens_backend_client.models.get_organizations_response import GetOrganizationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationsResponse from a JSON string
get_organizations_response_instance = GetOrganizationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationsResponse.to_json())

# convert the object into a dict
get_organizations_response_dict = get_organizations_response_instance.to_dict()
# create an instance of GetOrganizationsResponse from a dict
get_organizations_response_form_dict = get_organizations_response.from_dict(get_organizations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


