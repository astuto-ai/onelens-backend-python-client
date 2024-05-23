# TenantAnomalyTicketDetailsMixin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomaly_id** | **str** | The id of the anomaly being violated. | 

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


