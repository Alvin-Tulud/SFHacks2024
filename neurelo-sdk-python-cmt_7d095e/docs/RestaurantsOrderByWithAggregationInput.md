# RestaurantsOrderByWithAggregationInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | [**RestaurantsAvgOrderByAggregateInput**](RestaurantsAvgOrderByAggregateInput.md) |  | [optional] 
**count** | [**RestaurantsCountOrderByAggregateInput**](RestaurantsCountOrderByAggregateInput.md) |  | [optional] 
**max** | [**RestaurantsMaxOrderByAggregateInput**](RestaurantsMaxOrderByAggregateInput.md) |  | [optional] 
**min** | [**RestaurantsMinOrderByAggregateInput**](RestaurantsMinOrderByAggregateInput.md) |  | [optional] 
**sum** | [**RestaurantsSumOrderByAggregateInput**](RestaurantsSumOrderByAggregateInput.md) |  | [optional] 
**about** | [**SortOrder**](SortOrder.md) |  | [optional] 
**name** | [**SortOrder**](SortOrder.md) |  | [optional] 
**rating** | [**SortOrder**](SortOrder.md) |  | [optional] 
**reviews** | [**SortOrder**](SortOrder.md) |  | [optional] 

## Example

```python
from neurelo.models.restaurants_order_by_with_aggregation_input import RestaurantsOrderByWithAggregationInput

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsOrderByWithAggregationInput from a JSON string
restaurants_order_by_with_aggregation_input_instance = RestaurantsOrderByWithAggregationInput.from_json(json)
# print the JSON string representation of the object
print RestaurantsOrderByWithAggregationInput.to_json()

# convert the object into a dict
restaurants_order_by_with_aggregation_input_dict = restaurants_order_by_with_aggregation_input_instance.to_dict()
# create an instance of RestaurantsOrderByWithAggregationInput from a dict
restaurants_order_by_with_aggregation_input_form_dict = restaurants_order_by_with_aggregation_input.from_dict(restaurants_order_by_with_aggregation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


