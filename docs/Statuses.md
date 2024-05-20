# Statuses

List of ticket Statuss for which tickets are to be fetched.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from onelens_backend_client.models.statuses import Statuses

# TODO update the JSON string below
json = "{}"
# create an instance of Statuses from a JSON string
statuses_instance = Statuses.from_json(json)
# print the JSON string representation of the object
print(Statuses.to_json())

# convert the object into a dict
statuses_dict = statuses_instance.to_dict()
# create an instance of Statuses from a dict
statuses_form_dict = statuses.from_dict(statuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


