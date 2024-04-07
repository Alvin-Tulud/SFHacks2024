# RestaurantsWhereInputAbout


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contains** | **str** |  | [optional] 
**ends_with** | **str** |  | [optional] 
**eq** | **str** |  | [optional] 
**equals** | **str** |  | [optional] 
**gt** | **str** |  | [optional] 
**gte** | **str** |  | [optional] 
**var_in** | **List[str]** |  | [optional] 
**lt** | **str** |  | [optional] 
**lte** | **str** |  | [optional] 
**mode** | [**QueryMode**](QueryMode.md) |  | [optional] 
**var_not** | [**NestedStringFilterNot**](NestedStringFilterNot.md) |  | [optional] 
**not_in** | **List[str]** |  | [optional] 
**search** | **str** |  | [optional] 
**starts_with** | **str** |  | [optional] 

## Example

```python
from neurelo.models.restaurants_where_input_about import RestaurantsWhereInputAbout

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsWhereInputAbout from a JSON string
restaurants_where_input_about_instance = RestaurantsWhereInputAbout.from_json(json)
# print the JSON string representation of the object
print RestaurantsWhereInputAbout.to_json()

# convert the object into a dict
restaurants_where_input_about_dict = restaurants_where_input_about_instance.to_dict()
# create an instance of RestaurantsWhereInputAbout from a dict
restaurants_where_input_about_form_dict = restaurants_where_input_about.from_dict(restaurants_where_input_about_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


