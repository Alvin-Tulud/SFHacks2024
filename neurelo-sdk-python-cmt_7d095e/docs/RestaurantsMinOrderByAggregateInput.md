# RestaurantsMinOrderByAggregateInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | [**SortOrder**](SortOrder.md) |  | [optional] 
**name** | [**SortOrder**](SortOrder.md) |  | [optional] 
**rating** | [**SortOrder**](SortOrder.md) |  | [optional] 

## Example

```python
from neurelo.models.restaurants_min_order_by_aggregate_input import RestaurantsMinOrderByAggregateInput

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsMinOrderByAggregateInput from a JSON string
restaurants_min_order_by_aggregate_input_instance = RestaurantsMinOrderByAggregateInput.from_json(json)
# print the JSON string representation of the object
print RestaurantsMinOrderByAggregateInput.to_json()

# convert the object into a dict
restaurants_min_order_by_aggregate_input_dict = restaurants_min_order_by_aggregate_input_instance.to_dict()
# create an instance of RestaurantsMinOrderByAggregateInput from a dict
restaurants_min_order_by_aggregate_input_form_dict = restaurants_min_order_by_aggregate_input.from_dict(restaurants_min_order_by_aggregate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


