# LastRunAtUpdateItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | The id of the tenant policy. | 
**last_run_at** | **datetime** | The timestamp of the last run of the policy. | 

## Example

```python
from onelens_backend_client.models.last_run_at_update_item import LastRunAtUpdateItem

# TODO update the JSON string below
json = "{}"
# create an instance of LastRunAtUpdateItem from a JSON string
last_run_at_update_item_instance = LastRunAtUpdateItem.from_json(json)
# print the JSON string representation of the object
print(LastRunAtUpdateItem.to_json())

# convert the object into a dict
last_run_at_update_item_dict = last_run_at_update_item_instance.to_dict()
# create an instance of LastRunAtUpdateItem from a dict
last_run_at_update_item_form_dict = last_run_at_update_item.from_dict(last_run_at_update_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


