# RestaurantsOrderByWithRelationInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | [**SortOrder**](SortOrder.md) |  | [optional] 
**name** | [**SortOrder**](SortOrder.md) |  | [optional] 
**rating** | [**SortOrder**](SortOrder.md) |  | [optional] 
**reviews** | [**SortOrder**](SortOrder.md) |  | [optional] 

## Example

```python
from neurelo.models.restaurants_order_by_with_relation_input import RestaurantsOrderByWithRelationInput

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsOrderByWithRelationInput from a JSON string
restaurants_order_by_with_relation_input_instance = RestaurantsOrderByWithRelationInput.from_json(json)
# print the JSON string representation of the object
print RestaurantsOrderByWithRelationInput.to_json()

# convert the object into a dict
restaurants_order_by_with_relation_input_dict = restaurants_order_by_with_relation_input_instance.to_dict()
# create an instance of RestaurantsOrderByWithRelationInput from a dict
restaurants_order_by_with_relation_input_form_dict = restaurants_order_by_with_relation_input.from_dict(restaurants_order_by_with_relation_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


