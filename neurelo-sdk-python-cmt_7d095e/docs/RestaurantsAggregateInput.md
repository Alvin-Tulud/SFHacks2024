# RestaurantsAggregateInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | **List[str]** |  | [optional] 
**count** | **List[str]** |  | [optional] 
**max** | **List[str]** |  | [optional] 
**min** | **List[str]** |  | [optional] 
**sum** | **List[str]** |  | [optional] 

## Example

```python
from neurelo.models.restaurants_aggregate_input import RestaurantsAggregateInput

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsAggregateInput from a JSON string
restaurants_aggregate_input_instance = RestaurantsAggregateInput.from_json(json)
# print the JSON string representation of the object
print RestaurantsAggregateInput.to_json()

# convert the object into a dict
restaurants_aggregate_input_dict = restaurants_aggregate_input_instance.to_dict()
# create an instance of RestaurantsAggregateInput from a dict
restaurants_aggregate_input_form_dict = restaurants_aggregate_input.from_dict(restaurants_aggregate_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


