# Restaurants


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**about** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**rating** | **float** |  | [optional] 
**reviews** | **List[str]** |  | [optional] 

## Example

```python
from neurelo.models.restaurants import Restaurants

# TODO update the JSON string below
json = "{}"
# create an instance of Restaurants from a JSON string
restaurants_instance = Restaurants.from_json(json)
# print the JSON string representation of the object
print Restaurants.to_json()

# convert the object into a dict
restaurants_dict = restaurants_instance.to_dict()
# create an instance of Restaurants from a dict
restaurants_form_dict = restaurants.from_dict(restaurants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


