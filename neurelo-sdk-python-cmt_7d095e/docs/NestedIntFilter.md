# NestedIntFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **int** |  | [optional] 
**equals** | **int** |  | [optional] 
**gt** | **int** |  | [optional] 
**gte** | **int** |  | [optional] 
**var_in** | **List[int]** |  | [optional] 
**lt** | **int** |  | [optional] 
**lte** | **int** |  | [optional] 
**var_not** | [**NestedIntFilterNot**](NestedIntFilterNot.md) |  | [optional] 
**not_in** | **List[int]** |  | [optional] 

## Example

```python
from neurelo.models.nested_int_filter import NestedIntFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NestedIntFilter from a JSON string
nested_int_filter_instance = NestedIntFilter.from_json(json)
# print the JSON string representation of the object
print NestedIntFilter.to_json()

# convert the object into a dict
nested_int_filter_dict = nested_int_filter_instance.to_dict()
# create an instance of NestedIntFilter from a dict
nested_int_filter_form_dict = nested_int_filter.from_dict(nested_int_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


