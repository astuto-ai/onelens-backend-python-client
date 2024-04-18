# ResponseOverrideTenantAnomalyConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OverrideTenantAnomalyConfigResponse**](OverrideTenantAnomalyConfigResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_override_tenant_anomaly_config_response import ResponseOverrideTenantAnomalyConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseOverrideTenantAnomalyConfigResponse from a JSON string
response_override_tenant_anomaly_config_response_instance = ResponseOverrideTenantAnomalyConfigResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseOverrideTenantAnomalyConfigResponse.to_json())

# convert the object into a dict
response_override_tenant_anomaly_config_response_dict = response_override_tenant_anomaly_config_response_instance.to_dict()
# create an instance of ResponseOverrideTenantAnomalyConfigResponse from a dict
response_override_tenant_anomaly_config_response_form_dict = response_override_tenant_anomaly_config_response.from_dict(response_override_tenant_anomaly_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


