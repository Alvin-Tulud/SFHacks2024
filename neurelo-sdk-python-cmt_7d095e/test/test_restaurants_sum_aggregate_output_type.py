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

from neurelo.models.restaurants_sum_aggregate_output_type import RestaurantsSumAggregateOutputType  # noqa: E501

class TestRestaurantsSumAggregateOutputType(unittest.TestCase):
    """RestaurantsSumAggregateOutputType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestaurantsSumAggregateOutputType:
        """Test RestaurantsSumAggregateOutputType
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestaurantsSumAggregateOutputType`
        """
        model = RestaurantsSumAggregateOutputType()  # noqa: E501
        if include_optional:
            return RestaurantsSumAggregateOutputType(
                rating = 1.337
            )
        else:
            return RestaurantsSumAggregateOutputType(
        )
        """

    def testRestaurantsSumAggregateOutputType(self):
        """Test RestaurantsSumAggregateOutputType"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
