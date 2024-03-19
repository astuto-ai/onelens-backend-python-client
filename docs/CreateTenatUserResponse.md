# CreateTenatUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the user | 
**ol_user_id** | **str** | The catalog DB user identifier. | 
**status** | [**Status**](Status.md) |  | 
**role** | [**Role**](Role.md) |  | 
**sources** | [**Sources**](Sources.md) |  | 

## Example

```python
from openapi_client.models.create_tenat_user_response import CreateTenatUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTenatUserResponse from a JSON string
create_tenat_user_response_instance = CreateTenatUserResponse.from_json(json)
# print the JSON string representation of the object
print(CreateTenatUserResponse.to_json())

# convert the object into a dict
create_tenat_user_response_dict = create_tenat_user_response_instance.to_dict()
# create an instance of CreateTenatUserResponse from a dict
create_tenat_user_response_form_dict = create_tenat_user_response.from_dict(create_tenat_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


