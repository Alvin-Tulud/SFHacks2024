# NestedStringFilterNot


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
**var_not** | [**NestedStringFilterNot**](NestedStringFilterNot.md) |  | [optional] 
**not_in** | **List[str]** |  | [optional] 
**search** | **str** |  | [optional] 
**starts_with** | **str** |  | [optional] 

## Example

```python
from neurelo.models.nested_string_filter_not import NestedStringFilterNot

# TODO update the JSON string below
json = "{}"
# create an instance of NestedStringFilterNot from a JSON string
nested_string_filter_not_instance = NestedStringFilterNot.from_json(json)
# print the JSON string representation of the object
print NestedStringFilterNot.to_json()

# convert the object into a dict
nested_string_filter_not_dict = nested_string_filter_not_instance.to_dict()
# create an instance of NestedStringFilterNot from a dict
nested_string_filter_not_form_dict = nested_string_filter_not.from_dict(nested_string_filter_not_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


