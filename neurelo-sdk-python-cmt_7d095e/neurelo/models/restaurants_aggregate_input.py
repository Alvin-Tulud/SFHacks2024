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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator

class RestaurantsAggregateInput(BaseModel):
    """
    RestaurantsAggregateInput
    """
    avg: Optional[conlist(StrictStr, min_items=1)] = Field(None, alias="_avg")
    count: Optional[conlist(StrictStr, min_items=1)] = Field(None, alias="_count")
    max: Optional[conlist(StrictStr, min_items=1)] = Field(None, alias="_max")
    min: Optional[conlist(StrictStr, min_items=1)] = Field(None, alias="_min")
    sum: Optional[conlist(StrictStr, min_items=1)] = Field(None, alias="_sum")
    __properties = ["_avg", "_count", "_max", "_min", "_sum"]

    @validator('avg')
    def avg_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('rating'):
                raise ValueError("each list item must be one of ('rating')")
        return value

    @validator('count')
    def count_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('_all', 'about', 'name', 'rating', 'reviews'):
                raise ValueError("each list item must be one of ('_all', 'about', 'name', 'rating', 'reviews')")
        return value

    @validator('max')
    def max_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('about', 'name', 'rating', 'reviews'):
                raise ValueError("each list item must be one of ('about', 'name', 'rating', 'reviews')")
        return value

    @validator('min')
    def min_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('about', 'name', 'rating', 'reviews'):
                raise ValueError("each list item must be one of ('about', 'name', 'rating', 'reviews')")
        return value

    @validator('sum')
    def sum_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ('rating'):
                raise ValueError("each list item must be one of ('rating')")
        return value

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
    def from_json(cls, json_str: str) -> RestaurantsAggregateInput:
        """Create an instance of RestaurantsAggregateInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RestaurantsAggregateInput:
        """Create an instance of RestaurantsAggregateInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RestaurantsAggregateInput.parse_obj(obj)

        _obj = RestaurantsAggregateInput.parse_obj({
            "avg": obj.get("_avg"),
            "count": obj.get("_count"),
            "max": obj.get("_max"),
            "min": obj.get("_min"),
            "sum": obj.get("_sum")
        })
        return _obj


