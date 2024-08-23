# RecommendationUnitMigrationServiceApi

All URIs are relative to *http://localhost*

Method | Description
------------- | -------------
[**create_recommendation_unit_pull_request**](RecommendationUnitMigrationServiceApi.md#create_recommendation_unit_pull_request) | Create a pull request for the recommendation_unit template
[**sync_recommendation_unit_from_repo**](RecommendationUnitMigrationServiceApi.md#sync_recommendation_unit_from_repo) | Sync recommendation_unit from repo


# **create_recommendation_unit_pull_request**
> CreateRecommenadtionUnitPullResponse create_recommendation_unit_pull_request(create_recommendation_unit_pull_request)

Create a pull request for the recommendation_unit template

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.create_recommenadtion_unit_pull_response import CreateRecommenadtionUnitPullResponse
from onelens_backend_client.models.create_recommendation_unit_pull_request import CreateRecommendationUnitPullRequest
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
    api_instance = onelens_backend_client.RecommendationUnitMigrationServiceApi(api_client)
    create_recommendation_unit_pull_request = onelens_backend_client.CreateRecommendationUnitPullRequest() # CreateRecommendationUnitPullRequest | 

    try:
        # Create a pull request for the recommendation_unit template
        api_response = api_instance.create_recommendation_unit_pull_request(create_recommendation_unit_pull_request)
        print("The response of RecommendationUnitMigrationServiceApi->create_recommendation_unit_pull_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationUnitMigrationServiceApi->create_recommendation_unit_pull_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_recommendation_unit_pull_request** | [**CreateRecommendationUnitPullRequest**](CreateRecommendationUnitPullRequest.md)|  | 

### Return type

[**CreateRecommenadtionUnitPullResponse**](CreateRecommenadtionUnitPullResponse.md)

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

# **sync_recommendation_unit_from_repo**
> SyncRecommendationUnitFromRepoResponse sync_recommendation_unit_from_repo(sync_recommendation_unit_from_repo_request)

Sync recommendation_unit from repo

### Example


```python
import onelens_backend_client
from onelens_backend_client.models.sync_recommendation_unit_from_repo_request import SyncRecommendationUnitFromRepoRequest
from onelens_backend_client.models.sync_recommendation_unit_from_repo_response import SyncRecommendationUnitFromRepoResponse
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
    api_instance = onelens_backend_client.RecommendationUnitMigrationServiceApi(api_client)
    sync_recommendation_unit_from_repo_request = onelens_backend_client.SyncRecommendationUnitFromRepoRequest() # SyncRecommendationUnitFromRepoRequest | 

    try:
        # Sync recommendation_unit from repo
        api_response = api_instance.sync_recommendation_unit_from_repo(sync_recommendation_unit_from_repo_request)
        print("The response of RecommendationUnitMigrationServiceApi->sync_recommendation_unit_from_repo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecommendationUnitMigrationServiceApi->sync_recommendation_unit_from_repo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sync_recommendation_unit_from_repo_request** | [**SyncRecommendationUnitFromRepoRequest**](SyncRecommendationUnitFromRepoRequest.md)|  | 

### Return type

[**SyncRecommendationUnitFromRepoResponse**](SyncRecommendationUnitFromRepoResponse.md)

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

