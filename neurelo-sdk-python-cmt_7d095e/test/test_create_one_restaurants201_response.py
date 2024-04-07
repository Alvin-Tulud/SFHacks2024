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

from neurelo.models.create_one_restaurants201_response import CreateOneRestaurants201Response  # noqa: E501

class TestCreateOneRestaurants201Response(unittest.TestCase):
    """CreateOneRestaurants201Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateOneRestaurants201Response:
        """Test CreateOneRestaurants201Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateOneRestaurants201Response`
        """
        model = CreateOneRestaurants201Response()  # noqa: E501
        if include_optional:
            return CreateOneRestaurants201Response(
                data = neurelo.models.restaurants.restaurants(
                    about = '', 
                    name = '', 
                    rating = 1.337, 
                    reviews = [
                        ''
                        ], )
            )
        else:
            return CreateOneRestaurants201Response(
                data = neurelo.models.restaurants.restaurants(
                    about = '', 
                    name = '', 
                    rating = 1.337, 
                    reviews = [
                        ''
                        ], ),
        )
        """

    def testCreateOneRestaurants201Response(self):
        """Test CreateOneRestaurants201Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
