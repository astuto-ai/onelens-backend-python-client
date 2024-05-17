# DataRetrieverApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**query_data_retriever**](DataRetrieverApi.md#query_data_retriever) | Query Data Retriever


# **query_data_retriever**
> ResponseDataRetrieverResponse query_data_retriever(data_retriever_request)

Query Data Retriever

An API endpoint that retrieves tenant with tenant IDs.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.data_retriever_request import DataRetrieverRequest
from onelens_backend_client.models.response_data_retriever_response import ResponseDataRetrieverResponse
from onelens_backend_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = onelens_backend_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with onelens_backend_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelens_backend_client.DataRetrieverApi(api_client)
    data_retriever_request = onelens_backend_client.DataRetrieverRequest() # DataRetrieverRequest | 

    try:
        # Query Data Retriever
        api_response = api_instance.query_data_retriever(data_retriever_request)
        print("The response of DataRetrieverApi->query_data_retriever:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataRetrieverApi->query_data_retriever: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_retriever_request** | [**DataRetrieverRequest**](DataRetrieverRequest.md)|  | 

### Return type

[**ResponseDataRetrieverResponse**](ResponseDataRetrieverResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

