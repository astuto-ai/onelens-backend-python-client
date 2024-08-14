# CloudAccountMetadataServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get_cloud_account_metadata**](CloudAccountMetadataServiceApi.md#get_cloud_account_metadata) | get cloud account metadata for tenant


# **get_cloud_account_metadata**
> GetCloudAccountMetadataResponse get_cloud_account_metadata(get_cloud_account_metadata_request)

get cloud account metadata for tenant

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_cloud_account_metadata_request import GetCloudAccountMetadataRequest
from onelens_backend_client.models.get_cloud_account_metadata_response import GetCloudAccountMetadataResponse
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
    api_instance = onelens_backend_client.CloudAccountMetadataServiceApi(api_client)
    get_cloud_account_metadata_request = onelens_backend_client.GetCloudAccountMetadataRequest() # GetCloudAccountMetadataRequest | 

    try:
        # get cloud account metadata for tenant
        api_response = api_instance.get_cloud_account_metadata(get_cloud_account_metadata_request)
        print("The response of CloudAccountMetadataServiceApi->get_cloud_account_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudAccountMetadataServiceApi->get_cloud_account_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_cloud_account_metadata_request** | [**GetCloudAccountMetadataRequest**](GetCloudAccountMetadataRequest.md)|  | 

### Return type

[**GetCloudAccountMetadataResponse**](GetCloudAccountMetadataResponse.md)

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

