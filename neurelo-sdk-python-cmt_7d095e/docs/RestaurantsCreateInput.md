# RestaurantsCreateInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | **str** |  | 
**name** | **str** |  | 
**rating** | **float** |  | 
**reviews** | [**RestaurantsCreateInputReviews**](RestaurantsCreateInputReviews.md) |  | [optional] 

## Example

```python
from neurelo.models.restaurants_create_input import RestaurantsCreateInput

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsCreateInput from a JSON string
restaurants_create_input_instance = RestaurantsCreateInput.from_json(json)
# print the JSON string representation of the object
print RestaurantsCreateInput.to_json()

# convert the object into a dict
restaurants_create_input_dict = restaurants_create_input_instance.to_dict()
# create an instance of RestaurantsCreateInput from a dict
restaurants_create_input_form_dict = restaurants_create_input.from_dict(restaurants_create_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


