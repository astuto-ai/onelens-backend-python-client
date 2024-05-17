# DataRetrieverRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | [**DataRetrieverQuery**](DataRetrieverQuery.md) | Query to be executed | 

## Example

```python
from onelens_backend_client.models.data_retriever_request import DataRetrieverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DataRetrieverRequest from a JSON string
data_retriever_request_instance = DataRetrieverRequest.from_json(json)
# print the JSON string representation of the object
print(DataRetrieverRequest.to_json())

# convert the object into a dict
data_retriever_request_dict = data_retriever_request_instance.to_dict()
# create an instance of DataRetrieverRequest from a dict
data_retriever_request_form_dict = data_retriever_request.from_dict(data_retriever_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


