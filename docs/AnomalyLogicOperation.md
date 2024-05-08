# AnomalyLogicOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AndItem]**](AndItem.md) |  | [optional] 
**var_or** | [**List[OrItem]**](OrItem.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.anomaly_logic_operation import AnomalyLogicOperation

# TODO update the JSON string below
json = "{}"
# create an instance of AnomalyLogicOperation from a JSON string
anomaly_logic_operation_instance = AnomalyLogicOperation.from_json(json)
# print the JSON string representation of the object
print(AnomalyLogicOperation.to_json())

# convert the object into a dict
anomaly_logic_operation_dict = anomaly_logic_operation_instance.to_dict()
# create an instance of AnomalyLogicOperation from a dict
anomaly_logic_operation_form_dict = anomaly_logic_operation.from_dict(anomaly_logic_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


