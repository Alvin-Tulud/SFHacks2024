# RestaurantsGroupByInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | **List[str]** |  | [optional] 
**count** | **List[str]** |  | [optional] 
**max** | **List[str]** |  | [optional] 
**min** | **List[str]** |  | [optional] 
**sum** | **List[str]** |  | [optional] 
**about** | **bool** |  | [optional] 
**name** | **bool** |  | [optional] 
**rating** | **bool** |  | [optional] 
**reviews** | **bool** |  | [optional] 

## Example

```python
from neurelo.models.restaurants_group_by_input import RestaurantsGroupByInput

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsGroupByInput from a JSON string
restaurants_group_by_input_instance = RestaurantsGroupByInput.from_json(json)
# print the JSON string representation of the object
print RestaurantsGroupByInput.to_json()

# convert the object into a dict
restaurants_group_by_input_dict = restaurants_group_by_input_instance.to_dict()
# create an instance of RestaurantsGroupByInput from a dict
restaurants_group_by_input_form_dict = restaurants_group_by_input.from_dict(restaurants_group_by_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


