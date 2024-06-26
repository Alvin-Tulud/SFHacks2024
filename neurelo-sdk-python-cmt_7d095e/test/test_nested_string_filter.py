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

from neurelo.models.nested_string_filter import NestedStringFilter  # noqa: E501

class TestNestedStringFilter(unittest.TestCase):
    """NestedStringFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NestedStringFilter:
        """Test NestedStringFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NestedStringFilter`
        """
        model = NestedStringFilter()  # noqa: E501
        if include_optional:
            return NestedStringFilter(
                contains = '',
                ends_with = '',
                eq = '',
                equals = '',
                gt = '',
                gte = '',
                var_in = [
                    ''
                    ],
                lt = '',
                lte = '',
                var_not = None,
                not_in = [
                    ''
                    ],
                search = '',
                starts_with = ''
            )
        else:
            return NestedStringFilter(
        )
        """

    def testNestedStringFilter(self):
        """Test NestedStringFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
