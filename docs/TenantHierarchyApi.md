# TenantHierarchyApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_default_hierarchy**](TenantHierarchyApi.md#create_default_hierarchy) | Create Default Hierarchy
[**create_root_node**](TenantHierarchyApi.md#create_root_node) | Create Root Node
[**get_hierarchy_leaf_nodes**](TenantHierarchyApi.md#get_hierarchy_leaf_nodes) | Get Hierarchy Leaf Nodes


# **create_default_hierarchy**
> ResponseCreateDefaultHierarchyResponse create_default_hierarchy(tenant_id)

Create Default Hierarchy

An API endpoint to create default org hierarchy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_create_default_hierarchy_response import ResponseCreateDefaultHierarchyResponse
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
    api_instance = onelens_backend_client.TenantHierarchyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Create Default Hierarchy
        api_response = api_instance.create_default_hierarchy(tenant_id)
        print("The response of TenantHierarchyApi->create_default_hierarchy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantHierarchyApi->create_default_hierarchy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ResponseCreateDefaultHierarchyResponse**](ResponseCreateDefaultHierarchyResponse.md)

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

# **create_root_node**
> ResponseCreateHierarchyRootNodeResponse create_root_node(tenant_id, create_hierarchy_root_node_api_request)

Create Root Node

An API endpoint to create a branch node in org hierarchy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_hierarchy_root_node_api_request import CreateHierarchyRootNodeAPIRequest
from onelens_backend_client.models.response_create_hierarchy_root_node_response import ResponseCreateHierarchyRootNodeResponse
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
    api_instance = onelens_backend_client.TenantHierarchyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 
    create_hierarchy_root_node_api_request = onelens_backend_client.CreateHierarchyRootNodeAPIRequest() # CreateHierarchyRootNodeAPIRequest | 

    try:
        # Create Root Node
        api_response = api_instance.create_root_node(tenant_id, create_hierarchy_root_node_api_request)
        print("The response of TenantHierarchyApi->create_root_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantHierarchyApi->create_root_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 
 **create_hierarchy_root_node_api_request** | [**CreateHierarchyRootNodeAPIRequest**](CreateHierarchyRootNodeAPIRequest.md)|  | 

### Return type

[**ResponseCreateHierarchyRootNodeResponse**](ResponseCreateHierarchyRootNodeResponse.md)

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

# **get_hierarchy_leaf_nodes**
> ResponseCreateDefaultHierarchyResponse get_hierarchy_leaf_nodes(tenant_id)

Get Hierarchy Leaf Nodes

An API endpoint to create default org hierarchy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_create_default_hierarchy_response import ResponseCreateDefaultHierarchyResponse
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
    api_instance = onelens_backend_client.TenantHierarchyApi(api_client)
    tenant_id = 'tenant_id_example' # str | 

    try:
        # Get Hierarchy Leaf Nodes
        api_response = api_instance.get_hierarchy_leaf_nodes(tenant_id)
        print("The response of TenantHierarchyApi->get_hierarchy_leaf_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantHierarchyApi->get_hierarchy_leaf_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | 

### Return type

[**ResponseCreateDefaultHierarchyResponse**](ResponseCreateDefaultHierarchyResponse.md)

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

