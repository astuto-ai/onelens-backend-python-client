# FeedbackModel

Model representing user feedback with a value indicating feedback status and additional optional details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.feedback_model import FeedbackModel

# TODO update the JSON string below
json = "{}"
# create an instance of FeedbackModel from a JSON string
feedback_model_instance = FeedbackModel.from_json(json)
# print the JSON string representation of the object
print(FeedbackModel.to_json())

# convert the object into a dict
feedback_model_dict = feedback_model_instance.to_dict()
# create an instance of FeedbackModel from a dict
feedback_model_form_dict = feedback_model.from_dict(feedback_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


