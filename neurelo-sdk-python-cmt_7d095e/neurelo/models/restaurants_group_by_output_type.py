# coding: utf-8

"""
    Neurelo API Spec

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from neurelo.models.restaurants_avg_aggregate_output_type import RestaurantsAvgAggregateOutputType
from neurelo.models.restaurants_count_aggregate_output_type import RestaurantsCountAggregateOutputType
from neurelo.models.restaurants_max_aggregate_output_type import RestaurantsMaxAggregateOutputType
from neurelo.models.restaurants_min_aggregate_output_type import RestaurantsMinAggregateOutputType
from neurelo.models.restaurants_sum_aggregate_output_type import RestaurantsSumAggregateOutputType

class RestaurantsGroupByOutputType(BaseModel):
    """
    RestaurantsGroupByOutputType
    """
    avg: Optional[RestaurantsAvgAggregateOutputType] = Field(None, alias="_avg")
    count: Optional[RestaurantsCountAggregateOutputType] = Field(None, alias="_count")
    max: Optional[RestaurantsMaxAggregateOutputType] = Field(None, alias="_max")
    min: Optional[RestaurantsMinAggregateOutputType] = Field(None, alias="_min")
    sum: Optional[RestaurantsSumAggregateOutputType] = Field(None, alias="_sum")
    about: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    rating: Optional[Union[StrictFloat, StrictInt]] = None
    reviews: Optional[conlist(StrictStr)] = None
    __properties = ["_avg", "_count", "_max", "_min", "_sum", "about", "name", "rating", "reviews"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> RestaurantsGroupByOutputType:
        """Create an instance of RestaurantsGroupByOutputType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of avg
        if self.avg:
            _dict['_avg'] = self.avg.to_dict()
        # override the default output from pydantic by calling `to_dict()` of count
        if self.count:
            _dict['_count'] = self.count.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max
        if self.max:
            _dict['_max'] = self.max.to_dict()
        # override the default output from pydantic by calling `to_dict()` of min
        if self.min:
            _dict['_min'] = self.min.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sum
        if self.sum:
            _dict['_sum'] = self.sum.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RestaurantsGroupByOutputType:
        """Create an instance of RestaurantsGroupByOutputType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RestaurantsGroupByOutputType.parse_obj(obj)

        _obj = RestaurantsGroupByOutputType.parse_obj({
            "avg": RestaurantsAvgAggregateOutputType.from_dict(obj.get("_avg")) if obj.get("_avg") is not None else None,
            "count": RestaurantsCountAggregateOutputType.from_dict(obj.get("_count")) if obj.get("_count") is not None else None,
            "max": RestaurantsMaxAggregateOutputType.from_dict(obj.get("_max")) if obj.get("_max") is not None else None,
            "min": RestaurantsMinAggregateOutputType.from_dict(obj.get("_min")) if obj.get("_min") is not None else None,
            "sum": RestaurantsSumAggregateOutputType.from_dict(obj.get("_sum")) if obj.get("_sum") is not None else None,
            "about": obj.get("about"),
            "name": obj.get("name"),
            "rating": obj.get("rating"),
            "reviews": obj.get("reviews")
        })
        return _obj

