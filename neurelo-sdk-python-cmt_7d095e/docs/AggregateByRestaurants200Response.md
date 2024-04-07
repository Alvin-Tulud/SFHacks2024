# AggregateByRestaurants200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AggregateRestaurants**](AggregateRestaurants.md) |  | 

## Example

```python
from neurelo.models.aggregate_by_restaurants200_response import AggregateByRestaurants200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateByRestaurants200Response from a JSON string
aggregate_by_restaurants200_response_instance = AggregateByRestaurants200Response.from_json(json)
# print the JSON string representation of the object
print AggregateByRestaurants200Response.to_json()

# convert the object into a dict
aggregate_by_restaurants200_response_dict = aggregate_by_restaurants200_response_instance.to_dict()
# create an instance of AggregateByRestaurants200Response from a dict
aggregate_by_restaurants200_response_form_dict = aggregate_by_restaurants200_response.from_dict(aggregate_by_restaurants200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


