# OverrideTenantAnomalyConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_overrides** | [**AnomalyLogicOperationOutput**](AnomalyLogicOperationOutput.md) |  | [optional] 
**state** | [**TenantAnomalyState**](TenantAnomalyState.md) | The state of the policy template. | 
**id** | **str** | The unique identifier of the tenant policy. | 

## Example

```python
from onelens_backend_client.models.override_tenant_anomaly_config_response import OverrideTenantAnomalyConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OverrideTenantAnomalyConfigResponse from a JSON string
override_tenant_anomaly_config_response_instance = OverrideTenantAnomalyConfigResponse.from_json(json)
# print the JSON string representation of the object
print(OverrideTenantAnomalyConfigResponse.to_json())

# convert the object into a dict
override_tenant_anomaly_config_response_dict = override_tenant_anomaly_config_response_instance.to_dict()
# create an instance of OverrideTenantAnomalyConfigResponse from a dict
override_tenant_anomaly_config_response_form_dict = override_tenant_anomaly_config_response.from_dict(override_tenant_anomaly_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


