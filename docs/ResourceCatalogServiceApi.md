# ResourceCatalogServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get_all**](ResourceCatalogServiceApi.md#get_all) | Get all resource catalogs
[**get_by_id**](ResourceCatalogServiceApi.md#get_by_id) | Get resource catalog by id
[**get_by_id_with_relations**](ResourceCatalogServiceApi.md#get_by_id_with_relations) | Get resource catalog by id with relations
[**get_resource_catalog_stats**](ResourceCatalogServiceApi.md#get_resource_catalog_stats) | Get Resource Catalog Stats


# **get_all**
> GetAllResourceCatalogsResponse get_all(get_all_resource_catalogs_request)

Get all resource catalogs

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_all_resource_catalogs_request import GetAllResourceCatalogsRequest
from onelens_backend_client.models.get_all_resource_catalogs_response import GetAllResourceCatalogsResponse
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
    api_instance = onelens_backend_client.ResourceCatalogServiceApi(api_client)
    get_all_resource_catalogs_request = onelens_backend_client.GetAllResourceCatalogsRequest() # GetAllResourceCatalogsRequest | 

    try:
        # Get all resource catalogs
        api_response = api_instance.get_all(get_all_resource_catalogs_request)
        print("The response of ResourceCatalogServiceApi->get_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCatalogServiceApi->get_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_all_resource_catalogs_request** | [**GetAllResourceCatalogsRequest**](GetAllResourceCatalogsRequest.md)|  | 

### Return type

[**GetAllResourceCatalogsResponse**](GetAllResourceCatalogsResponse.md)

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
    api_instance = onelens_backend_client.ResourceCatalogServiceApi(api_client)
    resource_catalog_request = onelens_backend_client.ResourceCatalogRequest() # ResourceCatalogRequest | 

    try:
        # Get resource catalog by id
        api_response = api_instance.get_by_id(resource_catalog_request)
        print("The response of ResourceCatalogServiceApi->get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCatalogServiceApi->get_by_id: %s\n" % e)
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

# **get_by_id_with_relations**
> GetResourceWithRelationResponse get_by_id_with_relations(resource_catalog_request)

Get resource catalog by id with relations

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_resource_with_relation_response import GetResourceWithRelationResponse
from onelens_backend_client.models.resource_catalog_request import ResourceCatalogRequest
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
    api_instance = onelens_backend_client.ResourceCatalogServiceApi(api_client)
    resource_catalog_request = onelens_backend_client.ResourceCatalogRequest() # ResourceCatalogRequest | 

    try:
        # Get resource catalog by id with relations
        api_response = api_instance.get_by_id_with_relations(resource_catalog_request)
        print("The response of ResourceCatalogServiceApi->get_by_id_with_relations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCatalogServiceApi->get_by_id_with_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_catalog_request** | [**ResourceCatalogRequest**](ResourceCatalogRequest.md)|  | 

### Return type

[**GetResourceWithRelationResponse**](GetResourceWithRelationResponse.md)

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

# **get_resource_catalog_stats**
> GetResourceCatalogStatsResponse get_resource_catalog_stats(get_resource_catalog_stats_request)

Get Resource Catalog Stats

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_resource_catalog_stats_request import GetResourceCatalogStatsRequest
from onelens_backend_client.models.get_resource_catalog_stats_response import GetResourceCatalogStatsResponse
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
    api_instance = onelens_backend_client.ResourceCatalogServiceApi(api_client)
    get_resource_catalog_stats_request = onelens_backend_client.GetResourceCatalogStatsRequest() # GetResourceCatalogStatsRequest | 

    try:
        # Get Resource Catalog Stats
        api_response = api_instance.get_resource_catalog_stats(get_resource_catalog_stats_request)
        print("The response of ResourceCatalogServiceApi->get_resource_catalog_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCatalogServiceApi->get_resource_catalog_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_resource_catalog_stats_request** | [**GetResourceCatalogStatsRequest**](GetResourceCatalogStatsRequest.md)|  | 

### Return type

[**GetResourceCatalogStatsResponse**](GetResourceCatalogStatsResponse.md)

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

