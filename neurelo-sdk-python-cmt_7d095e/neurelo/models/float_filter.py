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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, conlist
from neurelo.models.float_filter_not import FloatFilterNot

class FloatFilter(BaseModel):
    """
    FloatFilter
    """
    eq: Optional[Union[StrictFloat, StrictInt]] = None
    equals: Optional[Union[StrictFloat, StrictInt]] = None
    gt: Optional[Union[StrictFloat, StrictInt]] = None
    gte: Optional[Union[StrictFloat, StrictInt]] = None
    var_in: Optional[conlist(Union[StrictFloat, StrictInt])] = Field(None, alias="in")
    lt: Optional[Union[StrictFloat, StrictInt]] = None
    lte: Optional[Union[StrictFloat, StrictInt]] = None
    var_not: Optional[FloatFilterNot] = Field(None, alias="not")
    not_in: Optional[conlist(Union[StrictFloat, StrictInt])] = Field(None, alias="notIn")
    __properties = ["eq", "equals", "gt", "gte", "in", "lt", "lte", "not", "notIn"]

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
    def from_json(cls, json_str: str) -> FloatFilter:
        """Create an instance of FloatFilter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_not
        if self.var_not:
            _dict['not'] = self.var_not.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FloatFilter:
        """Create an instance of FloatFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FloatFilter.parse_obj(obj)

        _obj = FloatFilter.parse_obj({
            "eq": obj.get("eq"),
            "equals": obj.get("equals"),
            "gt": obj.get("gt"),
            "gte": obj.get("gte"),
            "var_in": obj.get("in"),
            "lt": obj.get("lt"),
            "lte": obj.get("lte"),
            "var_not": FloatFilterNot.from_dict(obj.get("not")) if obj.get("not") is not None else None,
            "not_in": obj.get("notIn")
        })
        return _obj


