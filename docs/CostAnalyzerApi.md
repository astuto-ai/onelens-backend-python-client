# CostAnalyzerApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**fetch_cost_analyzer_graph**](CostAnalyzerApi.md#fetch_cost_analyzer_graph) | Fetch Cost Analyzer Graph
[**fetch_cost_analyzer_stats**](CostAnalyzerApi.md#fetch_cost_analyzer_stats) | Fetch Cost Analyzer Stats
[**fetch_cost_analyzer_table**](CostAnalyzerApi.md#fetch_cost_analyzer_table) | Fetch Cost Analyzer Table


# **fetch_cost_analyzer_graph**
> CostAnalyzerGraphResponse fetch_cost_analyzer_graph(cost_analyzer_graph_request)

Fetch Cost Analyzer Graph

enables an anomaly for a tenant in the tenant DB.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.cost_analyzer_graph_request import CostAnalyzerGraphRequest
from onelens_backend_client.models.cost_analyzer_graph_response import CostAnalyzerGraphResponse
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
    api_instance = onelens_backend_client.CostAnalyzerApi(api_client)
    cost_analyzer_graph_request = onelens_backend_client.CostAnalyzerGraphRequest() # CostAnalyzerGraphRequest | 

    try:
        # Fetch Cost Analyzer Graph
        api_response = api_instance.fetch_cost_analyzer_graph(cost_analyzer_graph_request)
        print("The response of CostAnalyzerApi->fetch_cost_analyzer_graph:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAnalyzerApi->fetch_cost_analyzer_graph: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_analyzer_graph_request** | [**CostAnalyzerGraphRequest**](CostAnalyzerGraphRequest.md)|  | 

### Return type

[**CostAnalyzerGraphResponse**](CostAnalyzerGraphResponse.md)

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

# **fetch_cost_analyzer_stats**
> CostAnalyzerStatsResponse fetch_cost_analyzer_stats(cost_analyzer_stats_request)

Fetch Cost Analyzer Stats

fetches stats for cost analyzer.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.cost_analyzer_stats_request import CostAnalyzerStatsRequest
from onelens_backend_client.models.cost_analyzer_stats_response import CostAnalyzerStatsResponse
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
    api_instance = onelens_backend_client.CostAnalyzerApi(api_client)
    cost_analyzer_stats_request = onelens_backend_client.CostAnalyzerStatsRequest() # CostAnalyzerStatsRequest | 

    try:
        # Fetch Cost Analyzer Stats
        api_response = api_instance.fetch_cost_analyzer_stats(cost_analyzer_stats_request)
        print("The response of CostAnalyzerApi->fetch_cost_analyzer_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAnalyzerApi->fetch_cost_analyzer_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_analyzer_stats_request** | [**CostAnalyzerStatsRequest**](CostAnalyzerStatsRequest.md)|  | 

### Return type

[**CostAnalyzerStatsResponse**](CostAnalyzerStatsResponse.md)

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

# **fetch_cost_analyzer_table**
> CostAnalyzerTableResponse fetch_cost_analyzer_table(cost_analyzer_table_request)

Fetch Cost Analyzer Table

fetches table for cost analyzer.

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.cost_analyzer_table_request import CostAnalyzerTableRequest
from onelens_backend_client.models.cost_analyzer_table_response import CostAnalyzerTableResponse
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
    api_instance = onelens_backend_client.CostAnalyzerApi(api_client)
    cost_analyzer_table_request = onelens_backend_client.CostAnalyzerTableRequest() # CostAnalyzerTableRequest | 

    try:
        # Fetch Cost Analyzer Table
        api_response = api_instance.fetch_cost_analyzer_table(cost_analyzer_table_request)
        print("The response of CostAnalyzerApi->fetch_cost_analyzer_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAnalyzerApi->fetch_cost_analyzer_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cost_analyzer_table_request** | [**CostAnalyzerTableRequest**](CostAnalyzerTableRequest.md)|  | 

### Return type

[**CostAnalyzerTableResponse**](CostAnalyzerTableResponse.md)

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

