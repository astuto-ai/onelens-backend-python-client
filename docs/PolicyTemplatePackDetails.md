# PolicyTemplatePackDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_schema** | [**SourceSchema**](SourceSchema.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.policy_template_pack_details import PolicyTemplatePackDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplatePackDetails from a JSON string
policy_template_pack_details_instance = PolicyTemplatePackDetails.from_json(json)
# print the JSON string representation of the object
print(PolicyTemplatePackDetails.to_json())

# convert the object into a dict
policy_template_pack_details_dict = policy_template_pack_details_instance.to_dict()
# create an instance of PolicyTemplatePackDetails from a dict
policy_template_pack_details_form_dict = policy_template_pack_details.from_dict(policy_template_pack_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


