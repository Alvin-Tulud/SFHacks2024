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

from neurelo.models.restaurants_update_input_reviews import RestaurantsUpdateInputReviews  # noqa: E501

class TestRestaurantsUpdateInputReviews(unittest.TestCase):
    """RestaurantsUpdateInputReviews unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RestaurantsUpdateInputReviews:
        """Test RestaurantsUpdateInputReviews
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RestaurantsUpdateInputReviews`
        """
        model = RestaurantsUpdateInputReviews()  # noqa: E501
        if include_optional:
            return RestaurantsUpdateInputReviews(
                push = None,
                set = [
                    ''
                    ]
            )
        else:
            return RestaurantsUpdateInputReviews(
        )
        """

    def testRestaurantsUpdateInputReviews(self):
        """Test RestaurantsUpdateInputReviews"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
