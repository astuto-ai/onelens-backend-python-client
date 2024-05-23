# ResourceCatalogApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_root_node**](ResourceCatalogApi.md#create_root_node) | Create Root Node
[**get_by_id**](ResourceCatalogApi.md#get_by_id) | Get resource catalog by id


# **create_root_node**
> ResponseResourceCatalogResponse create_root_node(tenant_id, resource_catalog_id)

Create Root Node

An API endpoint to get the resource catalog by ID

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_resource_catalog_response import ResponseResourceCatalogResponse
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
    api_instance = onelens_backend_client.ResourceCatalogApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    resource_catalog_id = 'resource_catalog_id_example' # str | 

    try:
        # Create Root Node
        api_response = api_instance.create_root_node(tenant_id, resource_catalog_id)
        print("The response of ResourceCatalogApi->create_root_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCatalogApi->create_root_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **resource_catalog_id** | **str**|  | 

### Return type

[**ResponseResourceCatalogResponse**](ResponseResourceCatalogResponse.md)

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

# **get_by_id**
> ResourceCatalogResponse get_by_id(resource_catalog_request)

Get resource catalog by id

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.resource_catalog_request import ResourceCatalogRequest
from onelens_backend_client.models.resource_catalog_response import ResourceCatalogResponse
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
    api_instance = onelens_backend_client.ResourceCatalogApi(api_client)
    resource_catalog_request = onelens_backend_client.ResourceCatalogRequest() # ResourceCatalogRequest | 

    try:
        # Get resource catalog by id
        api_response = api_instance.get_by_id(resource_catalog_request)
        print("The response of ResourceCatalogApi->get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCatalogApi->get_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_catalog_request** | [**ResourceCatalogRequest**](ResourceCatalogRequest.md)|  | 

### Return type

[**ResourceCatalogResponse**](ResourceCatalogResponse.md)

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

