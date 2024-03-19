# onelens_backend_client.DefaultApi

All URIs are relative to *http://localhost*

Method | Description
------------- | ------------- | -------------
[**root**](DefaultApi.md#root) | Root


# **root**
> object root()

Root

### Example


```python
import onelens_backend_client
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
    api_instance = onelens_backend_client.DefaultApi(api_client)

    try:
        # Root
        api_response = api_instance.root()
        print("The response of DefaultApi->root:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->root: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

