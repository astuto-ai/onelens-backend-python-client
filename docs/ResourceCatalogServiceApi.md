# ResourceCatalogServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**get_all**](ResourceCatalogServiceApi.md#get_all) | Get all resource catalogs
[**get_by_id**](ResourceCatalogServiceApi.md#get_by_id) | Get resource catalog by id
[**get_by_id_with_relations**](ResourceCatalogServiceApi.md#get_by_id_with_relations) | Get resource catalog by id with relations
[**get_resource_catalog_cost_data_stats**](ResourceCatalogServiceApi.md#get_resource_catalog_cost_data_stats) | Get Resource Catalog Cost Data Stats
[**get_resource_catalog_count_stats**](ResourceCatalogServiceApi.md#get_resource_catalog_count_stats) | Get Resource Catalog Count Stats
[**get_untagged_resource_catalog_count_stats**](ResourceCatalogServiceApi.md#get_untagged_resource_catalog_count_stats) | Get Untagged Resource Catalog Count Stats
[**upsert_resource_catalog_cost_data**](ResourceCatalogServiceApi.md#upsert_resource_catalog_cost_data) | Upsert resource catalog cost data


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

# **get_resource_catalog_cost_data_stats**
> GetResourceCatalogCostDataStatsResponse get_resource_catalog_cost_data_stats(get_resource_catalog_cost_data_stats_request)

Get Resource Catalog Cost Data Stats

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_resource_catalog_cost_data_stats_request import GetResourceCatalogCostDataStatsRequest
from onelens_backend_client.models.get_resource_catalog_cost_data_stats_response import GetResourceCatalogCostDataStatsResponse
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
    get_resource_catalog_cost_data_stats_request = onelens_backend_client.GetResourceCatalogCostDataStatsRequest() # GetResourceCatalogCostDataStatsRequest | 

    try:
        # Get Resource Catalog Cost Data Stats
        api_response = api_instance.get_resource_catalog_cost_data_stats(get_resource_catalog_cost_data_stats_request)
        print("The response of ResourceCatalogServiceApi->get_resource_catalog_cost_data_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCatalogServiceApi->get_resource_catalog_cost_data_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_resource_catalog_cost_data_stats_request** | [**GetResourceCatalogCostDataStatsRequest**](GetResourceCatalogCostDataStatsRequest.md)|  | 

### Return type

[**GetResourceCatalogCostDataStatsResponse**](GetResourceCatalogCostDataStatsResponse.md)

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

# **get_resource_catalog_count_stats**
> GetResourceCatalogCountStatsResponse get_resource_catalog_count_stats(get_resource_catalog_count_stats_request)

Get Resource Catalog Count Stats

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_resource_catalog_count_stats_request import GetResourceCatalogCountStatsRequest
from onelens_backend_client.models.get_resource_catalog_count_stats_response import GetResourceCatalogCountStatsResponse
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
    get_resource_catalog_count_stats_request = onelens_backend_client.GetResourceCatalogCountStatsRequest() # GetResourceCatalogCountStatsRequest | 

    try:
        # Get Resource Catalog Count Stats
        api_response = api_instance.get_resource_catalog_count_stats(get_resource_catalog_count_stats_request)
        print("The response of ResourceCatalogServiceApi->get_resource_catalog_count_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCatalogServiceApi->get_resource_catalog_count_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_resource_catalog_count_stats_request** | [**GetResourceCatalogCountStatsRequest**](GetResourceCatalogCountStatsRequest.md)|  | 

### Return type

[**GetResourceCatalogCountStatsResponse**](GetResourceCatalogCountStatsResponse.md)

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

# **get_untagged_resource_catalog_count_stats**
> GetUntaggedResourceCatalogCountStatsResponse get_untagged_resource_catalog_count_stats(get_untagged_resource_catalog_count_stats_request)

Get Untagged Resource Catalog Count Stats

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.get_untagged_resource_catalog_count_stats_request import GetUntaggedResourceCatalogCountStatsRequest
from onelens_backend_client.models.get_untagged_resource_catalog_count_stats_response import GetUntaggedResourceCatalogCountStatsResponse
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
    get_untagged_resource_catalog_count_stats_request = onelens_backend_client.GetUntaggedResourceCatalogCountStatsRequest() # GetUntaggedResourceCatalogCountStatsRequest | 

    try:
        # Get Untagged Resource Catalog Count Stats
        api_response = api_instance.get_untagged_resource_catalog_count_stats(get_untagged_resource_catalog_count_stats_request)
        print("The response of ResourceCatalogServiceApi->get_untagged_resource_catalog_count_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCatalogServiceApi->get_untagged_resource_catalog_count_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_untagged_resource_catalog_count_stats_request** | [**GetUntaggedResourceCatalogCountStatsRequest**](GetUntaggedResourceCatalogCountStatsRequest.md)|  | 

### Return type

[**GetUntaggedResourceCatalogCountStatsResponse**](GetUntaggedResourceCatalogCountStatsResponse.md)

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

# **upsert_resource_catalog_cost_data**
> object upsert_resource_catalog_cost_data(upsert_resource_catalog_cost_data_request)

Upsert resource catalog cost data

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.upsert_resource_catalog_cost_data_request import UpsertResourceCatalogCostDataRequest
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
    upsert_resource_catalog_cost_data_request = onelens_backend_client.UpsertResourceCatalogCostDataRequest() # UpsertResourceCatalogCostDataRequest | 

    try:
        # Upsert resource catalog cost data
        api_response = api_instance.upsert_resource_catalog_cost_data(upsert_resource_catalog_cost_data_request)
        print("The response of ResourceCatalogServiceApi->upsert_resource_catalog_cost_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ResourceCatalogServiceApi->upsert_resource_catalog_cost_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upsert_resource_catalog_cost_data_request** | [**UpsertResourceCatalogCostDataRequest**](UpsertResourceCatalogCostDataRequest.md)|  | 

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

