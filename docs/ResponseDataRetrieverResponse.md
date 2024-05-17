# ResponseDataRetrieverResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DataRetrieverResponse**](DataRetrieverResponse.md) |  | 
**message** | **str** |  | [optional] 

## Example

```python
from onelens_backend_client.models.response_data_retriever_response import ResponseDataRetrieverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseDataRetrieverResponse from a JSON string
response_data_retriever_response_instance = ResponseDataRetrieverResponse.from_json(json)
# print the JSON string representation of the object
print(ResponseDataRetrieverResponse.to_json())

# convert the object into a dict
response_data_retriever_response_dict = response_data_retriever_response_instance.to_dict()
# create an instance of ResponseDataRetrieverResponse from a dict
response_data_retriever_response_form_dict = response_data_retriever_response.from_dict(response_data_retriever_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


