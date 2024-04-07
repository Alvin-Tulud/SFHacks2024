# RestaurantsUpdateInputRating


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decrement** | **float** |  | [optional] 
**divide** | **float** |  | [optional] 
**increment** | **float** |  | [optional] 
**multiply** | **float** |  | [optional] 
**set** | **float** |  | [optional] 

## Example

```python
from neurelo.models.restaurants_update_input_rating import RestaurantsUpdateInputRating

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsUpdateInputRating from a JSON string
restaurants_update_input_rating_instance = RestaurantsUpdateInputRating.from_json(json)
# print the JSON string representation of the object
print RestaurantsUpdateInputRating.to_json()

# convert the object into a dict
restaurants_update_input_rating_dict = restaurants_update_input_rating_instance.to_dict()
# create an instance of RestaurantsUpdateInputRating from a dict
restaurants_update_input_rating_form_dict = restaurants_update_input_rating.from_dict(restaurants_update_input_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


