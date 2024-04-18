# AnomalyLogicOperationOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**List[AndItem]**](AndItem.md) |  | [optional] 
**var_or** | [**List[OrItem]**](OrItem.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.anomaly_logic_operation_output import AnomalyLogicOperationOutput

# TODO update the JSON string below
json = "{}"
# create an instance of AnomalyLogicOperationOutput from a JSON string
anomaly_logic_operation_output_instance = AnomalyLogicOperationOutput.from_json(json)
# print the JSON string representation of the object
print(AnomalyLogicOperationOutput.to_json())

# convert the object into a dict
anomaly_logic_operation_output_dict = anomaly_logic_operation_output_instance.to_dict()
# create an instance of AnomalyLogicOperationOutput from a dict
anomaly_logic_operation_output_form_dict = anomaly_logic_operation_output.from_dict(anomaly_logic_operation_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


