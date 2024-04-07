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

from neurelo.models.restaurants_create_many_input import RestaurantsCreateManyInput  # noqa: E501

class TestRestaurantsCreateManyInput(unittest.TestCase):
    """RestaurantsCreateManyInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestaurantsCreateManyInput:
        """Test RestaurantsCreateManyInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestaurantsCreateManyInput`
        """
        model = RestaurantsCreateManyInput()  # noqa: E501
        if include_optional:
            return RestaurantsCreateManyInput(
                about = '',
                name = '',
                rating = 1.337,
                reviews = None
            )
        else:
            return RestaurantsCreateManyInput(
                about = '',
                name = '',
                rating = 1.337,
        )
        """

    def testRestaurantsCreateManyInput(self):
        """Test RestaurantsCreateManyInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
