# RestaurantsScalarWhereWithAggregatesInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**RestaurantsScalarWhereWithAggregatesInputAND**](RestaurantsScalarWhereWithAggregatesInputAND.md) |  | [optional] 
**var_not** | [**RestaurantsScalarWhereWithAggregatesInputAND**](RestaurantsScalarWhereWithAggregatesInputAND.md) |  | [optional] 
**var_or** | [**List[RestaurantsScalarWhereWithAggregatesInput]**](RestaurantsScalarWhereWithAggregatesInput.md) |  | [optional] 
**about** | [**RestaurantsScalarWhereWithAggregatesInputAbout**](RestaurantsScalarWhereWithAggregatesInputAbout.md) |  | [optional] 
**name** | [**RestaurantsScalarWhereWithAggregatesInputAbout**](RestaurantsScalarWhereWithAggregatesInputAbout.md) |  | [optional] 
**rating** | [**RestaurantsScalarWhereWithAggregatesInputRating**](RestaurantsScalarWhereWithAggregatesInputRating.md) |  | [optional] 
**reviews** | [**StringNullableListFilter**](StringNullableListFilter.md) |  | [optional] 

## Example

```python
from neurelo.models.restaurants_scalar_where_with_aggregates_input import RestaurantsScalarWhereWithAggregatesInput

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsScalarWhereWithAggregatesInput from a JSON string
restaurants_scalar_where_with_aggregates_input_instance = RestaurantsScalarWhereWithAggregatesInput.from_json(json)
# print the JSON string representation of the object
print RestaurantsScalarWhereWithAggregatesInput.to_json()

# convert the object into a dict
restaurants_scalar_where_with_aggregates_input_dict = restaurants_scalar_where_with_aggregates_input_instance.to_dict()
# create an instance of RestaurantsScalarWhereWithAggregatesInput from a dict
restaurants_scalar_where_with_aggregates_input_form_dict = restaurants_scalar_where_with_aggregates_input.from_dict(restaurants_scalar_where_with_aggregates_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


