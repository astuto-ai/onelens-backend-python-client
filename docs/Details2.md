# Details2

Details of the ticket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | The id of the policy being violated. | 
**policy_template_id** | **str** | The id of the policy template being violated. | 
**policy_config** | **str** | The config of the policy being violated. | 
**policy_config_version** | **str** | The config version of the policy being violated. | 
**violation_attributes** | **str** | The attributes of the violation. | 
**anomalies** | **List[object]** | List of anomaly ids and rca ids. | 
**total_cost_impact** | **float** | Total cost incurred due to the anomaly. | 
**rca_hash** | **str** | The hash of the RCA associated with the anomaly. | 
**deviation** | **float** | The percentage delta of the anomaly. | 
**duration** | **float** | The duration of the anomaly. | 
**duration_unit** | **str** | The duration unit of the anomaly. | 
**source_type** | **str** | The source type of the anomaly. | 
**usage_type** | **str** | The usage type of the anomaly. | 
**operation_type** | **str** | The operation type of the anomaly. | 
**is_continuous** | **bool** | Is the anomaly continuous. | 

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


