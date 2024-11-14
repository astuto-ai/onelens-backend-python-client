# TicketsSelectedField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | Name of the field | 
**category** | [**TicketsSelectedFieldsCategory**](TicketsSelectedFieldsCategory.md) | Category of the field | 

## Example

```python
from onelens_backend_client.models.tickets_selected_field import TicketsSelectedField

# TODO update the JSON string below
json = "{}"
# create an instance of TicketsSelectedField from a JSON string
tickets_selected_field_instance = TicketsSelectedField.from_json(json)
# print the JSON string representation of the object
print(TicketsSelectedField.to_json())

# convert the object into a dict
tickets_selected_field_dict = tickets_selected_field_instance.to_dict()
# create an instance of TicketsSelectedField from a dict
tickets_selected_field_form_dict = tickets_selected_field.from_dict(tickets_selected_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


