# neurelo.RestaurantsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aggregate_by_restaurants**](RestaurantsApi.md#aggregate_by_restaurants) | **GET** /rest/restaurants/__aggregate | 
[**create_many_restaurants**](RestaurantsApi.md#create_many_restaurants) | **POST** /rest/restaurants | 
[**create_one_restaurants**](RestaurantsApi.md#create_one_restaurants) | **POST** /rest/restaurants/__one | 
[**delete_restaurants**](RestaurantsApi.md#delete_restaurants) | **DELETE** /rest/restaurants | 
[**delete_restaurants_by_name**](RestaurantsApi.md#delete_restaurants_by_name) | **DELETE** /rest/restaurants/{value} | 
[**find_restaurants**](RestaurantsApi.md#find_restaurants) | **GET** /rest/restaurants | 
[**find_restaurants_by_name**](RestaurantsApi.md#find_restaurants_by_name) | **GET** /rest/restaurants/{value} | 
[**group_by_restaurants**](RestaurantsApi.md#group_by_restaurants) | **GET** /rest/restaurants/__groupBy | 
[**update_restaurants**](RestaurantsApi.md#update_restaurants) | **PATCH** /rest/restaurants | 
[**update_restaurants_by_name**](RestaurantsApi.md#update_restaurants_by_name) | **PATCH** /rest/restaurants/{value} | 


# **aggregate_by_restaurants**
> AggregateByRestaurants200Response aggregate_by_restaurants(select, filter=filter, order_by=order_by, skip=skip, take=take)



Aggregate by restaurants

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import neurelo
from neurelo.models.aggregate_by_restaurants200_response import AggregateByRestaurants200Response
from neurelo.models.restaurants_aggregate_input import RestaurantsAggregateInput
from neurelo.models.restaurants_order_by_with_relation_input import RestaurantsOrderByWithRelationInput
from neurelo.models.restaurants_where_input import RestaurantsWhereInput
from neurelo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = neurelo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with neurelo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurelo.RestaurantsApi(api_client)
    select = neurelo.RestaurantsAggregateInput() # RestaurantsAggregateInput | 
    filter = neurelo.RestaurantsWhereInput() # RestaurantsWhereInput |  (optional)
    order_by = [neurelo.RestaurantsOrderByWithRelationInput()] # List[RestaurantsOrderByWithRelationInput] |  (optional)
    skip = 56 # int |  (optional)
    take = 56 # int |  (optional)

    try:
        api_response = api_instance.aggregate_by_restaurants(select, filter=filter, order_by=order_by, skip=skip, take=take)
        print("The response of RestaurantsApi->aggregate_by_restaurants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantsApi->aggregate_by_restaurants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | [**RestaurantsAggregateInput**](.md)|  | 
 **filter** | [**RestaurantsWhereInput**](.md)|  | [optional] 
 **order_by** | [**List[RestaurantsOrderByWithRelationInput]**](RestaurantsOrderByWithRelationInput.md)|  | [optional] 
 **skip** | **int**|  | [optional] 
 **take** | **int**|  | [optional] 

### Return type

[**AggregateByRestaurants200Response**](AggregateByRestaurants200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results found |  -  |
**400** | Invalid Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**503** | Timed Out |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_many_restaurants**
> CreateManyRestaurants201Response create_many_restaurants(restaurants_create_many_input)



Create multiple restaurants records

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import neurelo
from neurelo.models.create_many_restaurants201_response import CreateManyRestaurants201Response
from neurelo.models.restaurants_create_many_input import RestaurantsCreateManyInput
from neurelo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = neurelo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with neurelo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurelo.RestaurantsApi(api_client)
    restaurants_create_many_input = [neurelo.RestaurantsCreateManyInput()] # List[RestaurantsCreateManyInput] | 

    try:
        api_response = api_instance.create_many_restaurants(restaurants_create_many_input)
        print("The response of RestaurantsApi->create_many_restaurants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantsApi->create_many_restaurants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurants_create_many_input** | [**List[RestaurantsCreateManyInput]**](RestaurantsCreateManyInput.md)|  | 

### Return type

[**CreateManyRestaurants201Response**](CreateManyRestaurants201Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Records created |  -  |
**400** | Invalid Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**503** | Timed Out |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_one_restaurants**
> CreateOneRestaurants201Response create_one_restaurants(restaurants_create_input, select=select)



Create one restaurants record

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import neurelo
from neurelo.models.create_one_restaurants201_response import CreateOneRestaurants201Response
from neurelo.models.restaurants_create_input import RestaurantsCreateInput
from neurelo.models.restaurants_select_input import RestaurantsSelectInput
from neurelo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = neurelo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with neurelo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurelo.RestaurantsApi(api_client)
    restaurants_create_input = neurelo.RestaurantsCreateInput() # RestaurantsCreateInput | 
    select = neurelo.RestaurantsSelectInput() # RestaurantsSelectInput |  (optional)

    try:
        api_response = api_instance.create_one_restaurants(restaurants_create_input, select=select)
        print("The response of RestaurantsApi->create_one_restaurants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantsApi->create_one_restaurants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurants_create_input** | [**RestaurantsCreateInput**](RestaurantsCreateInput.md)|  | 
 **select** | [**RestaurantsSelectInput**](.md)|  | [optional] 

### Return type

[**CreateOneRestaurants201Response**](CreateOneRestaurants201Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Record created |  -  |
**400** | Invalid Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**503** | Timed Out |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_restaurants**
> CreateManyRestaurants201Response delete_restaurants(filter=filter)



Delete multiple restaurants records

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import neurelo
from neurelo.models.create_many_restaurants201_response import CreateManyRestaurants201Response
from neurelo.models.restaurants_where_input import RestaurantsWhereInput
from neurelo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = neurelo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with neurelo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurelo.RestaurantsApi(api_client)
    filter = neurelo.RestaurantsWhereInput() # RestaurantsWhereInput |  (optional)

    try:
        api_response = api_instance.delete_restaurants(filter=filter)
        print("The response of RestaurantsApi->delete_restaurants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantsApi->delete_restaurants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | [**RestaurantsWhereInput**](.md)|  | [optional] 

### Return type

[**CreateManyRestaurants201Response**](CreateManyRestaurants201Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Records deleted |  -  |
**400** | Invalid Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**503** | Timed Out |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_restaurants_by_name**
> CreateOneRestaurants201Response delete_restaurants_by_name(value, select=select)



Delete one restaurants record by name

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import neurelo
from neurelo.models.create_one_restaurants201_response import CreateOneRestaurants201Response
from neurelo.models.restaurants_select_input import RestaurantsSelectInput
from neurelo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = neurelo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with neurelo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurelo.RestaurantsApi(api_client)
    value = 'value_example' # str | 
    select = neurelo.RestaurantsSelectInput() # RestaurantsSelectInput |  (optional)

    try:
        api_response = api_instance.delete_restaurants_by_name(value, select=select)
        print("The response of RestaurantsApi->delete_restaurants_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantsApi->delete_restaurants_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**|  | 
 **select** | [**RestaurantsSelectInput**](.md)|  | [optional] 

### Return type

[**CreateOneRestaurants201Response**](CreateOneRestaurants201Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Record deleted |  -  |
**400** | Invalid Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**503** | Timed Out |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_restaurants**
> FindRestaurants200Response find_restaurants(select=select, filter=filter, order_by=order_by, skip=skip, take=take)



Retrieve multiple restaurants records

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import neurelo
from neurelo.models.find_restaurants200_response import FindRestaurants200Response
from neurelo.models.restaurants_order_by_with_relation_input import RestaurantsOrderByWithRelationInput
from neurelo.models.restaurants_select_input import RestaurantsSelectInput
from neurelo.models.restaurants_where_input import RestaurantsWhereInput
from neurelo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = neurelo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with neurelo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurelo.RestaurantsApi(api_client)
    select = neurelo.RestaurantsSelectInput() # RestaurantsSelectInput |  (optional)
    filter = neurelo.RestaurantsWhereInput() # RestaurantsWhereInput |  (optional)
    order_by = [neurelo.RestaurantsOrderByWithRelationInput()] # List[RestaurantsOrderByWithRelationInput] |  (optional)
    skip = 56 # int |  (optional)
    take = 56 # int |  (optional)

    try:
        api_response = api_instance.find_restaurants(select=select, filter=filter, order_by=order_by, skip=skip, take=take)
        print("The response of RestaurantsApi->find_restaurants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantsApi->find_restaurants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | [**RestaurantsSelectInput**](.md)|  | [optional] 
 **filter** | [**RestaurantsWhereInput**](.md)|  | [optional] 
 **order_by** | [**List[RestaurantsOrderByWithRelationInput]**](RestaurantsOrderByWithRelationInput.md)|  | [optional] 
 **skip** | **int**|  | [optional] 
 **take** | **int**|  | [optional] 

### Return type

[**FindRestaurants200Response**](FindRestaurants200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results found |  -  |
**400** | Invalid Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**503** | Timed Out |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_restaurants_by_name**
> CreateOneRestaurants201Response find_restaurants_by_name(value, select=select)



Find one restaurants record by name

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import neurelo
from neurelo.models.create_one_restaurants201_response import CreateOneRestaurants201Response
from neurelo.models.restaurants_select_input import RestaurantsSelectInput
from neurelo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = neurelo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with neurelo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurelo.RestaurantsApi(api_client)
    value = 'value_example' # str | 
    select = neurelo.RestaurantsSelectInput() # RestaurantsSelectInput |  (optional)

    try:
        api_response = api_instance.find_restaurants_by_name(value, select=select)
        print("The response of RestaurantsApi->find_restaurants_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantsApi->find_restaurants_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**|  | 
 **select** | [**RestaurantsSelectInput**](.md)|  | [optional] 

### Return type

[**CreateOneRestaurants201Response**](CreateOneRestaurants201Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results found |  -  |
**400** | Invalid Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**503** | Timed Out |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_by_restaurants**
> GroupByRestaurants200Response group_by_restaurants(select, filter=filter, order_by=order_by, group_by=group_by, having=having, skip=skip, take=take)



Group by restaurants

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import neurelo
from neurelo.models.group_by_restaurants200_response import GroupByRestaurants200Response
from neurelo.models.restaurants_group_by_input import RestaurantsGroupByInput
from neurelo.models.restaurants_order_by_with_aggregation_input import RestaurantsOrderByWithAggregationInput
from neurelo.models.restaurants_scalar_field_enum import RestaurantsScalarFieldEnum
from neurelo.models.restaurants_scalar_where_with_aggregates_input import RestaurantsScalarWhereWithAggregatesInput
from neurelo.models.restaurants_where_input import RestaurantsWhereInput
from neurelo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = neurelo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with neurelo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurelo.RestaurantsApi(api_client)
    select = neurelo.RestaurantsGroupByInput() # RestaurantsGroupByInput | 
    filter = neurelo.RestaurantsWhereInput() # RestaurantsWhereInput |  (optional)
    order_by = [neurelo.RestaurantsOrderByWithAggregationInput()] # List[RestaurantsOrderByWithAggregationInput] |  (optional)
    group_by = [neurelo.RestaurantsScalarFieldEnum()] # List[RestaurantsScalarFieldEnum] |  (optional)
    having = neurelo.RestaurantsScalarWhereWithAggregatesInput() # RestaurantsScalarWhereWithAggregatesInput |  (optional)
    skip = 56 # int |  (optional)
    take = 56 # int |  (optional)

    try:
        api_response = api_instance.group_by_restaurants(select, filter=filter, order_by=order_by, group_by=group_by, having=having, skip=skip, take=take)
        print("The response of RestaurantsApi->group_by_restaurants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantsApi->group_by_restaurants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select** | [**RestaurantsGroupByInput**](.md)|  | 
 **filter** | [**RestaurantsWhereInput**](.md)|  | [optional] 
 **order_by** | [**List[RestaurantsOrderByWithAggregationInput]**](RestaurantsOrderByWithAggregationInput.md)|  | [optional] 
 **group_by** | [**List[RestaurantsScalarFieldEnum]**](RestaurantsScalarFieldEnum.md)|  | [optional] 
 **having** | [**RestaurantsScalarWhereWithAggregatesInput**](.md)|  | [optional] 
 **skip** | **int**|  | [optional] 
 **take** | **int**|  | [optional] 

### Return type

[**GroupByRestaurants200Response**](GroupByRestaurants200Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Results found |  -  |
**400** | Invalid Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**503** | Timed Out |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_restaurants**
> CreateManyRestaurants201Response update_restaurants(restaurants_update_many_input, filter=filter)



Update multiple restaurants records

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import neurelo
from neurelo.models.create_many_restaurants201_response import CreateManyRestaurants201Response
from neurelo.models.restaurants_update_many_input import RestaurantsUpdateManyInput
from neurelo.models.restaurants_where_input import RestaurantsWhereInput
from neurelo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = neurelo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with neurelo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurelo.RestaurantsApi(api_client)
    restaurants_update_many_input = neurelo.RestaurantsUpdateManyInput() # RestaurantsUpdateManyInput | 
    filter = neurelo.RestaurantsWhereInput() # RestaurantsWhereInput |  (optional)

    try:
        api_response = api_instance.update_restaurants(restaurants_update_many_input, filter=filter)
        print("The response of RestaurantsApi->update_restaurants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantsApi->update_restaurants: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **restaurants_update_many_input** | [**RestaurantsUpdateManyInput**](RestaurantsUpdateManyInput.md)|  | 
 **filter** | [**RestaurantsWhereInput**](.md)|  | [optional] 

### Return type

[**CreateManyRestaurants201Response**](CreateManyRestaurants201Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Records updated |  -  |
**400** | Invalid Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**503** | Timed Out |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_restaurants_by_name**
> CreateOneRestaurants201Response update_restaurants_by_name(value, restaurants_update_input, select=select)



Update one restaurants record by name

### Example

* Api Key Authentication (ApiKey):
```python
import time
import os
import neurelo
from neurelo.models.create_one_restaurants201_response import CreateOneRestaurants201Response
from neurelo.models.restaurants_select_input import RestaurantsSelectInput
from neurelo.models.restaurants_update_input import RestaurantsUpdateInput
from neurelo.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = neurelo.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with neurelo.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = neurelo.RestaurantsApi(api_client)
    value = 'value_example' # str | 
    restaurants_update_input = neurelo.RestaurantsUpdateInput() # RestaurantsUpdateInput | 
    select = neurelo.RestaurantsSelectInput() # RestaurantsSelectInput |  (optional)

    try:
        api_response = api_instance.update_restaurants_by_name(value, restaurants_update_input, select=select)
        print("The response of RestaurantsApi->update_restaurants_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RestaurantsApi->update_restaurants_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **value** | **str**|  | 
 **restaurants_update_input** | [**RestaurantsUpdateInput**](RestaurantsUpdateInput.md)|  | 
 **select** | [**RestaurantsSelectInput**](.md)|  | [optional] 

### Return type

[**CreateOneRestaurants201Response**](CreateOneRestaurants201Response.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Record updated |  -  |
**400** | Invalid Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**503** | Timed Out |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

