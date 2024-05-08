# OrganizationFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[str]** |  | [optional] 
**names** | **List[str]** |  | [optional] 
**organization_states** | **List[str]** |  | [optional] 

## Example

```python
from onelens_backend_client.models.organization_filters import OrganizationFilters

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationFilters from a JSON string
organization_filters_instance = OrganizationFilters.from_json(json)
# print the JSON string representation of the object
print(OrganizationFilters.to_json())

# convert the object into a dict
organization_filters_dict = organization_filters_instance.to_dict()
# create an instance of OrganizationFilters from a dict
organization_filters_form_dict = organization_filters.from_dict(organization_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


