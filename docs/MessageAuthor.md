# MessageAuthor

Model representing the author of a message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | [optional] 
**role** | [**AuthorRole**](AuthorRole.md) | Role of the author (USER or ASSISTANT) | 

## Example

```python
from onelens_backend_client.models.message_author import MessageAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of MessageAuthor from a JSON string
message_author_instance = MessageAuthor.from_json(json)
# print the JSON string representation of the object
print(MessageAuthor.to_json())

# convert the object into a dict
message_author_dict = message_author_instance.to_dict()
# create an instance of MessageAuthor from a dict
message_author_form_dict = message_author.from_dict(message_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


