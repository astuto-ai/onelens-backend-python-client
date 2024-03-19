# PolicyTemplateFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_query** | [**SearchQuery**](SearchQuery.md) |  | [optional] 
**parent_ptp_ids** | **List[str]** | Filter by parent policy template pack id. | [optional] [default to []]
**states** | [**List[PolicyTemplateState]**](PolicyTemplateState.md) | Filter by state. Default is ACTIVE. | [optional] [default to [ACTIVE]]
**categories** | [**List[PolicyCategory]**](PolicyCategory.md) | Filter by type. | [optional] [default to []]
**providers** | [**List[Provider]**](Provider.md) | Filter by provider. | [optional] [default to []]
**services** | [**List[CreatePolicyTemplateRequestServicesInner]**](CreatePolicyTemplateRequestServicesInner.md) | Filter by services. | [optional] [default to []]
**execution_types** | [**List[PolicyExecutionType]**](PolicyExecutionType.md) | Filter by execution type. | [optional] [default to []]

## Example

```python
from openapi_client.models.policy_template_filters import PolicyTemplateFilters

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplateFilters from a JSON string
policy_template_filters_instance = PolicyTemplateFilters.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplateFilters.to_json())

# convert the object into a dict
policy_template_filters_dict = policy_template_filters_instance.to_dict()
# create an instance of PolicyTemplateFilters from a dict
policy_template_filters_form_dict = policy_template_filters.from_dict(policy_template_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


