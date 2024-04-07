# RestaurantsUpdatereviewsInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**push** | [**RestaurantsUpdatereviewsInputPush**](RestaurantsUpdatereviewsInputPush.md) |  | [optional] 
**set** | **List[str]** |  | [optional] 

## Example

```python
from neurelo.models.restaurants_updatereviews_input import RestaurantsUpdatereviewsInput

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsUpdatereviewsInput from a JSON string
restaurants_updatereviews_input_instance = RestaurantsUpdatereviewsInput.from_json(json)
# print the JSON string representation of the object
print RestaurantsUpdatereviewsInput.to_json()

# convert the object into a dict
restaurants_updatereviews_input_dict = restaurants_updatereviews_input_instance.to_dict()
# create an instance of RestaurantsUpdatereviewsInput from a dict
restaurants_updatereviews_input_form_dict = restaurants_updatereviews_input.from_dict(restaurants_updatereviews_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


