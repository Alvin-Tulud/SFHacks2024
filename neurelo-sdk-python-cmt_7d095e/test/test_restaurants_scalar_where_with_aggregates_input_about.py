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

from neurelo.models.restaurants_scalar_where_with_aggregates_input_about import RestaurantsScalarWhereWithAggregatesInputAbout  # noqa: E501

class TestRestaurantsScalarWhereWithAggregatesInputAbout(unittest.TestCase):
    """RestaurantsScalarWhereWithAggregatesInputAbout unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestaurantsScalarWhereWithAggregatesInputAbout:
        """Test RestaurantsScalarWhereWithAggregatesInputAbout
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestaurantsScalarWhereWithAggregatesInputAbout`
        """
        model = RestaurantsScalarWhereWithAggregatesInputAbout()  # noqa: E501
        if include_optional:
            return RestaurantsScalarWhereWithAggregatesInputAbout(
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
                max = neurelo.models.nested_string_filter.NestedStringFilter(
                    contains = '', 
                    ends_with = '', 
                    eq = '', 
                    equals = '', 
                    gt = '', 
                    gte = '', 
                    in = [
                        ''
                        ], 
                    lt = '', 
                    lte = '', 
                    not = null, 
                    not_in = [
                        ''
                        ], 
                    search = '', 
                    starts_with = '', ),
                min = neurelo.models.nested_string_filter.NestedStringFilter(
                    contains = '', 
                    ends_with = '', 
                    eq = '', 
                    equals = '', 
                    gt = '', 
                    gte = '', 
                    in = [
                        ''
                        ], 
                    lt = '', 
                    lte = '', 
                    not = null, 
                    not_in = [
                        ''
                        ], 
                    search = '', 
                    starts_with = '', ),
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
                mode = 'default',
                var_not = None,
                not_in = [
                    ''
                    ],
                search = '',
                starts_with = ''
            )
        else:
            return RestaurantsScalarWhereWithAggregatesInputAbout(
        )
        """

    def testRestaurantsScalarWhereWithAggregatesInputAbout(self):
        """Test RestaurantsScalarWhereWithAggregatesInputAbout"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
