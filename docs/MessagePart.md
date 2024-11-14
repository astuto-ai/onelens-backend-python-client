# MessagePart

Model representing a part of a message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**MessagePartType**](MessagePartType.md) | Type of the message part | 
**value** | **object** |  | 

## Example

```python
from onelens_backend_client.models.message_part import MessagePart

# TODO update the JSON string below
json = "{}"
# create an instance of MessagePart from a JSON string
message_part_instance = MessagePart.from_json(json)
# print the JSON string representation of the object
print(MessagePart.to_json())

# convert the object into a dict
message_part_dict = message_part_instance.to_dict()
# create an instance of MessagePart from a dict
message_part_form_dict = message_part.from_dict(message_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


