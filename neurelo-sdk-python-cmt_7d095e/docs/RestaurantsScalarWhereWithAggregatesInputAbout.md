# RestaurantsScalarWhereWithAggregatesInputAbout


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | [**NestedIntFilter**](NestedIntFilter.md) |  | [optional] 
**max** | [**NestedStringFilter**](NestedStringFilter.md) |  | [optional] 
**min** | [**NestedStringFilter**](NestedStringFilter.md) |  | [optional] 
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
**var_not** | [**NestedStringWithAggregatesFilterNot**](NestedStringWithAggregatesFilterNot.md) |  | [optional] 
**not_in** | **List[str]** |  | [optional] 
**search** | **str** |  | [optional] 
**starts_with** | **str** |  | [optional] 

## Example

```python
from neurelo.models.restaurants_scalar_where_with_aggregates_input_about import RestaurantsScalarWhereWithAggregatesInputAbout

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsScalarWhereWithAggregatesInputAbout from a JSON string
restaurants_scalar_where_with_aggregates_input_about_instance = RestaurantsScalarWhereWithAggregatesInputAbout.from_json(json)
# print the JSON string representation of the object
print RestaurantsScalarWhereWithAggregatesInputAbout.to_json()

# convert the object into a dict
restaurants_scalar_where_with_aggregates_input_about_dict = restaurants_scalar_where_with_aggregates_input_about_instance.to_dict()
# create an instance of RestaurantsScalarWhereWithAggregatesInputAbout from a dict
restaurants_scalar_where_with_aggregates_input_about_form_dict = restaurants_scalar_where_with_aggregates_input_about.from_dict(restaurants_scalar_where_with_aggregates_input_about_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


