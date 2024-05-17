# HierarchyNodeServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_default_hierarchy**](HierarchyNodeServiceApi.md#create_default_hierarchy) | create default hierarchy
[**create_root_node**](HierarchyNodeServiceApi.md#create_root_node) | create a root node in org hierarchy
[**get_leaf_nodes**](HierarchyNodeServiceApi.md#get_leaf_nodes) | get hierarchy leaf nodes


# **create_default_hierarchy**
> object create_default_hierarchy(create_default_hierarchy_request)

create default hierarchy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_default_hierarchy_request import CreateDefaultHierarchyRequest
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
    api_instance = onelens_backend_client.HierarchyNodeServiceApi(api_client)
    create_default_hierarchy_request = onelens_backend_client.CreateDefaultHierarchyRequest() # CreateDefaultHierarchyRequest | 

    try:
        # create default hierarchy
        api_response = api_instance.create_default_hierarchy(create_default_hierarchy_request)
        print("The response of HierarchyNodeServiceApi->create_default_hierarchy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HierarchyNodeServiceApi->create_default_hierarchy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_default_hierarchy_request** | [**CreateDefaultHierarchyRequest**](CreateDefaultHierarchyRequest.md)|  | 

### Return type

**object**

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

# **create_root_node**
> CreateHierarchyRootNodeResponse create_root_node(create_hierarchy_root_node_request)

create a root node in org hierarchy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_hierarchy_root_node_request import CreateHierarchyRootNodeRequest
from onelens_backend_client.models.create_hierarchy_root_node_response import CreateHierarchyRootNodeResponse
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
    api_instance = onelens_backend_client.HierarchyNodeServiceApi(api_client)
    create_hierarchy_root_node_request = onelens_backend_client.CreateHierarchyRootNodeRequest() # CreateHierarchyRootNodeRequest | 

    try:
        # create a root node in org hierarchy
        api_response = api_instance.create_root_node(create_hierarchy_root_node_request)
        print("The response of HierarchyNodeServiceApi->create_root_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HierarchyNodeServiceApi->create_root_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_hierarchy_root_node_request** | [**CreateHierarchyRootNodeRequest**](CreateHierarchyRootNodeRequest.md)|  | 

### Return type

[**CreateHierarchyRootNodeResponse**](CreateHierarchyRootNodeResponse.md)

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

# **get_leaf_nodes**
> GetLeafNodesResponse get_leaf_nodes(get_leaf_nodes_request)

get hierarchy leaf nodes

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_leaf_nodes_request import GetLeafNodesRequest
from onelens_backend_client.models.get_leaf_nodes_response import GetLeafNodesResponse
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
    api_instance = onelens_backend_client.HierarchyNodeServiceApi(api_client)
    get_leaf_nodes_request = onelens_backend_client.GetLeafNodesRequest() # GetLeafNodesRequest | 

    try:
        # get hierarchy leaf nodes
        api_response = api_instance.get_leaf_nodes(get_leaf_nodes_request)
        print("The response of HierarchyNodeServiceApi->get_leaf_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HierarchyNodeServiceApi->get_leaf_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_leaf_nodes_request** | [**GetLeafNodesRequest**](GetLeafNodesRequest.md)|  | 

### Return type

[**GetLeafNodesResponse**](GetLeafNodesResponse.md)

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

