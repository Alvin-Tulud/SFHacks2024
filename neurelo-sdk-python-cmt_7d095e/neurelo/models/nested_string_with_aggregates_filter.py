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
from pydantic import BaseModel, Field, StrictStr, conlist
from neurelo.models.nested_int_filter import NestedIntFilter
from neurelo.models.nested_string_filter import NestedStringFilter

class NestedStringWithAggregatesFilter(BaseModel):
    """
    NestedStringWithAggregatesFilter
    """
    count: Optional[NestedIntFilter] = Field(None, alias="_count")
    max: Optional[NestedStringFilter] = Field(None, alias="_max")
    min: Optional[NestedStringFilter] = Field(None, alias="_min")
    contains: Optional[StrictStr] = None
    ends_with: Optional[StrictStr] = Field(None, alias="endsWith")
    eq: Optional[StrictStr] = None
    equals: Optional[StrictStr] = None
    gt: Optional[StrictStr] = None
    gte: Optional[StrictStr] = None
    var_in: Optional[conlist(StrictStr)] = Field(None, alias="in")
    lt: Optional[StrictStr] = None
    lte: Optional[StrictStr] = None
    var_not: Optional[NestedStringWithAggregatesFilterNot] = Field(None, alias="not")
    not_in: Optional[conlist(StrictStr)] = Field(None, alias="notIn")
    search: Optional[StrictStr] = None
    starts_with: Optional[StrictStr] = Field(None, alias="startsWith")
    __properties = ["_count", "_max", "_min", "contains", "endsWith", "eq", "equals", "gt", "gte", "in", "lt", "lte", "not", "notIn", "search", "startsWith"]

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
    def from_json(cls, json_str: str) -> NestedStringWithAggregatesFilter:
        """Create an instance of NestedStringWithAggregatesFilter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of count
        if self.count:
            _dict['_count'] = self.count.to_dict()
        # override the default output from pydantic by calling `to_dict()` of max
        if self.max:
            _dict['_max'] = self.max.to_dict()
        # override the default output from pydantic by calling `to_dict()` of min
        if self.min:
            _dict['_min'] = self.min.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_not
        if self.var_not:
            _dict['not'] = self.var_not.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NestedStringWithAggregatesFilter:
        """Create an instance of NestedStringWithAggregatesFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NestedStringWithAggregatesFilter.parse_obj(obj)

        _obj = NestedStringWithAggregatesFilter.parse_obj({
            "count": NestedIntFilter.from_dict(obj.get("_count")) if obj.get("_count") is not None else None,
            "max": NestedStringFilter.from_dict(obj.get("_max")) if obj.get("_max") is not None else None,
            "min": NestedStringFilter.from_dict(obj.get("_min")) if obj.get("_min") is not None else None,
            "contains": obj.get("contains"),
            "ends_with": obj.get("endsWith"),
            "eq": obj.get("eq"),
            "equals": obj.get("equals"),
            "gt": obj.get("gt"),
            "gte": obj.get("gte"),
            "var_in": obj.get("in"),
            "lt": obj.get("lt"),
            "lte": obj.get("lte"),
            "var_not": NestedStringWithAggregatesFilterNot.from_dict(obj.get("not")) if obj.get("not") is not None else None,
            "not_in": obj.get("notIn"),
            "search": obj.get("search"),
            "starts_with": obj.get("startsWith")
        })
        return _obj

from neurelo.models.nested_string_with_aggregates_filter_not import NestedStringWithAggregatesFilterNot
NestedStringWithAggregatesFilter.update_forward_refs()

