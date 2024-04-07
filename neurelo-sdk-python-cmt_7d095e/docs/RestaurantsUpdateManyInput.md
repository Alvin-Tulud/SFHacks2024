# RestaurantsUpdateManyInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | [**RestaurantsUpdateInputAbout**](RestaurantsUpdateInputAbout.md) |  | [optional] 
**name** | [**RestaurantsUpdateInputAbout**](RestaurantsUpdateInputAbout.md) |  | [optional] 
**rating** | [**RestaurantsUpdateInputRating**](RestaurantsUpdateInputRating.md) |  | [optional] 
**reviews** | [**RestaurantsUpdateInputReviews**](RestaurantsUpdateInputReviews.md) |  | [optional] 

## Example

```python
from neurelo.models.restaurants_update_many_input import RestaurantsUpdateManyInput

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsUpdateManyInput from a JSON string
restaurants_update_many_input_instance = RestaurantsUpdateManyInput.from_json(json)
# print the JSON string representation of the object
print RestaurantsUpdateManyInput.to_json()

# convert the object into a dict
restaurants_update_many_input_dict = restaurants_update_many_input_instance.to_dict()
# create an instance of RestaurantsUpdateManyInput from a dict
restaurants_update_many_input_form_dict = restaurants_update_many_input.from_dict(restaurants_update_many_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


