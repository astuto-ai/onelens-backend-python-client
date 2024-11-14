# CostAnalyzerServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**fetch_graph_for_cost_analyzer**](CostAnalyzerServiceApi.md#fetch_graph_for_cost_analyzer) | Fetch Graph For Cost Analyzer
[**fetch_stats_for_cost_analyzer**](CostAnalyzerServiceApi.md#fetch_stats_for_cost_analyzer) | Fetch Stats For Cost Analyzer
[**fetch_table_for_cost_analyzer**](CostAnalyzerServiceApi.md#fetch_table_for_cost_analyzer) | Fetch Table For Cost Analyzer


# **fetch_graph_for_cost_analyzer**
> CostAnalyzerGraphResponse fetch_graph_for_cost_analyzer(cost_analyzer_graph_request)

Fetch Graph For Cost Analyzer

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
    api_instance = onelens_backend_client.CostAnalyzerServiceApi(api_client)
    cost_analyzer_graph_request = onelens_backend_client.CostAnalyzerGraphRequest() # CostAnalyzerGraphRequest | 

    try:
        # Fetch Graph For Cost Analyzer
        api_response = api_instance.fetch_graph_for_cost_analyzer(cost_analyzer_graph_request)
        print("The response of CostAnalyzerServiceApi->fetch_graph_for_cost_analyzer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAnalyzerServiceApi->fetch_graph_for_cost_analyzer: %s\n" % e)
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

# **fetch_stats_for_cost_analyzer**
> CostAnalyzerStatsResponse fetch_stats_for_cost_analyzer(cost_analyzer_stats_request)

Fetch Stats For Cost Analyzer

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
    api_instance = onelens_backend_client.CostAnalyzerServiceApi(api_client)
    cost_analyzer_stats_request = onelens_backend_client.CostAnalyzerStatsRequest() # CostAnalyzerStatsRequest | 

    try:
        # Fetch Stats For Cost Analyzer
        api_response = api_instance.fetch_stats_for_cost_analyzer(cost_analyzer_stats_request)
        print("The response of CostAnalyzerServiceApi->fetch_stats_for_cost_analyzer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAnalyzerServiceApi->fetch_stats_for_cost_analyzer: %s\n" % e)
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

# **fetch_table_for_cost_analyzer**
> CostAnalyzerTableResponse fetch_table_for_cost_analyzer(cost_analyzer_table_request)

Fetch Table For Cost Analyzer

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
    api_instance = onelens_backend_client.CostAnalyzerServiceApi(api_client)
    cost_analyzer_table_request = onelens_backend_client.CostAnalyzerTableRequest() # CostAnalyzerTableRequest | 

    try:
        # Fetch Table For Cost Analyzer
        api_response = api_instance.fetch_table_for_cost_analyzer(cost_analyzer_table_request)
        print("The response of CostAnalyzerServiceApi->fetch_table_for_cost_analyzer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CostAnalyzerServiceApi->fetch_table_for_cost_analyzer: %s\n" % e)
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

