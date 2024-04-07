# RestaurantsWhereInputRating


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **float** |  | [optional] 
**equals** | **float** |  | [optional] 
**gt** | **float** |  | [optional] 
**gte** | **float** |  | [optional] 
**var_in** | **List[float]** |  | [optional] 
**lt** | **float** |  | [optional] 
**lte** | **float** |  | [optional] 
**var_not** | [**FloatFilterNot**](FloatFilterNot.md) |  | [optional] 
**not_in** | **List[float]** |  | [optional] 

## Example

```python
from neurelo.models.restaurants_where_input_rating import RestaurantsWhereInputRating

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsWhereInputRating from a JSON string
restaurants_where_input_rating_instance = RestaurantsWhereInputRating.from_json(json)
# print the JSON string representation of the object
print RestaurantsWhereInputRating.to_json()

# convert the object into a dict
restaurants_where_input_rating_dict = restaurants_where_input_rating_instance.to_dict()
# create an instance of RestaurantsWhereInputRating from a dict
restaurants_where_input_rating_form_dict = restaurants_where_input_rating.from_dict(restaurants_where_input_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


