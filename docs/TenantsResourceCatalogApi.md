# TenantsResourceCatalogApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_root_node**](TenantsResourceCatalogApi.md#create_root_node) | Create Root Node


# **create_root_node**
> ResponseResourceHierarchyMappingResponse create_root_node()

Create Root Node

An API endpoint to create resource and hierarchy mapping

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_resource_hierarchy_mapping_response import ResponseResourceHierarchyMappingResponse
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
    api_instance = onelens_backend_client.TenantsResourceCatalogApi(api_client)

    try:
        # Create Root Node
        api_response = api_instance.create_root_node()
        print("The response of TenantsResourceCatalogApi->create_root_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantsResourceCatalogApi->create_root_node: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResponseResourceHierarchyMappingResponse**](ResponseResourceHierarchyMappingResponse.md)

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

