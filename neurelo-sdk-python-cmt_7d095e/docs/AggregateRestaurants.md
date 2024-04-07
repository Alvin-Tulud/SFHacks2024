# AggregateRestaurants


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | [**RestaurantsAvgAggregateOutputType**](RestaurantsAvgAggregateOutputType.md) |  | [optional] 
**count** | [**RestaurantsCountAggregateOutputType**](RestaurantsCountAggregateOutputType.md) |  | [optional] 
**max** | [**RestaurantsMaxAggregateOutputType**](RestaurantsMaxAggregateOutputType.md) |  | [optional] 
**min** | [**RestaurantsMinAggregateOutputType**](RestaurantsMinAggregateOutputType.md) |  | [optional] 
**sum** | [**RestaurantsSumAggregateOutputType**](RestaurantsSumAggregateOutputType.md) |  | [optional] 

## Example

```python
from neurelo.models.aggregate_restaurants import AggregateRestaurants

# TODO update the JSON string below
json = "{}"
# create an instance of AggregateRestaurants from a JSON string
aggregate_restaurants_instance = AggregateRestaurants.from_json(json)
# print the JSON string representation of the object
print AggregateRestaurants.to_json()

# convert the object into a dict
aggregate_restaurants_dict = aggregate_restaurants_instance.to_dict()
# create an instance of AggregateRestaurants from a dict
aggregate_restaurants_form_dict = aggregate_restaurants.from_dict(aggregate_restaurants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


