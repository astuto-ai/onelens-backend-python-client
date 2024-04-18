# AnomalyLogicOperationInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AndItem]**](AndItem.md) |  | [optional] 
**var_or** | [**List[OrItem]**](OrItem.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.anomaly_logic_operation_input import AnomalyLogicOperationInput

# TODO update the JSON string below
json = "{}"
# create an instance of AnomalyLogicOperationInput from a JSON string
anomaly_logic_operation_input_instance = AnomalyLogicOperationInput.from_json(json)
# print the JSON string representation of the object
print(AnomalyLogicOperationInput.to_json())

# convert the object into a dict
anomaly_logic_operation_input_dict = anomaly_logic_operation_input_instance.to_dict()
# create an instance of AnomalyLogicOperationInput from a dict
anomaly_logic_operation_input_form_dict = anomaly_logic_operation_input.from_dict(anomaly_logic_operation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


