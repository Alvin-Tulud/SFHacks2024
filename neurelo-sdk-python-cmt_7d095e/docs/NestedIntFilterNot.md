# NestedIntFilterNot


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
from neurelo.models.nested_int_filter_not import NestedIntFilterNot

# TODO update the JSON string below
json = "{}"
# create an instance of NestedIntFilterNot from a JSON string
nested_int_filter_not_instance = NestedIntFilterNot.from_json(json)
# print the JSON string representation of the object
print NestedIntFilterNot.to_json()

# convert the object into a dict
nested_int_filter_not_dict = nested_int_filter_not_instance.to_dict()
# create an instance of NestedIntFilterNot from a dict
nested_int_filter_not_form_dict = nested_int_filter_not.from_dict(nested_int_filter_not_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


