# StringNullableListFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eq** | **List[str]** |  | [optional] 
**equals** | **List[str]** |  | [optional] 
**has** | **str** |  | [optional] 
**has_every** | **List[str]** |  | [optional] 
**has_some** | **List[str]** |  | [optional] 
**is_empty** | **bool** |  | [optional] 

## Example

```python
from neurelo.models.string_nullable_list_filter import StringNullableListFilter

# TODO update the JSON string below
json = "{}"
# create an instance of StringNullableListFilter from a JSON string
string_nullable_list_filter_instance = StringNullableListFilter.from_json(json)
# print the JSON string representation of the object
print StringNullableListFilter.to_json()

# convert the object into a dict
string_nullable_list_filter_dict = string_nullable_list_filter_instance.to_dict()
# create an instance of StringNullableListFilter from a dict
string_nullable_list_filter_form_dict = string_nullable_list_filter.from_dict(string_nullable_list_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


