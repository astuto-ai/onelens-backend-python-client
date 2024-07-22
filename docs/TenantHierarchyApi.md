# TenantHierarchyApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_default_hierarchy**](TenantHierarchyApi.md#create_default_hierarchy) | Create Default Hierarchy
[**create_hierarchy_node**](TenantHierarchyApi.md#create_hierarchy_node) | Create Hierarchy Node
[**create_root_node**](TenantHierarchyApi.md#create_root_node) | Create Root Node
[**delete_hierarchy_node**](TenantHierarchyApi.md#delete_hierarchy_node) | Delete Hierarchy Node
[**get_hierarchy**](TenantHierarchyApi.md#get_hierarchy) | Get Hierarchy
[**get_hierarchy_leaf_nodes**](TenantHierarchyApi.md#get_hierarchy_leaf_nodes) | Get Hierarchy Leaf Nodes
[**publish_custom_hierarchy**](TenantHierarchyApi.md#publish_custom_hierarchy) | Publish Custom Hierarchy
[**update_hierarchy_node**](TenantHierarchyApi.md#update_hierarchy_node) | Update Hierarchy Node


# **create_default_hierarchy**
> ResponseCreateDefaultHierarchyResponse create_default_hierarchy()

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

    try:
        # Create Default Hierarchy
        api_response = api_instance.create_default_hierarchy()
        print("The response of TenantHierarchyApi->create_default_hierarchy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantHierarchyApi->create_default_hierarchy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hierarchy_node**
> ResponseCreateHierarchyRootNodeResponse create_hierarchy_node(create_hierarchy_node_api_request)

Create Hierarchy Node

An API endpoint to create a branch node in org hierarchy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_hierarchy_node_api_request import CreateHierarchyNodeAPIRequest
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
    create_hierarchy_node_api_request = onelens_backend_client.CreateHierarchyNodeAPIRequest() # CreateHierarchyNodeAPIRequest | 

    try:
        # Create Hierarchy Node
        api_response = api_instance.create_hierarchy_node(create_hierarchy_node_api_request)
        print("The response of TenantHierarchyApi->create_hierarchy_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantHierarchyApi->create_hierarchy_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_hierarchy_node_api_request** | [**CreateHierarchyNodeAPIRequest**](CreateHierarchyNodeAPIRequest.md)|  | 

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

# **create_root_node**
> ResponseCreateHierarchyRootNodeResponse create_root_node(create_hierarchy_root_node_api_request)

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
    create_hierarchy_root_node_api_request = onelens_backend_client.CreateHierarchyRootNodeAPIRequest() # CreateHierarchyRootNodeAPIRequest | 

    try:
        # Create Root Node
        api_response = api_instance.create_root_node(create_hierarchy_root_node_api_request)
        print("The response of TenantHierarchyApi->create_root_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantHierarchyApi->create_root_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_hierarchy_node**
> ResponseCreateHierarchyRootNodeResponse delete_hierarchy_node(node_id)

Delete Hierarchy Node

An API endpoint to delete a node in org hierarchy

### Example


```python
import onelens_backend_client
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
    node_id = 'node_id_example' # str | 

    try:
        # Delete Hierarchy Node
        api_response = api_instance.delete_hierarchy_node(node_id)
        print("The response of TenantHierarchyApi->delete_hierarchy_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantHierarchyApi->delete_hierarchy_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 

### Return type

[**ResponseCreateHierarchyRootNodeResponse**](ResponseCreateHierarchyRootNodeResponse.md)

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

# **get_hierarchy**
> ResponseGetHierarchyResponse get_hierarchy(state=state, type=type)

Get Hierarchy

An API endpoint to fetch org hierarchy with filters

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.hierarchy_state import HierarchyState
from onelens_backend_client.models.hierarchy_type import HierarchyType
from onelens_backend_client.models.response_get_hierarchy_response import ResponseGetHierarchyResponse
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
    state = onelens_backend_client.HierarchyState() # HierarchyState | Filter by state(ACTIVE, INACTIVE, DRAFT) (optional)
    type = onelens_backend_client.HierarchyType() # HierarchyType | Filter by type(DEFAUT, CUSTOM) (optional)

    try:
        # Get Hierarchy
        api_response = api_instance.get_hierarchy(state=state, type=type)
        print("The response of TenantHierarchyApi->get_hierarchy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantHierarchyApi->get_hierarchy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | [**HierarchyState**](.md)| Filter by state(ACTIVE, INACTIVE, DRAFT) | [optional] 
 **type** | [**HierarchyType**](.md)| Filter by type(DEFAUT, CUSTOM) | [optional] 

### Return type

[**ResponseGetHierarchyResponse**](ResponseGetHierarchyResponse.md)

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

# **get_hierarchy_leaf_nodes**
> ResponseCreateDefaultHierarchyResponse get_hierarchy_leaf_nodes()

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

    try:
        # Get Hierarchy Leaf Nodes
        api_response = api_instance.get_hierarchy_leaf_nodes()
        print("The response of TenantHierarchyApi->get_hierarchy_leaf_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantHierarchyApi->get_hierarchy_leaf_nodes: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish_custom_hierarchy**
> ResponseCreateHierarchyRootNodeResponse publish_custom_hierarchy()

Publish Custom Hierarchy

An API endpoint to publish org hierarchy

### Example


```python
import onelens_backend_client
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

    try:
        # Publish Custom Hierarchy
        api_response = api_instance.publish_custom_hierarchy()
        print("The response of TenantHierarchyApi->publish_custom_hierarchy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantHierarchyApi->publish_custom_hierarchy: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ResponseCreateHierarchyRootNodeResponse**](ResponseCreateHierarchyRootNodeResponse.md)

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

# **update_hierarchy_node**
> ResponseCreateHierarchyRootNodeResponse update_hierarchy_node(node_id, update_hierarchy_node_api_request)

Update Hierarchy Node

An API endpoint to update a node in org hierarchy

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_create_hierarchy_root_node_response import ResponseCreateHierarchyRootNodeResponse
from onelens_backend_client.models.update_hierarchy_node_api_request import UpdateHierarchyNodeAPIRequest
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
    node_id = 'node_id_example' # str | 
    update_hierarchy_node_api_request = onelens_backend_client.UpdateHierarchyNodeAPIRequest() # UpdateHierarchyNodeAPIRequest | 

    try:
        # Update Hierarchy Node
        api_response = api_instance.update_hierarchy_node(node_id, update_hierarchy_node_api_request)
        print("The response of TenantHierarchyApi->update_hierarchy_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantHierarchyApi->update_hierarchy_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**|  | 
 **update_hierarchy_node_api_request** | [**UpdateHierarchyNodeAPIRequest**](UpdateHierarchyNodeAPIRequest.md)|  | 

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

