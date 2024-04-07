# coding: utf-8

"""
    Neurelo API Spec

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class RestaurantsScalarFieldEnum(str, Enum):
    """
    RestaurantsScalarFieldEnum
    """

    """
    allowed enum values
    """
    ABOUT = 'about'
    NAME = 'name'
    RATING = 'rating'
    REVIEWS = 'reviews'

    @classmethod
    def from_json(cls, json_str: str) -> RestaurantsScalarFieldEnum:
        """Create an instance of RestaurantsScalarFieldEnum from a JSON string"""
        return RestaurantsScalarFieldEnum(json.loads(json_str))

