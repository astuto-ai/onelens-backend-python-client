# TenantAnomalySettingFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**states** | [**List[TenantAnomalyState]**](TenantAnomalyState.md) | Filter by state. Default is ACTIVE. | [optional] [default to [ACTIVE]]

## Example

```python
from onelens_backend_client.models.tenant_anomaly_setting_filters import TenantAnomalySettingFilters

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAnomalySettingFilters from a JSON string
tenant_anomaly_setting_filters_instance = TenantAnomalySettingFilters.from_json(json)
# print the JSON string representation of the object
print(TenantAnomalySettingFilters.to_json())

# convert the object into a dict
tenant_anomaly_setting_filters_dict = tenant_anomaly_setting_filters_instance.to_dict()
# create an instance of TenantAnomalySettingFilters from a dict
tenant_anomaly_setting_filters_form_dict = tenant_anomaly_setting_filters.from_dict(tenant_anomaly_setting_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


