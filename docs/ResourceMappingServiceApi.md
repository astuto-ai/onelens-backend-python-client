# ResourceMappingServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create**](ResourceMappingServiceApi.md#create) | create a resource hierarchy mapping
[**get_mapping_by_ol_id**](ResourceMappingServiceApi.md#get_mapping_by_ol_id) | get resource hierarchy mapping by ol id


# **create**
> object create(resource_hierarchy_mapping_request)

create a resource hierarchy mapping

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.resource_hierarchy_mapping_request import ResourceHierarchyMappingRequest
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
    api_instance = onelens_backend_client.ResourceMappingServiceApi(api_client)
    resource_hierarchy_mapping_request = onelens_backend_client.ResourceHierarchyMappingRequest() # ResourceHierarchyMappingRequest | 

    try:
        # create a resource hierarchy mapping
        api_response = api_instance.create(resource_hierarchy_mapping_request)
        print("The response of ResourceMappingServiceApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceMappingServiceApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_hierarchy_mapping_request** | [**ResourceHierarchyMappingRequest**](ResourceHierarchyMappingRequest.md)|  | 

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

# **get_mapping_by_ol_id**
> GetResourceHierarchyMappingByOlIdResponse get_mapping_by_ol_id(get_resource_hierarchy_mapping_by_ol_id_request)

get resource hierarchy mapping by ol id

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_resource_hierarchy_mapping_by_ol_id_request import GetResourceHierarchyMappingByOlIdRequest
from onelens_backend_client.models.get_resource_hierarchy_mapping_by_ol_id_response import GetResourceHierarchyMappingByOlIdResponse
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
    api_instance = onelens_backend_client.ResourceMappingServiceApi(api_client)
    get_resource_hierarchy_mapping_by_ol_id_request = onelens_backend_client.GetResourceHierarchyMappingByOlIdRequest() # GetResourceHierarchyMappingByOlIdRequest | 

    try:
        # get resource hierarchy mapping by ol id
        api_response = api_instance.get_mapping_by_ol_id(get_resource_hierarchy_mapping_by_ol_id_request)
        print("The response of ResourceMappingServiceApi->get_mapping_by_ol_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceMappingServiceApi->get_mapping_by_ol_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_resource_hierarchy_mapping_by_ol_id_request** | [**GetResourceHierarchyMappingByOlIdRequest**](GetResourceHierarchyMappingByOlIdRequest.md)|  | 

### Return type

[**GetResourceHierarchyMappingByOlIdResponse**](GetResourceHierarchyMappingByOlIdResponse.md)

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

