# NestedFloatWithAggregatesFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | [**NestedFloatFilter**](NestedFloatFilter.md) |  | [optional] 
**count** | [**NestedIntFilter**](NestedIntFilter.md) |  | [optional] 
**max** | [**NestedFloatFilter**](NestedFloatFilter.md) |  | [optional] 
**min** | [**NestedFloatFilter**](NestedFloatFilter.md) |  | [optional] 
**sum** | [**NestedFloatFilter**](NestedFloatFilter.md) |  | [optional] 
**eq** | **float** |  | [optional] 
**equals** | **float** |  | [optional] 
**gt** | **float** |  | [optional] 
**gte** | **float** |  | [optional] 
**var_in** | **List[float]** |  | [optional] 
**lt** | **float** |  | [optional] 
**lte** | **float** |  | [optional] 
**var_not** | [**FloatWithAggregatesFilterNot**](FloatWithAggregatesFilterNot.md) |  | [optional] 
**not_in** | **List[float]** |  | [optional] 

## Example

```python
from neurelo.models.nested_float_with_aggregates_filter import NestedFloatWithAggregatesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NestedFloatWithAggregatesFilter from a JSON string
nested_float_with_aggregates_filter_instance = NestedFloatWithAggregatesFilter.from_json(json)
# print the JSON string representation of the object
print NestedFloatWithAggregatesFilter.to_json()

# convert the object into a dict
nested_float_with_aggregates_filter_dict = nested_float_with_aggregates_filter_instance.to_dict()
# create an instance of NestedFloatWithAggregatesFilter from a dict
nested_float_with_aggregates_filter_form_dict = nested_float_with_aggregates_filter.from_dict(nested_float_with_aggregates_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


