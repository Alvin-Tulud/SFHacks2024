# StringFilter


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
from neurelo.models.string_filter import StringFilter

# TODO update the JSON string below
json = "{}"
# create an instance of StringFilter from a JSON string
string_filter_instance = StringFilter.from_json(json)
# print the JSON string representation of the object
print StringFilter.to_json()

# convert the object into a dict
string_filter_dict = string_filter_instance.to_dict()
# create an instance of StringFilter from a dict
string_filter_form_dict = string_filter.from_dict(string_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


