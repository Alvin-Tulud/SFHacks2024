# RestaurantsCountAggregateOutputType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **int** |  | [optional] 
**about** | **int** |  | [optional] 
**name** | **int** |  | [optional] 
**rating** | **int** |  | [optional] 
**reviews** | **int** |  | [optional] 

## Example

```python
from neurelo.models.restaurants_count_aggregate_output_type import RestaurantsCountAggregateOutputType

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsCountAggregateOutputType from a JSON string
restaurants_count_aggregate_output_type_instance = RestaurantsCountAggregateOutputType.from_json(json)
# print the JSON string representation of the object
print RestaurantsCountAggregateOutputType.to_json()

# convert the object into a dict
restaurants_count_aggregate_output_type_dict = restaurants_count_aggregate_output_type_instance.to_dict()
# create an instance of RestaurantsCountAggregateOutputType from a dict
restaurants_count_aggregate_output_type_form_dict = restaurants_count_aggregate_output_type.from_dict(restaurants_count_aggregate_output_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


