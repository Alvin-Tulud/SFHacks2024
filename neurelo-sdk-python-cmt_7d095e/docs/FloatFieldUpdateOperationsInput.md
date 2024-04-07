# FloatFieldUpdateOperationsInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decrement** | **float** |  | [optional] 
**divide** | **float** |  | [optional] 
**increment** | **float** |  | [optional] 
**multiply** | **float** |  | [optional] 
**set** | **float** |  | [optional] 

## Example

```python
from neurelo.models.float_field_update_operations_input import FloatFieldUpdateOperationsInput

# TODO update the JSON string below
json = "{}"
# create an instance of FloatFieldUpdateOperationsInput from a JSON string
float_field_update_operations_input_instance = FloatFieldUpdateOperationsInput.from_json(json)
# print the JSON string representation of the object
print FloatFieldUpdateOperationsInput.to_json()

# convert the object into a dict
float_field_update_operations_input_dict = float_field_update_operations_input_instance.to_dict()
# create an instance of FloatFieldUpdateOperationsInput from a dict
float_field_update_operations_input_form_dict = float_field_update_operations_input.from_dict(float_field_update_operations_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


