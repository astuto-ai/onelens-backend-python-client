# CloudAccountMetadataApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get_cloud_account_metadata**](CloudAccountMetadataApi.md#get_cloud_account_metadata) | Get Cloud Account Metadata


# **get_cloud_account_metadata**
> ResponseGetCloudAccountMetadataResponse get_cloud_account_metadata(get_cloud_account_metadata_request)

Get Cloud Account Metadata

An API endpoint to get tenant cloud account metadata like cloud id, alias...

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_cloud_account_metadata_request import GetCloudAccountMetadataRequest
from onelens_backend_client.models.response_get_cloud_account_metadata_response import ResponseGetCloudAccountMetadataResponse
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
    api_instance = onelens_backend_client.CloudAccountMetadataApi(api_client)
    get_cloud_account_metadata_request = onelens_backend_client.GetCloudAccountMetadataRequest() # GetCloudAccountMetadataRequest | 

    try:
        # Get Cloud Account Metadata
        api_response = api_instance.get_cloud_account_metadata(get_cloud_account_metadata_request)
        print("The response of CloudAccountMetadataApi->get_cloud_account_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountMetadataApi->get_cloud_account_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cloud_account_metadata_request** | [**GetCloudAccountMetadataRequest**](GetCloudAccountMetadataRequest.md)|  | 

### Return type

[**ResponseGetCloudAccountMetadataResponse**](ResponseGetCloudAccountMetadataResponse.md)

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

