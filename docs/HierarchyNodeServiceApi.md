# HierarchyNodeServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_default_hierarchy**](HierarchyNodeServiceApi.md#create_default_hierarchy) | create default hierarchy
[**create_node**](HierarchyNodeServiceApi.md#create_node) | create a node in org hierarchy
[**create_root_node**](HierarchyNodeServiceApi.md#create_root_node) | create a root node in org hierarchy
[**delete_node**](HierarchyNodeServiceApi.md#delete_node) | delete a node in org hierarchy
[**get_hierarchy**](HierarchyNodeServiceApi.md#get_hierarchy) | get hierarchy
[**get_hierarchy_flat**](HierarchyNodeServiceApi.md#get_hierarchy_flat) | get hierarchy flat
[**get_hierarchy_node_by_id**](HierarchyNodeServiceApi.md#get_hierarchy_node_by_id) | get hierarchy node by id
[**get_leaf_nodes**](HierarchyNodeServiceApi.md#get_leaf_nodes) | get hierarchy leaf nodes
[**publish_custom_hierarchy**](HierarchyNodeServiceApi.md#publish_custom_hierarchy) | publish custom hierarchy
[**update_node**](HierarchyNodeServiceApi.md#update_node) | update a node in org hierarchy


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

# **create_node**
> CreateHierarchyNodeResponse create_node(create_hierarchy_node_request)

create a node in org hierarchy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_hierarchy_node_request import CreateHierarchyNodeRequest
from onelens_backend_client.models.create_hierarchy_node_response import CreateHierarchyNodeResponse
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
    create_hierarchy_node_request = onelens_backend_client.CreateHierarchyNodeRequest() # CreateHierarchyNodeRequest | 

    try:
        # create a node in org hierarchy
        api_response = api_instance.create_node(create_hierarchy_node_request)
        print("The response of HierarchyNodeServiceApi->create_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HierarchyNodeServiceApi->create_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_hierarchy_node_request** | [**CreateHierarchyNodeRequest**](CreateHierarchyNodeRequest.md)|  | 

### Return type

[**CreateHierarchyNodeResponse**](CreateHierarchyNodeResponse.md)

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

# **delete_node**
> object delete_node(delete_hierarchy_node_request)

delete a node in org hierarchy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.delete_hierarchy_node_request import DeleteHierarchyNodeRequest
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
    delete_hierarchy_node_request = onelens_backend_client.DeleteHierarchyNodeRequest() # DeleteHierarchyNodeRequest | 

    try:
        # delete a node in org hierarchy
        api_response = api_instance.delete_node(delete_hierarchy_node_request)
        print("The response of HierarchyNodeServiceApi->delete_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HierarchyNodeServiceApi->delete_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_hierarchy_node_request** | [**DeleteHierarchyNodeRequest**](DeleteHierarchyNodeRequest.md)|  | 

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

# **get_hierarchy**
> GetHierarchyResponse get_hierarchy(get_hierarchy_request)

get hierarchy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_hierarchy_request import GetHierarchyRequest
from onelens_backend_client.models.get_hierarchy_response import GetHierarchyResponse
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
    get_hierarchy_request = onelens_backend_client.GetHierarchyRequest() # GetHierarchyRequest | 

    try:
        # get hierarchy
        api_response = api_instance.get_hierarchy(get_hierarchy_request)
        print("The response of HierarchyNodeServiceApi->get_hierarchy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HierarchyNodeServiceApi->get_hierarchy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_hierarchy_request** | [**GetHierarchyRequest**](GetHierarchyRequest.md)|  | 

### Return type

[**GetHierarchyResponse**](GetHierarchyResponse.md)

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

# **get_hierarchy_flat**
> GetHierarchyFlatResponse get_hierarchy_flat(get_hierarchy_flat_request)

get hierarchy flat

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_hierarchy_flat_request import GetHierarchyFlatRequest
from onelens_backend_client.models.get_hierarchy_flat_response import GetHierarchyFlatResponse
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
    get_hierarchy_flat_request = onelens_backend_client.GetHierarchyFlatRequest() # GetHierarchyFlatRequest | 

    try:
        # get hierarchy flat
        api_response = api_instance.get_hierarchy_flat(get_hierarchy_flat_request)
        print("The response of HierarchyNodeServiceApi->get_hierarchy_flat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HierarchyNodeServiceApi->get_hierarchy_flat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_hierarchy_flat_request** | [**GetHierarchyFlatRequest**](GetHierarchyFlatRequest.md)|  | 

### Return type

[**GetHierarchyFlatResponse**](GetHierarchyFlatResponse.md)

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

# **get_hierarchy_node_by_id**
> object get_hierarchy_node_by_id(get_hierarchy_node_by_id_request)

get hierarchy node by id

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_hierarchy_node_by_id_request import GetHierarchyNodeByIdRequest
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
    get_hierarchy_node_by_id_request = onelens_backend_client.GetHierarchyNodeByIdRequest() # GetHierarchyNodeByIdRequest | 

    try:
        # get hierarchy node by id
        api_response = api_instance.get_hierarchy_node_by_id(get_hierarchy_node_by_id_request)
        print("The response of HierarchyNodeServiceApi->get_hierarchy_node_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HierarchyNodeServiceApi->get_hierarchy_node_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_hierarchy_node_by_id_request** | [**GetHierarchyNodeByIdRequest**](GetHierarchyNodeByIdRequest.md)|  | 

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

# **publish_custom_hierarchy**
> object publish_custom_hierarchy(publish_custom_hierarchy_request)

publish custom hierarchy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.publish_custom_hierarchy_request import PublishCustomHierarchyRequest
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
    publish_custom_hierarchy_request = onelens_backend_client.PublishCustomHierarchyRequest() # PublishCustomHierarchyRequest | 

    try:
        # publish custom hierarchy
        api_response = api_instance.publish_custom_hierarchy(publish_custom_hierarchy_request)
        print("The response of HierarchyNodeServiceApi->publish_custom_hierarchy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HierarchyNodeServiceApi->publish_custom_hierarchy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **publish_custom_hierarchy_request** | [**PublishCustomHierarchyRequest**](PublishCustomHierarchyRequest.md)|  | 

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

# **update_node**
> UpdateHierarchyNodeResponse update_node(update_hierarchy_node_request)

update a node in org hierarchy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.update_hierarchy_node_request import UpdateHierarchyNodeRequest
from onelens_backend_client.models.update_hierarchy_node_response import UpdateHierarchyNodeResponse
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
    update_hierarchy_node_request = onelens_backend_client.UpdateHierarchyNodeRequest() # UpdateHierarchyNodeRequest | 

    try:
        # update a node in org hierarchy
        api_response = api_instance.update_node(update_hierarchy_node_request)
        print("The response of HierarchyNodeServiceApi->update_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HierarchyNodeServiceApi->update_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_hierarchy_node_request** | [**UpdateHierarchyNodeRequest**](UpdateHierarchyNodeRequest.md)|  | 

### Return type

[**UpdateHierarchyNodeResponse**](UpdateHierarchyNodeResponse.md)

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

