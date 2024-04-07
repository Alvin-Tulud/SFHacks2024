# GroupByRestaurants200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RestaurantsGroupByOutputType]**](RestaurantsGroupByOutputType.md) |  | 

## Example

```python
from neurelo.models.group_by_restaurants200_response import GroupByRestaurants200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GroupByRestaurants200Response from a JSON string
group_by_restaurants200_response_instance = GroupByRestaurants200Response.from_json(json)
# print the JSON string representation of the object
print GroupByRestaurants200Response.to_json()

# convert the object into a dict
group_by_restaurants200_response_dict = group_by_restaurants200_response_instance.to_dict()
# create an instance of GroupByRestaurants200Response from a dict
group_by_restaurants200_response_form_dict = group_by_restaurants200_response.from_dict(group_by_restaurants200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


