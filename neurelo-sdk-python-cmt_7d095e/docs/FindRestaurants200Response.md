# FindRestaurants200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Restaurants]**](Restaurants.md) |  | 

## Example

```python
from neurelo.models.find_restaurants200_response import FindRestaurants200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FindRestaurants200Response from a JSON string
find_restaurants200_response_instance = FindRestaurants200Response.from_json(json)
# print the JSON string representation of the object
print FindRestaurants200Response.to_json()

# convert the object into a dict
find_restaurants200_response_dict = find_restaurants200_response_instance.to_dict()
# create an instance of FindRestaurants200Response from a dict
find_restaurants200_response_form_dict = find_restaurants200_response.from_dict(find_restaurants200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


