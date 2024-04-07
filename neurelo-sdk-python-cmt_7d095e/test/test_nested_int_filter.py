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

from neurelo.models.nested_int_filter import NestedIntFilter  # noqa: E501

class TestNestedIntFilter(unittest.TestCase):
    """NestedIntFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NestedIntFilter:
        """Test NestedIntFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NestedIntFilter`
        """
        model = NestedIntFilter()  # noqa: E501
        if include_optional:
            return NestedIntFilter(
                eq = 56,
                equals = 56,
                gt = 56,
                gte = 56,
                var_in = [
                    56
                    ],
                lt = 56,
                lte = 56,
                var_not = None,
                not_in = [
                    56
                    ]
            )
        else:
            return NestedIntFilter(
        )
        """

    def testNestedIntFilter(self):
        """Test NestedIntFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()