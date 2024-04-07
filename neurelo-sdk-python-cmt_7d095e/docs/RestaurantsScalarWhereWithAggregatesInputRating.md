# RestaurantsScalarWhereWithAggregatesInputRating


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | [**NestedFloatFilter**](NestedFloatFilter.md) |  | [optional] 
**count** | [**NestedIntFilter**](NestedIntFilter.md) |  | [optional] 
**max** | [**NestedFloatFilter**](NestedFloatFilter.md) |  | [optional] 
**min** | [**NestedFloatFilter**](NestedFloatFilter.md) |  | [optional] 
**sum** | [**NestedFloatFilter**](NestedFloatFilter.md) |  | [optional] 
**eq** | **float** |  | [optional] 
**equals** | **float** |  | [optional] 
**gt** | **float** |  | [optional] 
**gte** | **float** |  | [optional] 
**var_in** | **List[float]** |  | [optional] 
**lt** | **float** |  | [optional] 
**lte** | **float** |  | [optional] 
**var_not** | [**FloatWithAggregatesFilterNot**](FloatWithAggregatesFilterNot.md) |  | [optional] 
**not_in** | **List[float]** |  | [optional] 

## Example

```python
from neurelo.models.restaurants_scalar_where_with_aggregates_input_rating import RestaurantsScalarWhereWithAggregatesInputRating

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsScalarWhereWithAggregatesInputRating from a JSON string
restaurants_scalar_where_with_aggregates_input_rating_instance = RestaurantsScalarWhereWithAggregatesInputRating.from_json(json)
# print the JSON string representation of the object
print RestaurantsScalarWhereWithAggregatesInputRating.to_json()

# convert the object into a dict
restaurants_scalar_where_with_aggregates_input_rating_dict = restaurants_scalar_where_with_aggregates_input_rating_instance.to_dict()
# create an instance of RestaurantsScalarWhereWithAggregatesInputRating from a dict
restaurants_scalar_where_with_aggregates_input_rating_form_dict = restaurants_scalar_where_with_aggregates_input_rating.from_dict(restaurants_scalar_where_with_aggregates_input_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


