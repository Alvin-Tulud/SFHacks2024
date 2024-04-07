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


from typing import Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr

class RestaurantsMinAggregateOutputType(BaseModel):
    """
    RestaurantsMinAggregateOutputType
    """
    about: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    rating: Optional[Union[StrictFloat, StrictInt]] = None
    __properties = ["about", "name", "rating"]

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
    def from_json(cls, json_str: str) -> RestaurantsMinAggregateOutputType:
        """Create an instance of RestaurantsMinAggregateOutputType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if about (nullable) is None
        # and __fields_set__ contains the field
        if self.about is None and "about" in self.__fields_set__:
            _dict['about'] = None

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if rating (nullable) is None
        # and __fields_set__ contains the field
        if self.rating is None and "rating" in self.__fields_set__:
            _dict['rating'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RestaurantsMinAggregateOutputType:
        """Create an instance of RestaurantsMinAggregateOutputType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RestaurantsMinAggregateOutputType.parse_obj(obj)

        _obj = RestaurantsMinAggregateOutputType.parse_obj({
            "about": obj.get("about"),
            "name": obj.get("name"),
            "rating": obj.get("rating")
        })
        return _obj


