# coding: utf-8

"""
    Neurelo API Spec

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from neurelo.models.float_with_aggregates_filter import FloatWithAggregatesFilter  # noqa: E501

class TestFloatWithAggregatesFilter(unittest.TestCase):
    """FloatWithAggregatesFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FloatWithAggregatesFilter:
        """Test FloatWithAggregatesFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FloatWithAggregatesFilter`
        """
        model = FloatWithAggregatesFilter()  # noqa: E501
        if include_optional:
            return FloatWithAggregatesFilter(
                avg = neurelo.models.nested_float_filter.NestedFloatFilter(
                    eq = 1.337, 
                    equals = 1.337, 
                    gt = 1.337, 
                    gte = 1.337, 
                    in = [
                        1.337
                        ], 
                    lt = 1.337, 
                    lte = 1.337, 
                    not = null, 
                    not_in = [
                        1.337
                        ], ),
                count = neurelo.models.nested_int_filter.NestedIntFilter(
                    eq = 56, 
                    equals = 56, 
                    gt = 56, 
                    gte = 56, 
                    in = [
                        56
                        ], 
                    lt = 56, 
                    lte = 56, 
                    not = null, 
                    not_in = [
                        56
                        ], ),
                max = neurelo.models.nested_float_filter.NestedFloatFilter(
                    eq = 1.337, 
                    equals = 1.337, 
                    gt = 1.337, 
                    gte = 1.337, 
                    in = [
                        1.337
                        ], 
                    lt = 1.337, 
                    lte = 1.337, 
                    not = null, 
                    not_in = [
                        1.337
                        ], ),
                min = neurelo.models.nested_float_filter.NestedFloatFilter(
                    eq = 1.337, 
                    equals = 1.337, 
                    gt = 1.337, 
                    gte = 1.337, 
                    in = [
                        1.337
                        ], 
                    lt = 1.337, 
                    lte = 1.337, 
                    not = null, 
                    not_in = [
                        1.337
                        ], ),
                sum = neurelo.models.nested_float_filter.NestedFloatFilter(
                    eq = 1.337, 
                    equals = 1.337, 
                    gt = 1.337, 
                    gte = 1.337, 
                    in = [
                        1.337
                        ], 
                    lt = 1.337, 
                    lte = 1.337, 
                    not = null, 
                    not_in = [
                        1.337
                        ], ),
                eq = 1.337,
                equals = 1.337,
                gt = 1.337,
                gte = 1.337,
                var_in = [
                    1.337
                    ],
                lt = 1.337,
                lte = 1.337,
                var_not = None,
                not_in = [
                    1.337
                    ]
            )
        else:
            return FloatWithAggregatesFilter(
        )
        """

    def testFloatWithAggregatesFilter(self):
        """Test FloatWithAggregatesFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
