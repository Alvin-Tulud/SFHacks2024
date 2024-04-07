# RestaurantsUpdateInputReviews


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**push** | [**RestaurantsUpdatereviewsInputPush**](RestaurantsUpdatereviewsInputPush.md) |  | [optional] 
**set** | **List[str]** |  | [optional] 

## Example

```python
from neurelo.models.restaurants_update_input_reviews import RestaurantsUpdateInputReviews

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsUpdateInputReviews from a JSON string
restaurants_update_input_reviews_instance = RestaurantsUpdateInputReviews.from_json(json)
# print the JSON string representation of the object
print RestaurantsUpdateInputReviews.to_json()

# convert the object into a dict
restaurants_update_input_reviews_dict = restaurants_update_input_reviews_instance.to_dict()
# create an instance of RestaurantsUpdateInputReviews from a dict
restaurants_update_input_reviews_form_dict = restaurants_update_input_reviews.from_dict(restaurants_update_input_reviews_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


