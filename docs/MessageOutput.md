# MessageOutput

Model representing a message in a conversation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**parts** | [**List[MessagePart]**](MessagePart.md) | Parts of the message | 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**author** | [**MessageAuthor**](MessageAuthor.md) | Author of the message | 

## Example

```python
from onelens_backend_client.models.message_output import MessageOutput

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOutput from a JSON string
message_output_instance = MessageOutput.from_json(json)
# print the JSON string representation of the object
print(MessageOutput.to_json())

# convert the object into a dict
message_output_dict = message_output_instance.to_dict()
# create an instance of MessageOutput from a dict
message_output_form_dict = message_output.from_dict(message_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


