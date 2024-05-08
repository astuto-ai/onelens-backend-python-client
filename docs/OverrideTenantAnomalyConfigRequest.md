# OverrideTenantAnomalyConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_override** | [**AnomalyLogicOperation**](AnomalyLogicOperation.md) | The config overrides for the anomaly. | 
**tenant_id** | **str** | The id of the tenant. | 
**node_id** | **object** |  | [optional] 

## Example

```python
from onelens_backend_client.models.override_tenant_anomaly_config_request import OverrideTenantAnomalyConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OverrideTenantAnomalyConfigRequest from a JSON string
override_tenant_anomaly_config_request_instance = OverrideTenantAnomalyConfigRequest.from_json(json)
# print the JSON string representation of the object
print(OverrideTenantAnomalyConfigRequest.to_json())

# convert the object into a dict
override_tenant_anomaly_config_request_dict = override_tenant_anomaly_config_request_instance.to_dict()
# create an instance of OverrideTenantAnomalyConfigRequest from a dict
override_tenant_anomaly_config_request_form_dict = override_tenant_anomaly_config_request.from_dict(override_tenant_anomaly_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


