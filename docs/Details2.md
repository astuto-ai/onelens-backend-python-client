# Details2

Details of the ticket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | The id of the policy being violated. | 
**entity_id** | **str** | The id of the resource experiencing policy violation. | 
**entity_type** | **str** | The type of the resource experiencing policy violation. | 
**policy_template_id** | **str** | The id of the policy template being violated. | 
**policy_config** | **str** | The config of the policy being violated. | 
**policy_config_version** | **str** | The config version of the policy being violated. | 
**violation_attributes** | **str** | The attributes of the violation. | 
**anomaly_id** | **str** | The id of the anomaly being violated. | 

## Example

```python
from onelens_backend_client.models.details2 import Details2

# TODO update the JSON string below
json = "{}"
# create an instance of Details2 from a JSON string
details2_instance = Details2.from_json(json)
# print the JSON string representation of the object
print(Details2.to_json())

# convert the object into a dict
details2_dict = details2_instance.to_dict()
# create an instance of Details2 from a dict
details2_form_dict = details2.from_dict(details2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


