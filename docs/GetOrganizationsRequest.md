# GetOrganizationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**OrganizationFilters**](OrganizationFilters.md) | Filters to apply to the policy templates. | [optional] 

## Example

```python
from onelens_backend_client.models.get_organizations_request import GetOrganizationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationsRequest from a JSON string
get_organizations_request_instance = GetOrganizationsRequest.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationsRequest.to_json())

# convert the object into a dict
get_organizations_request_dict = get_organizations_request_instance.to_dict()
# create an instance of GetOrganizationsRequest from a dict
get_organizations_request_form_dict = get_organizations_request.from_dict(get_organizations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


