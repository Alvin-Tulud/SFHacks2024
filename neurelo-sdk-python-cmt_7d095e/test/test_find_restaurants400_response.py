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

from neurelo.models.find_restaurants400_response import FindRestaurants400Response  # noqa: E501

class TestFindRestaurants400Response(unittest.TestCase):
    """FindRestaurants400Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FindRestaurants400Response:
        """Test FindRestaurants400Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FindRestaurants400Response`
        """
        model = FindRestaurants400Response()  # noqa: E501
        if include_optional:
            return FindRestaurants400Response(
                errors = [
                    neurelo.models._error_response._ErrorResponse(
                        details = neurelo.models.details.details(), 
                        error = '', )
                    ]
            )
        else:
            return FindRestaurants400Response(
                errors = [
                    neurelo.models._error_response._ErrorResponse(
                        details = neurelo.models.details.details(), 
                        error = '', )
                    ],
        )
        """

    def testFindRestaurants400Response(self):
        """Test FindRestaurants400Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
