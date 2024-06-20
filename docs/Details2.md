# Details2

Details of the ticket

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | The id of the policy being violated. | 
**policy_template_id** | **str** | The id of the policy template being violated. | 
**policy_config** | **object** | The config of the policy being violated. | 
**policy_config_hash** | **str** |  | [optional] 
**policy_config_version** | **int** | The config version of the policy being violated. | 
**violation_attributes** | **object** | The attributes of the violation. | 
**potential_cost_saving** | **float** | The potential cost accrued because of the violation. | 
**preferred_recommendation_id** | **str** |  | [optional] 
**rule_definition_hash** | **str** |  | [optional] 
**anomalies** | [**List[AnomalyRcaIdsMixin]**](AnomalyRcaIdsMixin.md) | List of anomaly ids and rca ids. | 
**total_cost_impact** | **float** | Total cost incurred due to the anomaly. | 
**rca_hash** | **str** | The hash of the RCA associated with the anomaly. | 
**deviation** | [**Deviation**](Deviation.md) |  | 
**duration** | **float** | The duration of the anomaly. | 
**duration_unit** | **str** | The duration unit of the anomaly. | 
**source_type** | [**AnomalySourceType**](AnomalySourceType.md) | The source type of the anomaly. | 
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


