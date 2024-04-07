# RestaurantsGroupByOutputType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | [**RestaurantsAvgAggregateOutputType**](RestaurantsAvgAggregateOutputType.md) |  | [optional] 
**count** | [**RestaurantsCountAggregateOutputType**](RestaurantsCountAggregateOutputType.md) |  | [optional] 
**max** | [**RestaurantsMaxAggregateOutputType**](RestaurantsMaxAggregateOutputType.md) |  | [optional] 
**min** | [**RestaurantsMinAggregateOutputType**](RestaurantsMinAggregateOutputType.md) |  | [optional] 
**sum** | [**RestaurantsSumAggregateOutputType**](RestaurantsSumAggregateOutputType.md) |  | [optional] 
**about** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**rating** | **float** |  | [optional] 
**reviews** | **List[str]** |  | [optional] 

## Example

```python
from neurelo.models.restaurants_group_by_output_type import RestaurantsGroupByOutputType

# TODO update the JSON string below
json = "{}"
# create an instance of RestaurantsGroupByOutputType from a JSON string
restaurants_group_by_output_type_instance = RestaurantsGroupByOutputType.from_json(json)
# print the JSON string representation of the object
print RestaurantsGroupByOutputType.to_json()

# convert the object into a dict
restaurants_group_by_output_type_dict = restaurants_group_by_output_type_instance.to_dict()
# create an instance of RestaurantsGroupByOutputType from a dict
restaurants_group_by_output_type_form_dict = restaurants_group_by_output_type.from_dict(restaurants_group_by_output_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


