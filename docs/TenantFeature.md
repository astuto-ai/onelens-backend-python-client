# TenantFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the tenant feature | 
**feature_id** | **str** | Unique identifier for the feature from catalog | 
**feature_name** | **str** | Name of the feature | 
**is_enabled** | **bool** | Whether the feature is enabled | 
**scope** | [**TenantFeatureScope**](TenantFeatureScope.md) | Scope of the feature | 
**entity_id** | **str** |  | [optional] 
**config** | [**FeatureConfig**](FeatureConfig.md) |  | [optional] 
**created_at** | **datetime** | Creation datetime of the feature | 
**updated_at** | **datetime** | Update datetime of the feature | 

## Example

```python
from onelens_backend_client.models.tenant_feature import TenantFeature

# TODO update the JSON string below
json = "{}"
# create an instance of TenantFeature from a JSON string
tenant_feature_instance = TenantFeature.from_json(json)
# print the JSON string representation of the object
print(TenantFeature.to_json())

# convert the object into a dict
tenant_feature_dict = tenant_feature_instance.to_dict()
# create an instance of TenantFeature from a dict
tenant_feature_form_dict = tenant_feature.from_dict(tenant_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


