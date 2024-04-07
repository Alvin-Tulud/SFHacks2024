# RestaurantsSelectInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**related** | **bool** |  | [optional] 
**scalars** | **bool** |  | [optional] 
**about** | **bool** |  | [optional] 
**name** | **bool** |  | [optional] 
**rating** | **bool** |  | [optional] 
**reviews** | **bool** |  | [optional] 

## Example

```python
from neurelo.models.restaurants_select_input import RestaurantsSelectInput

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsSelectInput from a JSON string
restaurants_select_input_instance = RestaurantsSelectInput.from_json(json)
# print the JSON string representation of the object
print RestaurantsSelectInput.to_json()

# convert the object into a dict
restaurants_select_input_dict = restaurants_select_input_instance.to_dict()
# create an instance of RestaurantsSelectInput from a dict
restaurants_select_input_form_dict = restaurants_select_input.from_dict(restaurants_select_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


