# AnomalyRcaIdsMixin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomaly_id** | **str** | The unique identifier of the anomaly | 
**rca_ids** | **List[str]** | List of rca ids associated with the anomaly | 

## Example

```python
from onelens_backend_client.models.anomaly_rca_ids_mixin import AnomalyRcaIdsMixin

# TODO update the JSON string below
json = "{}"
# create an instance of AnomalyRcaIdsMixin from a JSON string
anomaly_rca_ids_mixin_instance = AnomalyRcaIdsMixin.from_json(json)
# print the JSON string representation of the object
print(AnomalyRcaIdsMixin.to_json())

# convert the object into a dict
anomaly_rca_ids_mixin_dict = anomaly_rca_ids_mixin_instance.to_dict()
# create an instance of AnomalyRcaIdsMixin from a dict
anomaly_rca_ids_mixin_form_dict = anomaly_rca_ids_mixin.from_dict(anomaly_rca_ids_mixin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


