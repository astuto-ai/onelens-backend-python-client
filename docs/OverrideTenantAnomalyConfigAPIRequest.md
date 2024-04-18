# OverrideTenantAnomalyConfigAPIRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_override** | [**AnomalyLogicOperationInput**](AnomalyLogicOperationInput.md) | The config overrides for the anomaly. | 

## Example

```python
from onelens_backend_client.models.override_tenant_anomaly_config_api_request import OverrideTenantAnomalyConfigAPIRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OverrideTenantAnomalyConfigAPIRequest from a JSON string
override_tenant_anomaly_config_api_request_instance = OverrideTenantAnomalyConfigAPIRequest.from_json(json)
# print the JSON string representation of the object
print(OverrideTenantAnomalyConfigAPIRequest.to_json())

# convert the object into a dict
override_tenant_anomaly_config_api_request_dict = override_tenant_anomaly_config_api_request_instance.to_dict()
# create an instance of OverrideTenantAnomalyConfigAPIRequest from a dict
override_tenant_anomaly_config_api_request_form_dict = override_tenant_anomaly_config_api_request.from_dict(override_tenant_anomaly_config_api_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


