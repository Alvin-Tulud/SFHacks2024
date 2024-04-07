# FindRestaurants400Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ErrorResponse]**](ErrorResponse.md) |  | 

## Example

```python
from neurelo.models.find_restaurants400_response import FindRestaurants400Response

# TODO update the JSON string below
json = "{}"
# create an instance of FindRestaurants400Response from a JSON string
find_restaurants400_response_instance = FindRestaurants400Response.from_json(json)
# print the JSON string representation of the object
print FindRestaurants400Response.to_json()

# convert the object into a dict
find_restaurants400_response_dict = find_restaurants400_response_instance.to_dict()
# create an instance of FindRestaurants400Response from a dict
find_restaurants400_response_form_dict = find_restaurants400_response.from_dict(find_restaurants400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


