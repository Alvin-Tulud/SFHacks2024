# NestedStringWithAggregatesFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | [**NestedIntFilter**](NestedIntFilter.md) |  | [optional] 
**max** | [**NestedStringFilter**](NestedStringFilter.md) |  | [optional] 
**min** | [**NestedStringFilter**](NestedStringFilter.md) |  | [optional] 
**contains** | **str** |  | [optional] 
**ends_with** | **str** |  | [optional] 
**eq** | **str** |  | [optional] 
**equals** | **str** |  | [optional] 
**gt** | **str** |  | [optional] 
**gte** | **str** |  | [optional] 
**var_in** | **List[str]** |  | [optional] 
**lt** | **str** |  | [optional] 
**lte** | **str** |  | [optional] 
**var_not** | [**NestedStringWithAggregatesFilterNot**](NestedStringWithAggregatesFilterNot.md) |  | [optional] 
**not_in** | **List[str]** |  | [optional] 
**search** | **str** |  | [optional] 
**starts_with** | **str** |  | [optional] 

## Example

```python
from neurelo.models.nested_string_with_aggregates_filter import NestedStringWithAggregatesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NestedStringWithAggregatesFilter from a JSON string
nested_string_with_aggregates_filter_instance = NestedStringWithAggregatesFilter.from_json(json)
# print the JSON string representation of the object
print NestedStringWithAggregatesFilter.to_json()

# convert the object into a dict
nested_string_with_aggregates_filter_dict = nested_string_with_aggregates_filter_instance.to_dict()
# create an instance of NestedStringWithAggregatesFilter from a dict
nested_string_with_aggregates_filter_form_dict = nested_string_with_aggregates_filter.from_dict(nested_string_with_aggregates_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


