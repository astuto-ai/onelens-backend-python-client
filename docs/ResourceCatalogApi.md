# ResourceCatalogApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get_resource_catalog**](ResourceCatalogApi.md#get_resource_catalog) | Get Resource Catalog
[**get_resource_catalog_with_relationships**](ResourceCatalogApi.md#get_resource_catalog_with_relationships) | Get Resource Catalog With Relationships


# **get_resource_catalog**
> ResponseResourceCatalogResponse get_resource_catalog(resource_catalog_id)

Get Resource Catalog

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
    resource_catalog_id = 'resource_catalog_id_example' # str | 

    try:
        # Get Resource Catalog
        api_response = api_instance.get_resource_catalog(resource_catalog_id)
        print("The response of ResourceCatalogApi->get_resource_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCatalogApi->get_resource_catalog: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_resource_catalog_with_relationships**
> ResponseGetResourceWithRelationResponse get_resource_catalog_with_relationships(resource_catalog_id)

Get Resource Catalog With Relationships

An API endpoint to get the resource catalog by ID

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.response_get_resource_with_relation_response import ResponseGetResourceWithRelationResponse
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
    resource_catalog_id = 'resource_catalog_id_example' # str | 

    try:
        # Get Resource Catalog With Relationships
        api_response = api_instance.get_resource_catalog_with_relationships(resource_catalog_id)
        print("The response of ResourceCatalogApi->get_resource_catalog_with_relationships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCatalogApi->get_resource_catalog_with_relationships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_catalog_id** | **str**|  | 

### Return type

[**ResponseGetResourceWithRelationResponse**](ResponseGetResourceWithRelationResponse.md)

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

