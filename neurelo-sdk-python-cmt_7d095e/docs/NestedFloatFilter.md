# NestedFloatFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **float** |  | [optional] 
**equals** | **float** |  | [optional] 
**gt** | **float** |  | [optional] 
**gte** | **float** |  | [optional] 
**var_in** | **List[float]** |  | [optional] 
**lt** | **float** |  | [optional] 
**lte** | **float** |  | [optional] 
**var_not** | [**FloatFilterNot**](FloatFilterNot.md) |  | [optional] 
**not_in** | **List[float]** |  | [optional] 

## Example

```python
from neurelo.models.nested_float_filter import NestedFloatFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NestedFloatFilter from a JSON string
nested_float_filter_instance = NestedFloatFilter.from_json(json)
# print the JSON string representation of the object
print NestedFloatFilter.to_json()

# convert the object into a dict
nested_float_filter_dict = nested_float_filter_instance.to_dict()
# create an instance of NestedFloatFilter from a dict
nested_float_filter_form_dict = nested_float_filter.from_dict(nested_float_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


