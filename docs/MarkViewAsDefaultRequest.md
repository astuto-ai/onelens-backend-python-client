# MarkViewAsDefaultRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the saved view | 
**ol_user_id** | **str** | Unique onelens identifier for the user | 
**tenant_id** | **str** | The unique identifier of the tenant | 

## Example

```python
from onelens_backend_client.models.mark_view_as_default_request import MarkViewAsDefaultRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MarkViewAsDefaultRequest from a JSON string
mark_view_as_default_request_instance = MarkViewAsDefaultRequest.from_json(json)
# print the JSON string representation of the object
print(MarkViewAsDefaultRequest.to_json())

# convert the object into a dict
mark_view_as_default_request_dict = mark_view_as_default_request_instance.to_dict()
# create an instance of MarkViewAsDefaultRequest from a dict
mark_view_as_default_request_form_dict = mark_view_as_default_request.from_dict(mark_view_as_default_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


