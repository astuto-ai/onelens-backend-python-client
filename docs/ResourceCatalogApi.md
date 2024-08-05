# ResourceCatalogApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get_all_resource_catalogs**](ResourceCatalogApi.md#get_all_resource_catalogs) | Get All Resource Catalogs
[**get_resource_catalog**](ResourceCatalogApi.md#get_resource_catalog) | Get Resource Catalog
[**get_resource_catalog_stats**](ResourceCatalogApi.md#get_resource_catalog_stats) | Get Resource Catalog Stats
[**get_resource_catalog_with_relationships**](ResourceCatalogApi.md#get_resource_catalog_with_relationships) | Get Resource Catalog With Relationships


# **get_all_resource_catalogs**
> ResponseGetResourceWithRelationResponse get_all_resource_catalogs(get_all_resource_catalogs_api_request)

Get All Resource Catalogs

An API endpoint to get all resource catalogs

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_all_resource_catalogs_api_request import GetAllResourceCatalogsApiRequest
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
    get_all_resource_catalogs_api_request = onelens_backend_client.GetAllResourceCatalogsApiRequest() # GetAllResourceCatalogsApiRequest | 

    try:
        # Get All Resource Catalogs
        api_response = api_instance.get_all_resource_catalogs(get_all_resource_catalogs_api_request)
        print("The response of ResourceCatalogApi->get_all_resource_catalogs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCatalogApi->get_all_resource_catalogs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_all_resource_catalogs_api_request** | [**GetAllResourceCatalogsApiRequest**](GetAllResourceCatalogsApiRequest.md)|  | 

### Return type

[**ResponseGetResourceWithRelationResponse**](ResponseGetResourceWithRelationResponse.md)

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

# **get_resource_catalog_stats**
> ResponseGetResourceCatalogStatsResponse get_resource_catalog_stats(get_resource_catalog_stats_api_request)

Get Resource Catalog Stats

API to get all Resource Catalog Stats

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_resource_catalog_stats_api_request import GetResourceCatalogStatsAPIRequest
from onelens_backend_client.models.response_get_resource_catalog_stats_response import ResponseGetResourceCatalogStatsResponse
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
    get_resource_catalog_stats_api_request = onelens_backend_client.GetResourceCatalogStatsAPIRequest() # GetResourceCatalogStatsAPIRequest | 

    try:
        # Get Resource Catalog Stats
        api_response = api_instance.get_resource_catalog_stats(get_resource_catalog_stats_api_request)
        print("The response of ResourceCatalogApi->get_resource_catalog_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCatalogApi->get_resource_catalog_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_resource_catalog_stats_api_request** | [**GetResourceCatalogStatsAPIRequest**](GetResourceCatalogStatsAPIRequest.md)|  | 

### Return type

[**ResponseGetResourceCatalogStatsResponse**](ResponseGetResourceCatalogStatsResponse.md)

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

