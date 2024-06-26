# CloudMetadataApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_root_node**](CloudMetadataApi.md#create_root_node) | Create Root Node
[**create_root_node_0**](CloudMetadataApi.md#create_root_node_0) | Create Root Node


# **create_root_node**
> ResponseGetCloudMetadataResponse create_root_node(tenant_id)

Create Root Node

An API endpoint to get tenant cloud metadata like cloud id, region, service...

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_cloud_metadata_response import ResponseGetCloudMetadataResponse
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
    api_instance = onelens_backend_client.CloudMetadataApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Create Root Node
        api_response = api_instance.create_root_node(tenant_id)
        print("The response of CloudMetadataApi->create_root_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudMetadataApi->create_root_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ResponseGetCloudMetadataResponse**](ResponseGetCloudMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_root_node_0**
> ResponseGetCloudMetadataResponse create_root_node_0()

Create Root Node

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_cloud_metadata_response import ResponseGetCloudMetadataResponse
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
    api_instance = onelens_backend_client.CloudMetadataApi(api_client)

    try:
        # Create Root Node
        api_response = api_instance.create_root_node_0()
        print("The response of CloudMetadataApi->create_root_node_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudMetadataApi->create_root_node_0: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResponseGetCloudMetadataResponse**](ResponseGetCloudMetadataResponse.md)

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

