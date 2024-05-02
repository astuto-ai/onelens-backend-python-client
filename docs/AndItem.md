# AndItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gte** | [**List[AndItemGteInner]**](AndItemGteInner.md) |  | [optional] 
**gt** | [**List[AndItemGteInner]**](AndItemGteInner.md) |  | [optional] 

## Example

```python
from onelens_backend_client.models.and_item import AndItem

# TODO update the JSON string below
json = "{}"
# create an instance of AndItem from a JSON string
and_item_instance = AndItem.from_json(json)
# print the JSON string representation of the object
print(AndItem.to_json())

# convert the object into a dict
and_item_dict = and_item_instance.to_dict()
# create an instance of AndItem from a dict
and_item_form_dict = and_item.from_dict(and_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


