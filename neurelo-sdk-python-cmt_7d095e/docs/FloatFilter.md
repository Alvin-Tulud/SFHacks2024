# FloatFilter


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
from neurelo.models.float_filter import FloatFilter

# TODO update the JSON string below
json = "{}"
# create an instance of FloatFilter from a JSON string
float_filter_instance = FloatFilter.from_json(json)
# print the JSON string representation of the object
print FloatFilter.to_json()

# convert the object into a dict
float_filter_dict = float_filter_instance.to_dict()
# create an instance of FloatFilter from a dict
float_filter_form_dict = float_filter.from_dict(float_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


