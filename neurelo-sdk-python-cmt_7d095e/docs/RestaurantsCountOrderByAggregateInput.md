# RestaurantsCountOrderByAggregateInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | [**SortOrder**](SortOrder.md) |  | [optional] 
**name** | [**SortOrder**](SortOrder.md) |  | [optional] 
**rating** | [**SortOrder**](SortOrder.md) |  | [optional] 
**reviews** | [**SortOrder**](SortOrder.md) |  | [optional] 

## Example

```python
from neurelo.models.restaurants_count_order_by_aggregate_input import RestaurantsCountOrderByAggregateInput

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsCountOrderByAggregateInput from a JSON string
restaurants_count_order_by_aggregate_input_instance = RestaurantsCountOrderByAggregateInput.from_json(json)
# print the JSON string representation of the object
print RestaurantsCountOrderByAggregateInput.to_json()

# convert the object into a dict
restaurants_count_order_by_aggregate_input_dict = restaurants_count_order_by_aggregate_input_instance.to_dict()
# create an instance of RestaurantsCountOrderByAggregateInput from a dict
restaurants_count_order_by_aggregate_input_form_dict = restaurants_count_order_by_aggregate_input.from_dict(restaurants_count_order_by_aggregate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


