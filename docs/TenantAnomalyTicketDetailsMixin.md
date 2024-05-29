# TenantAnomalyTicketDetailsMixin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from onelens_backend_client.models.tenant_anomaly_ticket_details_mixin import TenantAnomalyTicketDetailsMixin

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAnomalyTicketDetailsMixin from a JSON string
tenant_anomaly_ticket_details_mixin_instance = TenantAnomalyTicketDetailsMixin.from_json(json)
# print the JSON string representation of the object
print(TenantAnomalyTicketDetailsMixin.to_json())

# convert the object into a dict
tenant_anomaly_ticket_details_mixin_dict = tenant_anomaly_ticket_details_mixin_instance.to_dict()
# create an instance of TenantAnomalyTicketDetailsMixin from a dict
tenant_anomaly_ticket_details_mixin_form_dict = tenant_anomaly_ticket_details_mixin.from_dict(tenant_anomaly_ticket_details_mixin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


