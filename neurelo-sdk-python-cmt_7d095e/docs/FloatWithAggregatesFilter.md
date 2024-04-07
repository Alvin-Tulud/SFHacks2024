# FloatWithAggregatesFilter


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
from neurelo.models.float_with_aggregates_filter import FloatWithAggregatesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of FloatWithAggregatesFilter from a JSON string
float_with_aggregates_filter_instance = FloatWithAggregatesFilter.from_json(json)
# print the JSON string representation of the object
print FloatWithAggregatesFilter.to_json()

# convert the object into a dict
float_with_aggregates_filter_dict = float_with_aggregates_filter_instance.to_dict()
# create an instance of FloatWithAggregatesFilter from a dict
float_with_aggregates_filter_form_dict = float_with_aggregates_filter.from_dict(float_with_aggregates_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


