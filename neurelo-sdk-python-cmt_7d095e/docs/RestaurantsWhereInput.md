# RestaurantsWhereInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_and** | [**RestaurantsWhereInputAND**](RestaurantsWhereInputAND.md) |  | [optional] 
**var_not** | [**RestaurantsWhereInputAND**](RestaurantsWhereInputAND.md) |  | [optional] 
**var_or** | [**List[RestaurantsWhereInput]**](RestaurantsWhereInput.md) |  | [optional] 
**about** | [**RestaurantsWhereInputAbout**](RestaurantsWhereInputAbout.md) |  | [optional] 
**name** | [**RestaurantsWhereInputAbout**](RestaurantsWhereInputAbout.md) |  | [optional] 
**rating** | [**RestaurantsWhereInputRating**](RestaurantsWhereInputRating.md) |  | [optional] 
**reviews** | [**StringNullableListFilter**](StringNullableListFilter.md) |  | [optional] 

## Example

```python
from neurelo.models.restaurants_where_input import RestaurantsWhereInput

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsWhereInput from a JSON string
restaurants_where_input_instance = RestaurantsWhereInput.from_json(json)
# print the JSON string representation of the object
print RestaurantsWhereInput.to_json()

# convert the object into a dict
restaurants_where_input_dict = restaurants_where_input_instance.to_dict()
# create an instance of RestaurantsWhereInput from a dict
restaurants_where_input_form_dict = restaurants_where_input.from_dict(restaurants_where_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


